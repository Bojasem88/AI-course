# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 06:27:49 2019

@author: Mohammad Hamid & Mohammad Marwan
"""

# importing Packeges
import chatterbot
from chatterbot.trainers import ListTrainer
import speech_recognition as sr
import pyttsx3
import json
import time
import requests
from flask import Flask,render_template, request

# Creating App varialbe for Flask
app = Flask(__name__)
# Text to speech "Phase2"
engine = pyttsx3.init()
# Creating the training model
bot = chatterbot.ChatBot("newbot")
trainer2=ListTrainer(bot)
# Importing dataset
folder = r"chatbotdata"
import os
files = os.listdir(folder)
# Train the model
for file in files:
    data = open (folder+"\\"+file).readlines()
    trainer2.train(data)
# Sending the file Index.html for get requrest on local host    
@app.route('/',methods=['POST','GET'])
def main():
    return render_template("index.html")
# replying to the get request by the user with the response
@app.route('/get')
def get_response():
    userqus = request.args.get('msg')
    return str(bot.get_response(userqus))
# calling the app to run when the main file is imported. this is to ensure running from Terminal only
if __name__=='__main__':
    app.run(debug=False)   
