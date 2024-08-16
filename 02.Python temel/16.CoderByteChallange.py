kelime = "cats AND*Dogs--?are Awesome"

for i in range(33,48):
    kelime = kelime.replace(chr(i), " ")
for i in range(58, 65):
    kelime = kelime.replace(chr(i), " ")
for i in range(91, 97):
    kelime = kelime.replace(chr(i), " ")
for i in range(123,127):
    kelime = kelime.replace(chr(i), " ")

# kelime = kelime.split(" ")

a = ""
for i in kelime.split(" "):
    i = i.capitalize()
    a += i
print(a)