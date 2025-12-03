#include <bits/stdc++.h>
using namespace std;

// Class to implement a stack using a single queue
class Q {
    queue<int> qt;

public:
    // Push element x onto stack
    void push(int x) {
        int s = qt.size();
        qt.push(x);
        for (int i = 0; i < s; i++) {
            qt.push(qt.front());
            qt.pop();
        }
    }

    // Removes the element on top of the stack
    void pop() {
        if (!qt.empty()) {
            qt.pop();
        } else {
            cout << "Stack is empty. Cannot pop." << endl;
        }
    }

    // Get the top element
    int top() {
        if (!qt.empty()) {
            return qt.front();
        } else {
            cout << "Stack is empty." << endl;
            return -1; // Return a sentinel value
        }
    }

    // Check if the stack is empty
    bool empty() {
        return qt.empty();
    }
};

int main() {
    Q stack;

    stack.push(10);
    stack.push(20);
    stack.push(30);

    cout << "Top element: " << stack.top() << endl;

    stack.pop();
    cout << "Top element after one pop: " << stack.top() << endl;

    stack.pop();
    stack.pop();
    stack.pop(); // Attempt to pop from empty stack

    return 0;
}
