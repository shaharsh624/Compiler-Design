%option noyywrap
%{
    #include<stdio.h>
    int count_char = 0;
    int count_word = 1;
    int count_line = 1;
%}

%%
"\n" {count_line++; count_word++; count_char++;}
" " {count_word++; count_char++;}
. {count_char++;}
%%

int main(){
    yyin =fopen("3_b_input.txt", "r");
    yylex();
    printf("Characters: %d", count_char);
    printf("\nWords: %d", count_word);
    printf("\nLines: %d", count_line);
    fclose(yyin);
    return 0;
}