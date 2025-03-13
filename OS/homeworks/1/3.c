#include <stdio.h>
#include <stdlib.h>

// first n fibonacci numbers as + and - string

int main() {
    int fib_1 = 1;
    int fib_2 = 2;
    int n;

    scanf("%d", &n);

    for(int i = 1; i <= n; i++) {
        if(i<fib_1) {
            printf("-");
        }
        if (i == fib_1) {
            printf("+");
            int temp = fib_1 + fib_2;
            fib_1 = fib_2;
            fib_2 = temp;
        }
    }
    printf("\n");

    return 0;
}