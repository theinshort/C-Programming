/*
 * C Program to Display Floyd’s triangle using For Loop
 */
 
#include <stdio.h>
 
void floyds_triangle(int rows)
{
    int i, j, k = 1;
    for (i = 1; i <= rows; i++)
    {
        for (j = 1; j <= i; j++)
        {
            printf("%4.d ", k ++);
        }
        printf("\n");
    }
}
 
int main(void)
{
    int rows;
    printf("Enter the number of rows: ");
    scanf("%d", &rows);
 
    floyds_triangle(rows);
 
    return 0;
}