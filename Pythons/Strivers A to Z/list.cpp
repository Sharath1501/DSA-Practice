#include<bits/stdc++.h>
using namespace std;
class node{
    public:
    int data;
    node* next;
    public:
    node(int data1){
        data = data1;
        next = nullptr;
    }
};

node* convertss(vector<int> &arr){
    node* head = new node(arr[0]);
    node* mover = head;
    for(int i=1;i<arr.size();i++){
        node* temp= new node(arr[i]);
        mover->next = temp;
        mover = temp;
    }
    return head;
}

node* deleteatlast(node* head){
    if(head == NULL || head->next == NULL) return head;
    node* temp = head;
    while(temp->next->next){
        temp = temp->next;
    }
    free(temp->next);
    temp->next = nullptr;
    return head; 
}
node* deletek(node* head,int datas){
    if(head == NULL) return head;
    if(head->data == datas){
        node* temp = head;
        head= head->next;
        free(temp);
          return head;
    }
   node* temp = head;
   node* prev = NULL;
    while(temp!=NULL){
     if(temp->data == datas){
        prev->next = prev->next->next;
        free(temp);
        break;
     }
     prev = temp;
     temp = temp->next;
    }
    return head;
  
}
node* insertlast(node* head, int val){
  if(head == NULL) return new node(val);
  node* temp = head;
  while(temp->next){
    temp = temp->next;
  }
  node* newnode = new node(val);
  temp->next = newnode;
  return head;
}

int main(){
    vector<int>arr = {23,3,4,5};
    node* head =convertss(arr);

    head = insertlast(head,50);
     node* temp = head;
    while(temp){
       cout<< temp->data<<endl;
       temp = temp->next;
    }

    return 0;
}