import requests, time, openai, consts
from answer import answer

ai_token = consts.ai_token
tg_token = consts.tg_token
openai.api_key = ai_token

class Bot:
    def __init__(self, token) -> None:
        self.token = token
        pass
    
    def req(self, method: str, query: list | str='') -> any:
      if query:
         if type(query) == list:
          buf = '?'
          for elem in query:
              buf += str(elem[0]) + '=' + str(elem[1]) + '&'

          query = buf[0:len(buf)-1]
          
      return requests.get(f'https://api.telegram.org/bot{self.token}/{method}{query}').json()
    
    def getMe(self):
      return self.req('getMe')
    
    def getUpdates(self, offset:str=None) -> list:
       return self.req('getUpdates', '' if offset == None else [['offset', str(offset)]])
    
    def sendMessage(self, chatId: int, message: str):
       return self.req('sendMessage', [['chat_id', str(chatId)],['text', message]])

bot = Bot(tg_token)

sec = 0
while True:
  time.sleep(1)
  
  try:
    if len(bot.getUpdates()['result']) > 0:
      message = bot.getUpdates()['result'][0]
      
      #########
      
      answer(bot, openai, message)

      #########
      
      bot.getUpdates(message['update_id']+1)
  except:
    print('Occured err')
    None # nothing to worry :)