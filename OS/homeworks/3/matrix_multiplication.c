#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>

struct ThreadArguments
{
    int **matrixA;
    int **matrixB;
    int **result;
    int rowA;
    int colB;
    int n;
};

void *vectorMultiply(void *thread_arg)
{
    struct ThreadArguments arg = *((struct ThreadArguments *)thread_arg);
    int r = 0;
    for (int i = 0; i < arg.n; i++)
    {
        r += arg.matrixA[arg.rowA][i] * arg.matrixB[i][arg.colB];
    }
    arg.result[arg.rowA][arg.colB] = r;
    free(thread_arg);
    return NULL;
}

void matrixMultiply(int **matrixA, int rowsA, int colsA,
                    int **matrixB, int rowsB, int colsB,
                    int **result)
{
    if (colsA != rowsB)
    {
        printf("Error: Incompatible matrix dimensions for multiplication.\n");
        return;
    }

    pthread_t threads[rowsA * colsB];
    int threadCounts = 0;
    for (int i = 0; i < rowsA; i++)
    {
        for (int j = 0; j < colsB; j++)
        {
            struct ThreadArguments *arg = malloc(sizeof(struct ThreadArguments));
            *arg = (struct ThreadArguments){matrixA, matrixB, result, i, j, colsA};
            pthread_create(&threads[threadCounts], NULL, vectorMultiply, (void *)arg);
            threadCounts++;
        }
    }

    for (int i = 0; i < rowsA * colsB; i++)
    {
        pthread_join(threads[i], NULL);
    }
}

void printMatrix(int **matrix, int rows, int cols)
{
    for (int i = 0; i < rows; i++)
    {
        for (int j = 0; j < cols; j++)
        {
            printf("%d\t", matrix[i][j]);
        }
        printf("\n");
    }
}

int main()
{
    int rowsA, colsA, rowsB, colsB;

    scanf("%d", &rowsA);
    scanf("%d", &colsA);
    scanf("%d", &rowsB);
    scanf("%d", &colsB);

    int **matrixA = malloc(rowsA * sizeof(int *));
    int **matrixB = malloc(rowsB * sizeof(int *));
    int **result = malloc(rowsA * sizeof(int *));

    for (int i = 0; i < rowsA; i++)
    {
        matrixA[i] = (int *)malloc(colsA * sizeof(int));
    }

    for (int i = 0; i < rowsB; i++)
    {
        matrixB[i] = (int *)malloc(colsB * sizeof(int));
    }

    for (int i = 0; i < rowsA; i++)
    {
        result[i] = (int *)malloc(colsB * sizeof(int));
    }

    for (int i = 0; i < rowsA; i++)
    {
        for (int j = 0; j < colsA; j++)
        {
            scanf("%d", &matrixA[i][j]);
        }
    }

    for (int i = 0; i < rowsB; i++)
    {
        for (int j = 0; j < colsB; j++)
        {
            scanf("%d", &matrixB[i][j]);
        }
    }

    matrixMultiply(matrixA, rowsA, colsA, matrixB, rowsB, colsB, result);

    if (colsA == rowsB)
    {
        printMatrix(result, rowsA, colsB);
    }

    for (int i = 0; i < rowsA; i++)
    {
        free(matrixA[i]);
        free(result[i]);
    }
    for (int i = 0; i < rowsB; i++)
    {
        free(matrixB[i]);
    }
    free(matrixA);
    free(matrixB);
    free(result);

    return 0;
}