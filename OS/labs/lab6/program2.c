#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <sys/ipc.h>
#include <sys/msg.h>

#define MAX_TEXT 1024

struct Msg
{
    long int type;
    char text[MAX_TEXT];
};

int main()
{
    int running = 1;
    int msgid;
    struct Msg my_msg;
    int msg_to_receive = 0;
    msgid = msgget((key_t)1234, 0666 | IPC_CREAT);
    printf("Listening for messages. To stop, enter 'end'.\n");
    while (running)
    {
        msgrcv(msgid, (void *)&my_msg, MAX_TEXT, msg_to_receive, 0);
        printf("New Message: %s", my_msg.text);
        if (strncmp(my_msg.text, "end", 3) == 0)
        {
            running = 0;
        }
    }
    msgctl(msgid, IPC_RMID, 0);
    return 0;
}
