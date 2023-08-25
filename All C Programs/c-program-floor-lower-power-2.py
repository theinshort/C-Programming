/*
 * C Program to round floor of integer to next lower power of 2
 */
#include <stdio.h>
 
int main ()
{
	int num = 0;
	printf("\nEnter the number: ");
	scanf ("%d", &num);
	num --;
	num = num | (num >> 1);
	num = num | (num >> 2);
	num = num | (num >> 4);
	num = num | (num >> 8);
	num = num | (num >> 16);
	num ++;
	printf ("\n NEXT NUMBER LOWER TO THE POWER OF 2 : %d\n", num);
	return 0;
}