# Import the Flask application instance from the flaskblog package
from flaskblog import app

# Run the application only if this file is executed directly (not imported)
if __name__=="__main__":
   # Start the Flask development server
   # host="0.0.0.0" makes the server accessible from any IP address
   # debug=True enables debug mode with auto-reload and detailed error messages
   app.run(host="0.0.0.0",debug=True)