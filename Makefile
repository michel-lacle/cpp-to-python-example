default: rectangle

rectangle: rectangle.o
	g++ -Wall -O3 -shared rectangle.cpp -o rectangle.so

run:
	python3 run_library.py

clean:
	rm -fr *.so
