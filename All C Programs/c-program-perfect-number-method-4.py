/*
 * C program to find the perfect numbers between two limits.
 */
 
#include<stdio.h>
#include<stdlib.h>
 
int isPerfect(int n)
{
    int i, sum = 0;
    for (i = 1; i < n; i++)
    {
        if (n % i == 0)
        {
            sum += i;
        }
    }
    if (sum == n)
    {
        return 1;
    }
    else
    {
        return 0;
    }
}
 
void printPerfect(int lower, int upper)
{
    int i;
    for (i = lower; i <= upper; i++)
    {
        if (isPerfect(i))
        {
            printf("%d ", i);
        }
    }
}
 
int main(void)
{
    int lower, upper;
    printf("Enter the lower limit: ");
    scanf("%d", &lower);
    printf("Enter the upper limit: ");
    scanf("%d", &upper);
    printf("The perfect numbers between %d and %d are: \n", lower, upper);
    printPerfect(lower, upper);
    return 0;
}