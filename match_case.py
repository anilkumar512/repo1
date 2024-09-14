question=input("Who invented telephone?\nA.Alexander Grahambell\t\t\tB.Einstein\nC.Nicolas Tesla\t\tD.Thomas Alva Edison\n")
match question:
    case "A":
        print("Option A.Alexander Grahambell is locked")

    case "B":
        print("Option B.Einstein is locked")

    case "C":
        print("Option C.Nicolas Tesla is locked")

    case "D":
        print("Option D.Thomas Alva Edison is locked")
    case _:
        print("Invalid option")