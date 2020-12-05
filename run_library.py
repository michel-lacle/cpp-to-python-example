import os 
import ctypes
 
def main():
	here = os.path.dirname(os.path.abspath(__file__))

	print(f"{here}")

	TestLib = ctypes.cdll.LoadLibrary(f'{here}/library.so')
	print(TestLib.SampleAddInt(1, 2))
 
if __name__ == '__main__':
	main()
