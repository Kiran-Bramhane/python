# Slicing : - Selecting Sub Sequences
lang = "english"


# syntx = [start argument : stop argument -1]

print(lang[::-1]) # reverse string
print(lang[1:4]) # selecting characters from index 1 to 3
print(lang[2:]) # selecting characters from index 2 to end
print(lang[:5]) # selecting characters from start to index 4
print(lang[::]) # print all characters


# step argument in the string slicing
# syntx = [start argument : stop argument -1 : step argument]
print(lang[0:8:2]) # print characters in the steps two


name = input("enter you name: ")
print(f"this is the name {name[::-1]}")