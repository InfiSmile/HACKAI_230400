from uagents import Context, Model, Protocol
import requests

# Define a model for requesting current temperature
class CurrentTempRequest(Model):
    location: str

# Define a model for the temperature response
class TempResponse(Model):
    current_temperature: float

# Create a Protocol for temperature-related communication
temp_proto = Protocol()

# Define a message handler for requesting current temperature
@temp_proto.on_message(model=CurrentTempRequest, replies={TempResponse})
async def current_temp_handler(ctx: Context, sender: str, msg: CurrentTempRequest):
    # Get the current temperature for the specified location
    current_temperature = await get_current_temperature(location=msg.location)

    # Send the temperature response back to the sender
    await ctx.send(sender, TempResponse(current_temperature=current_temperature))

# Function to fetch the current temperature using an external API
async def get_current_temperature(location):
    # Replace this with loading API key from environment variables
    api_key = "bd62d2514739f378f2f8be39d8781bc0"
    base_url = "https://api.openweathermap.org/data/2.5/weather?q="

    complete_url = f"{base_url}{location}&appid={api_key}"

    try:
        response = requests.get(complete_url)
        data = response.json()
        # Extract temperature data from the response (replace with actual API structure)
        temperature = data["main"]["temp"]
        return (temperature - 273.15)
    except Exception as e:
        print(f"Error fetching temperature: {e}")
        return 0







