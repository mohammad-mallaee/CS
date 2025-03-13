#include <stdio.h>
#include <string.h>
#include <pthread.h>
#include <stdlib.h>
#include <sys/shm.h>
#include <unistd.h>

#define TEXT_SIZE 2048
#define SHM_READ 11021
#define SHM_WRITE 11022

struct ThreadArguments
{
    char *text;
    char *search;
};

void *count(void *thread_arg)
{
    struct ThreadArguments arg = *((struct ThreadArguments *)thread_arg);
    int textLength = strlen(arg.text);
    int searchLength = strlen(arg.search);
    int j = 0;
    int *occurrences = (int *)malloc(sizeof(int));
    for (int i = 0; i < textLength; i++)
    {
        if (*(arg.text + i) != *(arg.search + j))
        {
            continue;
        }
        j++;
        if (j == searchLength)
        {
            *occurrences = *occurrences + 1;
            j = 0;
        }
    }
    free(thread_arg);
    return (void *)occurrences;
}

pthread_t run_count_thread(char *text, char *search)
{
    pthread_t t;
    struct ThreadArguments *arg = malloc(sizeof(struct ThreadArguments));
    *arg = (struct ThreadArguments){text, search};
    pthread_create(&t, NULL, count, (void *)arg);
    return t;
}

int main()
{
    int shmid_read = shmget((key_t)SHM_READ, TEXT_SIZE, 0666);
    while (shmid_read == -1)
    {
        sleep(1);
        shmid_read = shmget((key_t)SHM_READ, TEXT_SIZE, 0666);
    }
    void *shm_read = shmat(shmid_read, NULL, 0);
    char *text = (char *)shm_read;
    
    int *linux_counts, *bsd_counts;
    pthread_t t1 = run_count_thread(text, "Linux");
    pthread_t t2 = run_count_thread(text, "BSD");
    pthread_join(t1, (void *)&linux_counts);
    pthread_join(t2, (void *)&bsd_counts);
    int occurrences = *bsd_counts + *linux_counts;

    int shmid_write = shmget((key_t)SHM_WRITE, TEXT_SIZE, 0666 | IPC_CREAT);
    void *shm_write = shmat(shmid_write, NULL, 0);
    char *t = (char *)shm_write;
    sprintf(t, "%d", occurrences);

    return 0;
}