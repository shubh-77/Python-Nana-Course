my_set={"Januray","Februray","March"}
my_set.add("April")
my_set.add("May")

for i in my_set:
    print(i)

print(my_set)
my_set.remove("Januray")
print(f"After removing january:{my_set}")