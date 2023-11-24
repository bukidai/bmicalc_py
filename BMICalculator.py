class BMICalculator:
    def __init__(self, height, weight):
        self.height = height
        self.weight = weight

    def calculateBMI(self):
        return self.weight / (self.height**2)

    def getBMI(self):
        bmi = self.calculateBMI()
        if bmi < 18.5:
            return "Underweight"
        elif bmi < 25:
            return "Normal"
        elif bmi < 30:
            return "Overweight"
        else:
            return "Obese"
