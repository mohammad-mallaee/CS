#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h>

/*
    Q1. 
    Create a parent-child relationship between two processes. The parent should print two statements:
        A) Parent (P) is having ID < PID >
        B) ID of P’s Child is < PID_of_Child >
    The child should print two statements:
        C) Child is having ID < PID >
        D) My Parent ID is < PID_of_Parent >
    Make use of wait() in such a manner that the order of the four statements A, B, C and D is:
        A C D B
*/

int main()
{
    printf("Parent (P) is having ID %d\n", getpid());
    pid_t pid = fork();
    if (0 == pid) {
        printf("Child is having ID %d\n", getpid());
        printf("My Parent ID is %d\n", getppid());
    } else {
        wait(NULL);
        printf("ID of P’s Child is %d\n", pid);
    }
    return 0;
}
