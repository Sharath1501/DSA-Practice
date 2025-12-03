#include<bits/stdc++.h>
using namespace std;
class node{
    public:
    int data;
    node* next;
    node* back;

    public:
    node(int data1,node* next1,node* back1){
        data = data1;
        next = next1;
        back = back1;
    }

    public:
    node(int data1){
        data = data1;
        next = nullptr;
        back = nullptr;
    }
};
node* convertarr(vector<int> &arr){
    node* head = new node(arr[0]);
    node* prev =head;
    for(int i=1;i<arr.size();i++){
        node* temp = new node(arr[i],nullptr,prev);
        prev->next = temp;
        prev = temp;
    }
    return head;
}
node* deletehead(node* head){
    if(head == NULL) return NULL;
    node* prev = head;
    head = head->next;
    prev->next = nullptr;
    head->back = nullptr;
    delete prev;
    return head;
}
node* deletelast(node* head){
    if(head == NULL || head->next == NULL) return NULL;
    node* tail = head;
    while(tail->next != NULL){
        tail = tail->next;
    }
    node* newtail = tail->back;
    newtail->next = nullptr;
    tail->back = nullptr;
    delete tail;
    return head;
    
}
int main(){
    vector<int> arr = {2,3,45,5};
    node* head = convertarr(arr);
    node* ank = deletelast(head);
    node* temp = ank;
    while(temp){
        cout<<temp->data<<endl;
        temp = temp->next;
    }
    return 0;
}