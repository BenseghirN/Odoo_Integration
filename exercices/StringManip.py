# text=input("Enter a string: ")
# max_length = 10
# if len(text) > max_length:
#     text = text[:max_length] + "..."
# print("The string is: " + text) 

text = input("Enter a string: ")
print(f"The string is: {text[:10] + '...' if len(text) > 10 else text}")