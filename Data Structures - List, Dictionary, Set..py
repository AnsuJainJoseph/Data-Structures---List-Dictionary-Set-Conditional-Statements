
age_list = [24,25,26,27,28]
print(age_list)

name_list = ["Anju","Ansu","Ansa","Annu","Antu"]
print (name_list)


name_list.append("Yazhini")
print(name_list)

age_list.insert(2, 30)
print(age_list)

name_list.remove("Yazhini")
print(name_list)

age_list.pop()
print(age_list)

age_list.extend([29, 30, 26])
print(age_list)

age_list.sort (reverse=True)
print(age_list)

print("Maximum age:", max(age_list))
print("Minimum age:", min(age_list))
print("Sum of all ages:", sum(age_list))


print(name_list[0])

print(name_list[-1])

print(name_list[2:5])

print(name_list[::-1])



student_marks = {"Anju": 75,"Ansu": 90,"Ansa": 85,"Annu": 68,"Antu": 95}
print(student_marks)

print(student_marks["Annu"])

student_marks["Janani"] = 80
print(student_marks)

student_marks["Antu"] = 82
print(student_marks)

print(student_marks.keys())
print(student_marks.values())
print(student_marks.items())



my_set = set(['a', 'e', 'i', 'o', 'u', 'a', 'a', 'i'])
print(my_set)


'''my_set[4] = 's'
print(my_set)'''

my_set.add('s')
print(my_set)

set1 = {1, 3, 5, 7, 9}
print("Set 1:", set1)

set2 = {2, 3, 5, 8, 10}
print("Set 2:", set2)


print(set1.union(set2))
print(set1.intersection(set2))

print(set2.union(set1))
print(set2.intersection(set1))



score = int(input("Enter your score (0 to 10): "))
if score >7 and score <=10:
    print("Above Average: Excellent work! Keep it up!")
elif score >=4 and score <= 7:
    print("Average: Good effort! Keep practicing, there's room for improvement.")
elif score <4:
    print("Need to improve your performance, consistent practise will lead to better")
else:
    print ("invalid")
    
