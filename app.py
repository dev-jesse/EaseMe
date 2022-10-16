from flask import Flask, render_template, request
import cohere
from cohere.classify import Example
from random import randint

app = Flask(__name__)
co = cohere.Client('NvfQrz8ZrBLdqprvUu1fDVC1fdYEvLLK9SYUDOwK')

replies = {
    'motivation' : ["Be more concerned with you character than your reputation, as your character is what you really are, while your reputation is what others think you are", "We cannot solve problems with the kind of thinking we employed when we came up with them", "Stay away from those people who try to disparage your ambitions. Small minds will always do that, but great minds will give you a feeling that you can become great too.", "Success is not final; failure is not fatal: It is the courage to continue that counts."],
    'stress' : ["Sometimes letting things go is an act of far greater power than defending or hanging on", "Do not anticipate trouble, or worry about what may never happen. Keep in the sunlight.", "Time you enjoy wasting is not wasted time", "Rule number one is, don’t sweat the small stuff. Rule number two is, it’s all small stuff"],
    'anxiety' : ["If you get too engrossed and involved and concerned in regard to things over which you have no control, it will adversely affect the things over which you have control", "There are only two ways to live your life. One is as though nothing is a miracle. The other is as though everything is a miracle.", "The most important conversations you’ll ever have are the ones you’ll have with yourself", "we are all born so beautiful, the greatest tragedy is in being convinced we are not"],
    'laugh' :["How many flies does it take to screw in a lightbulb? Just two but I have no idea how they got in there.", "When does a joke become a dad joke? When it becomes apparent.", "What's blue and isn't very heavy?, Light blue"]
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
    
    request.args.update
    
    return


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/einsteinchat')
def EinsteinChat():
    return render_template('einsteinchat.html')

app.run(host='0.0.0.0', port=80)