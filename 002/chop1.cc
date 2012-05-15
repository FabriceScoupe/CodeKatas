/* +=+=+=+ Code Kata Two: Binary Chop +=+=+=+ */

// Recursion
int chop(int value, int* items, int size)
{
    int idx = -1;
    if (size > 1) {
        int mid = size / 2;
        if (value <= items[mid-1]) {
            idx = chop(value, items, mid);
        } else {
            idx = chop(value, &items[mid], size-mid);
            if (idx >= 0) idx += mid;
        }
    } else if (value == items[0]) {
        idx = 0;
    }
    return idx;
}
