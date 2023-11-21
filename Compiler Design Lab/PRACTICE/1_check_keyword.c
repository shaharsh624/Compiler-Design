#include <stdio.h>

int main()
{
    const char *keywords[] = {
        "auto", "break", "case", "char", "const", "continue", "default",
        "do", "double", "else", "enum", "extern", "float", "for", "goto",
        "if", "int", "long", "register", "return", "short", "signed", "sizeof",
        "static", "struct", "switch", "typedef", "union", "unsigned", "void", "volatile", "while"};

    FILE *f1;
    f1 = fopen("2_a_input.c", "r");
    char myString[100];
    while (fgets(myString, 100, f1))
    {
        printf("%s", myString);
        // for (int i = 0; i < 32; i++)
        // {
        //     if (myString == keywords[i])
        //     {
                
        //     }
        // }
    }
    fclose(f1);
}