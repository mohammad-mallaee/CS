#include <stdio.h>
#include <sys/shm.h>
#include <unistd.h>
#include <string.h>
#include <stdlib.h>

/*
    Q1. Write a program to create a shared memory segment of 2048 bytes
    and write some content into it. Then create a child process which then
    reads the content written by the parent process in the shared memory segment.
*/

int main()
{
    int shmid;
    void *shared_memory;
    char buffer[100];

    shmid = shmget((key_t)9999, 2048, 0666 | IPC_CREAT);
    if (shmid == -1)
    {
        printf("shmget failed");
        exit(1);
    }
    printf("Key of shared memory is %d \n", shmid);

    shared_memory = shmat(shmid, NULL, 0);
    printf("Process attached at %p \n", shared_memory);
    printf("Enter some data to write to shared memory\n");
    fgets(buffer, sizeof(buffer), stdin);

    strcpy(shared_memory, buffer);
    printf("You wrote: %s \n", (char *)shared_memory);

    pid_t pid = fork();
    if (0 == pid)
    {
        printf("I'm child having ID %d \n", getpid());
        printf("Shared memory data: %s \n", (char *)shared_memory);
    }
    else
    {
        wait(NULL);
    }

    if (shmdt(shared_memory) == -1)
    {
        perror("shmdt failed");
        exit(1);
    }
    printf("Shared memory detached \n");

    return 0;
}