#////////////////////////
#// 'with' statement
# with keyword is used to wrap the execution of block of code within methods defined by context manager.

# This code demonstrates how to use the with statement to open a file named 'file_path' 
# in write mode ('w'). It writes the text 'hello world !' to the file and automatically 
# handles the opening and closing of the file. The with statement is used for better
# resource management and ensures that the file is properly closed after the block is executed.
with open('file_operations.txt', 'w') as file:
    file.write('hello world !')