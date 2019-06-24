while True:
    try:
        number = int(input("What is your favourate number boss?\n"))
        print(number/2)
        break
    except ValueError:
        print("Make sure you entered a number.")
    except ZeroDivisionError:
        print("Don't pick a zero.")
    except:
        break
    finally:
        print("Loop completed.")
