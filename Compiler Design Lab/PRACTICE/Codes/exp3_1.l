%{
#include <stdio.h>
FILE *cFile;
%}

%%
"//"              { BEGIN IN_COMMENT; fprintf(cFile, "%s\n", yytext); }
"/*"              { BEGIN IN_MULTILINE_COMMENT; fprintf(cFile, "%s", yytext); }
<IN_COMMENT>.+    { fprintf(cFile, "%s\n", yytext); }
<IN_COMMENT>\n    { BEGIN 0; fprintf(cFile, "\n"); }
<IN_MULTILINE_COMMENT>"*/" { BEGIN 0; fprintf(cFile, "*/\n"); }
<IN_MULTILINE_COMMENT>.|\n   { fprintf(cFile, "%s", yytext); }

[^/\n]*           { printf("%s", yytext); }
"//"[^/\n]*       { printf("%s", yytext); }
\n                { printf("\n"); }
"/*"              { BEGIN IN_MULTILINE_COMMENT; printf("/*"); }
.                 { printf("%s", yytext); }

%%

int main(int argc, char *argv[]) {
    if (argc != 2) {
        printf("Usage: %s input.c\n", argv[0]);
        return 1;
    }

    FILE *input_file = fopen(argv[1], "r");
    if (!input_file) {
        perror("Failed to open input file");
        return 1;
    }

    cFile = fopen("comments.txt", "w");
    if (!cFile) {
        perror("Failed to open comments.txt");
        fclose(input_file);
        return 1;
    }

    yyin = input_file;
    yylex();

    fclose(input_file);
    fclose(cFile);

    return 0;
}
