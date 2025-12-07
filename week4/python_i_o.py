with open('output.txt', 'w') as f:
    for i in range(10):
       f.write("this is line: {i}\n")

with open('output.txt', 'w') as f:
    for i in range(20):
       f.write("this is line: %i\n"%i)