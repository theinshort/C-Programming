/*
 * C Program to Display Floyd’s triangle using while loop
 */
#include <stdio.h>
 
int main()
{
    int i = 1, j = 0, rows = 7;
    int num = 1;
    while (i <= rows) 
    {
        while (j <= i - 1) 
        {
            printf("%d ", num);
            j++;
            num++;
        }
        j = 0;
        i++;
        printf("\n");
    }
    return 0;
}