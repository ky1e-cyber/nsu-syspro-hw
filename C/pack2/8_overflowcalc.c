#include <stdio.h>
#include <inttypes.h>

// defined in inttypes.h:
// #define INT32_MAX 2147483647
// #define INT32_MIN -2147483648

int32_t min(int32_t a, int32_t b) {
    return a > b ? b : a;
}

int32_t max(int32_t a, int32_t b) {
    return a > b ? a : b;
}

void printOverflow(char *expr) {
    printf("INT32 overflow occured while computing %s\n", expr);
    return;
}

int isPlusOverflowed(int32_t a, int32_t b, int aIsNegative, int bIsNegative) {
    if (!(aIsNegative) && !(bIsNegative)) {
        if (INT32_MAX - b >= a) {
            return 0;
        }

        return 1;
    }

    if (aIsNegative && bIsNegative) {
        if (INT32_MIN - b <= a) {
            return 0;
        }

        return 1;
    }
    return 0;
}

int isMultOverflowed(int32_t a, int32_t b, int aIsNegative, int bIsNegative, int isLimitNegative) {
    if (isLimitNegative) {
        return a < (INT32_MIN / b);
    }
    if (aIsNegative && bIsNegative) { // (actually we can check only for one variable but i think that way its more readable)
        return a < (INT32_MAX / b);
    }
    return a > (INT32_MAX / b);
}


int main(void) {

    /// Init
    int32_t a = 0;
    int32_t b = 0;
    scanf("%d %d", &a, &b);

    int aIsNegative = (a < 0) & 1; // ensure that True == 1, False == 0
    int bIsNegative = (b < 0) & 1;
    ///

    /// Unary minus OP
    if (a == INT32_MIN) { 
        printOverflow("-a");
        
    } else {
        printf("-%d is %d\n", a, -a);
    }

    if (b == INT32_MIN) {
        printOverflow("-b");;
    } else {
        printf("-%d is %d\n", b, -b);
    }
    ///

    /// Plus OP
    if (isPlusOverflowed(a, b, aIsNegative, bIsNegative)) {
        printOverflow("a + b");
    } else {
        printf("%d + %d is %d\n", a, b, a + b);
    }
    ///

    /// Minus OP
    if (((b == INT32_MIN) && aIsNegative) || isPlusOverflowed(a, -b, aIsNegative, !bIsNegative)) {
        printOverflow("a - b");

    } else {
        printf("%d - %d is %d\n", a, b, a - b);
    }
    ///

    /// Mult OP
    int isLimitNegative = 0;

    if (aIsNegative ^ bIsNegative) {
        isLimitNegative = 1;
    }

    if (isMultOverflowed(min(a, b), max(a, b), aIsNegative, bIsNegative, isLimitNegative)) {
        printOverflow("a * b");

    } else {
        printf("%d * %d is %d\n", a, b, a * b);
    }
    ///

    /// Devision OP
    if (b == 0) {
        printf("Can't devide by zero (b = 0)\n");
        
    } else {
        if ((a == INT32_MIN) && (b == -1)) {
            printOverflow("a / b");
        } else {
            printf("%d / %d is %d\n", a, b, a / b);
        }
        printf("%d %% %d is %d\n", a, b, a % b); // even tho MIN / -1 is overflow, the answer is correct
    }
    ///

    /// Other..
    printf("%d == %d is %d\n", a, b, a == b);
    printf("%d != %d is %d\n", a, b, a != b);
    printf("%d > %d is %d\n", a, b, a > b);
    printf("%d < %d is %d\n", a, b, a < b);
    printf("%d >= %d is %d\n", a, b, a >= b);
    printf("%d <= %d is %d\n", a, b, a <= b);
    printf("%d && %d is %d\n", a, b, a && b);
    printf("%d & %d is %d\n", a, b, a & b);
    printf("%d || %d is %d\n", a, b, a || b);
    printf("%d | %d is %d\n", a, b, a | b);
    printf("!%d is %d\n", a, !a);
    printf("~%d is %d\n", a, ~a);
    printf("%d ^ %d is %d\n", a, b, a ^ b);
    printf("%d << 1 is %d\n", a, a << 1);
    printf("%d >> 1 is %d\n", a, a >> 1);
    ///


    return 0;
}

    
