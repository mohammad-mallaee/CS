#include <sys/shm.h>
#include <stdio.h>
#include <string.h>
#include <unistd.h>
#include <sys/msg.h>

#define MAX_SIZE 64

struct Msg
{
    long int type;
    char text[MAX_SIZE];
};

int main()
{
    printf("Listening for kill signal ...\n");
    struct Msg kill_msg;
    int msgid = msgget((key_t)2222, 0666 | IPC_CREAT);
    while (0 != strcmp((char *)kill_msg.text, "kill"))
    {
        msgrcv(msgid, (void *)&kill_msg, MAX_SIZE, 1, 0);
    }
    printf("Recevied kill signal from B\n");
    struct Msg seen_msg;
    strcpy(seen_msg.text, "seen");
    seen_msg.type = 2;
    msgsnd(msgid, (void *)&seen_msg, MAX_SIZE, 0);
    return 0;
}