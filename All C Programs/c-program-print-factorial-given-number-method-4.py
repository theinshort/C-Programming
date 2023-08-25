/*
 * C program to find the factorial of a given number using ternary operator
 */
 
#include <stdio.h>
int factorial(int n)
{
    // Using ternary operators
    return ((n==0||n==1)?1:n*factorial(n-1));
}
int main()
{
    // The number to calc n!
    int n;
    // variable to store ans
    int ans;
    printf("Enter a number to find it's Factorial: ");
    scanf("%d", &n);
    if (n < 0)
    {
        printf("Factorial of negative number not possible\n");
    }
    else
    {
        // Calling factorial method
        ans = factorial(n);
        printf("The Factorial of %d is %d.\n", n, ans);
    }
    return 0;
}