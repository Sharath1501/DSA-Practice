#include <bits/stdc++.h> 
#include<vector>
using namespace std;

int partition(vector<int> &arr, int low, int high) {
    int pivot = arr[low];
    int i = low;
    int j = high;
    while (i < j) {
        while (arr[i] > pivot && i <= high - 1) {
            i++;
        }
        while (arr[j] <= pivot && j >= low + 1) {
            j--;
        }
        if (i < j) swap(arr[i], arr[j]);
    }
    swap(arr[low], arr[j]);
    return j;
}

void qs(vector<int> &arr, int low, int high) {
    if (low < high) {
        int piindex = partition(arr, low, high);
        qs(arr, low, piindex - 1);
        qs(arr, piindex + 1, high);
    }
}

int main() {
    vector<int> arr = {4, 3, 23, 1, 2};  // Using vector instead of array
    qs(arr, 0, arr.size() - 1);

    // Output the sorted array
    for (int i = 0; i < arr.size(); i++) {
        cout << arr[i] << " ";
    }
    cout << endl;

    return 0;  // Return 0 to indicate successful execution
}
