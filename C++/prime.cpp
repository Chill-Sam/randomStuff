#include <iostream>
using namespace std;

int main() {
    int MAX_VAL;
    cout << "Input a number: ";
    cin >> MAX_VAL;
    int* primes = new int[MAX_VAL];
    for (int i = 1; i < MAX_VAL + 1; i++) {
        primes[i] = i;
    }
    primes[0] = 0;
    primes[1] = 0;

    int p = 2;
    while (p * p <= MAX_VAL) {
        if (p != 0) {
            for (int i = p * 2; i < MAX_VAL + 1; i = i + p) {
                primes[i] = 0;
            }
        }
        p = p + 1;
    }
    for ( int i = 1; i < MAX_VAL + 1; i++) {
        if (primes[i] != 0) {
            cout << primes[i] << "\n";
        }
    }
}