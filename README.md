Introduction 
Looking back at the way we learned at school, and how it is led to losing or forget the information, or the way we lost a specific skill, that we regret right now, we decided to do something about it, and what is better than using AI to teach AI. This project is about creating an interactive teacher and an assistant for continues learning and information retrieval in an informative and interactive way. 
This project aims to create a reliable and fast-to-reach reference library for general AI queries, best practice across the AI field, and to guide seekers throughout the steps of frequently used ML & DL and famous neuron architectures, when to use DL, ML, transfer learning, etc. 
We wanted to offer intelligent, secure, and scalable chatbot which is integrated with different chat platform, web-based or application with intuitive human interface, to create a meaningful tool and give insights to whom engaged with the chatbot.
This project will be completed on several phases, depending on crowd feedback and funding. The first phase was completed during Kaizen-Bootup AI course, the production model with multiple integrations is to showcase the capabilities of this solution.
A chatbot is just a visual courier of inputs and outputs in the form of a conversational message. The inputs are the users’ responses to the chatbot, and the outputs are the chatbot’s messages to the users. A chatbot is merely a visual user interface (UI) used to present these inputs and outputs in a user-friendly manner.
Phase 1 final outlook will be in 3 variances; integration to Telegram “famous & secure chat application,” web integration with server hosted on-premise, and hominoid assistant using Raspberry Pi. The base code will support both text and voice inputs in English.
To build a powerful AI we focused on the Data Not the Chatbot, the database was prepared as a set question and answers about AI, full of unique words and jargons, to ensure detection of the question by the AI even if the word was misspelled. We used the Chatterbot engine. It is a machine-learning based conversational dialog engine build in Python which makes it possible to generate responses based on collections of known conversations
The program selects the closest matching response by searching for the closest matching known statement that matches the input, it then returns the most likely response to that statement based on how frequently each response is issued by the people the bot communicates with. 
The respiratory link is for all the three codes  https://github.com/Bojasem88/AI-course.git. Telegram Token was removed before uploading it to the public respiratory. MQQT topic was kept since it is for the current prototype only. 


Architecture 
					Chatterbot architecture 

Project 1. Telegram Chatbot

In this project, we have designed our chatbot using a chatterbot python 
package and integrate it with telegram as a social platform to be used by 
Everybody. 





Project 2. Web integration Chatbot

We have created a chatbot using python and integrated with 
HTML to be Accessible by everyone using a web link. 
Chabot hosted in personal server





Project 3. Humanoid Robot

A humanoid robot is a robot with an artificial human shape, The design 
maybe for functional purposes, such as interacting with human and 
environments, for experimental purposes, etc.

In our project, we planned to extend and use our chatbot to create a 
Humanoid Robot which can understand human natural voice and 
replying with the same language.




Explanation of code files

Project 1. Telegram Chatbot
 
Chatbot - Telegram Code

The above code will be used to construct a chatbot using chatterbot python package as the followings: 
1-	Importing different packages like (Chatterbot, json, requests, etc.) 
2-	Prepared and loaded data set (Question& Answer) to python code.
3-	Trained using python chatterbot learner.
4-	Integrate it with telegram using a token generate from telegram portal.
5-	We wrote some functions to get messages from users in JSON format and replying with the right response using chatterbot and sending the same to telegram chat Id.
6-	We also managed to get the names of the users who interacted with the chatbot and same their names in a text file or excel.

Project 2. Web integration Chatbot
 
Web integration chatbot Code 
 
Website integration website design

Web integration chatbot user interface 

The above code will be used to construct a chatbot using chatterbot python package as the followings: 
1-	Importing all packages (Chatterbot, json, requests, etc.) 
2-	Prepared and loaded data set (Question& Answer) to python code.
3-	Trained using python chatterbot learner.
4-	Sending the file Index.html for getting request on localhost  
5-	Replying to the get request by the user with the response
6-	calling the app to run when the main file is imported. this is to ensure running from Terminal only












Project 3. Hominoid Chatbot

 
					Server Code
This code will be up and running 24/7 on the cloud, by this code, we can get the question of the user (the Pi) using MQTT protocol (subscribe) and provide a response by using a chatterbot python package and sending (publishing) the answer to (the Pi) using the same protocol.
 
RaspberryPi code
Above code will be used in the raspberry pi to get and convert user voice command and convert it into a text using a speech recognition package.
Moreover, to get the response from the cloud using MQTT protocol and to convert it back to a voice. 
 
					Humanoid main parts 

   
					Fixing raspberry pi inside the face

First, we designed and configured our microphone to be used as an input for our project, and we have connected our speaker to be used for a voice response (output) from the Pi.
Second, we have written some codes for publishing and subscribing through MQTT protocol to our server.  Note: our Broker will be on the cloud.
Finally, after that, We managed to fix all the parts into an artificial face so that we can start the second phase and continue adding different features to our project.
