#!usr/bin/env python3.6

if __name__ == "__main__":
    
# The list should be empty initially.
mylist = []
# Populate the list using append or insert.
mylist.append("S3")
mylist.append("EC2")
mylist.append("Lambda")
mylist.append("Cloud9")
#Print the list and the length of the list.
print("The AWS list is: ", mylist)
print("The length of the list is ", le(mylist))
#Remove two specific services from the list by name or by index.
mylist.remove("S3")
mylist.remove("EC2")
#Print the new list and the new length of the list.
print("The AWS list is: ", mylist)
print("The length of the list is: ", len(mylist))