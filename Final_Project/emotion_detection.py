import requests
import json

def emotion_detector(text_to_analyze):
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(URL, json = input_json, headers=header)
    dict_response = json.loads(response.text)

    if response.status_code == 200:
        return dict_response
    elif response.status_code == 400:
       dict_response = {
                           'anger': None,
                           'disgust': None, 
                           'fear': None, 
                           'joy': None, 
                           'sadness': None, 
                           'dominant_emotion': None}
    return dict_response

def emotion_predictor(matching_text):
    if all(value is None for value in matching_text.values()):
        return matching_text
    if matching_text['emotionPredictions'] is not None:
        emotions = matching_text['emotionPredictions'][0]['emotion']
        anger = emotions['anger']
        disgust = emotions['disgust']
        fear = emotions['fear']
        joy = emotions['joy']
        sadness = emotions['sadness']
        max_emotion = max(emotions, key=emotions.get)
        emotion_formated = {
                                'anger': anger,
                                'disgust': disgust,
                                'fear': fear,
                                'joy': joy,
                                'sadness': sadness,
                                'dominant_emotion': max_emotion
                                }
        return emotion_formated