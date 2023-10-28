/* Lex program to recognise keywords, numbers, words in a given statement */

%{
#include<stdio.h>
%}

%%
if|else|printf|break|char|continue|float|int|long|while {printf("%s is a keyword\n", yytext);}
[0-9]+ {printf("%s is a number\n", yytext);}
[a-zA-Z]+ {printf("%s is a word\n", yytext);}
.|\n {printf("");}
%%

int main() {
    printf("Enter some statement: \n");
    yylex();
}

int yywrap() {
    return 1;
}