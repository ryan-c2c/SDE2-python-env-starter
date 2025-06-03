"""
1. Import the wishlist Python file
2. Check the length (it needs to be 50)
3. If the length is not 50, append the additional items needed
4. Print the wish list 
"""

import wishlist as wl


#optional- make a variable to store wl.wish_list shown in alternateidea.py

#wish_list = wl.wish_list 


#check length
print(len(wl.wish_list))

#append 2 items 
wl.wish_list.append('earrings')
wl.wish_list.append('necklace')

#check length again
print(len(wl.wish_list))

#print wish list
print(wl.wish_list)