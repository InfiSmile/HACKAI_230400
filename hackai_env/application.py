from flask import Flask, render_template, request, redirect, url_for, sessions, jsonify
from uagents import Model, Context, Agent, Bureau
from flask_socketio import SocketIO, emit
from temp_request import CurrentTempRequest, TempResponse, temp_proto
from alert_request import alert_proto, fetch_temp, AlertResponse
import threading

# Create a lock for thread safety
lock = threading.Lock()

# Create Flask app
app = Flask(__name__)
socketio = SocketIO(app)

# Creating agents temp, user, and aler
temp = Agent(name="temp")
user = Agent(name="user")
aler = Agent(name="alert")

# Include protocols
aler.include(alert_proto)
temp.include(temp_proto)

location = ""
alert_status = ""
temp_min = 0.0
temp_max = 0.0
temperature = 0

# Route for the main page
@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('temperature.html', temperature=temperature, alert_status=alert_status)

# Function to request current temperature at intervals
@user.on_interval(period=5.0, messages=CurrentTempRequest)
async def get_current_temp(ctx: Context):
    global location
    await ctx.send(temp.address, CurrentTempRequest(location=location))

# Function to receive and process temperature responses
@user.on_message(model=TempResponse, replies=fetch_temp)
async def receive_temp(ctx: Context, sender: str, msg: TempResponse):
    global temp_min, temp_max, temperature
    temperature = msg.current_temperature
    await ctx.send(aler.address, fetch_temp(current_temp=temperature, temperature_min=temp_min, temperature_max=temp_max))

# Function to handle alert responses
@user.on_message(model=AlertResponse)
async def alert(ctx: Context, sender: str, msg: AlertResponse):
    global alert_status, temperature
    alert_status = msg.alert_status
    temperature = temperature

    if alert_status:
        ctx.logger.info(f"Alert! {alert_status}, current temperature is {temperature}")

    with lock:
        socketio.emit('update_data', {'temperature': temperature, 'alert_status': alert_status}, namespace='/data')

# Create a Bureau and add agents
bureau = Bureau()
bureau.add(user)
bureau.add(temp)
bureau.add(aler)

# Route for the main page with form
@app.route('/main', methods=["POST", "GET"])
def main():
    global location, temp_min, temp_max
    print("hi this is bureau")

    if request.method == 'POST':
        user_id = request.form['user_id']
        location = request.form['location']
        temp_min = float(request.form['temp_min'])
        temp_max = float(request.form['temp_max'])

    # Run the Bureau to monitor temperature
    bureau.run()
    print("ONE ROUND COMPLETED")

# Run the Flask app with SocketIO support
if __name__ == '__main__':
    socketio.run(app, debug=True)
