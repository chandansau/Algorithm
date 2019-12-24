# How do you find the missing number in a given integer array of 1 to 100


def missing_number(nu):
    if nu in (_ for _ in range(101)):
        print(nu, "present in b/w 1 to 100")


nu = int(input("Enter any number"))
missing_number(nu)


# ----------------2nd process ----------------------

def missing_number(nu):
    return str(nu) + " present in b/w 1 to 100" if nu in (_ for _ in range(101)) else 'Not present'


nu = int(input("Enter any number"))
print(missing_number(nu))
