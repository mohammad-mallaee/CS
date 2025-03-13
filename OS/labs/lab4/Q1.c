#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h>

/*
    Q1. Create two child process C1 and C2.
    Make sure that only C2 becomes an orphan process.
*/

int main()
{
    pid_t C_1 = fork();
    if (0 == C_1)
    {
        printf("C_1 is having ID %d \n", getpid());
        printf("C_1 exiting \n");
    }
    else
    {
        wait(NULL);
        pid_t C_2 = fork();
        if (0 == C_2)
        {
            sleep(3);
            printf("C_2 is having ID %d\n", getpid());
            printf("C_2 exiting \n");
        }
        else
        {
            printf("Parent is having ID %d \n", getpid());
            printf("Parent exiting \n");
        }
    }
    return 0;
}