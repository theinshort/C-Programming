/*
 * C Program to Find Transpose of a Matrix using Loops and Function
 */
 
#include <stdio.h>
 
void transpose_matrix(int m,int n, int array[10][10])
{
    //transposing array matrix
    int transpose[10][10];
    for (int i = 0;i < m;i++)
    {
        for (int j = 0; j < n; j++)
        {   
            transpose[j][i] = array[i][j];
        }
    }  
    printf("Transpose of matrix is \n");
    for (int i = 0; i< n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            printf("%d ", transpose[i][j]);
        }
        printf("\n");
    }
}
 
void main()
{
    static int array[10][10];
    int i, j, m, n;
 
    printf("Enter the order of the matrix \n");
    scanf("%d %d", &m, &n);
    printf("Enter the coefficients of the matrix\n");
    for (i = 0; i < m; ++i)
    {
        for (j = 0; j < n; ++j)
        {
            scanf("%d", &array[i][j]);
        }
    }
    printf("The given matrix is \n");
    for (i = 0; i < m; ++i)
    {
        for (j = 0; j < n; ++j)
        {
            printf("%d ", array[i][j]);
        }
        printf("\n");
    }
    transpose_matrix(m,n,array);
}