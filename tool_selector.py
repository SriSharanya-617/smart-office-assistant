import ollama

query = input("Enter Query: ")

prompt = f"""
You are a tool selector.

Available Tools:
1. Calculator
2. Weather
3. Time
4. UnitConverter
5. BMI

Rules:
- Mathematical expressions -> Calculator
- Weather questions -> Weather
- Time/date questions -> Time
- Unit conversions -> UnitConverter
- BMI calculations -> BMI

Return ONLY the tool name.

Query:
{query}
"""

response = ollama.chat(
    model="llama3",
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ]
)

tool = response["message"]["content"].strip()

print("\nSelected Tool:")
print(tool)