CFLAGS=-g
CC=g++ -Wall -Weffc++ -Werror

SHELL=/bin/bash

all: test_chop.passed

clean:
	rm -f *.o chop1

test_chop.passed: test_chop.sh chop1
	@./test_chop.sh chop1

chop1: chop1.cc chop_main.o
	@echo "Compiling $@..."
	@$(CC) $(CFLAGS) $^ -o $@

chop_main.o: chop_main.cc
	@echo "Compiling $@..."
	@$(CC) $(CFLAGS) -c $<
