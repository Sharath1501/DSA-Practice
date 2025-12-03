#include<stdio.h>
int main(){
    int data[10];
    int datatrec[10],c,c1,c2,c3,i;
    printf("Enter the 4 bits one by one\n");
    scanf("%d",&data[0]);
    scanf("%d",&data[1]);
    scanf("%d",&data[2]);
    scanf("%d",&data[4]);

    data[6] = data[0]^data[2]^data[4];
    data[5] = data[0]^data[1]^data[4];
    data[3] = data[0]^data[1]^data[2];
    printf("Encoded data\n");
    for(i=0;i<7;i++){
        printf("%d",data[i]);
    }

    printf("Write the data encoded to recive message:\n");
    for(i=0;i<7;i++){
        scanf("%d",&datatrec[i]);
    }
    c1 = datatrec[6]^datatrec[4]^datatrec[2]^datatrec[0];
    c2 = datatrec[5]^datatrec[4]^datatrec[1]^datatrec[0];
    c3 = datatrec[3]^datatrec[2]^datatrec[1]^datatrec[0];
    c = 4*c1+2*c2+c3;

    if(c==0){
        printf("messgae recieved correctly\n");
    }
    else{
        printf("Message error -paclet loss\n");
         printf("Sent message\n");
    for(i=0;i<7;i++){
        printf("%d",data[i]);
    }

    printf("Recieved message:\n");
    for(i=0;i<7;i++){
        printf("%d",datatrec[i]);
    }
    }
    
}