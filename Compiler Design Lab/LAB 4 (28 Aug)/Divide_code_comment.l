%{
#include<stdio.h>
#include<string.h>
%}


%%

"/*"[a-zA-Z0-9 \t\n]+"*/" {comments = fopen("comments.txt", "a");}
"//"[a-zA-Z0-9 \t\n]+ {comments = fopen("comments.txt", "a");}
. codes = fopen("codes.txt", "a");

fclose(comments);
fclose(codes);
%%

int main()
{
    yyin = fopen("input.txt", "r");
    yylex();
    fclose(yyin);
    return 0;
}
