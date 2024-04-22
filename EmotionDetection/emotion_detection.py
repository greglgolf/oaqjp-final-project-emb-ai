import json, requests


def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyse } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    #Input json: { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, json = myobj, headers=header)
    formatted_response = json.loads(response.text)
    emotions = formatted_response['emotionPredictions'][0]['emotion']
    max_emo = max(emotions, key=emotions.get)
    max_emo_score = emotions[max_emo]
    formatted_data = {
        'anger':emotions['anger'],
        'disgust':emotions['disgust'],
        'fear':emotions['fear'],
        'joy':emotions['joy'],
        'sadness':emotions['sadness'],
        'dominant_emotion':max_emo
    }
   
    #return {json.dumps(formatted_data, indent=4)}
    return formatted_data