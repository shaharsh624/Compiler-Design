%option noyywrap
%{
    #include <stdio.h>
%}

%%
[0-9]+ {
    int num = atoi(yytext);
    if (num%7==0){
        num += 3;
    }
    printf("%d\n", num);
}
%%

int main(){
    yylex();
    return 0;
}