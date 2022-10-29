#include <stdio.h>

signed char a;
signed char b;

int main(void) {
    scanf("%hhd %hhd", &a, &b);
    printf("%hhd + %hhd is %hhd\n",a, b, a + b);
    printf("%hhd - %hhd is %hhd\n",a, b, a - b);
    printf("%hhd * %hhd is %hhd\n",a, b, a * b);
    printf("%hhd / %hhd is %hhd\n",a, b, a / b);
    printf("-%hhd is %hhd\n", a, -a);
    printf("%hhd %% %hhd is %hhd\n",a, b, a % b);
    printf("%hhd == %hhd is %hhd\n",a, b, a == b);
    printf("%hhd != %hhd is %hhd\n",a, b, a != b);
    printf("%hhd > %hhd is %hhd\n",a, b, a > b);
    printf("%hhd < %hhd is %hhd\n",a, b, a < b);
    printf("%hhd >= %hhd is %hhd\n",a, b, a >= b);
    printf("%hhd <= %hhd is %hhd\n",a, b, a <= b);
    printf("%hhd && %hhd is %hhd\n",a, b, a && b);
    printf("%hhd & %hhd is %hhd\n",a, b, a & b);
    printf("%hhd || %hhd is %hhd\n",a, b, a || b);
    printf("%hhd | %hhd is %hhd\n",a, b, a | b);
    printf("!%hhd is %hhd\n",a, b, !a);
    printf("~%hhd is %hhd\n",a, b, ~a);
    printf("%hhd ^ %hhd is %hhd\n",a, b, a ^ b);
    printf("%hhd << 1 is %hhd\n",a, a << 1);
    printf("%hhd >> 1 is %hhd\n",a, a >> 1);
    signed char c = -127;
    printf("-127 - 1 is %hhd\n", c - 1);
    printf("-127 - 2 is %hhd\n", c - 2);
    printf("-127 / 0 is %hhd\n", c / 0);
    return 0;
}

    
