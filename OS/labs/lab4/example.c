#include <stdio.h>
#include <unistd.h>

int main()
{
    pid_t p = fork();
    if (0 == p)
    {
        sleep(3);
        printf("I'm child having PID %d \n", getpid());
        printf("My parent PID is %d \n", getppid());
    }
    else
    {
        printf("I'm parent is having PID %d \n", getpid());
        printf("My child PID is %d \n", p);
    }
    return 0;
}