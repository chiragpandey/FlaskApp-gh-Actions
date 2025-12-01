from flask import Flask 
# Importing the Flask class from the flask module

app = Flask(__name__) 
# Creating an instance of the Flask class/app. 
# __name_ is a special variable that holds the name of the current module &
# tells Flask where to looks for resources such as templates and static files.

@app.route('/') 
# A route decorator that binds the URL '/' to the hello_world function. It associates the hello_world function with the root URL (/).

def hello_world(): # A function that returns a simple string/'greeting message' when the root URL is accessed.
    return "Hello, World! This is a basic Flaks app. It will be deployed on EC2 by setting up a CI/CD pipeline using Github Actions"

@app.route('/greet/<name>') 
# A dynamic route that takes 'name' as a parameter from the URL. 
# Demonstrates a dynamic route, where <name> is a variable passed to the greet function

def greet(name): # A function that takes a name parameter and returns a personalized greeting message.
    return f"Hello, {name}! Welcome to our Flask application."

if __name__ == '__main__': # This block ensures that the Flask app runs only if the script is executed directly (not imported as a module).
    app.run(host='0.0.0.0', port=5000) # Running the Flask application on host
    app.run(debug=True) # Enabling debug mode for easier troubleshooting during development.