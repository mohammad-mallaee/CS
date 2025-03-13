#include <stdio.h>
#include <stdlib.h>

// print a diamond

int main() {
    int n;
    scanf("%d", &n);

    for(int i = 0; i < 2*n+1; i++) {
        for (int j = 0; j < abs(n - i); j++) {
            printf(" ");
        }
        int stars = 2*(n - abs(n - i)) + 1;
        for (int j = 0; j < stars; j++) {
            printf("*");
        }
        for (int j = 0; j < abs(n - i); j++) {
            printf(" ");
        }
        printf("\n");
    }

    return 0;
}