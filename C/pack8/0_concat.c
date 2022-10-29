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

size_t concat(int* arr1, size_t lenArr1, int* arr2, size_t lenArr2, int** retArr) {
    int* newArr = (int* )malloc((lenArr1 + lenArr2) * sizeof(int)); 
    
    size_t i = 0;
    while (i < lenArr1) {
        newArr[i] = arr1[i];
        i++;
    }

    for (size_t j = 0; j < lenArr2; j++) {
        newArr[i + j] = arr2[j];
    }    

    *retArr = newArr;
    return lenArr1 + lenArr2;
}

void runTests() {
    int* arr1;
    size_t lenArr1;
    int* arr2;
    size_t lenArr2;
    int* res;
    size_t lenRes;
    int* out = NULL;

    // Test 1
    arr1 = (int[] ){1, 2, 3, 4};
    lenArr1 = 4;
    arr2 = (int[] ){5, 6};
    lenArr2 = 2;
    res = (int[] ){1, 2, 3, 4, 5, 6};
    lenRes = lenArr1 + lenArr2;

    assert(concat(arr1, lenArr1, arr2, lenArr2, &out) == lenRes);
    assert(isEqArray(res, out, lenRes));
    free(out);
    printf("Test 1 passed\n");
    //

    // Test 2
    arr1 = (int[] ){1, 2, 3, 4};
    lenArr1 = 4;
    arr2 = (int[] ){1, 2, 3, 4, 5};
    lenArr2 = 5;
    res = (int[] ){1, 2, 3, 4, 1, 2, 3, 4, 5};
    lenRes = lenArr1 + lenArr2;

    assert(concat(arr1, lenArr1, arr2, lenArr2, &out) == lenRes);
    assert(isEqArray(res, out, lenRes));
    free(out);
    printf("Test 2 passed\n");
    //

    // Test 3
    arr1 = (int[] ){1, 2, 3, 4};
    lenArr1 = 4;
    arr2 = NULL;
    lenArr2 = 0;
    res = (int[] ){1, 2, 3, 4};
    lenRes = lenArr1 + lenArr2;

    assert(concat(arr1, lenArr1, arr2, lenArr2, &out) == lenRes);
    assert(isEqArray(res, out, lenRes));
    free(out);
    printf("Test 3 passed\n");
    //

    // Test 4
    arr1 = NULL;
    lenArr1 = 0;
    arr2 = (int[] ){1, 2, 3, 4};
    lenArr2 = 4;
    res = (int[] ){1, 2, 3, 4};
    lenRes = lenArr1 + lenArr2;

    assert(concat(arr1, lenArr1, arr2, lenArr2, &out) == lenRes);
    assert(isEqArray(res, out, lenRes));
    free(out);
    printf("Test 4 passed\n");
    //
}

int main() {
    runTests();
    return 0;
}