%option noyywrap

%{
#include "7_c_shift_reduce.tab.h"
%}

%%
[Tt]   { return T; }
\+    { return PLUS; }
\n    { return END; }
.     { /* Ignore other characters */ }
%%