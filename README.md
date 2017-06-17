# Udemy Python Tutorials
Following along with the tutorials and practice here.

## Notes
- Global Python:
    - Use 'continue' to go back to the top of the loop (instead of 'break', which breaks out of the loop)
- Section 03:
    - string.ascii_letters
    - string.ascii_lowercase
    - random.choice('abcdefg') will return one of the random characters.
    
- Section 04:
    - for item in gmail:
        - if 'gmail' in item:
            - print item
     
    - string formatting, 2 and 1 decimal places: print '{0:.2f}, {1:.1f}'.format(<value1>, <value2>)
    
    - for iterating through multiple lists, use:
        - for i, j in zip( \<list1\>, \<list2\>):
            - print i, j
    
- Section 05a, reading files:
    - file.read() to stream in the data.
    - file.tell() to see where you're at.
    - file.seek(0) to reset the pointer.
    - file.readlines() returns an array.
    - content = [i.rstrip('\n') for i in content] to strip new line from readline();
    - file.close() is required to release the file.
    
- Section 05b, writing files:
    - file.write(), then file.close()
        - have to add your own ' \n ' character.
    - pushing items to list, use 'append(obj)'
    
- Section 06:
    - docstrings: 
        - " print \<module\>.\_\_doc\_\_ " to get module's docstring
        - docstring in module is anything inside the """ header """ area.
        - works for methods and classes as well.
    - datetime module:
        - [strftime.org](http://strftime.org/)
        - (see dt-play.py comments for more information.)


- Numpy (as np):
    - n.arange(number): Creates a pre-filled array.
    - n.reshape(numberA, numberB, (numberC)): Reshape the current array into a multimensional array.
    - array.T = transpose swaps your rows and columns.
    - array.flat = lets you iterate through 1 by 1 in 'for loops'.
    - array.hstack((tuple)) = combine two arrays horizontally via a tuple.
    - array.vstack((tuple)) = combine two arrays vertically via a tuple.
    - NOTE: array splicing using img[0:2, 2:4] is rows,columns NOT x,y
    
    
- OpenCV:
    - cv2.imread() opens a file to a numpy array already.
    - print img.shape will give array dimensions.
    - 'glob' module:
        - import glob
        - glob.glob('*.jpg') will find all the types of files in a folder and put them in a list (array)
    

## Tutorials
- [Python Socket Programming Tutorial](http://www.binarytides.com/python-socket-programming-tutorial/)
- [Effbot.org: Python List reference](http://effbot.org/zone/python-list.htm)
- [Python Spot: Random Numbers](https://pythonspot.com/en/random-numbers/)