#include <stdio.h>

int a;
int b;

int main(void) {
    scanf("%d %d", &a, &b);
    printf("%d + %d is %d\n",a, b, a + b);
    printf("%d - %d is %d\n",a, b, a - b);
    printf("%d * %d is %d\n",a, b, a * b);
    if (b == 0) {
        printf("Can't devide by zero (b = 0)\n");
        
    } else {
        printf("%d %% %d is %d\n",a, b, a % b);
        printf("%d / %d is %d\n",a, b, a / b);
    }
    
    printf("-%d is %d\n", a, -a);
    printf("%d == %d is %d\n",a, b, a == b);
    printf("%d != %d is %d\n",a, b, a != b);
    printf("%d > %d is %d\n",a, b, a > b);
    printf("%d < %d is %d\n",a, b, a < b);
    printf("%d >= %d is %d\n",a, b, a >= b);
    printf("%d <= %d is %d\n",a, b, a <= b);
    printf("%d && %d is %d\n",a, b, a && b);
    printf("%d & %d is %d\n",a, b, a & b);
    printf("%d || %d is %d\n",a, b, a || b);
    printf("%d | %d is %d\n",a, b, a | b);
    printf("!%d is %d\n",a, !a);
    printf("~%d is %d\n",a, ~a);
    printf("%d ^ %d is %d\n",a, b, a ^ b);
    printf("%d << 1 is %d\n",a, a << 1);
    printf("%d >> 1 is %d\n",a, a >> 1);
    return 0;
}

    
