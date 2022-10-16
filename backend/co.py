import os, json
import random
from flask import Flask, render_template, request,jsonify
import cohere
from cohere.classify import Example
co = cohere.Client('ScMyVyouxrCBzKKQx4kUgBKvXc6Zg5rqmoYYVm5F')

app = Flask(__name__)


@app.route('/',methods = ['GET','POST'])
def index():
    service = os.environ.get('K_SERVICE', 'Unknown service')
    revision = os.environ.get('K_REVISION', 'Unknown revision')
    
    if request.method == 'POST':
        m = json.loads(request.data, strict=False)
        content = m.get("content") # object getter method
        id = m.get("id") # object getter method
        responseMessage = "none" 
        success = False
        top = m.get(int)
        if id == 0:
            success, responseMessage = intro(content)
        elif id == 1:
            success, responseMessage = intro_2(content)
        elif id == 2:
            success, responseMessage = intro_3(content)
        elif id == 3:
            success, responseMessage = topic(content)
        elif id == 4:
            if success == True:
                if (top == 1):
                    responseMessage = motivation(content)
                elif (top == 2):
                    responseMessage = lessAnxious(content)
                elif (top == 3):
                    responseMessage = energized(content)
                else:
                    responseMessage = feelGrateful(content)
        
        id += 1
        if not success:
                id = 10000;
        return jsonify(message = responseMessage,id = id);
    else:
        return render_template("index.html");

def intro(userRes):
    inputs=[userRes],
    if inputs is str:
        return ("Nice meeting you, " + inputs + ", how old are you")
    else:
        return(False, "Sorry, I don't quite understand")

def intro_2(userRes):
    input = [userRes],
    if input is int or float:
        return ("Wow, I remeber when I was " + input + " age! How are you feeling?")
    else:
        return (False, "Now, you're just being silly!")


def intro_3(userRes):
    inputs = [userRes],
    if inputs is str:
        return ("Okay, what would you like to feel right now?")
    else:
        return(False, "That's not an emotion!")


def topic(userRes): # CLASSIFY TOPIC
  classifications = co.classify(
    model='medium',
    taskDescription='',
    outputIndicator='',
    inputs=[userRes],
    examples=[])
  
  choice = classifications.classifications[0].prediction

  if choice == "Motivation":
    top = 1
    return (True,top, "")
  elif choice == "lessAnxious":
    top = 2
    return (True,top, "Money is so momentary. As a corgi myself, I would love it if you REFRESHed the page and talked about our timeless ENVIRONMENT with me!")
  elif choice == "energized":
    top = 3
    return(True,top, "s")
  elif choice == "feelGrateful":
    return (True, "s")
  else:
    return (False, "Sorry dear, I'm not that well versed in that topic, I do hope you feel better!")

def motivation(userRes):
    classifications = co.classify(
        model ="medium",
        taskDescription = "",
        outputIndicator = "",
        inputs =[userRes],
        examples = [])

def lessAnxious(userRes):
    classifications = co.classify(
        model ="medium",
        taskDescription = "",
        outputIndicator = "",
        inputs =[userRes],
        examples = [])

def energized(userRes):
    classifications = co.classify(
        model ="medium",
        taskDescription = "",
        outputIndicator = "",
        inputs =[userRes],
        examples = [])

def feelGrateful(userRes):
    classifications = co.classify(
        model ="medium",
        taskDescription = "",
        outputIndicator = "",
        inputs =[userRes],
        examples = [])

def question(userRes): # CLASSIFY BIODIVERSITY/EMISSION REDUCTION/RECYCLING 
  classifications = co.classify( 
    model='medium', 
    taskDescription='The following sorts user responses about environmental issues into categories', 
    outputIndicator='', 
    inputs=[userRes],
    examples=[Example("I don\'t eat my veggies", "Biodiversity"), Example("I wear fast fashion", "Biodiversity"), Example("I hunt endangered species", "Biodiversity"), Example("I don\'t finish my food and always toss my leftovers", "Biodiversity"), Example("I use too many tissues", "Biodiversity"), Example("I released my goldfish into the wild", "Biodiversity"), Example("I always get take out", "Biodiversity"), Example("I turn species extinct", "Biodiversity"), Example("I drive a gas powered car", "Emission Reduction"), Example("I leave the lights on when I leave the room", "Emission Reduction"), Example("I take 1 hour showers", "Emission Reduction"), Example("I go on long drives as a coping mechanism", "Emission Reduction"), Example("My A/C is always on", "Emission Reduction"), Example("I drive instead of walk or carpool", "Emission Reduction"), Example("I don\'t unplug my electronics when they\'re finished charging", "Emission Reduction"), Example("I drive my car alone", "Emission Reduction"), Example("I built a nuclear powerplant", "Emission Reduction"), Example("I hate public transportation", "Emission Reduction"), Example("I want to reduce my carbon emissions", "Emission Reduction"), Example("I\'m contributing to climate change", "Emission Reduction"), Example("I emit a lot of carbon emissions", "Emission Reduction"), Example("I produce a lot of methane", "Emission Reduction"), Example("I use a lot of fertilizer", "Emission Reduction"), Example("I don\'t know the difference between recycling and garbage", "Recycling"), Example("I put my gum under the table", "Recycling"), Example("I never keep trash in my pockets", "Recycling"), Example("I don\'t separate my trash", "Recycling"), Example("I pour my oil down the drain", "Recycling"), Example("I buy single use plastics", "Recycling"), Example("I buy plastic water bottles instead of using a reusable one", "Recycling"), Example("I use plastic straws", "Recycling"), Example("I toss my electronics and batteries into the garbage", "Recycling"), Example("I always use plastic bags when grocery shopping", "Recycling"), Example("I buy things that I don\'t need", "Recycling"), Example("I use paper documents", "Recycling"), Example("I don\'t recycle", "Recycling")]) 

  fileName = ""

  choice = classifications.classifications[0].prediction
  print("SHOWING RESULTS FOR:", choice) 
  pass1 = ""
  
  with open('recyclingt.txt', encoding="utf-8") as f:
    pass1 = f.read()
    
  if choice == "Biodiversity":
    fileName = "biodiversity.txt"
  elif choice == "Emission Reduction":
    fileName = "emissions.txt"
  elif choice == "Recycling":
    fileName = "recycling.txt"

  pass2 = ""
  with open(fileName, encoding="utf-8") as f:
      pass2 = f.read()

  p =   "This program will generate a numbered list of tips from the passage.\n--Passage:" + pass1 + "\n\nTLDR: 1. No bags. Like really, no bags.\n2. Small things are big problems.\n3. Make sure it’s clean, empty and dry\n4. Combined materials are trash\n5. Know your plastics\n6. Stop wishcycling\n7. Teach yourself\n--\nPassage:" + pass2 + "\n\nTLDR:";

  prediction = co.generate(
    model='xlarge', 
    prompt= p,
      max_tokens=150, 
    temperature=0.3, 
    k=0, 
    p=1, 
    frequency_penalty=0.1, 
    presence_penalty=0, 
    stop_sequences=["--"], 
    return_likelihoods='NONE')
  return (True, "Here are some tips to address the negative impacts of that:\n" + '\n'.join(prediction.generations[0].text.split('\n')[:-1]))



if __name__ == '__main__':
    server_port = os.environ.get('PORT', '8080')
    app.run(debug=False, port=server_port, host='0.0.0.0')