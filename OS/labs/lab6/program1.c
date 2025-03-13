#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
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
    my_msg.type = 1;
    char buffer[MAX_TEXT];

    msgid = msgget((key_t)1234, 0666 | IPC_CREAT);
    if (msgid == -1)
    {
        printf("msgget failed with error\n");
        exit(-1);
    }
    printf("msgid = %d\n", msgid);

    while (running)
    {
        printf("Enter your message: ");
        fgets(buffer, sizeof(buffer), stdin);
        strcpy(my_msg.text, buffer);
        if (msgsnd(msgid, (void *)&my_msg, MAX_TEXT, 0) == -1)
        {
            printf("msgsnd failed\n");
            exit(-1);
        }
        if (strncmp(buffer, "end", 3) == 0)
        {
            running = 0;
        }
    }
}
