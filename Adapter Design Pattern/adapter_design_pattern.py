class WeatherProvider:
    """
    Existing class providing weather information with temperature in Celsius.
    """

    def get_temperature(self):
        return 25  # Dummy temperature value in Celsius


class FahrenheitAdapter:
    """
    Adapter class to convert temperature from Celsius to Fahrenheit.
    """

    def __init__(self, weather_provider):
        self.weather_provider = weather_provider

    def get_temperature(self):
        # Retrieve temperature in Celsius from the WeatherProvider
        celsius_temperature = self.weather_provider.get_temperature()
        # Convert Celsius to Fahrenheit
        fahrenheit_temperature = (celsius_temperature * 9 / 5) + 32
        return fahrenheit_temperature


# Example usage:
if __name__ == "__main__":
    weather_provider = WeatherProvider()
    fahrenheit_adapter = FahrenheitAdapter(weather_provider)

    # Using the adapter to get temperature in Fahrenheit
    temperature_fahrenheit = fahrenheit_adapter.get_temperature()
    print(f"Temperature in Fahrenheit: {temperature_fahrenheit:.2f}°F")  # Output: Temperature in Fahrenheit: 77.00°F
