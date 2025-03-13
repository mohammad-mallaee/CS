#include <stdio.h>
#include <unistd.h>
#include <string.h>
#include <sys/shm.h>
#include <sys/wait.h>
#include <sys/msg.h>

#define MAX_SIZE 64

struct Msg
{
    long int type;
    char text[MAX_SIZE];
};

int main()
{
    int shmid1 = shmget((key_t)1111, MAX_SIZE, 0666 | IPC_CREAT);
    void *shm1 = shmat(shmid1, NULL, 0);

    int msgid = msgget((key_t)2222, 0666 | IPC_CREAT);

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
            sleep(1);
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
                sleep(1);
            }
            printf("Recevied kill signal from A\n");
            strcpy(shm1, "seen");
            struct Msg kill_msg;
            strcpy(kill_msg.text, "kill");
            kill_msg.type = 1;
            printf("Sending kill signal to P2\n");
            int a = msgsnd(msgid, (void *)&kill_msg, MAX_SIZE, 0);
            struct Msg seen_msg;
            while (0 != strcmp((char *)seen_msg.text, "seen"))
            {
                msgrcv(msgid, (void *)&seen_msg, MAX_SIZE, 2, 0);
            }
            printf("Received seen signal from P2\n");
            msgctl(msgid, IPC_RMID, 0);
        }
        else
        {
            wait(NULL);
            wait(NULL);
        }
    }

    return 0;
}