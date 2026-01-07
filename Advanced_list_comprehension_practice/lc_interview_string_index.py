text = "interview"
new_list=[v.upper() if i%2!=0 else v.lower() for i,v in enumerate(text)]
print(new_list)