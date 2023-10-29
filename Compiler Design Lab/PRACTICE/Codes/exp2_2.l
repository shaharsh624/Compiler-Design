%{
#include <stdio.h>
%}
%option noyywrap 
%%
int|float|char|string|if|else|while|for|return|void|main   { printf("Keyword: %s\n", yytext); }
[a-zA-Z_][a-zA-Z0-9_]*    { printf("Identifier: %s\n", yytext); }
[0-9]+                   { printf("Number: %s\n", yytext); }
.                         { printf("Other: %s\n", yytext); }

%%
int main() {
    yylex();
    return 0;
}
