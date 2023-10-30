%{
#include <stdio.h>
%}

%%
[0-9]+ {
    int num = atoi(yytext); // Convert matched text to an integer
    if (num % 7 == 0) {
        num += 3;
    }
    printf("Output: %d ", num);
}
%%

int main() {
    yylex(); 
}

int yywrap() {
    return 1;
}