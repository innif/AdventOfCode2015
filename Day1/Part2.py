f = open("Day1\input.txt", "r")
string = f.read()  
floor = 0 
for i, c in enumerate(string):
    if c == '(': floor += 1
    if c == ')': floor -= 1
    if floor == -1:
        print(i + 1)
        break


