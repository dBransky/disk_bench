CC = gcc
CFLAGS = -Wall -Wextra -std=c99 -O0 -g
LDFLAGS = -lm

TARGET = io_bench
SRCS = io_bench.c

$(TARGET): $(SRCS)
	$(CC) $(CFLAGS) -o $(TARGET) $(SRCS) $(LDFLAGS)

.PHONY: clean
clean:
	rm -f $(TARGET)
debug:
	$(CC) $(CFLAGS) -g -o $(TARGET) $(SRCS) $(LDFLAGS)