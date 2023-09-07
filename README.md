# HNG-backend-internship

This repository contains all the task solutions for the HNG internship program from stage one to stage ten.

## Stage One

### Objective :dart:

Create and host an endpoint using any programming language of your choice. The endpoint should take two GET request query parameters and return specific information in JSON format.

### Requirements :spiral_note_pad:

The information required includes:

- Slack name
- Current day of the week
- Current UTC time (with validation of +/-2)
- Track
- The GitHub URL of the file being run
- The GitHub URL of the full source code
- A Status Code of Success

**JSON Format:**

```json
{
  "current_day": "Thursday",
  "github_file_url": "https://github.com/DT-GAMER/HNG-backend-internship/blob/main/app.py",
  "github_repo_url": "https://github.com/DT-GAMER/HNG-backend-internship",
  "slack_name": "Abakpa Dominic",
  "status_code": 200,
  "track": "backend",
  "utc_time": "2023-09-07T11:52:12Z"
}

