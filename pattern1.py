""" program to print pattern
*
* *
* * *
"""


#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3
for i in range(3):
    for j in range(3):
        if i > j:
                print("*" , end=' ')
    print("*")

