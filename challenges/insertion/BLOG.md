Insertion sort is a sorting algorithm that builds the final sorted list one item at a time

lets look at a sample list:
[8,4,23,42,16,15]

The first time through the function, we start at index 0, which has the value of 8. We set a variable, lets call it low to 8. We then go through the array, and if a value is lower than low, we set low to the new number. In this case, the lowest number is 4, so low will be set to 4. We then switch 8 with the index that 4 is found out, so our array is now
[4,8,23,42,16,15] 

The next time through we have our index at 1, which has a the value of 8. We go through the array with low set to 8, and nothing is smaller, so we make no switches. our array is still:
[4,8,23,42,16,15]

The next time through our index is set to 2, which has a value of 23. Low is set to 23. We go through the array, and the lowest number after index 2 is 15, so we swap index 2 and the index where we found 15. our array is set to 
[4,8,15,42,16,23]

The next time we go through the arrray, our index is set to 3, which has a value of 42. Low is set to 42. The lowest number after 42 is 16, so we set low to 16. We then swap index 3 with the index in which 16 is found. Our array is now:
[4,8,15,16,42,23]

The next time we go through the arrray, our index is set to 4, which has a value of 42. Low is set to 42. The lowest number after 42 is 23, so we set low to 23. We then swap index 4 with the index in which 16 is found. Our array is now:
[4,8,15,16,23,42]

We now have a sorted list!

