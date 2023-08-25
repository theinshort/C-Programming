/*
 * C Program to find the roots of a quadratic equation and their nature.
 */
 
#include<stdio.h>
#include<math.h> //Header file is include as we use sqrt function.
int main()
{
    /*
        Quadratic Equation is in the form a*x^2 + b*x + c = 0
        a=>coefficient of x^2
        b=>coefficient of x
        c=>constant
    */
    float a,b,c;
    float d;  //discriminant of the equation.
    float root1,root2;
    float imaginary_part;  //for instances where discriminant < 0
 
    printf("The equation is in the form of a*x^2 + b*x + c = 0 \n");
    printf("Enter the coefficient of term x^2 i.e a = ");
    scanf("%f",&a);
    printf("\n");
 
    printf("Enter the coefficient of term x i.e b = ");
    scanf("%f",&b);
    printf("\n");
 
    printf("Enter the constant term i.e c = ");
    scanf("%f",&c);
    printf("\n");
 
 
    if(a==0)
    {
        printf("The equation given is not a quadratic equation \n");
        return 0;
    }
 
    //Value of discriminant is found here.
    d=(b*b)-(4.0*a*c);
 
    //Printing the discriminant of the equation.
    printf("Discriminant of the equation: %f",d);
    printf("\n");
 
    if(d>0)
    {
        printf("Roots are real and unique\n");
        root1=b*(-1.0); //finding the first root.
 
        //As we are operating on floating point number, so have written -1.0
        root1=root1+sqrt(d);
        root1=root1/(2.0*a);
        root2=b*(-1.0);  //finding the second root.
        root2=root2-sqrt(d);
        root2=root2/(2.0*a);
        printf("root 1= %f \n root 2= %f",root1,root2);
    }
    if(d==0)
    {
        root1=((b*-1.0)/(2.0*a));
        root2=root1;
        printf("Root are real and equal to each other\n");
        printf("root 1= %f \n root 2= %f",root1,root2);
    }
    if(d<0)
    {
        imaginary_part=sqrt(-1.0*d)/(2.0*a);
        root1=(-1.0*b)/(2.0*a);
        root2=root1;
        //root1's real part is equal to root2's real part also the imaginary part
        //but one is summation of both parts and one is diffrence of both parts
        printf("Roots are imaginary \n");
        printf("Root 1= %f+%f i \t \nRoot 2= %f-%f i",root1,imaginary_part,root2,imaginary_part);
    }
    return 0;
}