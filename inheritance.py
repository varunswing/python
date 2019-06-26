class Parent():
    def last_name(self):
        print('kumari')

class Child(Parent):
    def first_name(self):
        print('Paridhi')

    def last_name(self):
        print('Lumari')

paridhi = Child()
paridhi.first_name()
paridhi.last_name()