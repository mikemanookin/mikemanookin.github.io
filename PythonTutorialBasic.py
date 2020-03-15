


# Define a numerical array
x = [7, 9, 12, 5, 2, 13, 9];

# Define an array containing strings.
c = ['seven', 'nine', 'twelve', 'five', 'two', 'thirteen', 'nine'];


## For-loop examples

# Go through the values defined in a for loop and print the values to the
# command line.
for j in range(0, 10):
    print(j)

# Let's loop through all of the values in the numerical array and display
# what we've found to the command line.
for value in x:
    print(value)

# Now, let's do the same for the cell containing our strings.
for value in c:
    print(value)

## While-loop examples.
done = False;
count = 0;
while count < len(x):
    print(x[count])
    count += 1;

## If-then-else statement examples

# Let's loop through all of the values in the numerical array and display
# what we've found to the command line.
for j in range(0, len(x)):
    if (x[j] == 5):
        print("I found 5!")
    elif (x[j] == 7):
        print("I found 7!")
    else:
        print("I found %d!" % x[j])

# Now, let's do the same for the cell containing our strings.
for j in range(0, len(c)):
    if (c[j] == "five"):
        print("I found five!")
    elif (c[j] == "seven"):
        print("I found seven!")
    else:
        print("I found %s!" % c[j])

## Implementation of a switch-case statement.
def xswitch(i):
    switcher={
        0:'Sunday',
        1:'Monday',
        2:'Tuesday',
        3:'Wednesday',
        4:'Thursday',
        5:'Friday',
        6:'Saturday'
    }
    return switcher.get(i,"Invalid day of week")



## Searching for values in an array.

# Search for the index numbers in the array that contain the desired
# values. If the value isn't there, it will return empty.
# For the numerical array; find values equal to 9.
tf = [i for i in range(len(x)) if x[i] == 9]
print tf

# Find all of the values greater than or equal to 7.
tf2 = [i for i in range(len(x)) if x[i] >= 7]
print tf2

tf3 = [i for i in range(len(c)) if c[i] == "nine"]
print tf3
