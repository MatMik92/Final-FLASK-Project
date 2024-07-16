"""
Emotion Detection App using Flask.
This module sets up a Flask application for detecting emotions in text.
"""
from flask import Flask, request, render_template
from .emotion_detection import emotion_detector

app = Flask("Emotion Detection App")

@app.route("/")
def render_index_page():
    """
    Render the index page.

    :return: The rendered index.html template.
    """
    return render_template('index.html')

@app.route("/emotionDetector", methods=['GET'])
def emotion_detector_route():
    """
    Handle the emotion detection route.

    This function retrieves the text to analyze from the request, uses the
    emotion_detector function to analyze it, and returns a formatted response.

    :return: Formatted response with emotion analysis.
    """
    statement = request.args.get('textToAnalyze')
    emotions = emotion_detector(statement)
    if emotions['dominant_emotion'] is None:
        return "Invalid text! Please try again."

    formatted_response = (
        f"For the given statement, the system response is 'anger': {emotions['anger']}, "
        f"'disgust': {emotions['disgust']}, 'fear': {emotions['fear']}, 'joy': {emotions['joy']}, "
        f"'sadness': {emotions['sadness']}. The dominant emotion is "
        f"{emotions['dominant_emotion']}."
    )

    return formatted_response

if __name__ == '__main__':
    app.run(host='localhost', port=5000)
