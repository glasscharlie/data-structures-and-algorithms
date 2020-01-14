test_odd = [1, 2, 3, 4, 7, 8, 9] 
test_even = [1, 2, 3, 4]

def add_to_middle(list, val):
  if len(list) % 2 == 1:
    midpoint = len(list)//2+1
    new_lst = list[0:midpoint] + [val] + list[midpoint:] 
    return (new_lst)

  if len(list) % 2 == 0:
    midpoint = len(list)//2
    new_lst = list[0:midpoint] + [val] + list[midpoint:] 
    return (new_lst) 
  
  

add_to_middle(test_odd, 12)
add_to_middle(test_even, 12)