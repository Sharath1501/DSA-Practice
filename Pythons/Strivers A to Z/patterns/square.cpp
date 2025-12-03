#include <iostream>
#include <thread>
#include <chrono> // For std::chrono::seconds
using namespace std;

void taskA() {
    for (int i = 0; i < 10; i++) {
        std::this_thread::sleep_for(std::chrono::seconds(1)); // Correct usage
        printf("Task A : %d\n", i); // Fixed newline character
        fflush(stdout); // Ensure output is flushed
    }
}

void taskB() {
    for (int i = 0; i < 10; i++) {
        std::this_thread::sleep_for(std::chrono::seconds(1)); // Correct usage
        printf("Task B : %d\n", i); // Fixed newline character
        fflush(stdout); // Ensure output is flushed
    }
}

int main() {
    std::thread t1(taskA); // Fixed missing std:: namespace
    std::thread t2(taskB); // Fixed missing std:: namespace

    t1.join(); // Ensure threads complete before program exit
    t2.join();

    return 0;
}
