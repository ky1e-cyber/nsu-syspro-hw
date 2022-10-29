#include <stdio.h>
#include <inttypes.h>
#include <assert.h>

int max(int a, int b) {
    return a > b ? a : b;
}

int maxInTen(int *values) {
    int maxValue = values[0];
    for (uint8_t i = 1; i < 10; i++) {
        maxValue = max(maxValue, values[i]);
    }
    return maxValue;
}

void unit_test(int values[][10], int *ans, size_t size) {
    for (size_t i = 0; i < size; i++) {
        assert(values[i] > 0);

        assert(maxInTen(values[i]) == ans[i]);
        printf("Test %lu passed\n", i);
    }

}

int main() {
    int values[][10] = {{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}, {41, 432, 553, 0, -13, 31, 2, 6, 9, 0}, {-1, -1, -100, 0, -2, -33, -55, -8, -10, -9}};
    int ans[] = {10, 553, 0};
    unit_test(values, ans, sizeof(values) / sizeof(values[0]));
    return 0;
}