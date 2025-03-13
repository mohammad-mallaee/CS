#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>

/*
    Q2. Create a parent-child relationship between two processes such that
    the Child process creates a file named Relation.txt and the Parent process
    write some content into it by taking the input from the user.
*/

int main()
{
    FILE *file;
    pid_t pid = fork();
    if (0 == pid)
    {
        file = fopen("Relation.txt", "w");
        if (NULL == file)
        {
            exit(1);
        }
        fclose(file);
    }
    else
    {
        int exit_status;
        wait(&exit_status);
        if (0 == exit_status)
        {
            char input[256];
            // You have to use fopen() in parent too, otherwise you will get a segmentation fault error.
            file = fopen("Relation.txt", "w");

            printf("Enter text to write to file\n");
            fgets(input, sizeof(input), stdin);
            fprintf(file, "%s", input);

            fclose(file);
            printf("File written successfully\n");
        }
        else
        {
            printf("Error on creating file\n");
            exit(1);
        }
    }
    return 0;
}