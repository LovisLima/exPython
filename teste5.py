my_string = str(input("Digite algo: \n "))
str=""
for i in my_string:
    str = i+str
print("Reversed string:\n " ,str)