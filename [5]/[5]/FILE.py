# create an text file, put some texts into it then display the result.
import os

# wb+ = Opens a file for both writing and reading in binary format. 
# Overwrites the existing file if the file exists.
# If the file does not exist, creates a new file for reading and writing.
fo = open("foo.txt", "wb+")
fo.write(b'Python is a great language.\nYeah its great!!\n');
fo.close()
del fo

fo = open("foo.txt", "r")
for x in fo:
    print(x)
fo.close()