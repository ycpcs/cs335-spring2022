#include <stdio.h>

int x = 100;

int main()
{
	int a = 2;
	float b = 3.141592;

	static int y;

	int* ptr = new int[2];
	ptr[0] = 10;
	ptr[1] = 20;

	delete[] ptr;

	return 1;
}
