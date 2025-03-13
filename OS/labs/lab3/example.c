#include <stdio.h>
#include <unistd.h>

int main()
{
    pid_t pid = fork();
    if (0 == pid)
    {
        printf("Child having ID %d\n", getpid());
    }
    else
    {
        printf("Parent having ID %d\n", getpid());
        sleep(10);
    }
    return 0;
}