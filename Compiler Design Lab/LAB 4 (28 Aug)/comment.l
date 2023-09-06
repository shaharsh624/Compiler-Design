%{
#include<stdio.h>
#include<string.h>
int count=0;
%}


%%
"/*"[a-zA-Z0-9 \t\n]+"*/" {count++;}
"//"[a-zA-Z0-9 \t]+ {count++;}
%%

int main()
{
    yyin = fopen("input.txt", "r");
    yylex();
    fclose(yyin);
    printf("Number of comment lines: %d", count);
}

int yywrap()
{
    return 1;
}