Rows = int(input("Enter the Number of rows:"))

num = 1
for row in range(1, Rows + 1):
    for column in range(row):
        print(num, end="")
        num = num + 1
    print()    