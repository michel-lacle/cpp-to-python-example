default: library

library: library.o
	g++ -Wall -O3 -shared library.cpp -o library.so

run:
	python3 run_library.py

clean:
	rm -fr *.so
