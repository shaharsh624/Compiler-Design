%{
#include <stdio.h>
FILE *commentsFile;
%}


%%


\/\/(.*) {
    fprintf(commentsFile, "%s\n", yytext);
}


\/\*(.*\n)*.*\*\/ {
    fprintf(commentsFile, "%s\n", yytext);
}

%%


int yywrap() {
    return 1;
}


int main() {
    yyin = fopen("input.c", "r");
    yyout = fopen("out.c", "w");
    commentsFile = fopen("comments.txt", "w"); 

    yylex();

    fclose(yyin);
    fclose(yyout);
    fclose(commentsFile); 

    return 0;
}