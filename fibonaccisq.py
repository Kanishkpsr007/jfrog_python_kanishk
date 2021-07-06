# Program to display the Fibonacci sequence up to 10 terms

nterms = 10

# first two terms
n1, n2 = 0, 1
count = 0
print("Fibonacci sequence upto 10 terms:")
while count < nterms:
    print(n1)
    nth = n1 + n2
    # update values
    n1 = n2
    n2 = nth
    count += 1