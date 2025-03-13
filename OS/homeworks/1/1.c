#include <stdio.h>
#include <stdlib.h>

// n!

int main() {
    int n;
    int result = 1;
    scanf("%d", &n);
    for(int i=n; i>=1; i--) {
        result *= i;
    }
    printf("%d\n", result);
    return 0;
}