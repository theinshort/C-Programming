/*
 * C Program to find the nth Armstrong number
 */
#include<stdio.h>
#include<stdlib.h>
#include<math.h>
void main()
{
    int n, count=1;
    printf("*******Value of n should be maximum 31*******");
    printf("\nPlease Enter n to find nth Armstrong Number = ");
    scanf("%d",&n);
    if(n>31)
    {
        printf("\nInteger range of Armstrong Number exceeded. 
      \nPlease enter the value of n less than or equal to 31.");
        exit(1);
    }
    for(int i = 1; i <= 1000000000; i++)
    {
        int num=i, rem, sum=0;
        int digit = (int) log10(num) + 1; //To count number of digits
 
        //Calculating the sum of power of digits of a number
        while(num > 0)
        {
            rem = num % 10;     //To find last digit of the number.
            sum = sum + pow(rem,digit);
            num = num / 10;
        }
        // Check for Armstrong number
        if(i == sum)
        {
            if(count==n)
            {
                printf("%d\n",i);
                break;
            }
            else
            {
                count++;
            }
        }
    }
}