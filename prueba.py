import datetime, random
from typing import final

# Variables

x = random.randrange(2000)
y = random.randrange(2000)
z = random.randrange(5000)

# End Variables


# Function

def suma(arr):
    res = 0
    for x in range(0, len(arr) - 1):
        res += arr[x] + (arr[x+1])
    
    return res

menor = min(x, y, z)
mayor = max(y, x, z)
res = suma([x, y, z])
absolute = abs(-7)

# End Function

print("")

# If Elif Else

if res > 1000 and res < 1500:
    numMsg = "El numero es", res, "y es mayor que 1000"
elif res > 1500:
    numMsg = "El numero es", res, "y es mayor que 1500"
else:
    numMsg = "El numero es", res, "y es menor que 1000"

# End If Elif Else


# Ciclo For

msg = []
for x in range(0, 3):
    pre = "Numero: " + str((x + 1))
    msg.append(pre)

# End Ciclo For


# Date Function

date = datetime.datetime.now()

# End Date Function

# String Functions

str = " Francisco Rivao, esta es mi prueba "
strUpper = str.upper()
strLower = str.lower()
strStripped = str.strip()
strReplaced = str.replace("Francisco", "Christian")
strSplit = str.split(",")

if strStripped.startswith("F"):
    pass


age = 36
name = "John"
text = "My name is {}, and I am {}"
finalText = text.format(name, age)

# End String Functions

# List = Array
# Set = Objeto
# Tuple = Constante que puede tener varios valores

print("")