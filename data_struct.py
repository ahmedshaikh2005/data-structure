print("=== Lists ===")
number_list = [5, 10, 15, 20, 30, 40, 50]
number_list.append(60)  
number_list.remove(30) 
print("List after operations:", number_list)
number_list.reverse()
print(number_list)  

print("=== Tuples ===")
numbres = (1, 2, 3, 4, 5)
print("Tuple:", numbres)
print("Accessing element at index 2:", numbres[2]) 

print("=== Dictionaries ===")
my_dict = {
    "name": "Ahmed",
    "age": 20,
    "city": "karachi"
}
my_dict["age"] = 20  
my_dict["job"] = "Developer"
del my_dict["city"]  
print("Dictionary after operations:", my_dict)
print("Keys:", list(my_dict.keys()))  
print("Values:", list(my_dict.values()))  

print("=== Sets ===")
sets_numbers = {1, 2, 3, 4, 5}
sets_numbers.add(6)  
sets_numbers.discard(3)  
sets_numbers.update([7, 8, 9])  
print("Set after operations:", sets_numbers)
print("Checking if 5 is in set:", 5 in sets_numbers)  



