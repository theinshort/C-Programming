/*
 * C program to find the area of a triangle using function
 */
#include<stdio.h>
#include<math.h>
 
//Function to calculate area
float calc_area(float a,float b,float c)
{
    float s = (a+b+c)/2;
 
    //Return area of triangle
    return sqrt(s*(s-a)*(s-b)*(s-c));
}
int main()
{
    float a, b, c, s, area;
    printf("\nEnter three sides of triangle\n");
    scanf("%f%f%f",&a,&b,&c);
 
    //Area with 2 digits of precision
    printf("\n Area of triangle: %.2f\n", calc_area(a,b,c));
    return 0;
}