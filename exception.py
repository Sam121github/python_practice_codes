while True:
    try:
        number = int(input("what's your favourite number\n"))
        print(18/number)
        break
    except ValueError:
        print("please enter a valid input format")
    except ZeroDivisionError:
        print("you cannot enter zero as your input.... Please try again!!")

    finally:
        print("program running")

