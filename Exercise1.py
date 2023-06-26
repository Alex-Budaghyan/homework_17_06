string = input("Enter the sentence: ")
i = 0
while i < len(string):
    if not string[i].isalnum() and string[i] != " ":
        string = string[:i] + ' ' + string[i + 1:]
    else:
        i += 1
d = {}
string = string.lower().split()
for i in string:
    if i not in d.keys():
        d[i] = 1
    else:
        d[i] += 1
d = sorted(d.items())
for keys, values in d:
    print(keys, ": ", values)
