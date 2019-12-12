# data-structures-and-algorithms

|   Challenge          |     Completed     |  Link                                                   |
|----------            |:-------------:    |------:                                                  |
| Array Reverse        |          Yes      | [here](array_reverse/array_reverse.py)                  |
| Array Shift          |          Yes      | [here] (array_shift/array_shift.py)                     |
| Array Binary Search  |          Yes      | [here] (array-binary-search/array_binary_search.py)     |
| linked-list          |          Yes      | [here] (linked-list/linked_list.py)                     |
| linked-list_three    |          Yes      | [here] (linked-list/linked_list.py)                     |
| ll-merge             |          Yes      | [here] challenges/ll_merge/ll_merge.py                  |
-------------------------------------------------------------
# Reverse an Array
print the reverse of an array without using reverse

## Challenge
Write a function called reverseArray which takes an array as an argument. Without utilizing any of the built-in methods available to your language, return an array with elements in reversed order.

## Approach & Efficiency
We took the aproach of making a for loop iterating over the length of the array that take the value of i and places it at index 0, and then grabs the rest of the array.

## Solution
[array_reverse]C:\Users\charl\Documents\codefellows\401\data-structures-and-algorithms\assets\array_reverse.jpg
-----------------------------------------------------------------------

# Array Shift
Add a value to the middle of an array

## Challenge
Write a function called add_to_middle which takes in an array and a value. Without using build it language methods, return an array with the value inserted to the middle of the array

## Approach & Efficiency
We took the aproach of deviding the length of the array in half, and then using slice to add together the first half of the array, then the value, then the second half of the array

## Solution
[array_shift]/home/glasscharlie/charl/Documents/codefellows/401/data-structures-and-algorithms/assets/array_shift.jpg
-----------------------------------------------------------------------

# Array Binary Search
Search an array for a value, return the index of that value in the array if matches

## Challenge
Write a function called binary_search that takes in a sorted array and the search key. Returns the index of the array’s element that is equal to the search key, or -1 if the element does not exist.

## Approach & Efficiency
We took the approach of making a function, then making a for loop set to the length of the array. We had a variable named i that was set at 0, if the search value matched the item in the list, it returns that value of i, if not i goes up by 1 and it checks the next thing on the list. If none of the items in the list match, it returns -1 instead.

## Solution
[array_binary_search]/home/glasscharlie/charl/Documents/codefellows/401/data-structures-and-algorithms/assets/array_binary_search.jpg
-----------------------------------------------------------------------

# linked-list
Create classes for Node and Linked-List that can add a node to the begining of the linked list.
Create methods for linked-list that can add before and after a given value, and append to the end of the list.
create a method for linked-list that can tell you the value at a length from the end of the list

## Challenge
Create a Node class that has properties for the value stored in the Node, and a pointer to the next Node. Within your LinkedList class, include a head property. Upon instantiation, an empty Linked List should be created. Create an insert, includes and toString method

## Approach & Efficiency
We took the approach of making a Node class that take in a value. Then made a linked-list class that has methods to add nodes to the linked list, check the linked list to see if a value is already inside it, and can print the linked list in the form of a string.

## soliton
[kth_from_end]/home/glasscharlie/charl/Documents/codefellows/401/data-structures-and-algorithms/assets/kth_from_end.jpg

# kth from end
create a method for linked-list that can tell you the value at a length from the end of the list

## Challenge
Write a method for the Linked List class which takes a number, k, as a parameter. Return the node’s value that is k from the end of the linked list. You have access to the Node class and all the properties on the Linked List class as well as the methods created in previous challenges.

## Approach & Efficiency
We took the approach of making a method called kth_from_end that iterates through the linked list and adds them all to an array. We then made an if statement that checks to see if k is between 0 and the length, and the value of that from the end of the list
## soluton
[kth_from_end]/home/glasscharlie/charl/Documents/codefellows/401/data-structures-and-algorithms/assets/kth_from_end.jpg


# ll-merge
create a function that merges two linked lists together while alternating nodes from each list

## Challenge
Write a function called mergeLists which takes two linked lists as arguments. Zip the two linked lists together into one so that the nodes alternate between the two lists and return a reference to the head of the zipped list. Try and keep additional space down to O(1). You have access to the Node class and all the properties on the Linked List class as well as the methods created in previous challenges.

## Approach & Efficiency
We took the approach of making a function called merge_list that takes in two linked lists, and alternates setting the next of each list to the next of the other list until it cant anymore.
## soliton
[ll-merge]/home/glasscharlie/charl/Documents/codefellows/401/data-structures-and-algorithms/assets/kth_from_end.jpg
