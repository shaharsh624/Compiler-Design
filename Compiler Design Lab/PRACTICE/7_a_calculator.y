%{
#include<stdio.h>
int yylex();
void yyerror(char* s);
%}

%token ID
%left '+''-'
%left '*''/''%'

%%
S:E {
    printf("Result = %d\n", $1);
}

E : E '+' E     {$$ = $1 + $3;}
|   E '-' E     {$$ = $1 - $3;}
|   E '*' E     {$$ = $1 * $3;}
|   E '/' E     {$$ = $1 / $3;}
|   E '%' E     {$$ = $1 % $3;}
|   '(' E ')'   {$$ = $2;}
|   ID          {$$ = $1;}
;
%%

int main() {
    printf("\nEnter the expression: ");
    yyparse();
}

void yyerror(char *msg) {
    fprintf(stderr, "Error: %s\n", msg);
}