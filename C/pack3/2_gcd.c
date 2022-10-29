#include <stdio.h>
#include <assert.h>

int gcd(int a, int b) { //- a / b
    assert(a > 0 && b > 0);
    while ((a != 0) && (b != 0)) {
        if (a >= b) {
            a = a % b;
        } else {
            b = b % a;
        }
    }
    return a + b;
}

void unit_test(int values[][2], int *ans, size_t size) {
    for (size_t i = 0; i < size; i++) {
        assert(values[i][0] > 0 && values[i][1]);

        assert(gcd(values[i][0], values[i][1]) == ans[i]);
        printf("Test %lu passed\n", i);
    }

}

int main() {
    int test_values[][2] = {{4, 2}, {55, 11}, {64, 32}, {213213, 41325}};
    int ans[] = {2, 11, 32, 3};
    unit_test(test_values, ans, sizeof(test_values) / sizeof(test_values[0]));
    return 0;
}