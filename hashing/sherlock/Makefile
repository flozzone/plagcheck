CC = gcc
CFLAGS = -Wall -ansi -pedantic -O2 -g
SOURCE = *.c *.h *akefile*
PROGRAM = sherlock

all:	$(PROGRAM)

$(PROGRAM):	sherlock.c
	#$(CC) $(CFLAGS) -o sherlock sherlock.c
	python setup.py build_ext --inplace

clean:
	rm -f *.o core $(PROGRAM) *.so Build

