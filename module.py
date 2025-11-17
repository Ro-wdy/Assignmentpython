import mymodule

greeting = mymodule.greet("Rhodah") 


Person1 = "My name is " + mymodule.person[  "first_name" ] + " " + mymodule.person[  "last_name" ] + " and I am " +" "+ str(mymodule.person[ "age"]) + " years old from " + mymodule.person[  "city" ] + "."
print(Person1)
Person2= mymodule.person["first_name"]
print(Person2)

print(mymodule.add(3, 5))       
print(mymodule.multiply(4, 6))