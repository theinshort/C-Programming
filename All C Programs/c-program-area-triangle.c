/*
 * C program to find the area of a triangle using formula
 */
#include <stdio.h>
void main()
{
    float base,height;
    printf("Enter Base and Height: ");
    scanf("%f %f",&base,&height);
    float area = (base * height) / 2;
 
    //Area with precision of 2 decimal places
    printf("Area of Triangle is %0.2f",area);
}