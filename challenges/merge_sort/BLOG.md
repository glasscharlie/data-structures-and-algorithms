merge sort is breaking down a list into sub-lists, until each sublist consists of only one element. Then it merges those sublists back together in order.

lets look at [8,4,23,42,16,15] as our example list.

it first splits the original list in half, which gives us two lists
[8,4,23] + [42,16,15]

neither list is a single element, so it splits them again
[8,4] [23]  +  [42,16] [15]

the right most element on each side is already a single element, so it only splits the left ones
[8] [4] + [23]   +   [42] [16] + [15]

now that each list only has a single element, it compares the lists that are were last split, so in thist case 8 and 4, and 42 and 16, and sorts them into an list.

[4,8] + [23]     +   [16,42] + [15]

it then compares the two list on each side, looking at the left most value of each list and comparing them to sort them into a new list
[4,8,23]   +   [15,16,42]

it then compares the remaining list on each side, looking at the left most value of each list and comparing them to sort them into a new list.
[4,8,15,16,23,42]

our list is now sorted!