#include<stdio.h>
#include<stdlib.h>
struct node{
    int n_;
    struct node* next_;
};
typedef struct node node_t;
struct list{
    node_t* head_;
};
typedef struct list list_t;
list_t* initialize_list();
node_t* initialize_node(int);
void insert_node_begin(list_t*, node_t*);
void delete_node(list_t*, int);
int search_list(list_t*, int);
void print_list(list_t*);
void destroy_list(list_t*);

int main(){
    list_t* list = initialize_list();
    char choice;
    int number;
    int flag = 1;
    while(flag){
        printf("\nAdd a node at the beginning - 1\nDelete a node - 2\nSearch a node - 3\nPrint linked list -4\n");
        scanf(" %c",&choice);
        switch(choice){
            case '1':
                printf("\nEnter number to be added to the list: \n");
                scanf("%d",&number);
                node_t* node = initialize_node(number);
                insert_node_begin(list, node);
                break;
            case '2':
                printf("\nEnter number to be deleted from the list: \n");
                scanf("%d",&number);
                delete_node(list, number);
                break;
            case '3':
                printf("\nEnter number to be searched in the list: \n");
                scanf("%d",&number);
                int res = search_list(list, number);
                printf("Number is at index = %d\n",res);
                break;
            case '4':
                print_list(list);
                break;
            default:
                flag = 0;
        }
    }
    destroy_list(list);
    free(list);

    return 0;
}
list_t* initialize_list(){
    list_t* list = (list_t*)malloc(sizeof(list_t));
    list->head_ = NULL;
    return list;
}
node_t* initialize_node(int n){
    node_t* temp = (node_t*)malloc(sizeof(node_t));
    temp->n_ = n;
    temp->next_ = NULL;
    return temp;
}

void insert_node_begin(list_t* list, node_t* node){
    node_t* current = list->head_;
    if(current == NULL){
        list->head_ = node;
        return;
    }
    node->next_ = current;
    list->head_ = node;
}

void delete_node(list_t* list, int n){
    node_t* current = list->head_;
    if(current == NULL)
        return;
    node_t* previous = NULL;
    while(current != NULL && current->n_ != n){
        previous = current;
        current = current->next_;
    }
    //does not exist
    if(current == NULL)
        return;
    //middle or at the end
    else if(current != NULL && previous != NULL && current->n_ == n){
        previous->next_ = current->next_;
        free(current);
        current = NULL;
    //first element
    }else if(previous == NULL && current !=  NULL && current->n_ == n){
        node_t* temp = current;
        list->head_ = current->next_;
        free(temp);
        temp = NULL;
    }
}
int search_list(list_t* list, int n){
    node_t* current = list->head_;
    if(current == NULL)
        return -1;
    node_t* previous = NULL;
    int i = 0;
    while(current != NULL && current->n_ != n){
        previous = current;
        current = current->next_;
        i++;
    }
    if(current != NULL && current->n_ == n)
        return i;
    return -1;
}
void print_list(list_t* list){
    node_t* current = list->head_;
    if(current == NULL)
        return;
    node_t* previous = NULL;   
    printf("\n");
    while(current != NULL){
        printf("%d ",current->n_);
        previous = current;
        current = current->next_;
    }
    printf("\n");
}
void destroy_list(list_t* list){
    node_t* current = list->head_;
    if(current == NULL)
        return;
    node_t* previous = NULL;   
    while(current != NULL){
        previous = current;
        current = current->next_;
        free(previous);
        previous = NULL;
    }
}