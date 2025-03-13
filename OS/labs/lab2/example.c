#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>

int main()
{
    pid_t p;
    printf("before fork \n");
    p = fork();
    if (p == 0)
    {
        printf("I'm child having pid %d \n", getpid());
        printf("My parent pid is %d \n", getppid());
    }
    else
    {
        wait(NULL);
        printf("I'm parent having pid %d \n", getpid());
        printf("My child pid is %d \n", p);
    }
    printf("Common \n");
    return 0;
}