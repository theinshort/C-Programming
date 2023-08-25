/*
 * C Program to Check Number is Palindrome or Not using Iterative.
 */
 
#include <stdio.h>
 
// function to reverse digits of num
int reverse(int num)
{
    int rev = 0;
    while (num > 0)
    {
        rev = rev * 10 + num % 10;
        num = num / 10;
    }
    return rev;
}
 
//Check if the number is palindrome or not
int isPalindrome(int n)
{
 
    //call the function reverse(n)
    int rev = reverse(n);
 
    // Check if rev and n are equal or not.
    if (rev == n)
        return 1;
    else
        return 0;
}
 
//main function
int main()
{
    int n,res;
    printf("Enter the number: ");
    scanf("%d",&n);
    res = isPalindrome(n);  //Call the function isPalindrome
    if(res==1)
        printf("%d is a palindrome number.",n);
    else
        printf("%d is not a palindrome number.",n);
    return 0;
}