%{
#include<stdio.h>
int singleLineComment = 0;
int multiLineComment = 0;
FILE *f1;
FILE *f2;
%}

%%
"//"[a-zA-Z0-9 \t]+"\n" {fprintf(f1, "%s\n", yytext); singleLineComment++;}
"/*"[a-zA-Z0-9 \t\n]"*/" {fprintf(f1, "%s\n", yytext); multiLineComment++;}
.|\n {fprintf(f2, "%s\n", yytext);}
%%

int main(){
    yyin = fopen("3_a_input.txt", "r");
    comment=fopen("3_a_comment.txt", "w");
    code=fopen("3_a_code.txt", "w");
    yylex();
    fclose(yyin);
    fclose(comment);
    fclose(code);

    printf("Multi line Comments: %d", multiLineComment);
    printf("Single line Comments: %d", singleLineComment);
}