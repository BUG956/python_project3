# Open the file in read mode
lp = open("learning_python.txt", 'r')

# Print the entire file
print(lp.read())

# Return to the start of the file
lp.seek(0)

# Print each line in the file
for i in lp:
    print(i, end='')

# Return to the start of the file again
lp.seek(0)

# Read lines into a list and print them
textlines = []  # Blank list for lines of text read from file

for line in lp:
    textlines.append(line)  # Add line to list

for x in textlines:
    print(x, end='')  # Print from list

# Replace 'Python' with 'PHP' in each line and print
for y in textlines:
    print(y.replace('Python', 'PHP'), end='')

# Close the file
lp.close()
