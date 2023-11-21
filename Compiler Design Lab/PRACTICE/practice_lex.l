%option noyywrap

%{
    #include<stdio.h>
%}

%%
[a-zA-Z0-9]+ {printf("Token: %s, Length: %d\n", yytext, yyleng);}
.|\n {printf("");}
%%

int main(){
    printf("Enter Something: \n");
    scanf("%d", yyin);
    yylex();
    return 0;
}