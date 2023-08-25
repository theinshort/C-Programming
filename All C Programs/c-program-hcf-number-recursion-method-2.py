/*
 * C program to find the HCF of two integers using for-loop
 */
#include<stdio.h>
void main()
{
    int n1, n2, i, HCF;
 
    printf("Enter two integers: ");
    scanf("%d %d", &n1, &n2);
 
    int min = (n1 < n2)? n1:n2;  // to find minimum of the two numbers.
 
    for(i=min; i >=1; --i)
    {
        // Checks if i divides both the integers
        if(n1%i==0 && n2%i==0)
        {
            HCF = i;
            break;
        }
    }
 
    printf("HCF of %d and %d is %d", n1, n2, HCF);
}