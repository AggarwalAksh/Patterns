# Aksh 09/03/2023 Star pyramid
n = int(input('Enter the number of rows'))
for i in range(n):
    print(" " * (n-i-1) + "* " * (i+1))
for i in range(n-1):
    print(" " * (i+1) + "* " * (n-i-1))
