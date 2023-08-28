%{
    #include<stdio.h>
    int num1;
    int num2;
%}

%%
"+" {printf("%d", num1+num2);}
"-" {printf("%d", num1-num2);}
"*" {printf("%d", num1*num2);}
"/" {printf("%d", num1/num2);}
.* {printf("Invalid Input");}
%%

int main() {
    printf("Enter 1st number: ");
    scanf("%d", &num1);
    printf("Enter 2nd number: ");
    scanf("%d", &num2);
    printf("Enter the operation:");
    yylex();
    return 0;
}

int yywrap()
{
    return 1;
}
