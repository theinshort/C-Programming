/*
 * C program to simulate a simple calculator to perform arithmetic
 * operations like addition, subtraction, multiplication and division
 */
#include <stdio.h>
 
void main()
{
    char operator;
    float num1, num2, result;
 
    printf("Simulation of a Simple Calculator\n");
    printf("*********************************\n");
    printf("Enter two numbers \n");
    scanf("%f %f", &num1, &num2);
    printf("Enter the operator [+,-,*,/] \n");
    scanf("%s", &operator);
    if(operator == '+')
        result = num1 + num2;
    else if(operator == '-')
        result = num1 - num2;
    else if(operator == '*')
        result = num1 * num2;
    else if(operator == '/')
        result = num1 / num2;
    else
        printf("Error in operation");
    printf("\n%5.2f %c %5.2f = %5.2f\n", num1, operator, num2, result);
}