#include <iostream>
#include <cstdlib>
using namespace std;

/* +=+=+=+ Code Kata Two: Binary Chop +=+=+=+ */

/*
 * Usage: chop <value> [<item0> [<item1 ... ] ]
 *        <items> must be sorted.
 *        Displays index of <value> in list of <item>s, or -1
 */

extern int chop(int value, int* items, int size);

int main(int argc, char* argv[])
{
    if (argc <= 2) {
        cout << -1 << endl;
    } else {
        int* items = new int [argc-2];
        for(int i=0; i < argc-2; ++i) items[i] = atoi(argv[i+2]);
        cout << chop(atoi(argv[1]), items, argc-2) << endl;
        delete[] items;
    }
    return 0;
}
