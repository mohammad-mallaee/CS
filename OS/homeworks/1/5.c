#include <stdio.h>
#include <stdlib.h>

// khayam-pascal triangle

int main() {
    int n;
    scanf("%d", &n);

    int lastrow[n];
    for(int i = 0; i < n; i++) {
        int newrow[n];
        for (int j = 0; j <= i; j++) {
            int number;
            if (j == 0) {
                number = 1;
            } else if (j == i) {
                number = 1;
            } else {
                number = lastrow[j - 1] + lastrow[j];
            }
            newrow[j] = number;
            printf("%d ", number);
        }
        printf("\n");
        for (int j = 0; j <= i; j++) {
            lastrow[j] = newrow[j];
        }
    }

    return 0;
}