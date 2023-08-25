/*
 C Program to Print Armstrong Number between a given range
 */
#include <stdio.h>
#include <math.h>
void main()
{
    int low, high;   //for taking user input for range 
    printf("Enter the starting value of the range: ");
    scanf("%d", &low);
    printf("Enter the ending value of the range: ");
    scanf("%d", &high);
    printf("All Armstrong numbers between %d and %d are:\n", low, high);
    for(int n=low;n<=high;n++)                                       
    {
        int num = n,rem,sum=0;
        if(n<=9)
        { 
            printf("%d ",n);
        }
        else
        {
            int digit = (int) log10(num) + 1;  //To count number of digits
 
            //Calculating sum of power of digits of a number
            while(num > 0)
            {
                rem = num % 10; //To find last digit of the number
                sum = sum + pow(rem,digit);
                num = num / 10;
            }
 
            if (sum == n)
            {
                printf("%d ", n);
            }
        }
    }
}