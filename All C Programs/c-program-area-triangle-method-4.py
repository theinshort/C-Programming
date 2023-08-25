/*
 * C program to find the area of a triangle using pointer
 */
#include<stdio.h>
#include<math.h>
 
// Function to calculate area
void calc_area(float a,float b,float c,float *area)
{
    float s = (a+b+c)/2;
 
    // Storing area at memory location of area by dereferencing it
    *area = sqrt(s*(s-a)*(s-b)*(s-c));
}
int main()
{
    float a, b, c, area;
    printf("\nEnter three sides of triangle\n");
    scanf("%f%f%f",&a,&b,&c);
 
    // Calling function to calculate area
    calc_area(a,b,c,&area);
 
    //Area with 2 digits of precision
    printf("\n Area of triangle: %.2f\n",area);
 
    return 0;
}