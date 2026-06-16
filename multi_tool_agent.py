import time

from calculator_tool import calculator_tool
from weather_tool import weather_tool
from time_tool import current_time_tool
from unit_converter import unit_converter
from bmi_tool import bmi_calculator


def select_tool(query):

    query = query.lower()

    # Weather
    if "weather" in query:
        return "Weather"

    # Time
    elif "time" in query or "date" in query:
        return "Time"

    # BMI
    elif "bmi" in query:
        return "BMI"

    # Unit Conversion
    elif (
        "km" in query
        or "meter" in query
        or "meters" in query
        or "kg" in query
        or "gram" in query
        or "grams" in query
    ):
        return "UnitConverter"

    # Calculator
    elif any(op in query for op in ["+", "-", "*", "/"]):
        return "Calculator"

    else:
        return "Unknown"


# Main Program

query = input("Enter Query: ")

start_time = time.time()

tool = select_tool(query)

print("\nThought:")
print(f"I should use the {tool} tool.")

print("\nAction:")
print(tool)

# Execute Selected Tool

if tool == "Weather":
    observation = weather_tool(query)

elif tool == "Time":
    observation = current_time_tool(query)

elif tool == "BMI":
    observation = bmi_calculator(query)

elif tool == "UnitConverter":
    observation = unit_converter(query)

elif tool == "Calculator":
    observation = calculator_tool(query)

else:
    observation = "Tool not found"

print("\nObservation:")
print(observation)

print("\nFinal Answer:")
print(observation)

end_time = time.time()

response_time = round(end_time - start_time, 4)

print("\nPerformance Report")
print("-------------------")
print("Tool Selected :", tool)
print("Result Generated :", observation)
print("Response Time :", response_time, "seconds")