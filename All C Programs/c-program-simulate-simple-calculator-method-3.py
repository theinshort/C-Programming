/*
 * C program to simulate a simple calculator to perform arithmetic
 * operations like addition, subtraction, multiplication, division, remainder etc.
 */
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
 
void main()
{
    float num1, num2, result;  // used for all other operations except remainder
    int ch,n1,n2,res;  //used for remainder operation
    do{
        printf("\nSimulation of a Simple Calculator\n");
        printf("*********************************\n");
        printf("Select a number to perform operation on Calculator");
        printf("\n1->Addition\t 2->Subtraction\t 3->Multiplication\t 4->Division\t 
               5->Remainder\t 6- >Square\t 7->Square Root 8->Exit\n");
        scanf("%d",&ch);
 
        switch(ch)
        {
            // Add two numbers
            case 1:
                printf("Enter two numbers \n");
                scanf("%f %f", &num1, &num2);
                result = num1 + num2;
                printf("\n%.2f + %.2f = %.2f\n",num1,num2,result);
                break;
 
            // Subtract two numbers
            case 2:
                printf("Enter two numbers \n");
                scanf("%f %f", &num1, &num2);
                result = num1 - num2;
                printf("\n%.2f - %.2f = %.2f\n",num1,num2,result);
                break;
 
            // Multiplication of two numbers
            case 3:
                printf("Enter two numbers \n");
                scanf("%f %f", &num1, &num2);
                result = num1 * num2;
                printf("\n%.2f * %.2f = %.2f\n",num1,num2,result);
                break;
 
            // Division of two numbers
            case 4:
                printf("Enter two numbers \n");
                scanf("%f %f", &num1, &num2);
                result = num1 / num2;
                printf("\n%.2f / %.2f = %.2f\n",num1,num2,result);
                break;
 
            // Remainder of two numbers
            case 5:
                printf("Enter two numbers \n");
                scanf("%d %d", &n1, &n2);
                res = n1 % n2;
                printf("Remainder of two numbers = %d\n",res);
                break;
 
            // Square of number
            case 6:
                printf("Enter the number \n");
                scanf("%f", &num2);
                result = num2 * num2;
                printf("Square of %.2f = %.2f\n",num2,result);
                break;
 
            // Square root of a number
            case 7:
                printf("Enter the number \n");
                scanf("%f", &num1);
                result = sqrt(num1);
                printf("Square Root of %.2f = %.2f\n",num1,result);
                break;
 
            case 8:
                printf ("Execution Terminated");
                exit(0);
                break;
 
            default:
                printf("Error in Operation");
                break;
        }
    }while(ch!=8);
}