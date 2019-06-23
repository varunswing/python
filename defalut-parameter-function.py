def gender(sex = "Unknown"):
    if sex is 'm':
        sex = "Male"
    elif sex is 'f':
        sex = "Female"
    print(sex)

gender('m')
gender('f')
gender()