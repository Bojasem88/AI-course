# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 06:27:49 2019

@author: Mohammad Hamid & Mohammad Marwan
"""

# importing Packeges
from flask import Flask,render_template, request
import chatterbot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Creating App varialbe for Flask
app = Flask(__name__)

bot = chatterbot.ChatBot('smartbot')

# train the model
trainer = ChatterBotCorpusTrainer(bot)
trainer.train("chatterbot.corpus.english.ai")
# Sending the file Index.html for get requrest on local host 
@app.route('/',methods=['POST','GET'])
def main():
    return render_template("index2.html")
# replying to the get request by the user with the response
@app.route('/get')
def get_response():
    userqus = request.args.get('msg')
    return str(bot.get_response(userqus))
# calling the app to run when the main file is imported. this is to ensure running from Terminal only
if __name__=='__main__':
    app.run(debug=False)