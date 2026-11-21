rain = [1,1,0,1,1]
arr = []
a = rain[-1]
for i in range(0, len(rain)-1):
    if rain[i] == rain[i + 1] == 1 :
        arr.append("Alice")
    elif rain[i] == 1:
        arr.append("Bob")
    elif a == rain[i] == 1:
        arr.append("Alice")
    elif a == 1:
        arr.append("Bob")
    else:
        arr.append("None")
print(arr)