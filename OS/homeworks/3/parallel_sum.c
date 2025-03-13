#include <stdio.h>
#include <sys/msg.h>
#include <unistd.h>
#include <string.h>
#include <sys/wait.h>

struct Result
{
    long int type;
    long result;
};

struct Info
{
    int m;
    int n;
    int l;
    int j;
    int msgid;
};

void calculate_sum(struct Info info);
void create_child(struct Info info);

int main()
{
    int n;
    int m;
    scanf("%d", &n);
    scanf("%d", &m);
    int l = (int)(n / m) + (n % m == 0 ? 0 : 1);
    int msgid = msgget((key_t)1829, IPC_CREAT | 0666);
    if (msgid == -1)
    {
        printf("Error creating message queue\n");
        return 1;
    }

    pid_t child = fork();
    if (child == 0)
    {
        struct Info info = {m, n, l, 0, msgid};
        calculate_sum(info);
        struct Info child_info = {m, n, l, 1, msgid};
        create_child(child_info);
    }
    else
    {
        long result = 0;
        for (int i = 0; i < m; i++)
        {
            struct Result msg;
            msgrcv(msgid, &msg, sizeof(long), 1, 0);
            result += msg.result;
        }
        printf("%ld\n", result);
        msgctl(msgid, IPC_RMID, NULL);
    }
    return 0;
}

void calculate_sum(struct Info info)
{
    long r = 0;
    int end = (info.j + 1) * info.l < info.n ? (info.j + 1) * info.l : info.n;
    for (int i = info.j * info.l + 1; i <= end; i++)
    {
        r += i;
    }
    struct Result result = {1, r};
    if (msgsnd(info.msgid, (void *)&result, sizeof(long), 0) == -1)
    {
        printf("Error sending result\n");
    }
}

void create_child(struct Info info)
{
    if (info.j >= info.m)
    {
        return;
    }

    pid_t child = fork();
    if (child == 0)
    {
        calculate_sum(info);
    }
    else
    {
        struct Info new_info = {info.m, info.n, info.l, info.j + 1, info.msgid};
        create_child(new_info);
    }
}