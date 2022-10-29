#include <stdio.h>
#include <assert.h>

int countDeviders(int x) {
    assert(x > 0);
    size_t counter = 0;
    for (int i = x; i > 0; i--) {
        counter += ((x % i == 0) & 1);
    }

    return counter;
}

void unit_test(int *values, int *ans, size_t size) {
    for (size_t i = 0; i < size; i++) {
        assert(values[i] > 0);

        assert(countDeviders(values[i]) == ans[i]);
        printf("Test %lu passed\n", i);
    }

}

int main() {
    int test_values[] = {24, 432, 4, 66, 2};
    int ans[] = {8, 20, 3, 8, 2};
    unit_test(test_values, ans, sizeof(test_values) / sizeof(test_values[0]));
    return 0;
}