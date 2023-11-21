%option noyywrap

%{
#include<stdio.h>    
%}

%%
[a-zA-Z0-9][a-zA-Z0-9]*([+-/*]+[a-zA-Z0-9][a-zA-Z0-9]*)* {printf("Valid Expression: %s \n", yytext);}
['\n'] {printf("");}
. {printf("Invalid Expression: %s \n", yytext);}
%%


int main(){
    yyin = fopen("exam_1_1.txt", "r");
    yylex();
    fclose(yyin);
}