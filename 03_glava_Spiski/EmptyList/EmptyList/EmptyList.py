#initiate empty list
motorcycles = []
#add element in list
motorcycles.append('ducati')
motorcycles.append('yamaha')
motorcycles.append('honda')
print(motorcycles)
#use Insert method 
motorcycles.insert(1,'harley')
print(motorcycles)

# use del for delete from list
del motorcycles[0]
print(motorcycles)

popped_motorcycles = motorcycles.pop()
print(motorcycles)
print(popped_motorcycles)

#удаление по значению
print('удаление по значению')
motorcycles.remove('harley')
print(motorcycles)