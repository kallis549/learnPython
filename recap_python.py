#recap of python


#** What is 7 to the power of 4?**
print (7**4)


#** Split this string:**
#s = "Hi there Sam!"
#*into a list. *
s = "Hi, there, Sam!"
print (s.split(","))

s = "Hi there Sam!"
print (s.split())

#** Given the variables:**
#planet = "Earth"
#diameter = 12742
#** Use .format() to print the following string: **
#The diameter of Earth is 12742 kilometers.
planet = "Earth"
diameter = 12742
print ("The diameter of {a} is {b} kilometers".format(b=diameter, a=planet ))

#** Given this nested list, use indexing to grab the word "hello" **
lst = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
vari = lst[3][1][2][0]
print (vari)
print (lst[3][1][2][0])

#** Given this nested dictionary grab the word "hello". Be prepared, this will be annoying/tricky **
d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}
print(d['k1'][3]['tricky'][3]['target'][3])

#** Create a function that grabs the email website domain from a string in the form: **
#user@domain.com
#So for example, passing "user@domain.com" would return: domain.com
def getdomain(str):
	return str.split('@')[1]
print (getdomain('user@barkhurdar.com'))

#** Create a basic function that returns True if the word 'dog' is contained 
#in the input string. Don't worry about edge cases like a punctuation being 
#attached to the word dog, but do account for capitalization. **
def getDog(str):
	arr = str.split()
	for x in arr:
		if x == 'dog':
			return True
	return False

print (getDog("this is a test of the dog"))
print (getDog("this is a test of the Dog"))
print (getDog("this is a test of thedog"))

def findDog(str):
	return str.find('dog') != -1;
print (findDog("this is a test of the dog"))
print (findDog("this is a test of the Dog"))
print (findDog("this is a test of thedog"))

#** Create a function that counts the number of times the word "dog" occurs 
#in a string. Again ignore edge cases. **
def countDog(str):
	return str.count('dog');
print (countDog("this is a test of the dog"))
print (countDog("this is a test of the Dog"))
print (countDog("this is a test of thedoggone dog"))


##Try the same with lambda function
t = lambda var:var.count('dog')
print(t("this is a test dog"))

t = lambda var:var.find('dog') != -1
print(t("this is a test dog"))

#** Use lambda expressions and the filter() function to filter out words from a list that don't start with the letter 's'. For example:**
#seq = ['soup','dog','salad','cat','great']
#should be filtered down to:
#['soup','salad']

def beginsWithS(str):
	rslt = []
	for x in str:
		if x[0] == 's':
			rslt.append(x)
	return rslt
print (beginsWithS(['soup','dog','salad','cat','great']))

def fltrWithS(str):
	rslt = []
	for x in str:
		if x.startswith('s'):
			print(x)
			rslt.append(x)
	return rslt
print (fltrWithS(['soup','dog','salad','cat','great']))

def fltrfunc(str):
	for x in str:
		if x.startswith('s'):
			return True
	return False

##USING LAMBDA
arr = ['soup','dog','salad','cat','great', 'salad', 'such']
print(list(filter(lambda var: var.startswith('s'), arr)))


## *You are driving a little too fast, and a police officer stops you. 
## Write a function to return one of 3 possible results: "No ticket",
## "Small ticket", or "Big Ticket". If your speed is 60 or less, the 
## result is "No Ticket". If speed is between 61 and 80 inclusive, the 
## result is "Small Ticket". If speed is 81 or more, the result is
## "Big Ticket". Unless it is your birthday (encoded as a boolean value 
## in the parameters of the function) -- on your birthday, your speed 
## can be 5 higher in all cases. *

def caught_speeding(speed, isbirthday):
	if isbirthday == True:
		speed = speed - 5
	if speed <= 60:
		return "NO TICKET"
	elif speed > 60 and speed <= 80:
		return "SMALL TICKET"
	else :
		return "BIG TICKET"

print (caught_speeding(85, True))
print (caught_speeding(85, False))

