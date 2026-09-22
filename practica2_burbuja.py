cal = [9.2,10,9.6,8.4,5.9,6.8,7.2,8.5,9.1,10,8.7,9.6,6.8,7.9,9.9]
a = len(cal)
swapped = True
while swapped:
    swapped = False
    for i in range(a-1):
        if cal[i]>cal[i+1]:
            cal[i],cal[i+1] = cal[i+1],cal[i]
            swapped = True
print ("ORDEN ASCENDENTE: ", cal)
print("")
a = len(cal)
swapped = True
while swapped:
    swapped = False
    for i in range(a-1):
        if cal[i]<cal[i+1]:
            cal[i],cal[i+1] = cal[i+1],cal[i]
            swapped = True
print ("ORDEN DESCENDENTE: ", cal)