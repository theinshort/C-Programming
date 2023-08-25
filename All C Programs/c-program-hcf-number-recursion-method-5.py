/*
 * C Program to find HCF of two Numbers using Recursive Euclidean Algorithm
 */
#include<stdio.h>
 
int HCF_algorithm(int a, int b)
{
    int x = (a > b) ? a : b; // a is greater number
    int y = (a < b) ? a : b; // b is smaller number
 
    if (y == 0) {
        return x;
    } else {
        return HCF_algorithm(y, (x % y));
    }
}
 
int main()
{
    int num1, num2, HCF;
    printf("\nEnter two numbers to find HCF using Euclidean algorithm: ");
    scanf("%d%d", &num1, &num2);
    HCF = HCF_algorithm(num1, num2);
 
    printf("The HCF of %d and %d is %d\n", num1, num2, HCF);
    return 0;
}