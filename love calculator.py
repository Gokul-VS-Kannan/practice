name1=input("Enter his name:")
name2=input("Enter her name:")
combine_name=name1+name2
lower_names=combine_name.lower()

t=lower_names.count('t')
r=lower_names.count('r')
u=lower_names.count('u')
e=lower_names.count('e')

true=t+r+u+e

l=lower_names.count('l')
o=lower_names.count('o')
v=lower_names.count('v')
e=lower_names.count('e')

love=l+o+v+e

love_score=int(str(true)+str(love))


if love_score<10 or love_score>90:
    print(f"Your love score is {love_score} and you go like coke and mentose")
elif love_score>=40 and love_score<=50:
    print(f"Your love score is {love_score} and you are alright together")
else:
    print(f"Your love score is {love_score}")