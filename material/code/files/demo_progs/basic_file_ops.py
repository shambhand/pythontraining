#! /usr/bin/python3
print ("[1]:Opening myfile.txt for writing") 
f = open ("myfile.txt", 'w') 
print ("[2]:Writing strings to myfile.txt") 
f.write ("Hello,World!\n") 
f.write ("This is a last line in this file\n") 
print ("[3]:Closing myfile.txt") 
f.close ()
print ("[4]:Opening file again for reading") 
f = open ("myfile.txt") 
print ("[5]:Reading a line in a file into a string") 
file_line_one = f.readline ()
print ("File line one:", file_line_one) 
print ("[6]:Reading next line") 
file_line_two = f.readline () 
print ("File line two:", file_line_two)
print ("[7]:Closing file") 
f.close () 
