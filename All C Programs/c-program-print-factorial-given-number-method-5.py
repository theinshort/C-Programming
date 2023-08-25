/*
 * C program to find the factorial factorial numbers in a given range.
 */
 
#include<stdio.h>
int main()
{
    long fact=1;
    int start,end;
    printf("Enter the starting value of range: ");
    scanf("%d",&start);
    printf("Enter the ending value of range: ");
    scanf("%d",&end);
    printf("Factorial series of the given range is: ");
    for(int n=start;n<=end;n++)
    {
        // Calculating factorial for each number of range
        fact=1;
        for(int x=1;x<=n;x++)
        {
            fact=fact*x;
        }
        // Printing the output
        printf("%ld ",fact);
    }
    return 0;
}