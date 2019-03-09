try:
    print(10/2)
    # print(10/0)
except NameError as ne:
    print("in NameError except, ",ne)
except ArithmeticError:
    print("Arrithmatic problem")
else:
    print("try statement is successfully executed!")
finally:
    print("final statement")