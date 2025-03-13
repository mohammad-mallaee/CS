#include <stdio.h>
#include <unistd.h>

/*
    Q1. Create a scenario where a parent has two child process C1 and C2
    such that C1 becomes a zombie while C2 becomes an orphan process.
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
        sleep(5);
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