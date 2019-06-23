def allowed_dating_age(my_age):
    girl_age = my_age/2 + 7
    return girl_age

varun_limit = allowed_dating_age(18)
vipul_limit = allowed_dating_age(27)
print("Varun can date a girl", varun_limit, "years or old.")
print("Vipul can date a girl", vipul_limit, "years or old.")