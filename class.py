class Car (object):

    def __init__(self, model, color, company, horsepower):
        self.model = model
        self.color = color
        self.company = company
        self.horsepower = horsepower

    def start(self):
        print("started")

    def stop(self):
        print("stop")

    def pertrol(self):
        print("fueling")

    def change_gear(self):
        print("changing")

tesla = Car("Tesla_ModelX","Black","Tesla","328hp")

print(tesla.model)
print(tesla.color)
print(tesla.company)
print(tesla.horsepower)



    
