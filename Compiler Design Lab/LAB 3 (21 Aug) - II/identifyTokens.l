%{
    #include<stdio.h>
    int tokenCount = 0;
%}

letter [A-Za-z_]
digit [0-9]

%%
int|void|if|else|while|switch  {printf("%s : keyword (length: %d)\n", yytext, yyleng); tokenCount++;}
{letter}({letter}|{digit})*    {printf("%s : identifier (length: %d)\n", yytext, yyleng); tokenCount++;}
"+"|"/"|"*"|"-"|"%"|"**"       {printf("%s : operator (length: %d)\n", yytext, yyleng); tokenCount++;}
"("|")"|"{"|"}"|";"|":"|"\\"|"|"|","|"["|"]"   {printf("%s : separator (length: %d)\n", yytext, yyleng); tokenCount++;}

%%

void main()
{
    yyin = fopen("input.txt","r");
    yylex();
    printf("Total tokens: %d\n", tokenCount);
}

int yywrap()
{
    return 1;
}