/*
 * C Program to Display Floyd’s triangle using recursion
 */
#include <stdio.h>
 
void floydTriangleRecursive(int a, int b)
{
    if (a == b)
        return;
    for (int j = b * (b + 1) / 2 + 1; j <= (b + 1) * (b + 2) / 2; j ++)
        printf("%4.d", j);
    printf("\n");
    return floydTriangleRecursive(a, b + 1);
}
 
int main(void)
{
    int n;
    printf("Enter the number of rows: ");
    scanf("%d", &n);
    floydTriangleRecursive(n, 0);
    return 0;
}