#print("Hello world!")
#print("Bye world!")
############### intro ###############
'''
num1 = int(raw_input("Enter number #1: "))
num2 = int(raw_input("Enter number #2: "))
total = num1 + num2
print("The sum is " + str(total))
#'''
######### Conditional Statement ###############
'''
num = int(raw_input("Enter a number"))
if num > 0:
    print("That's a positive number")
elif num < 0:
    print("That's a negative number!")
else:
    print("Zero is neither positive nor negative")
'''
############## Loops ############## - loops start from 0 to the number input
'''
string = "hello there"
for letter in string:
    print(letter.upper())

for i in range(5): # Python Loop
    print(i)       # Java Loop - for (let i = 0, i < 5; i++)
'''
########## String Formatting (% Operator) ##################
'''
my_name = "Bob"
friend1 = "Alice"
friend2 = "John"
friend3 = "Mallory"

print("My name is %s and my friends are %s, %s and %s" %
(my_name, friend1, friend2, friend3))
'''
############# String Formatting (% Operator) ############
'''
name = "Marina"
age = 19
print("My name is  "+ name + " and I'm "+ str(age) + " years old.")
print("My name is %s and I'm %s years old." % (name ,age))
'''
################ Functions ###############
'''
def greetAgent():
    print("Bond. James Bond.")

def greetAgent(first_name, last_name):
    print("%s. %s %s. " % (last_name, first_name, last_name))

def createAgentGreeting(first_name, last_name):
    return "%s. %s %s." % (last_name, first_name, last_name)

greetAgent('James', 'Bond') # This is calling the function
greetAgent('Alexis','Mejia') # Prints the name of the input desired
'''
################ Exercise ################

def findSum(x):
    y = 0
    for i in range(x):
       y = y + i

    return y + x
    #return y 

print(findSum(10))
