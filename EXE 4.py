name = input("Student name")

maths = int(input("maths"))
english = int(input("english"))
chem = int(input("chem"))
kiswa = int(input("kiswa"))
comps = int(input("comps"))


average = (maths + english + chem + kiswa + comps) /5
print(f"average = {average}")

if average >= 0 and average <= 39:
    print("E")

if average >= 40 and average <= 50:
    print("D")

if average >= 51 and average <= 60:
    print("C")

if average >= 61 and average <= 70:
    print("B")

if average >= 71 and average <= 100:
    print("A")

else:
  print("error")