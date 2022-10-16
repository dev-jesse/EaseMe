from flask import Flask, render_template, request
import cohere
from cohere.classify import Example
from random import randint

app = Flask(__name__)
co = cohere.Client('NvfQrz8ZrBLdqprvUu1fDVC1fdYEvLLK9SYUDOwK')

replies = {
    'motivation' : [],
    'stress' : [],
    'anxiety' : [],
    'laugh' :[]
}

@app.route('/get')
def get_response():
    userText = request.args.get('msg')
    
    response = co.classify( 
    model='large', 
    inputs=[userText], 
    examples=[Example("give me hope", "motivation"), Example("show me some motivation", "motivation"), Example("amp my day up", "motivation"), Example("get me hyped up for the day", "motivation"), Example("say something inspirational", "motivation"), Example("why am i always so tired", "stress"), Example("how to calm down", "stress"), Example("my brain hurts", "stress"), Example("why am i so mad", "stress"), Example("frustrated with everything", "stress"), Example("i am constantly sad", "anxiety"), Example("why do i always overthink", "anxiety"), Example("i get so nervous", "anxiety"), Example("worrying all the time", "anxiety"), Example("mind wont shut off", "anxiety"), Example("tell me a joke", "laugh"), Example("say something funny", "laugh"), Example("give me something to laugh to", "laugh"), Example("help cheer me up", "laugh"), Example("make my day better", "laugh")]) 
    
    replies_list = replies[response.classifications[0].prediction]
    res = replies_list[randint(1, len(replies_list) - 1)]
    
    
    return


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/einsteinchat')
def EinsteinChat():
    return render_template('einsteinchat.html')

app.run(host='0.0.0.0', port=80)