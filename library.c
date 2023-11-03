#include <stdio.h>
#include <stdlib.h>
#include <string.h>


struct book{
    char name[30];
    char author[30];
    int id;
    struct book *next;
};

struct student{
    char name[30];
    char email[20];
    char book[20];
    char a[30];
    int id;
    struct student *next;
};

void main_menu();
int main(){
    main_menu();
    return 0;
}


void main_menu(){
    int choice;
    while(1){
        printf(" MAIN MENU: ");
        printf("1.ISSUE OF BOOKS ");
        printf("2.RETURN OF BOOKS ");
        printf("3.EXIT\n ");
        printf(" Enter your choice: ");
        scanf("%d",&choice);
        switch(choice){
            case 1:{
                break;
            }
            case 2:{
                break;
            }
            case 3:{
                exit(1);
            }
            default:{
                printf("Invalid Option");
            }
        }
    }
}