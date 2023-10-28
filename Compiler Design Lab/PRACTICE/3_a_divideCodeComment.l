%{
#include<stdio.h>
#include<string.h>
int count = 0;
FILE *comment;
FILE *code;
%}

%%
"/*"[a-zA-Z0-9 \t\n]+"*/" {fprintf(comment, "%s\n", yytext);}
"//"[a-zA-Z0-9 \t]+"\n" {fprintf(comment, "%s\n", yytext);}
.|\n {fprintf(code, "%s", yytext);}
%%

int main()
{
    yyin = fopen("3_a_input.txt", "r");
    comment=fopen("3_a_comment.txt", "w");
    code=fopen("3_a_code.txt", "w");
    yylex();
    fclose(yyin);
}

int yywrap() {
    return 1;
}