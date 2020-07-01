#Task 1
print("Trial and Error") #pound for comments

#Task 2
x = 2
if x == 2: #use colon in if statements
    # usually indented by four spaces
    print("x is 2.")

#Task 3
myint = 4
print(myint) #string is defined with ""

#Task 4
myfloat = 7.0
print(myfloat)
myfloat = float(7) #float to identify floating point number
print(myfloat)

#Task 5 #string can be defined by single quote (") or double quotes (")
mystring = 'hello'
print(mystring)
mystring = "hello"
print(mystring)

#use double quote to ignore apostrophes
mystring = "I don't see the reason"
print(mystring)

#Task 6 #string can be added with +
one = 1
two = 2
three = one + two
print(three)

hello = "hello"
world = "world"
helloworld = hello + " " + world
print(helloworld)

#however, string and integer do not work
#print(one + two + hello)

#Task 7
a, b = 3, 4
print(a,b)

#Exercise in integer, string, float
#string contains hello, floating contains 10.0, integer contains 20
string1 = "hello"
float1 = 10.0
int1 = 20

if string1 == "hello":
    print("String: %s" % string1) # % to return identified variable
if isinstance(float1, float) and float1 == 10.0: # isinstance to check the variable is float or any els
    print("Float: %f" % float1)
if isinstance(int1, int) and int1 == 20:
    print("Integer: %d" % int1)
 
#Task 8 Lists
mylist = []
mylist.append(1) #fill list with 1
mylist.append(2) #fill list with 2
mylist.append(3) #fill list with 3
print(mylist[0]) #print 1 (1 is first entry in mylist)
print(mylist[1]) #print 2 (2 is second entry in mylist)
print(mylist[2]) #print 3 (3 is third entry in mylist)

for x in mylist:
    print(x)     #print mylist (defined as x)

#Task 8
#mylist = [1,2,3]
#print(mylist[10]) #error since list only consits of 0 1 2 order

#Lists Exercise
numbers = [1,2,3]
strings = ["Hello", "World"]
names = ["John", "Eric", "Jessica"]

#alternative way
numbers = []
strings = []

numbers.append(1)
numbers.append(2)
numbers.append(3)

strings.append("Hello")
strings.append("World")

#second name is second entry in names list
second_name = names[1]

print(numbers)
print(strings)
print("The second name in the list is %s" % second_name)

#Arithmetics
number = 1 + 2 * 3 / 4.0
print(number) #already follows order convention

remainder = 11 % 3
print(remainder) #returns 2, which is the remainder of 11/3

#double asterisk indicates power of
squared = 7 ** 2 #as in 7^2
cubed = 2 ** 3 #as in 2^3
print(squared)
print(cubed)

#multiple strings with operator
hellos = "Hello" * 10
print(hellos)

#operator with list
even_number = []
odd_number = []

even_number.append(2)
even_number.append(4)
even_number.append(6)
even_number.append(8)

odd_number.append(1)
odd_number.append(3)
odd_number.append(5)
odd_number.append(7)

all_numbers = odd_number + even_number
print(all_numbers) #jointed list based on order of list added, not by entries

#repetition can be inside print
mylist = [1,2,3]
print(mylist * 3)

#Arithmetic Exercise
#Create x list and y list which contain 10 objects
#in addition, create big list, contains x list and y list 10 times by combining both

x = object()
y = object()
print(x)
print(y)

x_list = [x] * 10
y_list = [y] * 10
big_list = x_list + y_list
print(x_list)
print(y_list)
print(big_list)

print('x_list contains %d objects' % len(x_list))
print('y_list contains %d objects' % len(y_list))
print('big_list contains %d objects' % len(big_list))

if x_list.count(x) == 10 and y_list.count(y) == 10:
    print("Almost there...")
if big_list.count(x) == 10 and big_list.count(y) ==10:
    print("Success!!")

#String formatting
name = "John"
age = 23
print("%s is %d years old" % (name,age)) # %s indicates string, %d indicates integer

mylist = [1,2,3]
print("A list: %s" % mylist)

#String Exercise
#output should be Hello John Doe. Your current balance is $53.44

data = ("John", "Doe", 53.44)
format_string = "Hello %s %s. Your current balance is $%s." #generated strings are based on order defined in data
print(format_string % data)

#Basic String Operations
astring = "Hello World!"
print(len(astring)) #length of string variable
print(astring.index("o")) #identify position of 'o', note that it only identifies first o entry
print(astring.count("l")) #identify how many 'l' from the string, case sensitive
print(astring[3:7]) #prints parts of string (position 3 to 7 in this case)
print(astring[3:7:2]) #prints parts of string (position 3 to 7, and skip 2 characters)
print(astring[3:7:1]) #prints parts of string (position 3 to 7, and skip 2 characters)
print(astring[::-1]) #prints the string in reverse order
print(astring.upper()) #print all in uppercase
print(astring.lower()) #print all in lowercase
print(astring.startswith("Hello")) #check the string component true or false
print(astring.endswith("asdasdadsasd")) #check the string component true or false
afewords = astring.split(" ")
print(afewords) #split the string into lists

#String Exercise
s = "Wholesome Materials!"
# Length should be 20
print("Length of s = %d" % len(s))

# First occurrence of "a" should be at index 8
print("The first occurrence of the letter a = %d" % s.index("a"))

# Number of a's should be 2
print("a occurs %d times" % s.count("a"))

# Slicing the string into bits
print("The first five characters are '%s'" % s[:5]) # Start to 5
print("The next five characters are '%s'" % s[5:10]) # 5 to 10
print("The thirteenth character is '%s'" % s[12]) # Just number 12
print("The characters with odd index are '%s'" %s[1::2]) #(0-based indexing)
print("The last five characters are '%s'" % s[-5:]) # 5th-from-last to end

# Convert everything to uppercase
print("String in uppercase: %s" % s.upper())

# Convert everything to lowercase
print("String in lowercase: %s" % s.lower())

# Check how a string starts
if s.startswith("Who"):
    print("String starts with 'Who'. Good!")

# Check how a string ends
if s.endswith("als!"):
    print("String ends with 'als!'. Good!")

# Split the string into three separate strings,
# each containing only a word
print("Split the words of the string: %s" % s.split(" "))