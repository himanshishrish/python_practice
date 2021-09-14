'''
to add a key to a dictionary. 

Sample Dictionary : {0: 10, 1: 20}
Expected Result : {0: 10, 1: 20, 2: 30}'''
data={
    0: 10,
    1: 20
}
print(data)
data.update({2:30})
print(data)