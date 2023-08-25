/*
 * C program to find the factorial of a given number using for loop.
 */
 
#include <stdio.h>
void main()
{
    // fact to store factorial of number N
    int fact = 1, n;
    // Take input
    printf("Enter the number: \n");
    scanf("%d", &n);
    // Check validity of N
    if (n <= 0)
    fact = 1;
    // Loop N times and multiply all positive numbers
    else
    {
        for (int i = 1; i <= n; i++)
        {
            fact = fact * i;
        }
    }
    // Print the fact.
    printf("Factorial of %d = %5d\n", n, fact);
}