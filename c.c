#include <stdio.h>
#include <stdlib.h>

typedef struct Node {
    int vertex;
    struct Node* next;
}NODE;

struct Graph {
    int numVertices;
    NODE** adjList;
};

NODE* createNode(int point) {
    NODE* newNode = (NODE*)malloc(sizeof(NODE));
    newNode->vertex = point;
    newNode->next = NULL;
    return newNode;
}

struct Graph* createGraph(int num) {
    struct Graph* graph = (struct Graph*)malloc(sizeof(struct Graph));
    graph->numVertices = num;
    graph->adjList = (NODE*)malloc((num + 1) * sizeof(NODE));

    for (int i = 1; i <= num; i++) {
        graph->adjList[i] = NULL;
    }

    return graph;
}

void addEdge(struct Graph* graph, int src, int dest) {
    NODE* newNode = createNode(dest);
    newNode->next = graph->adjList[src];
    graph->adjList[src] = newNode;

    newNode = createNode(src);
    newNode->next = graph->adjList[dest];
    graph->adjList[dest] = newNode;
}

int findFarthestNode(struct Graph* graph, int startNode) {
    if (graph->numVertices == 0) {
        return -1;
    }

    int* visited = (int*)malloc((graph->numVertices + 1) * sizeof(int));
    int farthestNode = -1;
    int* queue = (int*)malloc((graph->numVertices + 1) * sizeof(int));
    int front = 0, rear = 0;

    for (int i = 1; i <= graph->numVertices; i++) {
        visited[i] = 0;
    }

    visited[startNode] = 1;
    queue[rear++] = startNode;

    while (front < rear) {
        int currentNode = queue[front++];
        farthestNode = currentNode;

        NODE* current = graph->adjList[currentNode];
        while (current != NULL) {
            int neighbor = current->vertex;
            if (!visited[neighbor]) {
                visited[neighbor] = 1;
                queue[rear++] = neighbor;
            }
            current = current->next;
        }
    }

    free(visited);
    free(queue);

    if (farthestNode == startNode) {
        return -1;
    }

    return farthestNode;
}

int main() {
    int numVertices, numEdges;
    scanf("%d %d", &numVertices, &numEdges);

    if (numVertices == 0) {
        printf("-1\n");
        return 0;
    }

    struct Graph* graph = createGraph(numVertices);

    for (int i = 0; i < numEdges; i++) {
        int src, dest;
        scanf("%d %d", &src, &dest);
        addEdge(graph, src, dest);
    }

    int startNode;
    scanf("%d", &startNode);
    int farthestNode = findFarthestNode(graph, startNode);

    if (farthestNode == -1 && farthestNode==0) {
        printf("-1\n");
    } else {
        printf("%d\n", farthestNode);
    }

    free(graph->adjList);
    free(graph);

    return 0;
}