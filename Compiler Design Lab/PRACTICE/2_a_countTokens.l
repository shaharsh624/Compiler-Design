%option noyywrap
%{
    #include<stdio.h>
%}

%%
[a-zA-Z]+ {printf("\n\nToken: %s\nLength %d", yytext, yyleng);}
[0-9]+ {printf("\n\nToken: %s\nLength %d", yytext, yyleng);}
.|\n {printf("");}
%%

int main()
{
    yyin = fopen("2_a_input.c", "r");
    yylex();
    fclose(yyin);
    return 0;
}