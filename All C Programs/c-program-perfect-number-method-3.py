/*
 * C program to check whether a number is a perfect number or not using function
 */
 
#include <stdio.h>
 
int is_divisor(int number, int divisor)
{
    if (number % divisor == 0)
        return 1;
    else
        return 0;
}
 
int sum_of_divisors(int number)
{
    int i = 1, sum = 0;
    while (i < number)
    {
        if (is_divisor(number, i))
            sum += i;
         i++;
    }
    return sum;
}
 
int is_perfect_number(int number)
{
    if (sum_of_divisors(number) == number)
        return 1;
    else
        return 0;
}
 
int main(void)
{
    int number;
 
    printf("Enter the number: ");
    scanf("%d", &number);
 
    if (is_perfect_number(number))
        printf("The number is a perfect number");
    else
        printf("The number is not a perfect number");
}