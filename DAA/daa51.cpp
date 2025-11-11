#include <bits/stdc++.h>
using namespace std;

// Randomized partition (self-contained)
int randomizedPartition(vector<int> &arr, int low, int high, int &comparisons, int &swaps) {
    int randomIndex = low + rand() % (high - low + 1);
    swap(arr[low], arr[randomIndex]);
    swaps++;

    int pivot = arr[low];
    int left = low + 1, right = high;

    while (true) {
        while (left <= right && arr[left] <= pivot) { left++; comparisons++; }
        while (left <= right && arr[right] > pivot) { right--; comparisons++; }
        if (left > right) break;
        swap(arr[left], arr[right]);
        swaps++;
    }
    swap(arr[low], arr[right]);
    swaps++;
    return right;
}

void randomizedQuickSort(vector<int> &arr, int low, int high, int &comparisons, int &swaps) {
    if (low < high) {
        int pivotIndex = randomizedPartition(arr, low, high, comparisons, swaps);
        randomizedQuickSort(arr, low, pivotIndex - 1, comparisons, swaps);
        randomizedQuickSort(arr, pivotIndex + 1, high, comparisons, swaps);
    }
}

// Deterministic (for comparison)
int deterministicPartition(vector<int> &arr, int low, int high, int &comparisons, int &swaps) {
    int pivot = arr[low];
    int left = low + 1, right = high;

    while (true) {
        while (left <= right && arr[left] <= pivot) { left++; comparisons++; }
        while (left <= right && arr[right] > pivot) { right--; comparisons++; }
        if (left > right) break;
        swap(arr[left], arr[right]);
        swaps++;
    }
    swap(arr[low], arr[right]);
    swaps++;
    return right;
}

void deterministicQuickSort(vector<int> &arr, int low, int high, int &comparisons, int &swaps) {
    if (low < high) {
        int pivotIndex = deterministicPartition(arr, low, high, comparisons, swaps);
        deterministicQuickSort(arr, low, pivotIndex - 1, comparisons, swaps);
        deterministicQuickSort(arr, pivotIndex + 1, high, comparisons, swaps);
    }
}

// Helper
void printArray(const vector<int> &arr) {
    for (int num : arr) cout << num << " ";
    cout << endl;
}

int main() {
    srand(time(0));
    int n;
    cout << "Enter number of elements: ";
    cin >> n;

    vector<int> arr(n);
    cout << "Enter elements: ";
    for (int i = 0; i < n; i++) cin >> arr[i];

    vector<int> arrDet = arr, arrRand = arr;

    int ch;
    while (true) {
        cout << "\n1. Deterministic Quick Sort\n2. Randomized Quick Sort\n3. Exit\nEnter your choice: ";
        cin >> ch;

        int comparisons = 0, swaps = 0;
        if (ch == 1) {
            cout << "\nOriginal array: ";
            printArray(arrDet);
            deterministicQuickSort(arrDet, 0, n - 1, comparisons, swaps);
            cout << "Sorted array: ";
            printArray(arrDet);
            cout << "Comparisons: " << comparisons << ", Swaps: " << swaps << endl;
        } 
        else if (ch == 2) {
            cout << "\nOriginal array: ";
            printArray(arrRand);
            randomizedQuickSort(arrRand, 0, n - 1, comparisons, swaps);
            cout << "Sorted array: ";
            printArray(arrRand);
            cout << "Comparisons: " << comparisons << ", Swaps: " << swaps << endl;
        } 
        else break;
    }
    return 0;
}
