#include <iostream>
using namespace std;

void swapArray(int arr1[], int arr2[], int n) {
    int temp, i;
  
    for(i = 0; i < n; i++) {
        temp = arr1[i];
        arr1[i] = arr2[i];
        arr2[i] = temp;
    }
}

int main() {
    int i;
    int arr1[] = {10, 20, 50, 85, 72, 12, 24};
    int arr2[] = {20, 50, 70, 80, 75, 35, 12};
    
   
    swapArray(arr1, arr2, 7);

    for(i = 0; i < 7; i++)
        cout << arr1[i] << " ";
    cout << "\n";
    
    for(i = 0; i < 7; i++)
        cout << arr2[i] << " ";
        
    return 0;
}