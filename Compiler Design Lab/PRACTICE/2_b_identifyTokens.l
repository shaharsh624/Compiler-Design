%option noyywrap
%{
    #include<stdio.h>
%}

/* "printf("|"scanf("[.]+")" {printf("\nFormal String: %s", yytext);} */

%%
if|else|return|int|float|for|while {printf("\nKeyword: %s", yytext);}
[a-zA-Z][a-zA-Z0-9]* {printf("\nIdentifier: %s", yytext);}
[0-9]+ {printf("\nNumber: %s", yytext);}
"+"|"*"|"-"|"/"|"^" {printf("\nOperator: %s", yytext);}
","|";" {printf("\nSeperator: %s", yytext);}
.|\n {printf("");}
%%

int main(){
    yyin = fopen("2_a_input.c", "r");
    yylex();
    fclose(yyin);
    return 0;
}