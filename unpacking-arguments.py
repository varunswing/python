def health_calculator(age, apple_ate, cigs_smoked):
    answer = (100 - age) + (apple_ate * 0.5) - (cigs_smoked * 1)
    print(answer)

varun_age = [19, 20, 0]

health_calculator(varun_age[0], varun_age[1], varun_age[2])
health_calculator(*varun_age)