%{
    #include<stdio.h>
    int tokenCount = 0;
%}

letter [A-Za-z_]
digit [0-9]

%%
int|void|if|else|while|switch  {printf("%s is keyword (length: %d)\n", yytext, yyleng); tokenCount++;}

{letter}({letter}|{digit})* {printf("%s is identifier (length: %d)\n", yytext, yyleng); tokenCount++;}

{digit}({digit})* {printf("%s is number (length: %d)\n", yytext, yyleng); tokenCount++;}

"+"|"/"|"*"|"-"|"%"|"**"|"=" {printf("%s is operator (length: %d)\n", yytext, yyleng); tokenCount++;}

"("|")"|"{"|"}"|";"|":"|"\\"|"|"|","|"["|"]"|"#"|"<"|">"|"." {printf("%s is separator (length: %d)\n", yytext, yyleng); tokenCount++;}
.|\n {printf("");}
%%

void main()
{
    yyin = fopen("2_a_input.txt","r");
    yylex();
    printf("Total tokens: %d\n", tokenCount);
}

int yywrap()
{
    return 1;
}