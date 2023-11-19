%option noyywrap
%{
    #include "prac2.tab.h"
%}

%%
a   {   return A;}
b   {   return B;}
[\n]    {   return "\n";}
%%