# HACKAI_230400


# Temperature Monitoring Application

This Temperature Monitoring Application is a web-based system that allows users to monitor and receive alerts for temperature conditions. It communicates with external weather APIs to fetch real-time temperature data for specified locations and checks if the temperature falls outside the defined acceptable range.

## Project Overview

The project consists of a Flask-based web application with the following features:

1. **User Registration and Input**:
   - Users can access the application through a web interface.
   - They are required to provide a unique user ID, location, and preferred temperature range (minimum and maximum) via a form.
   - after clicking submit button reload the page
   - I have tried creating an interface . Also the output will be visible in the terminal window giving the alert_status.
   - If you want to check for another location just save the application file and after entering the location reload the page.

2. **Background Temperature Monitoring**:
   - The application continuously fetches temperature data from external APIs (e.g., OpenWeatherMap) in the background.
   - It uses asynchronous agents to send requests and receive temperature data.

3. **Alert System**:
   - If the fetched temperature goes below or above the specified range, an alert message is generated.
   - Users can receive alerts indicating that the temperature is outside their preferred range.

4. **Real-time Updates**:
   - The web page displays real-time updates of the current temperature and alert status.
   - Updates are sent to the web page using Flask-SocketIO, allowing dynamic content updates without the need for manual page refreshing.

## Getting Started

To run the Temperature Monitoring Application locally, follow these steps:

1. **Clone the Repository**:
   - Clone this repository to your local machine.

2. **Setup Virtual Environment (Optional)**:
   - Create a virtual environment to manage dependencies (recommended).
   - python -3.10 -m venv <name_of_your_env> (in my case it's hackai_env)
   - hackai_env/scripts/activate
   - pipenv --python 3.10
3. **Dependencies**:
   - pip install pipenv
   - pip install flask
   - pip install uagents
   - pip install Flask-SocketIO
   
**Run the Application**:
- Execute the `application.py` script to start the Flask application.
- make sure that you have three files and 1 folder in your environment folder 1. temp_request 2. application 3. alert_request and templates folder
- run the application.py file after following all the steps


