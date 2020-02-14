
# data-structures-and-algorithms

|   Challenge          |     Completed     |  Link                                                     |
|----------------------|:-----------------:|-----------------------------------------------------------|
| Array Reverse        |          Yes      | [here](array_reverse/array_reverse.py)                    |
| Array Shift          |          Yes      | [here] (array_shift/array_shift.py)                       |
| Array Binary Search  |          Yes      | [here] (array-binary-search/array_binary_search.py)       |
| linked-list          |          Yes      | [here] (linked-list/linked_list.py)                       |
| linked-list_three    |          Yes      | [here] (linked-list/linked_list.py)                       |
| fizzbuzz_tree        |          Yes      | [here] (challenges/fizz_buzz_tree/fizz_buzz_tree.py)      |
| breadth_first        |          Yes      | [here] (challenges/breadth/breadth.py)                    |
| insertion sort       |          Yes      | [here] (challenges/insertion/insertion.py)                |
| merge_sort           |          Yes      | [here] (challenges/merge_sort/sort.py)                    |
| quick_sort           |          Yes      | [here] (challenges/merge_sort/sort.py)                    |
| repeated_word        |          Yes      | [here] (challenges/repeated_words/repeated.py)            |
| multi-bracket-val    |          Yes      | [here] (challenges\multi_bracket_validation)              |
| tree-interseection   |          Yes      | [here] (challenges\tree_intersection\tree_intersection.py)|
| breadth_first        |          Yes      | [here] (data_structures/graph/graph.py)                   |
--------------------------------------------------------------------------------------------------------
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
-----------------------------------------------------------------------
# kth from end
create a method for linked-list that can tell you the value at a length from the end of the list

## Challenge
Write a method for the Linked List class which takes a number, k, as a parameter. Return the node’s value that is k from the end of the linked list. You have access to the Node class and all the properties on the Linked List class as well as the methods created in previous challenges.

## Approach & Efficiency
We took the approach of making a method called kth_from_end that iterates through the linked list and adds them all to an array. We then made an if statement that checks to see if k is between 0 and the length, and the value of that from the end of the list
## soliton
[kth_from_end]/home/glasscharlie/charl/Documents/codefellows/401/data-structures-and-algorithms/assets/kth_from_end.jpg
-----------------------------------------------------------------------
# Binary Tree and BST Implementation
create a node, binarytree and binarytreesearch classes that can add to the tree.

## Challenge
Create a Node class that has properties for the value stored in the node, the left child node, and the right child node.
Create a BinaryTree class. Define a method for each of the depth first traversals called preOrder, inOrder, and postOrder which returns an array of the values, ordered appropriately. Any exceptions or errors that come from your code should be semantic, capturable errors. For example, rather than a default error thrown by your language, your code should raise/throw a custom, semantic error that describes what went wrong in calling the methods you wrote for this lab. Create a BinarySearchTree class. Define a method named add that accepts a value, and adds a new node with that value in the correct location in the binary search tree. Define a method named contains that accepts a value, and returns a boolean indicating whether or not the value is in the tree at least once.
-----------------------------------------------------------------------
# fizzbuzz_tree
create a function that takes in a tree and returns a new tree with the values changed to the rules of fizzbuzz

## Challenge
Write a function called FizzBuzzTree which takes a tree as an argument. Create a new tree with the same structure as the original, but the values modified as follows: If the value is divisible by 3, replace the value with “Fizz”, If the value is divisible by 5, replace the value with “Buzz”, If the value is divisible by 3 and 5, replace the value with “FizzBuzz”, If the value is not divisible by 3 or 5, simply turn the number into a String.

## Approach & Efficiency
We took the approach of making a helper function called make_copy, that makes a copy of the tree. Then we made a function called fizzbuzz that iterates through the new tree and changes the value of the of the Node based on the rules of fizz buzz
## soliton
[fizzbuzz_tree]/home/glasscharlie/charl/Documents/codefellows/401/data-structures-and-algorithms/assets/fizzbuzz_tree.jpg
-----------------------------------------------------------------------

# breadth-first
create a function that takes in a tree and returns a list of the values in breadth-first order

## Challenge
Write a breadth first traversal method which takes a Binary Tree as its unique input. Traverse the input tree using a Breadth-first approach, and return a list of the values in the tree in the order they were encountered.

## Approach & Efficiency
We took the approach of making a function called breadth, which first adds the root to an estansiation of a Queue class. Then it looks to see if the front of the queue has a left and right, if so it adds those to the queue, and dequeues the front node. It then looks to see if the front has a left and right, and adds those to the queue and repeats itself until there is nothing left in the queue. 

## soliton
[breadth-first]/home/glasscharlie/charl/Documents/codefellows/401/data-structures-and-algorithms/assets/breadth-first.jpg
-----------------------------------------------------------------------
# insertion sort 
create a function that takes in a list and returns the array in sorted order, using the insertion sort method

## Challenge
Write a function that takes in a list, and returns the list in reverse order using the insertion sort method. Document a visual process of how it works using a test array.

## Approach & Efficiency
We took the approach of making a function called insertion, which loops through the array, and at each index it finds the lowest value that comes after, if a value is lower, it swaps the two numbers
----------------------------------------------------------------------
# merge sort 
create a function that takes in a list and return the array in sorted order, using the merge sort method. 

## Challenge
Write a function that takes in a list, and returns the list in reverse order using the merge sort method. Document a visual process of how it works using a test array. (for more info look at BLOG.md)

## Approach & Efficiency
We took the approach of making a function called merge_sort, which uses recursion to keep splitting the list into new list, until each list only has one element in it. It then compares the lists, sorting them into arrays until you have a sorted list. (for more info look at BLOG.md)
----------------------------------------------------------------------
# merge sort 
create a function that takes in a list and return the array in sorted order, using the quick sort method. 

## Challenge
Write a function that takes in a list, and returns the list in reverse order using the quick sort method. Document a visual process of how it works using a test array. (for more info look at BLOG.md)

## Approach & Efficiency
We took the approach of making a function called quick_sort, which takes a random element and makes it the pivot, it then sorts the list into two new lists, with all smaller elements in the left array and all higher elements in the right array. It does this recursively until all elements are by themselves, and then adds them all back together into a single list.
----------------------------------------------------------------------
# hashtable
Implement a Hashtable

## Challenge
Implement a Hashtable with the following methods: add: takes in both the key and value. This method should hash the key, and add the key and value pair to the table, handling collisions as needed. get: takes in the key and returns the value from the table. contains: takes in the key and returns a boolean, indicating if the key exists in the table already. hash: takes in an arbitrary key and returns an index in the collection
----------------------------------------------------------------------
# repeated_words 
Write a function that accepts a lengthy string parameter, return the first word to occur more than once in that provided string.

## Challenge
Write a function that accepts a lengthy string parameter, return the first word to occur more than once in that provided string.

## Approach & Efficiency
We took the approach of making a helper function called punctuation, that takes in a string, and returns a new string with all of the punctuation removed. We then wrote another function called repeated_word that takes in the new string without punctuation and returns the first repeated word in the string.

## Solution
[array_reverse]/home/glasscharlie/charl/Documents/codefellows/401/data-structures-and-algorithms/assets/repeated_name.jpg
----------------------------------------------------------------------
# multi-bracket-validation 
Write a function that takes in a string as its only argument, and returns a boolean representing whether or not the brackets in the string are balanced.  

## Challenge
Write a function that takes in a string as its only argument, and returns a boolean representing whether or not the brackets in the string are balanced. 

## Approach & Efficiency
We took the approach of making a function called multibracket validation, that loops through the string and adds opening brackets to an empty string. If there is a closing bracket, that doesn't have the opening bracket before it, it returns false, else returns true.

## Solution
[multi-bracket-validation]C:\Users\charl\Documents\codefellows\401\data-structures-and-algorithms\assets\multi-bracket-validation.jpg
----------------------------------------------------------------------
# tree-intersection 
Write a function called tree_intersection that takes two binary tree parameters. Without utilizing any of the built-in library methods available to your language, return a set of values found in both trees. 

## Challenge
Write a function called tree_intersection that takes two binary tree parameters. Without utilizing any of the built-in library methods available to your language, return a set of values found in both trees. 

## Approach & Efficiency
We took the approach of making a function called tree-insertion, that takes in two trees as a peramiter. It then adds values from the first tree to a set. It then checks the values of the 2nd tree, and if it is in the list already it adds it to a list. It then returns the list

## Solution
[multi-bracket-validation]C:\Users\charl\Documents\codefellows\401\data-structures-and-algorithms\assets\tree_intersection.jpg
----------------------------------------------------------------------
# breadth first
Extend your graph object with a breadth-first traversal method that accepts a starting node. Without utilizing any of the built-in methods available to your language, return a collection of nodes in the order they were visited. Display the collection.

## Challenge
Extend your graph object with a breadth-first traversal method that accepts a starting node. Without utilizing any of the built-in methods available to your language, return a collection of nodes in the order they were visited. Display the collection. 

## Approach & Efficiency
We took the approach of making a method on the graph class that takes in a starting node. It then finds each nodes neighbor, and if the neighbor node is not already seen, it adds it to the list

## Solution
[multi-bracket-validation]C:\Users\charl\Documents\codefellows\401\data-structures-and-algorithms\assets\tree_intersection.jpg
