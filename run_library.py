import os 
import ctypes
 
def main():
	here = os.path.dirname(os.path.abspath(__file__))

	rectangle_lib = ctypes.cdll.LoadLibrary(f'{here}/rectangle.so')
	print(rectangle_lib.set_value(3, 2))
 
if __name__ == '__main__':
	main()
