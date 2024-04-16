from flask import Flask, jsonify, render_template, redirect, url_for
import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration
class CustomError(Exception):
    pass
sentry_sdk.init(
    dsn="https://5fea07087b29959fee4b01cde17be551@o4507090108284928.ingest.us.sentry.io/4507097178636288",
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
     raise Exception("Europe website,2,Sebastian Cousins,Akamai DNS failure 'Intermittent DNS failures impacting EU0 - Europe website due to a known Akamai bug.',  'client_impact': 'Intermittent access issues for users of EU0 - Europe website. 1:35 PM ET: Multiple alerts for DNS failures received. Issue reproduced; no logs indicating request reached application. 2:00 PM ET: Engaged Akamai for DNS support. 2:20 PM ET: Akamai confirmed the symptoms are related to a known bug.")

@app.errorhandler(CustomError)
def handle_custom_error(error):
    response = jsonify({
        "message": str(error),
        "status": "error"
    })
    response.status_code = 500  # You can set this to whatever status code you deem appropriate
    return response
if __name__ == '__main__':
    app.run(debug=True, port=8090)




