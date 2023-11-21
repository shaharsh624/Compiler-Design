%{
#include <stdio.h>
%}

%%
^[a-zA-Z]*   {
    for (int i = yyleng; i >= 1; i--) {
        printf("%.*s\n", i, yytext);
    }
    return 0;
}

.|\n

%%

int main() {
    yylex();
    return 0;
}

int yywrap(){
    return 1;
}