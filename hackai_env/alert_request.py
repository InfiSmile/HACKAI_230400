from uagents import Context, Model, Protocol


class fetch_temp(Model):
    current_temp:float
    temperature_min: float
    temperature_max:float
    
class AlertResponse(Model):
    
    alert_status: str

# 

alert_proto= Protocol()


# @alert_proto.on_message(model=fetch_temp)
# async def check_temperature_alert( ctx: Context,sender:str,msg:fetch_temp):
#     print(f"hey: {msg.current_temp}")
# f"Temperature is below the preferred range {minimum}°C."
@alert_proto.on_message(model=fetch_temp,replies=AlertResponse)
async def check_temperature_alert( ctx: Context,sender:str,msg:fetch_temp):
        #ctx.logger.info(f"Received message from {sender}: {msg.current_temp}")
        minimum = msg.temperature_min
        maximum = msg.temperature_max
        # print(minimum)
        if msg.current_temp < minimum:
            
            await ctx.send(sender,AlertResponse(alert_status=f"Temperature is below the preferred range {minimum}°C."))
            
        if msg.current_temp > maximum:

            await ctx.send(sender,AlertResponse(alert_status=f"Temperature is above the preferred range {maximum}°C."))
            