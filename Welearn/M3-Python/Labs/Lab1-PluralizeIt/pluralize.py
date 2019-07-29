word = str(raw_input("Word: "))
#word = "smif"

if word[-3:] == "ife":
    print(word[:-3] + "ives")
else:
    print(word + 's')

if word[-3:] == "sh":
    print(word[:-3] + "shes")
else:
    print(word + '')

if word[-2:] == "us":
    print(word[:-2] + "i")

if word[-2:] == "ch":
    print(word[:-3] + "ches")
else:
    print(word + 's')

if word[-2:] == "ay":
    print(word + "s")
if word[-2:] == "oy":
    print(word + "s")
if word[-2:] == "ey":
    print(word + "s")
if word[-2:] == "uy":
    print(word + "s")
if word[-1:] == "y":
    print(word[:-3] + "ies")
