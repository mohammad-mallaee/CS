#include <stdio.h>
#include <unistd.h>
#include <string.h>
#include <sys/shm.h>
#include <sys/wait.h>

#define MAX_SIZE 64

int main()
{
    int shmid1 = shmget((key_t)1111, MAX_SIZE, 0666 | IPC_CREAT);
    void *shm1 = shmat(shmid1, NULL, 0);

    int shmid2 = shmget((key_t)2222, MAX_SIZE, 0666 | IPC_CREAT);
    void *shm2 = shmat(shmid2, NULL, 0);

    pid_t A = fork();
    if (0 == A)
    {
        char msg[MAX_SIZE];
        while (1)
        {
            printf("Enter the command:\n");
            fgets(msg, MAX_SIZE, stdin);
            if (0 == strncmp(msg, "kill", 4))
            {
                break;
            }
            printf("For killing threads, type 'kill'\n");
        }
        printf("Sending kill signal to B\n");
        strcpy(shm1, "kill");
        while (0 != strcmp((char *)shm1, "seen"))
        {
            sleep(2);
        }
        printf("Received seen signal from B\n");
    }
    else
    {
        pid_t B = fork();
        if (B == 0)
        {
            while (0 != strcmp((char *)shm1, "kill"))
            {
                sleep(2);
            }
            printf("Recevied kill signal from A\n");
            strcpy(shm1, "seen");
            printf("Sending kill signal to P2\n");
            strcpy(shm2, "kill");
            while (0 != strcmp((char *)shm2, "seen"))
            {
                sleep(2);
            }
            printf("Received seen signal from P2\n");
        }
        else
        {
            wait(NULL);
            wait(NULL);
        }
    }

    return 0;
}