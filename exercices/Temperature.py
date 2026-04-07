# Create a program that tells the user wether it is cold or not
# Ask the user for the temperature in Celsius
# If less than 10 degrees, print "It is cold!"
# If between 10 and 15 degrees, print "It is cool!"
# If between 15 and 20 degrees, print "It is warm!"
# If more than 20 degrees, print "It is hot!"
print("Enter the temperature in Celsius:")
temperature = float(input())
match temperature:
    case temp if temp < 10:
        print("It is cold!")
    case temp if 10 <= temp < 15:
        print("It is cool!")
    case temp if 15 <= temp < 20:
        print("It is warm!")
    case temp if temp >= 20:
        print("It is hot!")