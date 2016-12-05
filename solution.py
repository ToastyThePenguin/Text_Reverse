data = input("Please type something (not literally): ")
array = data.split()
backward = array[::-1]
print('This is what it looks like backwards:')
for word in backward:
     print(word,end = " ")