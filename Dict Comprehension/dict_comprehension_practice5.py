salaries = {
    "Amit": 40000,
    "Riya": 55000,
    "Karan": 30000,
    "Sneha": 60000
}
new_dict={k:v+v*0.1 for k,v in salaries.items() if v<50000}
print(new_dict)