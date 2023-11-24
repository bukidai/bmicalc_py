from BMICalculator import BMICalculator


def main():
    height = float(input("Enter height in meters: "))
    weight = float(input("Enter weight in kilograms: "))
    bmiCalc = BMICalculator(weight, height)
    print("BMI is", bmiCalc.calculateBMI(), bmiCalc.getBMI())


if __name__ == "__main__":
    main()
