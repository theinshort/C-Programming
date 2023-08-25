// c program to calculate factorial of a number using while loop
#include <stdio.h>
int main()
{
    int num, i = 1;
    unsigned long long int factorial_of_num = 1;
    printf("Enter the number whose factorial you want to calculate: ");
    scanf("%d", &num);
    while (i <= num)
    {
        factorial_of_num *= i;
        i++;
    }
 
    printf("Factorial of %d is %llu ", num, factorial_of_num);
    return 0;
}