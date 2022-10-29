#include <stdio.h>

void cursed(int* p0, int* p1, int* p2) {
    int n0;
    int n1;
    int n2;
    scanf("%d", &n0);
    scanf("%d", &n1);
    scanf("%d", &n2);

    if (n0 > 0) {
        *p1 = n1;
        *p2 = n2;
    } else {
        *p2 = n0 * n1 * n2 * (*p1) * (*p2);
        *p1 = *p0;
    }
    *p0 = n0; 
}

int main() {
    int v0 = 1;
    int v1 = 2;
    int v2 = 3;

    cursed(&v0, &v1, &v2);
    printf("%d %d %d\n", v0, v1, v2);

    return 0;
}

/*
input:
-1
3
3

output:
-1 1 -54
*/