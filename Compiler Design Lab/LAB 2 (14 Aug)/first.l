%{
#include<stdio.h>
%}

%%
"hi" { printf("hello\n"); }
.* { printf("Given input is not available.\n"); }
%%

int main()
{
    printf("Enter your input: ");
    yylex();
    return 0;
}

int yywrap()
{
    return 1;
}
