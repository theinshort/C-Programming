/*
 * C program to read a string and check if it is a 
 * palindrome. Display the result.
 */
 
#include <stdio.h>
#include <string.h>
#include <strings.h>
 
void isPalindromeStr(char str[], int len)
{
    char reverse_string[32] = { '\0' };
    for (int i = len - 1; i >= 0; i--)
    {
        reverse_string[len - i - 1] = str[i];
    }
 
    /* Compare the input string and its reverse. If both are equal
     * then the input string is palindrome. */
    printf("%s reversed is %s therefore ", str, reverse_string);
 
    // strcasecmp is defined in strings.h
    if (!strcasecmp(str, reverse_string))	
        printf("%s is a palindrome. \n", str);
    else
        printf("%s is not a palindrome. \n", str);
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
    int length = (int)strlen(str);
    isPalindromeStr(str, length);
    return 0;
}