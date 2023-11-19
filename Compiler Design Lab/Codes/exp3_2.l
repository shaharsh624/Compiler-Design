%{
#include<stdio.h>
int charCount = 0;
int wordCount = 0;
int lineCount = 0;
%}

%option noyywrap

%%
\n      { ++lineCount; ++charCount; }
[ \t]   { ++charCount; }
[^ \t\n] { ++charCount; ++wordCount; }
%%

int main(int argc, char *argv[]) {
    yyin = fopen(argv[1], "r");
    yylex();
    fclose(yyin);
    printf("Number of lines : %d\n", lineCount);
    printf("Number of words : %d\n", wordCount);
    printf("Number of characters : %d\n", charCount);
    return 0;
}