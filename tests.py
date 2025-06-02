
from functions.overwrite_file import overwrite_file 

print(overwrite_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum"))
print(overwrite_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))
print(overwrite_file("calculator", "/tmp/temp.txt", "this should not be allowed"))