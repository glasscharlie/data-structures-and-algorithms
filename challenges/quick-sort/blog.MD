## Quick Sort

Quick sort is based on the divide-and-conquer approach, it chooses one element as a pivot element and partitions the list around it such that the left side of pivot contains all the elements that are less than the pivot element, and right side contains all elements greater than the pivot

lets use the list [8,4,23,42,16,15] as our example.

it first selects a random element from the list to use our pivot, in our example lets use 16 as the pivot. it then splits the other elements into list that are lower elements and higher elements from the pivot.
[8,4,15] 16  [23,42]

since the list still have multiple values in them, it recursively calls itself, lets say the left partition is 8, and the right is 42.
It will sort the left list into two lists, one with elements lower than 8, and one with elements higher. The right list will move 42 into an array on the right side of 23, as it has a higher value.
[4]8[15] 16 23 [42]

It wont recursively go down anymore, because all of the numbers are seperated. Now it has all the elements sorted from smallest to largest, so it combines them all back into the list. 
[4,8,15,16,23,42]