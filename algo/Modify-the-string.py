# How-to-Modify-the-string
# You want to insert sub string or character into the main string at any position of the main string.


def StringModify():
    i = input("Enter the string:\t\n")
    char = input("Are you ready to insert the string.\n\nIf 'yes' press Y/y or If 'No' then press N/n\t\t")
    if char == 'Y' or char == 'y':
        print("You press Yes\n")
        n = int(input("Enter position number\t\n"))
        str1 = input("Enter any string to insert\t")
        print('\n\nModifyed string:\t', i[:n] + str1 + i[n:])

    elif char == 'N' or char == 'n':
        print("You Press No")
        pass

    print("\n\n\nThank you\n")


StringModify()
