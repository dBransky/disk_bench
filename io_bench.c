#define _GNU_SOURCE
#include <stdint.h>
#include <assert.h>
#include <math.h>
#include <sys/mman.h>  // for mmap
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <fcntl.h>
#include <time.h>
#include <math.h>
#include <getopt.h>

void permutate(int* arr, int size){
    for(int i=0;i<size;i++){
        int j = rand() % size;
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }
}
char* create_temp_file(unsigned long size) {
    char *filename = "/tmp/io_bench_file";
    int fd = open(filename, O_RDWR | O_CREAT, 0666);
    if (fd < 0) {
        perror("Failed to open temporary file");
        exit(1);
    }

    char *buffer = malloc(size);
    if (!buffer) {
        perror("Failed to allocate buffer");
        close(fd);
        exit(1);
    }

    for (unsigned long i = 0; i < size; i++) {
        buffer[i] = rand() % 256;
    }
    struct timespec start, end;
    clock_gettime(CLOCK_MONOTONIC, &start);
    if (write(fd, buffer, size) != size) {
        perror("Failed to write to temporary file");
        free(buffer);
        close(fd);
        exit(1);
    }
    clock_gettime(CLOCK_MONOTONIC, &end);
    double latency = (end.tv_sec - start.tv_sec) * 1e9 + (end.tv_nsec - start.tv_nsec);
    printf("Creating temporary file took %f ns\n", latency);

    free(buffer);
    close(fd);
    return filename;
}
void fill_random_buffer(char *buffer, int size) {
    for (int i = 0; i < size; i++) {
        buffer[i] = rand() % 256;
    }
}
double run_benchmark(int iterations, int* permuation, unsigned long iosize, int fd,int o_write, char *buffer,int indices) {
    int r_w=0;
    struct timespec first_iter_s, first_iter_e;
    double warmup;
    clock_gettime(CLOCK_MONOTONIC, &first_iter_s);
    for (int i = 0; i < iterations; i++) {
        int index = permuation[i];
        if(o_write){
            r_w = pwrite(fd, buffer, iosize, index*iosize);
        }
        else
        { 
            r_w = pread(fd, buffer, iosize, index*iosize);
        }
        if (r_w < iosize*0.99) {
            perror("Failed to read/write from/to file");
            printf("read write: %d\n", r_w);
            exit(1);
        }
        if (i == (indices-1)) {
            clock_gettime(CLOCK_MONOTONIC, &first_iter_e);
            warmup = (first_iter_e.tv_sec - first_iter_s.tv_sec) * 1e9 + (first_iter_e.tv_nsec - first_iter_s.tv_nsec);
        }
    }
    return warmup;
}

void print_usage() {
    printf("Usage: io_bench [options]\n");
    printf("Options:\n");
    printf("  -i, --iteration <n>  num of iterations; default=1000\n");
    printf("  -p, --pattern <str>    seq|rand; default=seq\n");
    printf("  -o  --opertaion <str>  read|write; default=read\n");
    printf("  -s, --iosize <nbytes>     size of each i/o operation; default=4KB\n");
    printf("  -f, --filesize <nbytes>   Size of the file used; default=4MB\n");
    printf("  -n, --file <str>       overrides filesize with this given file; defaul=NULL\n");
    printf("  -h, --help                Print this help message\n");
}
int main(int argc, char *argv[]) {
    int iterations = 1000;
    char *pattern = "seq";
    unsigned long iosize = 4096;
    unsigned long filesize = 1048576;
    char *filename = NULL;
    char *operation = "read";

    struct option long_options[] = {
        {"iteration", required_argument, 0, 'i'},
        {"pattern", required_argument, 0, 'p'},
        {"iosize", required_argument, 0, 's'},
        {"filesize", required_argument, 0, 'f'},
        {"file", required_argument, 0, 'n'},
        {"operation", required_argument, 0, 'o'},
        {"help", no_argument, 0, 'h'},
        {0, 0, 0, 0} // This terminates the array
    };

    int opt;
    int option_index = 0;
    while ((opt = getopt_long(argc, argv, ":o:i:p:s:f:n:h", long_options, &option_index)) != -1) {
        switch (opt) {
            case 'i':
                iterations = atoi(optarg);
                break;
            case 'p':
                pattern = optarg;
                break;
            case 's':
                iosize = strtoul(optarg, NULL, 0);
                break;
            case 'f':
                filesize = strtoul(optarg, NULL, 0);
                break;
            case 'n':
                filename = optarg;
                break;
            case 'o':
                operation = optarg;
                break;
            case 'h':
                print_usage();
                return 0;
            default:
                printf("Unknown option: %s\n", argv[optind - 1]);
                print_usage();
                return 1;
        }
    }
    // Placeholder for the actual benchmarking logic
    printf("Running IO benchmark with the following parameters:\n");
    printf("Iterations: %d\n", iterations);
    printf("Pattern: %s\n", pattern);
    printf("IO Size: %ld bytes\n", iosize);
    if (filename) {
        printf("File: %s\n", filename);
    }
    printf("Operation: %s\n", operation);
    int delete_file = 0;
    if (filename == NULL) {
        delete_file = 1;
        filename = create_temp_file(filesize);
    }
    // read the file size dynamically 
    struct stat st;
    stat(filename, &st);
    filesize = st.st_size;
    printf("File Size: %ld bytes\n", filesize);
    int open_flags = O_SYNC | O_DIRECT;
    int o_write=0;
    if (filesize % iosize != 0) {
        printf("File size must be a multiple of IO size\n");
        return 1;
    }
    if(strcmp(operation, "write") == 0) // move this out
        o_write=1;
    int* permuatation = malloc(sizeof(int)*iterations);
    for(int i=0;i<iterations;i++){
        permuatation[i]=i%(filesize/iosize);
    }
    if(strcmp(pattern, "rand") == 0){ // move this out
        permutate(permuatation, iterations);
    }
    char* buffer = mmap(NULL, iosize, PROT_READ | PROT_WRITE, MAP_PRIVATE | MAP_ANONYMOUS, -1, 0);
    // check buffer is aligned using posix_memalign 
    if (o_write){
        open_flags |= O_WRONLY;
        fill_random_buffer(buffer, iosize);
    }
    int fd = open(filename, open_flags);
    if (buffer == MAP_FAILED) {
        perror("Failed to allocate buffer using mmap");
        exit(1);
    }
    
    printf("==================================== <running benchmark> ====================================\n");
    struct timespec start, end;
    clock_gettime(CLOCK_MONOTONIC, &start);
    double warmup = run_benchmark(iterations, permuatation, iosize, fd, o_write, buffer, filesize/iosize);
    clock_gettime(CLOCK_MONOTONIC, &end);
    if(delete_file){
        remove(filename);
    }
    printf("warm up throughput: %f MB/s\n", ((filesize)/1e6)/((warmup)/1e9));
    printf("total throughput: %f MB/s\n", ((iosize*iterations)/1e6)/((end.tv_sec - start.tv_sec) + (end.tv_nsec - start.tv_nsec)/1e9));
    return 0;
}