//增添删除订单
#include<stdio.h>
#include<stdlib.h>
#include<string.h>


// char a[10][20]={"0","1","2","3","4","5","6","7","8","9"};


struct flight{
    char flight_id[20],departure_time[20],arrival_time[20],start[20],destination[20],company[20];
    int price,total_seats,seat_number;
    struct flight* next;
};
struct flight* now=NULL;
struct order{
    char name[20];
    struct flight* flight;
};
struct order head;
struct order head1[50];


// void insert(int i){
//     struct flight* temp=(struct flight*)malloc(sizeof(struct flight));
//     strcpy(temp->flight_id,a[i]);
//     strcpy(temp->start,a[i]);
//     strcpy(temp->destination,a[i+1]);
//     strcpy(temp->departure_time,a[i]);
//     strcpy(temp->arrival_time,a[i]);
//     strcpy(temp->company,a[i]);
//     temp->price=i;
//     temp->seat_number=i;
//     temp->next=head.flight;
//     head.flight=temp;
// }


int creat(char departure_time[],char flight_id[],int n){
    struct flight* temp1=head1[n].flight;
    while(temp1!=NULL){
        if(strcmp(temp1->departure_time,departure_time)==0&&strcmp(temp1->flight_id,flight_id)==0){
            return 0;
        }
        temp1=temp1->next;
    }
    temp1=head.flight;
    while(temp1!=NULL){
        if(strcmp(temp1->departure_time,departure_time)==0&&strcmp(temp1->flight_id,flight_id)==0){
            struct flight* temp=(struct flight*)malloc(sizeof(struct flight));
            strcpy(temp->flight_id,temp1->flight_id);
            strcpy(temp->departure_time,temp1->departure_time);
            strcpy(temp->arrival_time,temp1->arrival_time);
            strcpy(temp->start,temp1->start);
            strcpy(temp->destination,temp1->destination);
            strcpy(temp->company,temp1->company);
            temp->price=temp1->price;
            temp->total_seats=temp1->total_seats;
            temp1->seat_number--;
            temp->seat_number=temp1->seat_number;
            temp->next=head1[n].flight;
            head1[n].flight=temp;
            return 1;
        }
        temp1=temp1->next;
    }
    return 0;
}
int cancel(char departure_time[],char flight_id[],int n){
    struct flight* temp1=head1[n].flight;
    int j=0;
    while(temp1!=NULL){
        j++;
        if(strcmp(temp1->departure_time,departure_time)==0&&strcmp(temp1->flight_id,flight_id)==0){
            struct flight* temp3=head.flight;
            while(temp3!=NULL){
                if(strcmp(temp3->departure_time,departure_time)==0&&strcmp(temp3->flight_id,flight_id)==0){
                    temp3->seat_number++;
                }
                temp3=temp3->next;
            }
            if(temp1==head1[n].flight){
                head1[n].flight=temp1->next;
                free(temp1);
                return 1;
            }
            struct flight* temp2=head1[n].flight;
            for(int i=1;i<=j-2;i++){
                temp2=temp2->next;
            }
            temp2->next=temp1->next;
            free(temp1);
            return 1;
        }
        temp1=temp1->next;
    }
    return 0;
}
void print(int n){
    struct flight* temp=head1[n].flight;
    while(temp!=NULL){
        printf("%s %s %s %s %s %s %d\n",temp->flight_id,temp->departure_time,temp->arrival_time,temp->start,temp->destination,temp->company,temp->price);
        temp=temp->next;
    }
}
int main(){
    char departure_time[20],flight_id[20],name[20];
    int order_number,n=1;
    head.flight=NULL;
    // for(int i=1;i<=8;i++){
    //     insert(i);
    // }
    printf("name");
    scanf("%s",name);
    while(strcmp(name,"0")!=0){
        head1[n].flight=NULL;
        strcpy(head1[n].name,name);
        printf("1or2");
        scanf("%d",&order_number);
        while(order_number==1||order_number==2){
            if(order_number==1){
                printf("departure_time");
                scanf("%s",departure_time);
                printf("flight_id");
                scanf("%s",flight_id);
                printf("%d",creat(departure_time,flight_id,n));
            }else{
                printf("departure_time");
                scanf("%s",departure_time);
                printf("flight_id");
                scanf("%s",flight_id);
                printf("%d",cancel(departure_time,flight_id,n));
            }
            printf("1or2or3");
            scanf("%d",&order_number);
        }
        printf("name or 0");
        scanf("%s",name);
        n++;
    }
    for(int i=1;i<=n;i++){
        printf("%s\n",head1[i].name);
        print(i);
    }
    return 0;
}