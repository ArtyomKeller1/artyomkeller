n_f = open("homework3.txt", "w")
a = input()
employee = []
employee1 = []
payment = {}
z = 0
while a != "":
    b = a.split()
    b[1] = float(b[1])
    if b[1] < 20000:
        employee.append(b[0])
        employee1.append(b[1])
        z+=1
    a = input()
n_f.write(str(", ".join(employee) + "\n"))
n_f.write(str(sum(employee1)/z))

