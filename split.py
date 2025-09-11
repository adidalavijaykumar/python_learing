#Case Conversions
text = "Python PROGRAMMING"
print(text.lower())      # Converts all characters to lowercase
print(text.upper())      # Converts all characters to uppercase 

text2 = "986-Maria, ( D@t@ Engineer );; 27y"
name = text2[4:9]
role = text2[13:26].lower().replace("@","a")
age = text2.strip()[-3:-1]
print(f"name: {name} | role: {role} | age: {age}")


