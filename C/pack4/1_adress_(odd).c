#include <stdio.h>

int * foo() {
    int local = 0;
    return &local;
    // foo returns nil smh 
}

int * bar() {
    return foo();
}

int main() {
    printf("%p %p\n", foo(), bar());
    printf("%d\n", foo() == bar());
    return 0;
}