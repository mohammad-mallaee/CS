#include <stdio.h>
#include <unistd.h>

// Yeganeh Rastegari : 4014013040
// Alireza Ahmadi : 4014013007

int main()
{
    pid_t A = fork();
    if (A == 0)
    {
        pid_t C = fork();
        if (C == 0)
        {
            printf("I'm C and my pid is %d \n", getpid());
        }
        else
        {
            printf("I'm A and my PID is %d and my child C has PID %d \n", getpid(), C);
        }
    }
    else
    {
        pid_t B = fork();
        if (B == 0)
        {
            printf("I'm B and my PID is %d\n", getpid());
            pid_t D = fork();
            if (D == 0)
            {
                printf("I'm D and PID is %d \n", getpid());
            }
            else
            {
                pid_t E = fork();
                if (E == 0)
                {
                    printf("I'm E and my PID is %d\n", getpid());
                }
                else
                {
                    printf("I'm B with id: %d and child E has PID %d and chld D has PID %d \n", getpid(), E, D);
                }
            }
        }
        else
        {
            printf("I'm root with id: %d and child A has PID %d and chld B has PID %d \n", getpid(), A, B);
        }
    }
    return 0;
}