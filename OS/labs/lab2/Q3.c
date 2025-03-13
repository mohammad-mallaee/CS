#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>

int main()
{
    pid_t P1 = fork();
    if (0 == P1)
    {
        printf("I'm P1 having pid %d, my parent pid is %d \n", getpid(), getppid());
    }
    else
    {
        pid_t P2 = fork();
        if (0 == P2)
        {
            printf("I'm P2 having pid %d, my parent pid is %d \n", getpid(), getppid());
        }
        else
        {
            wait(NULL);
            wait(NULL);
            printf("I'm parent having pid %d \n", getpid());
            printf("My child pids are P1=%d, P2=%d \n", P1, P2);
        }
    }
}