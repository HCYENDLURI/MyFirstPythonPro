# L I S T

cheeses = ['Cheddar', 'Edam', 'Gouda']
numbers = [17, 123]
empty = []
print cheeses, numbers, empty
#['Cheddar', 'Edam', 'Gouda'] [17, 123] []

print cheeses[0]
#Cheddar

numbers[1] = 5
print numbers
#[17, 5]

print 'Edam' in cheeses
#True

print 'Brie' in cheeses
#False

t = ['a', 'b', 'c', 'd', 'e', 'f']
print t[1:3]
#['b', 'c']

# T U P L E

tup1 = ('physics', 'chemistry', 1997, 2000)
tup2 = (1, 2, 3, 4, 5 )
print "tup1[0]: ", tup1[0]
print "tup2[1:5]: ", tup2[1:5]
#tup1[0]:  physics
#tup2[1:5]:  [2, 3, 4, 5]

# D I C T I O N A R Y

test_dict = {"Arushi" : 22, "Anuradha" : 21, "Mani" : 21, "Haritha" : 21} 
print ("The dictionary before performing remove is : " + str(test_dict)) 
del test_dict['Mani']
print ("The dictionary after remove is : " + str(test_dict)) 
del test_dict['Manjeet'] 
#The dictionary before performing remove is : {'Anuradha': 21, 'Haritha': 21, 'Arushi': 22, 'Mani': 21}
#The dictionary after remove is : {'Anuradha': 21, 'Haritha': 21, 'Arushi': 22}
