#include <stdio.h>
#include <unistd.h>

// Yeganeh Rastegari : 4014013040
// Alireza Ahmadi : 4014013007

int main()
{
    printf("I'm root\n");
    pid_t A = fork();
    if (A == 0)
    {
        printf("I'm A\n");
        pid_t C = fork();
        if (C == 0)
        {
            printf("I'm C\n");
        }
    }
    else
    {
        pid_t B = fork();
        if (B == 0)
        {
            printf("I'm B\n");
            pid_t D = fork();
            if (D == 0)
            {
                printf("I'm D\n");
            }
            else
            {
                pid_t E = fork();
                if (E == 0)
                {
                    printf("I'm E\n");
                }
            }
        }
    }
    return 0;
}