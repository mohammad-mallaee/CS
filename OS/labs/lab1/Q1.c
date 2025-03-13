#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>

/*
    Q1. Write a program using fork() system call
    to create two child of the same process i.e.,
    Parent P having child process P1 and P2.
*/

int main()
{
    pid_t P1;
    printf("before fork \n");
    P1 = fork();
    if (P1 == 0)
    {
        printf("I'm P1 having pid %d, my parent pid is %d \n", getpid(), getppid());
    }
    else
    {
        pid_t P2 = fork();
        if (P2 == 0)
        {
            printf("I'm P2 having pid %d, my parent pid is %d \n", getpid(), getppid());
        }
        else
        {
            printf("I'm parent having pid %d \n", getpid());
            printf("My child pids are P1=%d, P2=%d \n", P1, P2);
        }
    }
    printf("Common \n");
    return 0;
}