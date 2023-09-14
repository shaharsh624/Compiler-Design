%{
#include<stdio.h>
int num;
int choice=1;
%}

%%

%%

int main()
{
    while (choice==1) {
        printf("Enter a number to check divisibility: ");
        scanf("%f", &num);
        if (num % 7 == 0) {
            num += 3;
            printf("Number after adding 3: %f", num);
        }
        else {
            printf("Not divisible by 7");
        }
        printf("\nEnter 1 to continue: ");
        scanf("%d", &choice);
    }
}

int yywrap()
{
    return 1;
}