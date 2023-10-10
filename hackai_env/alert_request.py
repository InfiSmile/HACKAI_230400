from uagents import Context, Model, Protocol

# Define a model for fetching temperature and specifying temperature limits
class fetch_temp(Model):
    current_temp: float
    temperature_min: float
    temperature_max: float

# Define a model for the alert response
class AlertResponse(Model):
    alert_status: str

# Create a Protocol for alert-related communication
alert_proto = Protocol()

# Define a message handler to check temperature and send alerts
@alert_proto.on_message(model=fetch_temp, replies=AlertResponse)
async def check_temperature_alert(ctx: Context, sender: str, msg: fetch_temp):
    # Get temperature and limits from the message
    current_temperature = msg.current_temp
    minimum = msg.temperature_min
    maximum = msg.temperature_max
    
    # Check if the current temperature is below the minimum
    if current_temperature < minimum:
        await ctx.send(sender, AlertResponse(alert_status=f"Temperature is below the preferred range {minimum}°C."))
    
    # Check if the current temperature is above the maximum
    if current_temperature > maximum:
        await ctx.send(sender, AlertResponse(alert_status=f"Temperature is above the preferred range {maximum}°C."))
