%{
    #include<stdio.h>
    #include<stdlib.h>
%}

%token ID
%left '+' '-'
%left '*' '/'

%%
S : E {
    printf("Result=%d\n",$1);
    exit(0);
}

E : E '+' E     {$$ = $1 + $3;}
  | E '-' E     {$$ = $1 - $3;}  
  | E '*' E     {$$ = $1 * $3;}
  | E '/' E     {$$ = $1 / $3;}
  | E '^' E     {$$ = $1 ^ $3;}
  | '(' E ')'   {$$ = $2;}
  | ID         {$$ = $1;}
  ;
%%

int yyerror()
{
    printf("Invalid Expression!");
    exit(0);
}

int main()
{
    printf("Enter the expression:");
    yyparse();
    return 0;
}