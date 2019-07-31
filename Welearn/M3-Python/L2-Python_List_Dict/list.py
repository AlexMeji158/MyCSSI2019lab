#################### Access elements on a list #############
'''
students = ["Alice", "Javi", "Damien"]
students.append("Delilah")
students.insert(1,"Zoe")
students.remove("Javi")
print(students)
'''
############ List iteration by Element #############
'''
smith_sibilings = ["Emily", "Monique","Giovanni"]
for name in smith_sibilings:
    print(name + "Smith")
'''
'''
x = 0
smith_sibilings2 = ["Emily", "Monique","Giovanni","Logan", "Melissa","Micheal","Alex"]
for name in smith_sibilings2:
    x = x + 1
    print(name + "Smith")
    print(x)
'''
'''
smith_sibilings3 = ["Emily", "Monique","Giovanni"]
students.append("Delilah")
students.append("Alex")
students.append("John")
students.append("Brian")

for name in smith_sibilings3:
    print(name + "Smith")
    print(len(smith_sibilings3))
'''
'''
smith_sibilings4 = ["Emily","Monique","Giovanni","Logan", "Melissa"]
for index in range(len(smith_sibilings4)):
    smith_sibilings4[index] = smith_sibilings4[index] + "Smith"

print(smith_sibilings4)
'''
################### Checking list Membership #################
'''
superheroes = ["Captain Marvel","Wonder Woman","Storm","Kamala Khan","Bumble Bee","Jessica Jones"]

demoted_hero = str(raw_input("What superhero do you want to eliminate from the top 5?"))

if demoted_hero in superheroes:
    superheroes.remove(demoted_hero)
    print("Top 5 heroes:", superheroes)
else:
    print("Hero not found.")
'''
############### Slicing ######################
'''
names = ["Rickon","Bran","Arya","Sansa","Jon","Robb"]
print (names[::-1]) # prints the list in reverse
print (names[4:2:-1]) # Only prints idx 4 and reverse idx 2, prints in reverse
print (names[:2]) # prints only the first 2 idx
print (names[::2]) # Skips every other
'''
####################### Lab ###############################
states = {
    "NY":"New York",
    "CA":"California",
    "TX":"Texas",
    "CO":"Colorado",
    "FL":"Florida",
    "AZ":"Arizona"
    }
userInput = str(raw_input("Write the abbreviation of the state you want. "))
'''
for abbreviation in states:
    if userInput in states:
        print(userInput + " is short for " + states[abbreviation])
    else:
        print("Not in the system.")
'''
if userInput == abbreviation in states:
    print(userInput + " is short for " + states[abbreviation])
