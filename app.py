from flask import Flask, request, jsonify
import datetime
import pytz

app = Flask(__name__)

# Define a dictionary to map track to GitHub URLs
track_to_github = {
    "backend": {
        "github_file_url": "https://github.com/DT-GAMER/HNG-backend-internship/blob/main/app.py",
        "github_repo_url": "https://github.com/DT-GAMER/HNG-backend-internship",
    }
}

def current_utc_time():
    utc_time = datetime.datetime.now(pytz.UTC)
    return utc_time.strftime("%Y-%m-%dT%H:%M:%SZ")

@app.route('/api')
def get_info():
    #Get query parameters from the request
    slack_name = request.args.get('slack_name')
    track = request.args.get('track')

    # Validate that the 'track' parameter is in the track_to_github dictionary
    if track not in track_to_github:
       return jsonify({"error": "invalid track"}), 400

    # Get the current day of the week
    current_day = datetime.datetime.now().strftime("%A")

    # Get current UTC
    utc_time = current_utc_time()

    # Create the response JSON
    response_json = {
        "slack_name": slack_name,
        "current_day": current_day,
        "utc_time": utc_time,
        "track": track,
        **track_to_github[track],
        "status_code": 200
    }

    return jsonify(response_json)

if __name__ == '__main__':
     app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
