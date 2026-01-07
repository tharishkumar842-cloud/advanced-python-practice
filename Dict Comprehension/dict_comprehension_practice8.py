new_dict={i:{"square":i**2,"cube":i**3,"is_multiple_of_4":i%4==0}
          for i in range(1,11)
          if i %2==0
          }
print(new_dict)
