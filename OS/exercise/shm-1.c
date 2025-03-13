#include <sys/shm.h>
#include <stdio.h>
#include <string.h>
#include <unistd.h>

#define MAX_SIZE 64

int main()
{
    printf("Waitin for shared memory ...\n");
    int shmid2 = shmget((key_t)2222, MAX_SIZE, 0666);
    while (shmid2 == -1)
    {
        sleep(2);
        shmid2 = shmget((key_t)2222, MAX_SIZE, 0666);
    }
    void *shm2 = shmat(shmid2, NULL, 0);
    printf("Listening for kill signal ...\n");
    while (0 != strcmp((char *)shm2, "kill"))
    {
        sleep(2);
    }
    printf("Recevied kill signal from B\n");
    strcpy(shm2, "seen");
    return 0;
}