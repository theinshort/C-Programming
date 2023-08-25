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
    fflush(stdin);
    printf("Enter the operator [+,-,*,/] \n");
    scanf("%s", &operator);
    switch(operator)
    {
        case '+': result = num1 + num2; // add two numbers
            break;
        case '-': result = num1 - num2; // subtract two numbers
            break;
        case '*': result = num1 * num2; // multiply two numbers
            break;
        case '/': result = num1 / num2; // divide two numbers
            break;
        default : printf("Error in operation");
            break;
    }
    printf("\n %5.2f %c %5.2f = %5.2f\n", num1, operator, num2, result);
}