name = ["one", 'two', 'three', "four", "five", "six", "seven", "eight", "nine"]
name_1 = ["ten", "eleven", 'twelve', 'thirteen', "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
name_2 = ["ten", "twenty", 'thirty', 'forty ', "fifty", "sixty", "seventy", "eighty", "ninety"]

print("Please Enter the number that you want to convert into words...")
print("Type QUIT or BACK to leave the program")
print("!! ONLY NUMBER IN THE RANGE OF 0000 - 9999 ARE ALLOWED !!")
print("")

while True:
    try:
        while True:
            x = input("Number:")
            y = int(x) - 1
            xx = str(x)
            z1 = xx[0]

            yy = int(z1) - 1

            if type(int(x)) == int:
                if int(x) == 0:
                    print("Zero".capitalize())

                elif len(xx) == 1:
                    print(name[y].capitalize())

                elif len(xx) == 2:
                    z2 = xx[1]
                    y2 = xx[1]

                    if int(xx[1]) == 0:
                        print(name_2[int(xx[0]) - 1].capitalize())
                    elif int(xx[0]) == 1:
                        print(name_1[int(z2)].capitalize())
                    else:
                        print(name_2[yy].capitalize() + " " + name[int(y2) - 1].capitalize())

                elif len(xx) == 3:
                    if int(xx[1]) == 0:
                        if int(xx[2]) == 0:
                            print(name[int(xx[0]) - 1].capitalize() + " hundred ".capitalize())
                        else:
                            print(name[int(xx[0]) - 1].capitalize() + " hundred and ".capitalize() + name[int(xx[2]) - 1].capitalize())
                    elif int(xx[1]) == 1:
                        print(name[int(xx[0]) - 1].capitalize() + " hundred and ".capitalize() + name_1[int(xx[2])].capitalize())
                    else:
                        if int(xx[2]) == 0:
                            print(name[int(xx[0]) - 1].capitalize() + " hundred and ".capitalize() + name_2[int(xx[1]) - 1].capitalize())
                        else:
                            print(name[int(xx[0]) - 1].capitalize() + " hundred and ".capitalize() + name_2[int(xx[1]) - 1].capitalize() + " " + name[
                                int(xx[2]) - 1].capitalize())

                elif len(xx) == 4:
                    z2 = xx[1]
                    y2 = xx[1]
                    if int(xx[1]) == 0:
                        if int(xx[2]) == 0:
                            if int(xx[3]) == 0:
                                print(name[int(xx[0]) - 1].capitalize() + " thousand".capitalize())
                            else:
                                print(name[int(xx[0]) - 1].capitalize() + " thousand and ".capitalize() + name[int(xx[3]) - 1].capitalize())
                        elif int(xx[2]) == 1:
                            print(name[int(xx[0]) - 1].capitalize() + " thousand and ".capitalize() + name_1[int(xx[3])].capitalize())
                        else:
                            if int(xx[3]) == 0:
                                print(name[int(xx[0]) - 1].capitalize() + " thousand and ".capitalize() + name_2[int(xx[2]) - 1].capitalize())
                            else:
                                print(name[int(xx[0]) - 1].capitalize() + " thousand and ".capitalize() + name_2[int(xx[2]) - 1].capitalize() + " " + name[
                                    int(xx[3]) - 1].capitalize())
                    else:
                        if int(xx[2]) == 0:
                            if int(xx[3]) == 0:
                                print(name[int(xx[0]) - 1].capitalize() + " thousand ".capitalize() + name[int(xx[1]) - 1].capitalize() + " hundred".capitalize())
                            else:
                                print(
                                    name[int(xx[0]) - 1].capitalize() + " thousand ".capitalize() + name[int(xx[1]) - 1].capitalize() + " hundred and ".capitalize() + name[
                                        int(xx[3]) - 1].capitalize())
                        elif int(xx[2]) == 1:
                            print(name[int(xx[0]) - 1].capitalize() + " thousand ".capitalize() + name[int(xx[1]) - 1].capitalize() + " hundred and ".capitalize() + name_1[
                                int(xx[3])].capitalize())

                        else:
                            if int(xx[3]) == 0:
                                print(name[int(xx[0]) - 1].capitalize().capitalize() + " thousand ".capitalize() + name[int(xx[1]) - 1].capitalize() + " hundred and ".capitalize() +
                                      name_2[
                                          int(xx[2]) - 1].capitalize())
                            else:
                                print(name[int(xx[0]) - 1].capitalize() + " thousand ".capitalize() + name[int(xx[1]) - 1].capitalize() + " hundred and ".capitalize() +
                                      name_2[
                                          int(xx[2]) - 1].capitalize() + " " + name[int(xx[3]) - 1].capitalize())
                elif len(xx) > 4:
                  print("PLEASE ENTER THE NUMBER FROM THE RANGE OF 0000 - 9999")





    except ValueError:
      if x.lower() == "quit":
        print("THANK YOU!")
        break
      elif x.lower() == "back":
        print("THANK YOU!")
        break
      else:
        print("PLEASE ENTER VALID DATA. FROM A RANGE 0000 - 9999")