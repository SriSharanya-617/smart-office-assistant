from datetime import datetime


def current_time_tool(query):

    now = datetime.now()

    current_datetime = now.strftime("%d-%m-%Y %I:%M:%S %p")

    return f"Current Date and Time: {current_datetime}"