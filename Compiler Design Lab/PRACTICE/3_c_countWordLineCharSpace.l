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
    yyin = fopen("3_c_input.txt", "r");
    yylex();
    printf("Number of words: %d\n", count_word);
    printf("Number of line: %d\n", count_line);
    printf("Number of char: %d\n", count_char);
    printf("Number of spaces: %d\n", count_space);
    fclose(yyin);
}

int yywrap()
{
    return 1;
}