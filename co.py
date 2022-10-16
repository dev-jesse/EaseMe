import cohere
from cohere.classify import Example
co = cohere.Client('NvfQrz8ZrBLdqprvUu1fDVC1fdYEvLLK9SYUDOwK')
response = co.classify(
  model='large',
  inputs=[],
  examples=[Example("give me hope", "motivation"), Example("show me some motivation", "motivation"), Example("amp my day up", "motivation"), Example("get me hyped up for the day", "motivation"), Example("say something inspirational", "motivation"), Example("why am i always so tired", "stress"), Example("how to calm down", "stress"), Example("my brain hurts", "stress"), Example("why am i so mad", "stress"), Example("frustrated with everything", "stress"), Example("i am constantly sad", "anxiety"), Example("why do i always overthink", "anxiety"), Example("i get so nervous", "anxiety"), Example("worrying all the time", "anxiety"), Example("mind wont shut off", "anxiety"), Example("tell me a joke", "laugh"), Example("say something funny", "laugh"), Example("give me something to laugh to", "laugh"), Example("help cheer me up", "laugh"), Example("make my day better", "laugh")])
print(response.classifications[0].prediction)