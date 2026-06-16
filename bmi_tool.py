import re


def bmi_calculator(query):

    try:

        numbers = re.findall(r"\d+\.?\d*", query)

        if len(numbers) < 2:
            return "Invalid input"

        weight = float(numbers[0])
        height = float(numbers[1])

        bmi = round(weight / (height ** 2), 2)

        if bmi < 18.5:
            category = "Underweight"

        elif bmi < 25:
            category = "Normal Weight"

        elif bmi < 30:
            category = "Overweight"

        else:
            category = "Obese"

        return f"BMI: {bmi}\nCategory: {category}"

    except Exception as e:
        return f"Error: {e}"