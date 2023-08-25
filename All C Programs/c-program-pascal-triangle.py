/*
    Naive approach to Print Pascals Triangle.
*/
#include <stdio.h>
long long int factorial(int);
void main()
{
    int rows;
    printf("Enter the Number of Rows in the Pascal Triangle::\t");
    scanf("%d",&rows);
    int arr[rows][rows];
    //initializing the array that will form base of the pascal triangle.
    for(int i=0;i<rows;i++)
    {
        for(int j=0;j<=i;j++)
        {
                arr[i][j]=(factorial(i)/(factorial(i-j)*factorial(j)));
                //Finding the value of iCj=[i!/(i-j!)*(j!)] for each place.
        }
    }
    for (int i = 0; i < rows; i++)
    {
        for (int k = rows -  i-1 ; k > 0; k--)
        {
               //Prints spaces as many as number of rows in the triangle-current number of row
                printf("  ");
        }
        for (int j = 0; j <= i; j++)
        {
            printf("%-5d", arr[i][j]);
            // %-5d means length specifier.
            //it means 5 spaces are provided for number it fills spaces from left to right.
        }
        printf("\n");
    }
    return ;
}
long long int factorial(int num)
{
    long long int j=1;
    while(num>0)
    {
        j=j*num;
        num--;
    }
    return j;
}