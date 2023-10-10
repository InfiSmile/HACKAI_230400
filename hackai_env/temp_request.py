from uagents import Context, Model, Protocol
import requests



class CurrentTempRequest(Model):
    location: str
    

class TempResponse(Model):
    current_temperature: float

temp_proto=Protocol()
@temp_proto.on_message(model=CurrentTempRequest,replies={TempResponse})
async def current_temp_handler(ctx: Context,sender: str, msg: CurrentTempRequest ):
        
        current_temperature = await get_current_temperature(location=msg.location)
        print(current_temperature)
        
             
        await ctx.send(sender, TempResponse(current_temperature=current_temperature))

    

async def get_current_temperature(location):
    api_key = "bd62d2514739f378f2f8be39d8781bc0"
    base_url = "https://api.openweathermap.org/data/2.5/weather?q="

    complete_url = f"{base_url}{location}&appid={api_key}"

    try:
        response = requests.get(complete_url)
        data = response.json()
        # Extract temperature data from the response (replace with actual API structure)
        temperature = data["main"]["temp"]
        return (temperature-273.15)
    except Exception as e:
       
        print(f"Error fetching temperature: {e}")
        return 0
    






