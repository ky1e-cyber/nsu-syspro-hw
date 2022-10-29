#include <stdio.h>
#include <stdlib.h>
#include <stddef.h>
#include <stdio.h>
#include <assert.h>

int isEqArray(int* arr1, int* arr2, size_t size) {
    for (size_t i = 0; i < size; i++) {
        if (arr1[i] != arr2[i]) {
            return 0;
        }
    }
    return 1;
}

int findSubArr(int* arr, size_t sizeArr, int* sub, size_t sizeSub) {
    if (sizeSub > sizeArr) {
        return -1;
    }

    for (size_t i = 0; i <= sizeArr - sizeSub; i++) {
        if (isEqArray(arr + i, sub, sizeSub)) {
            return i;
        }    
    }
    
    return -1;
}

void runTests() {
    int* arr;
    size_t lenArr;
    int* sub;
    size_t lenSub;

    // Test 1
    arr = (int[] ){0, 1, 8, 7, 4, 1, 8, 7, 6};
    lenArr = 9;
    sub = (int[] ){8, 7};
    lenSub = 2;
    assert(findSubArr(arr, lenArr, sub, lenSub) == 2);
    printf("Test 1 passed\n");
    //

    // Test 2
    arr = (int[] ){14, 6, 7};
    lenArr = 3;
    sub = (int[] ){1, 2, 3};
    lenSub = 3;
    assert(findSubArr(arr, lenArr, sub, lenSub) == -1);
    printf("Test 2 passed\n");
    //

    // Test 3
    arr = (int[] ){5, 21, 2, 4, 1}; 
    lenArr = 5;
    sub = NULL;
    lenSub = 0;
    assert(findSubArr(arr, lenArr, sub, lenSub) == 0);
    printf("Test 3 passed\n");
    //

    // Test 4
    arr = NULL; 
    lenArr = 0;
    sub = NULL;
    lenSub = 0;
    assert(findSubArr(arr, lenArr, sub, lenSub) == 0);
    printf("Test 4 passed\n");
    //
}

int main() {
    runTests();
    return 0;
}