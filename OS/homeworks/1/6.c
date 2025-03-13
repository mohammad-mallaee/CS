#include <stdio.h>
#include <stdlib.h>
#include <math.h>

// print sigma of (selected k from n) * x^k * a^(n-k)

int fact(int n) {
    int result = 1;
    for(int i=n; i>=1; i--) {
        result *= i;
    }
    return result;
}

int main() {
    int a, x, n;

    scanf("%d %d %d", &a, &x, &n);

    int result = 0;
    for (int k = 0; k <= n; k++) {
        result += (fact(n) / (fact(k) * fact(n - k))) * pow(x, k) * pow(a, n - k);
    }

    printf("%d\n", result);

    return 0;
}