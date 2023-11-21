%{
#include <stdio.h>
%}

%%
^i.*   {
        int count = 0;
        for (int i = 0; i < yyleng; i++) {
            if (yytext[i] == 'a' || yytext[i] == 'e' || yytext[i] == 'i' || yytext[i] == 'o' || yytext[i] == 'u' ||
                yytext[i] == 'A' || yytext[i] == 'E' || yytext[i] == 'I' || yytext[i] == 'O' || yytext[i] == 'U') {
                count++;
            }
        }
        printf("\nLine starting with 'i': %s\nNumber of vowels: %d\n", yytext, count);
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