def answer(bot, openai, message: object):
  if message['message']['text'] == '/start':
      bot.sendMessage(message['message']['chat']['id'], chat_completion.choices[0].message.content);
    
  if message['message']['text'].startswith('/gpt'):
    content = message['message']['text'].split(" ")
    content = " ".join(content[1:len(content)])
    print(content)

    chat_completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": content}])
    
    # print(chat_completion.choices[0])
    bot.sendMessage(message['message']['chat']['id'], chat_completion.choices[0].message.content)