%{
#include<stdio.h>
int count_word=1;
int count_char=0;    
int count_line=1;
int count_space=0;
%}

%%
" "+ {count_word++; count_space++;}
[\n]+ {count_line++; count_word++;}
. {count_char++;}
%%

int main()
{
    yyin = fopen("input.txt", "r");
    yylex();
    fclose(yyin);
    printf("\nNumber of words: %d", count_word);
    printf("\nNumber of line: %d", count_line);
    printf("\nNumber of char: %d", count_char);
    printf("\nNumber of spaces: %d", count_space);
}

int yywrap()
{
    return 1;
}