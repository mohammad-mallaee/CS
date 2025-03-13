#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

// a^2 + b^2 = c^2

int main() {
    int a, b, c;

    scanf("%d", &a);
    scanf("%d", &b);
    scanf("%d", &c);

    bool first = a * a + b * b == c * c;
    bool second = a * a + c * c == b * b;
    bool third = b * b + c * c == a * a;

    if (first || second || third) {
        printf("YES\n");
    } else {
        printf("NO\n");
    }

    return 0;
}