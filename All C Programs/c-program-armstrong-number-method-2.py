/*
 * C Program to Check whether a given Number is Armstrong
 */
 
#include <stdio.h>
#include <math.h>
 
void main()
{
    int number, sum = 0, rem = 0, cube = 0, temp, n=0;
 
    printf ("enter a number\n");
    scanf("%d", &number);
    temp = number;
    int num = number;
    while(num!=0)   // time complexity-->O(log n)
    {
        num = num/10;                                   
        n++;      // count of digits n
    }
    while (number != 0)	  // time complexity-->O(log n)
    {
        rem = number % 10;
        cube = pow(rem, n);
        sum = sum + cube;
        number = number / 10;
    }
    if (sum == temp)
        printf ("The given number is an Armstrong number");
    else
        printf ("The given number is not an Armstrong number");
}