#include<stdio.h>
void Print_BinCoeff(int); //function to print the pattern line by line.
int main()
{
    int rows;
    printf("Enter the Number of Rows in the Pascal Triangle::\t");
    scanf("%d",&rows);
    for(int i=0;i<rows;i++)//loop to iterate rows from 1 to rows
    {
        for (int k = rows -  i-1 ; k > 0; k--)
        {
            //Prints spaces as many as number of rows in the triangle-current number of row
            printf("  ");
        }
        Print_BinCoeff(i);//function to print the binomial coefficients.
    }
    return 0;
}
void Print_BinCoeff(int x)
{
    int temp=x;
    int answer=x;
    int c=2;
    for(int i=0;i<=x;i++)
    {	
        if(i==0 || i==x)
        {
            printf("%-5d",1);
        }
        else
        {
            printf("%-5d",answer);
            //It's a length specifier, so it specifies the slot in which the number can be adjusted.
            answer=answer*(temp-1);
            answer=answer/c;
            temp--;
            c++;
        }
    }
    printf("\n");
}