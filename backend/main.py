from flask import Flask, jsonify, render_template, redirect, url_for
import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration
class CustomError(Exception):
    pass
sentry_sdk.init(
    dsn="https://6da94bd27d7616efad7249447dee97b5@o4507090108284928.ingest.us.sentry.io/4507090114183168",
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    traces_sample_rate=1.0,
    # Set profiles_sample_rate to 1.0 to profile 100%
    # of sampled transactions.
    # We recommend adjusting this value in production.
    profiles_sample_rate=1.0,
)


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/error')
def trigger_error():
     raise CustomError("A custom error has been triggered!")

@app.errorhandler(CustomError)
def handle_custom_error(error):
    response = jsonify({
        "message": str(error),
        "status": "error"
    })
    response.status_code = 500  # You can set this to whatever status code you deem appropriate
    return response
if __name__ == '__main__':
    app.run(debug=True)




