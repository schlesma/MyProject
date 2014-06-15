# Hey Dad,

# I wrote this tutorial for you!  I hope you like it.  

print "First let's learn how to print to the screen." #Like this.

#Next let's look at how to grab input from the user and store it in a variable.

user_input = str(raw_input("Assign a value to user_input"))

#print out the user input.  Notice that you can use a comma to separate strings from variables
print "You entered",user_input

#Now let's move onto something more advanced.

# looping:

for i in xrange(100):
    print i

n = 0
while n < 100:
    print n
    n += 1

things = ["hello","how","are","you"]

for i in things:
    print i

for ind,val in enumerate(things):
    print "index:",ind,"value:",val

#list comprehensions

listing = [elem for elem in things if elem.startswith("h")]

#importing

import os
import sys
from subprocess import call

#system processes

curr_dir = os.getcwd()
os.chdir("../")
with open("things.py","w") as f:
    f.write("""
#A simple python script
print "Hello world!"
print "This script will be deleted after it's run"
""")

call(["python","things.py"]) #executes the script
os.remove("things.py") #removes the script
os.chdir(curr_dir)

#importing from local modules

with open("thing.py","w") as f:
    f.write("""
def what(x,y):
    return x+y
""")

m = __import__("thing")
print m.what(5,6)

# grabbing information from the internet

import requests #you'll have to download this library by installing pip
import lxml.html #you'll need to download this one as well

r = requests.get("https://www.google.com")
html = lxml.html.fromstring(r.text)
link_obj = html.xpath("//a")
links_list = [elem.values() for elem in link_obj]
links = [elem for elem in links_list if "http" in elem]
print links
        
 
 

