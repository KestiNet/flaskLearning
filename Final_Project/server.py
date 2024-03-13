from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

@app.route("/")
def render_index_page():
    return render_template("index.html")

@app.route("/emotionDetector")
def get_emotion_details():
    text_to_analyze = request.args.get("text")
    response = emotion_detector(text_to_analyze)
    if response["dominant_emotion"] is None:
        return "Text was invalid, try again"
    return f"For the given statement, the system response is 'anger': {response['anger']}, 'disgust': {response['disgust']}, 'fear': {response['fear']}, 'joy': {response['joy']} and 'sadness': {response['sadness']}. The dominant emotion is {response['dominant_emotion']}"


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000)