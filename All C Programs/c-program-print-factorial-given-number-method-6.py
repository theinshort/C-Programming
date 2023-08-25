/*
 * C program to find the factorial factorial numbers in a given range.
 */
 
#include<stdio.h>
int main()
{
    long fact=1;
    int start,end;
    printf("Enter the starting value of range ");
    scanf("%d",&start);
    printf("Enter the ending value of range ");
    scanf("%d",&end);
    printf("Factorial series of the given range is: ");
    int a=1;
    // Preconpute multiplication of numbers smaller than start
    for(int i=1;i<start;i++)
    {
        a=a*i;
    }
    // Iterate from start to end
    for(int n=start;n<=end;n++)
    {
        // Compute factorial
        fact=a*n;
        // Update the precomputed value
        a=a*n;
        printf("%ld ",fact);
    }
    return 0;
}