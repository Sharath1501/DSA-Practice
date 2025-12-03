#include<bits/stdc++.h>
using namespace std;

class node{
    public:
    int data;
    node* next;
    node* back;

    // Constructor to initialize a node with given data and pointers
    node(int data1, node* next1 = nullptr, node* back1 = nullptr){
        data = data1;
        next = next1;
        back = back1;
    }
};

// Function to convert a vector into a doubly linked list
node* convertll(vector<int> arr){
    node* head = new node(arr[0]);  // Create the head node
    node* prev = head;
    
    for(int i = 1; i < arr.size(); i++){
        node* temp = new node(arr[i], nullptr, prev);  // Create a new node with 'prev' as its back pointer
        prev->next = temp;  // Link the previous node's next to the new node
        prev = temp;  // Move the 'prev' pointer forward
    }
    return head;  // Return the head of the linked list
}

// Function to delete the first node of the list
node* deletefirst(node* head){
    if(head == nullptr || head->next == nullptr){  // If the list is empty or has only one node
        delete head;
        return nullptr;
    }
    
    node* temp = head;  // Store the current head
    head = head->next;  // Move head to the next node
    head->back = nullptr;  // Set the new head's back to null
    delete temp;  // Delete the old head
    return head;
}

// Function to delete the last node of the list
node* deletelast(node* head){
    if(head == nullptr || head->next == nullptr){  // If the list is empty or has only one node
        delete head;
        return nullptr;
    }
    
    node* temp = head;
    while(temp->next != nullptr){  // Traverse to the last node
        temp = temp->next;
    }
    
    temp->back->next = nullptr;  // Disconnect the last node from the list
    delete temp;  // Delete the last node
    return head;
}

// Function to delete a node at a specific index k (1-based index)
node* deleteatindex(node* head, int k){
    if(head == nullptr) return nullptr;  // Handle empty list case
    
    if(k == 1){  // If k = 1, delete the first node
        return deletefirst(head);
    }
    
    node* temp = head;
    int cnt = 1;

    // Traverse to the node at index k
    while(temp != nullptr && cnt < k){
        temp = temp->next;
        cnt++;
    }
    
    if(temp == nullptr) return head;  // If k is out of bounds, return the list unchanged
    
    if(temp->next == nullptr){  // If temp is the last node
        return deletelast(head);
    }
    if(temp->back == nullptr){  // If temp is the first node (already handled above)
        return deletefirst(head);
    }

    // If temp is a middle node
    node* prev = temp->back;
    node* next = temp->next;
    
    prev->next = next;  // Connect previous node to next node
    next->back = prev;  // Connect next node to previous node
    
    // Disconnect temp from the list
    temp->back = nullptr;
    temp->next = nullptr;
    
    delete temp;  // Delete the node at index k
    return head;
}
node* insertbefore(node* head,int val){
    node* temp = new node(val,head,nullptr);
    head->back = temp;
    return temp;
}
node* afterinsert(node* head,int val){
    node* temp = head;
    while(temp->next != NULL){
        temp = temp->next;
    }
    node* newtail = new node(val,nullptr,temp);
    temp->next =  newtail;
    return head;
}

// Function to print the doubly linked list
void print(node* head){
    while(head != nullptr){
        cout << head->data << " ";  // Print the data of each node
        head = head->next;  // Move to the next node
    }
    cout << endl;
}

int main(){
    vector<int> arr = {12, 3, 7, 8};
    node* head = convertll(arr);  // Convert vector to linked list

   // head = deleteatindex(head, 3);  
   // Delete the node at index 3
    head = insertbefore(head,5);
    head = afterinsert(head,11);
    print(head);  // Print the updated list
    
    return 0;
}
