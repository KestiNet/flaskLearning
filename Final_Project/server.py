"""
This is the main server for thsi flask application
"""
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector, emotion_predictor

app = Flask("emotion_detection_app")

@app.route("/")
def render_index_page():
    """
    This renders the index.html page
    """
    return render_template('index.html')

@app.route("/emotionDetector")
def sent_detector():
    """
    This function is used to detect the text that user provides
    """
    text_to_detect = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_detect)
    formated_response = emotion_predictor(response)
    if formated_response['dominant_emotion'] is None:
        return "Invalid text! Please try again."
    return (
        f"For the given statement, the system response is 'anger': {formated_response['anger']} "
        f"'disgust': {formated_response['disgust']}, 'fear': {formated_response['fear']}, "
        f"'joy': {formated_response['joy']} and 'sadness': {formated_response['sadness']}. "
        f"The dominant emotion is {formated_response['dominant_emotion']}."
    )

def run_emotion_detection():
    """
    Runs the flask app
    """
    app.run(host="0.0.0.0", port=5000)

if __name__ == "__main__":
    run_emotion_detection()
