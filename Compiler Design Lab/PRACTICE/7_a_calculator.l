%option noyywrap

%{
#include <stdio.h>
#include "7_a_calculator.tab.h"
int yylval;
%}

%%
[)] {return yytext[0];}
[(] {return yytext[0];}
[0-9][0-9]* {yylval=atoi(yytext); return ID;}
[0-9][0-9]*/[!|@|#|$|^|&|=] {return 0;}
[-+*/%] {return yytext[0];}
\n {return 0;}
[!|@|#|$|^|&|=] {return 0;}
. {return yytext[0];}

%%