/* * C Program to find the ascii value of all characters in a string */ #include <stdio.h> int main(){    char str[100];     //Input string    printf("Enter String: ");    gets(str);    int i=0;     //Iterating over string    while(str[i]!='\0')    {        //Printing ascii value by typecasting        printf("Ascii value of %c : %d\n",str[i],(int)str[i]);        ++i;    }    return 0;}