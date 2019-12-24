# How do you find the missing number in a given integer array of 1 to 100


def missing_number(nu):
    if nu in (_ for _ in range(101)):
        print(nu, "present in b/w 1 to 100")


nu = int(input("Enter any number"))
missing_number(nu)
