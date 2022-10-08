#Checking Fermat’s Last Theorem

def check_fermat(a, b, c, n):
  if n > 2 and a**n + b**n == c**n:
    print("Holy smokes! Fermat was wrong!")
  elif n <= 2:
    print("The exponent should be grater than '2'")
  else:
    print("No, that doesn't work.")

def user_inputs_fermat(a, b, c, n):
    a = int(input("Choose a number for 'a': "))
    b = int(input("Choose a number for 'b': "))
    c = int(input("Choose a number for 'c': "))
    n = int(input("Choose a number for 'n' that's greater than '2': "))
    check_fermat(a, b, c, n)

def check_fermat(a,b,c,n):
    if n <= 2:
        print("Fermat's Last Theorem only holds for n>2")
        return
    else:
        if a ** n + b ** n == c ** n:
            print("Holy smokes, Fermat was wrong!")
        else:
            print("No, that doesn't work")

def check_numbers():
    a = int(input("Choose a number for a: "))
    b = int(input("Choose a number for b: "))
    c = int(input("Choose a number for c: "))
    n = int(input("Choose a number for n: "))
    return check_fermat(a, b, c, n)

check_numbers()



