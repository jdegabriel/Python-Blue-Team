#!/usr/bin/env python3.7
import string
import random


def ec2_names(number, dept):
    EC2s = []
    letters = string.ascii_lowercase
    for i in range(number):
        char = ''.join(random.choice(letters) for i in range(3))
        num = random.randrange(1000,99999)
        EC2s.append(dept + '-' + char + '-' + str(num))
    return EC2s
    
if __name__ == "__main__":
    depts = ["marketing", "accounting", "finops"]
    number = int(input("The number of EC2 instances you need: "))
    dept = input("The department you are in: ")
    dept = dept.lower()
    if dept not in depts:
       print("You should not use this Name Generator.")
    else:
        print(ec2_names(number, dept))