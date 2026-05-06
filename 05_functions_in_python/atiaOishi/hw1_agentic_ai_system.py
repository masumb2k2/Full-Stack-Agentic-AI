from datetime import datetime as dt

def get_weather():
    print("calling weather tool...")
    return "Current weather: Sunny, 75°F, Light breeze"


def get_time():
    print("calling time tool...")
    current_time = dt.now().strftime("%B-%d-%Y %H:%M:%S")
    return f"Current time: {current_time}"


weather_keywords = [
    "weather", "forecast", "rain", "sunny", "temperature", "climate",
    "cold", "hot", "snow", "wind", "humidity", "storm", "thunderstorm",
    "cloudy", "clear", "precipitation", "conditions", "degrees",
    "celsius", "fahrenheit", "outside", "raining", "snowing"
]

time_keywords = [
    "time", "current time", "what time", "clock", "hour", "minute",
    "second", "am", "pm", "morning", "afternoon", "evening", "night",
    "now", "schedule", "timestamp", "o'clock"
]


def input_router(user_input):
    user_input_lower = user_input.lower()

    if any(keyword in user_input_lower for keyword in weather_keywords):
        return get_weather()

    elif any(keyword in user_input_lower for keyword in time_keywords):
        return get_time()

    return "Sorry, I don't understand. Please ask about weather or time."


def main():
    print("=" * 80)
    print("         Welcome to Smart Tool Router - Agentic AI System")
    print("=" * 80)

    print("\nYou can ask about time date and current Weather.")
    
    print("\nType 'exit' or 'quit' to terminate.\n")
    print("-" * 80)

    while True:
        try:
            user_input = input("\nHello, how can I assist you? ")

            if user_input.lower() in ["exit", "quit"]:
                print("Goodbye!")
                break

            if not user_input.strip():
                print("Please enter something valid.")
                continue

            result = input_router(user_input)
            print(result)

        except Exception as e:
            print("An error occurred:", e)


if __name__ == "__main__":
    main()