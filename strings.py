my_string = """I 
am
programmer"""
print(my_string)


my_strings = "hello"
char = my_strings[2]
print (char)

substring = my_strings[1:5]
print(substring)

substring = my_strings[::2]
print(substring)

substring = my_strings[::]
print(substring)

substring = my_strings[:: -1]
print(substring)

greeting = "hello"
name = "hey"
sentence = greeting + " " + name
print(sentence)


gre = "hii"
for x in gre:
    print(x)


gree = "hello world"
if 'e' in gree:
    print("yes")
else:
    print("no")


stri = '     beautiful world     '
print(stri)
stri = stri.strip()
print(stri)
print(stri.upper())
print(stri.startswith('b'))
print(stri.endswith('k'))
print(stri.find('u'))
print(stri.count('l'))
print(stri.replace('world', 'universe'))

my = "how are you"
my_list = my.split()
print(my_list)
new_string = ' '.join(my_list)
print(new_string)


from timeit import default_timer as timer
new = ['a'] * 6
print(new)

start = timer()
new_str = ' '
for i in new:
    new_str += i
stop = timer()
print(stop-start)

start = timer()
new_str = ' '.join(my_list)
stop = timer()
print(stop-start)


var = "tom"
my_s = "the variable is %s" % var
print(my_s)
my_s = "the variable is {}" .format(var)
print(my_s)
my_s = f"the variable is {var}"
print(my_s)
