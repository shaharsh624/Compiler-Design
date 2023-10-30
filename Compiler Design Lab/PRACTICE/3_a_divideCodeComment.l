%{
    #include<stdio.h>
    #include<string.h>
    int count = 0;
    FILE *comment;
    FILE *code;
    int multiComment = 0;
    int singleComment = 0;
%}

%%
"/*"[a-zA-Z0-9 \t\n]+"*/" {fprintf(comment, "%s\n", yytext); multiComment++;}
"//"[a-zA-Z0-9 \t]+"\n" {fprintf(comment, "%s\n", yytext); singleComment++;}
.|\n {fprintf(code, "%s", yytext);}
%%

int main()
{
    yyin = fopen("3_a_input.txt", "r");
    comment=fopen("3_a_comment.txt", "w");
    code=fopen("3_a_code.txt", "w");
    yylex();
    printf("Multiline Comments: %d", multiComment);
    printf("\nSingle Line Comments: %d", singleComment);
    fclose(yyin);
}

int yywrap() {
    return 1;
}