#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>

/*
    Q2. Write a program using fork() system call to
    create a hierarchy of 3 process such that
    P2 is the child of P1 and P1 is the child of P.
*/

int main()
{
    pid_t P1;
    printf("before fork \n");
    P1 = fork();
    if (P1 == 0)
    {
        printf("I'm P1 having pid %d, my parent pid is %d \n", getpid(), getppid());
        pid_t P2 = fork();
        if (P2 == 0)
        {
            printf("I'm P2 having pid %d, my parent pid is %d \n", getpid(), getppid());
        }
        else
        {
            printf("I'm P1 and my child pid is %d \n", P2);
        }
    }
    else
    {
        printf("I'm parent having pid %d \n", getpid());
        printf("My child pid is %d \n", P1);
    }
    printf("Common \n");
    return 0;
}