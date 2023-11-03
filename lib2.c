#include<stdio.h>
#include<string.h>
#include<stdlib.h>

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

int main(){
	printf("WELCOME TO LIBRARY");
	char username[20];
	char password[20];
	int x;
	while(1){
    printf("\n\nStaff Login: Enter 1");
	printf("\nStudent Login: Enter 2");
    printf("\n\nNow enter your choice:-");
	scanf("%d",&x);
    
    switch (x){
        case 1:
		    printf("\n\n\tWelcome Dear Staff");
            printf("\n\nEnter the Username : ");
	        scanf("%s",&username[10]);
    	
			printf("\nEnter the Password : ");
			scanf("%s",&password[10]);
    
			if(strcmp(username, "Staff") && strcmp(password, "Staff@123")){
    		  printf("\n\n\tLogin Successfull\t\n");
			}
			else{
    		printf("\n\n\tWrong credentials!!\t");
  		  	}
            break;
 
        case 2:
	    	printf("\n\n\tWelcome Dear Student");
            printf("\n\nEnter the Username : ");
	        scanf("%s",&username[10]);
    	
			printf("\nEnter the Password : ");
			scanf("%s",&password[10]);
    
			if(strcmp(username, "Student") && strcmp(password, "Student@123")){
    		  printf("\n\n\tLogin Successfull\t\n");
			}
			else{
    		printf("\n\n\tWrong credentials!!\t");
  		  	}
            break;
 
        default:
            printf("Default case is Matched.");
            break;
	}
	}
	return 0;
}