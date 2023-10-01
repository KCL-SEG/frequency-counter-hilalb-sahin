"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    # Your code goes here

    #  inside the frequencies add the item , if it already exists, then increase it
    for item in items:
        #converting all to string 
        item_str = str(item)

        if item_str in frequencies:
            #increase the existing value by 1 
            frequencies[item_str]+=1
        else:
            frequencies[item_str]= 1
            

    return frequencies


print(frequencies([100, 'Hello', '100', '100', 100]))