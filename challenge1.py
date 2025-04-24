# دریافت عدد از کاربر
number = int(input("لطفاً یک عدد وارد کن: "))

# چاپ جدول ضرب
print(f"جدول ضرب عدد {number}:")
for i in range(1, 13):
    result = number * i
    print(f"{number} × {i} = {result}")
