/*
 * C Program to Check whether the given Integer has an Alternate 
 * Pattern 
 */
#include <stdio.h>
#include <stdlib.h>
int main ()
{
	int num = 0, n = 0, i =0;
	int count = 0;
	printf("Enter the number: ");
	scanf ("%d", &num);
	n = num;
	// first lets count the number of bits
	while (n)
	{
		count ++;
		n = n >> 1;
	}
	printf ("\n COUNT : %d", count);
 
	// now check for alternative
	for (i = 0; i <= count - 2; i++)
	{
		if (((num >> i) & 1) == ((num >> (i+2)) & 1))
		{
			continue;
		}
		else
		{
			printf ("\nFALSE : ALTERNATIVE PATTERN DOES NOT EXIST\n");
			exit (0);
		}
 
	}
	printf ("\nTRUE : ALTERNATIVE PATTERN DOES EXIST\n");
        return 0;
}