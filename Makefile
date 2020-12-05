default: library

library: library.o
	g++ -Wall -O3 -shared library.cpp -o library.so

clean:
	rm -fr *.so
