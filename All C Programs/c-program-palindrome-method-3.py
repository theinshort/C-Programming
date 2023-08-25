/* C Program to check number is Palindrome or Not using recursion*/
 
#include <stdio.h>
 
//Check if the number is palindrome or not
int isPalindrome(int n,int rev)
{
    if (n==0)
        return rev;
 
    //calculate reverse of the number
    rev = rev * 10 + n % 10;
    isPalindrome(n/10,rev);
}
 
//main function
int main()
{
    int n,res,rev=0;
    printf("Enter the number: ");
    scanf("%d",&n);
    res = isPalindrome(n,rev);  //Call the function isPalindrome
    if(res==n)
        printf("%d is a palindrome number.",n);
    else
        printf("%d is not a palindrome number.",n);
    return 0;
}