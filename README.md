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
    
- Section 05:
    - file.read() to stream in the data.
    - file.tell() to see where you're at.
    - file.seek(0) to reset the pointer.
    - file.readlines() returns an array.
    - content = [i.strip('\n') for i in content] to strip new line from readline();
    
- Section 06:
    - file.write(), then file.close()


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