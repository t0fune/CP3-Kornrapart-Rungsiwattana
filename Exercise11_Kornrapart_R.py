num1 = int(input())
for i in range(num1):
    space = " " * (num1 - i - 1)
    Text = "*" * (2*i+1)
    print(space + Text + space)