def unit_converter(query):

    query = query.lower()

    parts = query.split()

    try:

        value = float(parts[0])
        from_unit = parts[1]
        to_unit = parts[3]

        if from_unit == "km" and to_unit == "meters":
            return f"{value * 1000} meters"

        elif from_unit == "meters" and to_unit == "km":
            return f"{value / 1000} km"

        elif from_unit == "kg" and to_unit == "grams":
            return f"{value * 1000} grams"

        elif from_unit == "grams" and to_unit == "kg":
            return f"{value / 1000} kg"

        else:
            return "Conversion not supported"

    except Exception as e:
        return f"Error: {e}"