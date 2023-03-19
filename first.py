##inname = input('What is your name?\n')
##print ('Hi, %s.' % inname)

friends = ['john', 'pat', 'gary', 'michael']
for i, name in enumerate(friends):
    print ("iteration {iteration} is {name}".format(iteration=i, name=name))

##print ('Hello World : this is %s' % inname)
## Exponential Calculation
pwr = 7 ** 4
print (pwr)

##Use Of Split
s = "hi there sam!"
arr = s.split()
print (arr[0], "|", arr[1])

## text replacement and formatting
planet = "EARTH"
diameter = 12742
print("The diameter of {a} is {b}".format(a=planet, b=diameter))

#array indexes - get hell0
lst = [1,2,[3,4],[5,[100,200,['hello', 'kalyan']],23,11],1,7]
print (lst[3][1][2][1])

#Tuple : Data Dictionary access - get hello
d= {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}
print (d['k1'][3]['tricky'][3]['target'][3])

#function - get domain name form email id
def getdomain(str):
	return str.split('@')[1]
getdomain('user@domain.com')

#function - findDog
def findDog(str):
	arr = str.split()
	for x in arr:
		if x == 'dog':
			return 'True'
	return 'False'

print(findDog('This is a test dog'))

#function - findDog
def findDog1(str):
	return 'dog' in str.lower().split()
	
print(findDog1('This is a test DOG'))

#function count number of dog in string
def countDogs(str):
	count = 0
	for x in str.lower().split():
		if x == 'dog':
			count = count +1 
	return count

print(countDogs('This dog runs faster than the other dog dude'))

#filter method usage - filter out the dogs
var = 'this dog is a dog dad of that dog and is faster than than dog babloo'
print(list(filter(lambda wrd: wrd.lower()!= 'dog', var.split())))

# lambda functions replacement for above functions
t = lambda var:var **2
print(t(6))

val = lambda str: 'dog' in str.lower().split()
print (val('this is a test dog'))

val = lambda str: str.count('dog')
print (val('this dog is a dog dad of that dog and is faster than than dog babloo'))

#lambda expressions and filter() function - select only words starting with s
seq = ['soup', 'dog','salad','cat','great']
print (list(filter(lambda wrd: wrd[0]=='s', seq)))


def caught_speeding(speed, is_birthday):
	if is_birthday:
		speeding = speed - 5
	else:
		speeding = speed

	if speeding > 80:
		return 'BIG TICKET'
	elif speeding > 60:
		return 'SMALL TICKET'
	else:
		return 'NO TICKET'

def caught_slowing(speed, is_birthday):		
	if is_birthday:
		speed = speed - 5

	if (speed <= 60 ) :
		return 'NO TICKET'
	elif (speed > 60 and speed < 80) :
		return 'SMALL TICKET'
	elif (speed > 80) :
		return 'BIG TICKET'
	else: 
		return 'NO TICKET'

print(caught_speeding(85,True))
print(caught_slowing(90,True))