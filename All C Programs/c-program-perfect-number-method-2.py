/*
 * C program to check whether a number is a perfect number or not using while loop
 */
 
#include <stdio.h>
 
int main(void)
{
    int number, i, sum = 0;
 
    printf("Enter the number: ");
    scanf("%d", &number);
 
    i = 1;
    while (i < number)
    {
        if (number % i == 0)
            sum += i;
        i++;
    }
 
    if (sum == number)
        printf("%d is a perfect number", number);
    else
        printf("%d is not a perfect number", number);
}