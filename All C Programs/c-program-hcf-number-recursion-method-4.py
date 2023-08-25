/*
 * C Program to find HCF of two Numbers using Euclidean Algorithm
 */
#include<stdio.h>
 
int HCF(int x, int y) {
    int r = 0, a, b;
    a = (x > y) ? x : y; // a is greater number
    b = (x < y) ? x : y; // b is smaller number
 
    r = b;
    while (a % b != 0) {
        r = a % b;
        a = b;
        b = r;
    }
    return r;
}
 
int main(int argc, char **argv) {
    printf("Enter the two numbers: ");
    int x, y;
    scanf("%d", &x);
    scanf("%d", &y);
    printf("The HCF of two numbers is: %d", HCF(x, y));
    return 0;
}