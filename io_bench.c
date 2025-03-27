#define _GNU_SOURCE
#include <signal.h>
#include <stdint.h>
#include <assert.h>
#include <math.h>
#include <sys/mman.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <fcntl.h>
#include <time.h>
#include <math.h>
#include <getopt.h>
unsigned long cluster_size=0;
unsigned long cluster_amount=1;
void handle_parent(int child_pid, int length) {
    sleep(length+2);
    char path[100];
    sprintf(path, "/proc/%d/io", child_pid);
    FILE *file = fopen(path, "r");
    char line[100];
    if (file == NULL) {
        perror("Failed to open /proc/pid/io");
        exit(1);
    }
    while (fgets(line, sizeof(line), file)) {
        printf("%s", line);
    }
    fclose(file);
    sprintf(path, "/proc/%d/stat", child_pid);
    file = fopen(path, "r");
    if (file == NULL) {
        perror("Failed to open /proc/pid/io");
        exit(1);
    }
    while (fgets(line, sizeof(line), file)) {
        printf("%s", line);
    }
    fclose(file);
    waitpid(child_pid, NULL, 0);
}
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
int run_benchmark(int* permuation, unsigned long iosize, int fd,int o_write, char *buffer,int indices, int epochs, int length,double* warmup,int verbose, unsigned long* latencies) {
    int r_w=0;
    struct timespec first_iter_s, first_iter_e, cur, prev;
    clock_gettime(CLOCK_MONOTONIC, &first_iter_s);
    for (int i = 0; i < epochs; i++) {
        for (int j = 0; j<indices; j++){
            clock_gettime(CLOCK_MONOTONIC, &cur);
            if (verbose){
                if (i != 0 || j != 0) {
                    latencies[(i)*indices + (j)-1] = (cur.tv_sec - prev.tv_sec) * 1e9 + (cur.tv_nsec - prev.tv_nsec);
                }
                prev = cur;
            }
            if ((cur.tv_sec - first_iter_s.tv_sec) + (cur.tv_nsec - first_iter_s.tv_nsec)/1e9 > length) {
                return (i)*indices + (j);
            }
            int index = permuation[j];
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
            // printf("%d\n",index);
        }
        if (i==0) {
            clock_gettime(CLOCK_MONOTONIC, &first_iter_e);
            *warmup = (first_iter_e.tv_sec - first_iter_s.tv_sec) * 1e9 + (first_iter_e.tv_nsec - first_iter_s.tv_nsec);
        }
    }
    return epochs*indices;
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
    printf("  -l, --length <n>       length of the benchmark in seconds; default=30\n");
    printf("  -v, --verbose       return per-syscall latency\n");
    printf("  -c, --cluster_size <n>   cluster_size ; default=filesize/clsuter_amount\n");
    printf("  -a, --cluster_amount <n>   cluster_amount ; default=1\n");
    printf("  -h, --help                Print this help message\n");
}
int main(int argc, char *argv[]) {
    long iterations = 256;
    int length = 30;
    char *pattern = "seq";
    unsigned long iosize = 4096;
    unsigned long filesize = 1048576;
    char *filename = NULL;
    char *operation = "read";
    int verbose = 0;
    struct option long_options[] = {
        {"iteration", required_argument, 0, 'i'},
        {"pattern", required_argument, 0, 'p'},
        {"iosize", required_argument, 0, 's'},
        {"filesize", required_argument, 0, 'f'},
        {"file", required_argument, 0, 'n'},
        {"operation", required_argument, 0, 'o'},
        {"cluster_size", required_argument, 0, 'c'},
        {"cluster_amount", required_argument, 0, 'a'},
        {"length", required_argument, 0, 'l'},
        {"verbose", no_argument, 0, 'v'},
        {"help", no_argument, 0, 'h'},
        {0, 0, 0, 0} // This terminates the array
    };

    int opt;
    int option_index = 0;
    while ((opt = getopt_long(argc, argv, "l:o:i:p:s:f:n:h:vc:a:", long_options, &option_index)) != -1) {
        switch (opt) {
            case 'a':
                cluster_amount = strtol(optarg,NULL,10);
                break;
            case 'c':
                cluster_size = strtol(optarg,NULL,10);
                break;
            case 'v':
                verbose = 1;
                break;
            case 'l':
                length = atoi(optarg);
                break;
            case 'i':
                iterations = strtol(optarg,NULL,10);
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
    printf("Iterations: %ld\n", iterations);
    printf("Test Length: %d seconds\n", length);
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
    int pid = fork();
    if (pid != 0) {
        handle_parent(pid, length);
        exit(0);
    }
    if (cluster_size==0){
        printf("cluster_size not provided setting to %ld/%ld\n",filesize,cluster_amount);
        cluster_size=filesize/cluster_amount;
    }
    printf("cluster_size: %ld\n",cluster_size);
    printf("cluster_amount: %ld\n",cluster_amount);
    int open_flags = O_DIRECT;
    int o_write=0;
    int indices=0;
    for (unsigned long i = 0; i < cluster_amount; i++) {
        for (unsigned long j = 0; j < cluster_size/iosize; j++) {
            if (j*iosize < cluster_size) {
                indices++;
            }
        }
    }
    if (filesize % iosize != 0) {
        printf("File size must be a multiple of IO size\n");
        return 1;
    }
    if(iterations%indices!=0){
        printf("iternation %ld must be a multiple of indices %d\n",iterations,indices);
        return 1;
    }
    int epochs = iterations/indices;
    if(strcmp(operation, "write") == 0)
        o_write=1;
    int* permuatation = malloc(sizeof(int)*(indices));
    int count=0;
    for (unsigned long i = 0; i < cluster_amount; i++) {
        for (unsigned long j = 0; j < cluster_size/iosize; j++) {
            if (j*iosize < cluster_size) {
                permuatation[count] = (i*(filesize/cluster_amount))/iosize + j;
                count++;
            }
        }
    }
    if(strcmp(pattern, "rand") == 0){
        permutate(permuatation, indices);
    }
    // for (int i = 0; i < indices; i++) {
    //     printf("%d\n",permuatation[i]);
    // }
    // exit(0);
    void* buffer = mmap(NULL, iosize, PROT_READ | PROT_WRITE, MAP_PRIVATE | MAP_ANONYMOUS, -1, 0);
    // check buffer is aligned using posix_memalign 
    if (posix_memalign(&buffer, iosize, iosize) != 0) {
        perror("posix_memalign failed");
        exit(1);
    }
    if (o_write){
        open_flags |= O_WRONLY;
        fill_random_buffer(buffer, iosize);
    }
    else {
        open_flags |= O_RDONLY;
    }
    int fd = open(filename, open_flags);
    if (buffer == MAP_FAILED) {
        perror("Failed to allocate buffer using mmap");
        exit(1);
    }
    
    printf("==================================== <running benchmark> ====================================\n");
    struct timespec start, end;
    clock_gettime(CLOCK_MONOTONIC, &start);
    double warmup = -1;
    unsigned long* latencies = NULL;
    if (verbose)
        latencies = malloc(sizeof(unsigned long)*indices*epochs);
    int iters_done = run_benchmark(permuatation, iosize, fd, o_write, buffer, indices, epochs, length, &warmup,verbose,latencies);
    clock_gettime(CLOCK_MONOTONIC, &end);
    if(delete_file){
        remove(filename);
    }
    if (warmup != -1) {
        printf("warm up throughput: %f MB/s\n", ((filesize)/1e6)/((warmup)/1e9));
    }
    printf("total throughput: %f MB/s\n", ((iosize*iters_done)/1e6)/((end.tv_sec - start.tv_sec) + (end.tv_nsec - start.tv_nsec)/1e9));
    printf("completed %d iterations\n", iters_done);
    if (verbose) {
        printf("Latencies:\n");
        for (int i = 0; i < epochs; i++) {
            for (int j = 0; j < indices; j++) {
                if (latencies[i*indices + j] == 0)
                    {
                        assert (i*indices + j +1== iters_done);
                        return 0;
                    }
                printf("%lu\n", latencies[i*indices + j]);
            }
        }
    }
    return 0;
}