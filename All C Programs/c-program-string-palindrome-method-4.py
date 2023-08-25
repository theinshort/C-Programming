/*
 * C program to read a string and check if it's a
 * palindrome. Display the result.
 */
 
#include <stdio.h>
#include <string.h>
#include <ctype.h>
 
void isPalindromeStr(char str[])
{
    int pt1 = 0;
    int pt2 = (int)strlen(str) - 1;
 
    while (pt2 > pt1)
    {
        if (tolower(str[pt1++]) != tolower(str[pt2--]))	
        {
            printf("%s is not a palindrome.\n", str);
            return;
        }
    }
    printf("%s is a palindrome.\n", str);
}
 
int main(void)
{
    char str[32];
    puts("Enter a string : ");
    /* gets is depreciated in favor of fgets as fgets
     * provides memory safety in terms of assigning the
     * variable with the maximum allowed size and from
     * the specified source, here stdin. */
 
    fgets(str, sizeof(str), stdin);
    strtok(str, "\n");
    isPalindromeStr(str);
    return 0;
}