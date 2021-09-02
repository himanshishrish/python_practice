name="Athanasia"

uname=name.upper()
lname=name.lower()

print("0riginal name is "+name)
print(name+" in capital is "+uname)
print(name+" in lower is "+lname)

print("////////////////////////////////////////")
address="butwal"
cname=address.capitalize()
print(address+" in capitalized is "+cname)

print("////////////////////////////////////////")
message="Every moment is a fresh beginning"
new=message.split(" ")
print(message)
print(new)
print(message.replace("Every","Each"))

print("////////////////////////////////////////")
space="   be gone"
print(space.strip())

print("////////////////////////////////////////")
words="Success is not final, failure is not fatal"
print(words)
print('Count of "is" =')
print(words.count("is"))

print("////////////////////////////////////////")
one="nice"
two="meet"
three="morning"
messageFormat="Good {2} .Its {0} to {1} you"
print(messageFormat.format(one,two,three))

