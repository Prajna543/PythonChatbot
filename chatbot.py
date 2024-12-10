import requests
from textblob import TextBlob
user_memory = {}
def sentiment_analysis(user_input):
    blob = TextBlob(user_input)
    sentiment = blob.sentiment.polarity
    if sentiment > 0:
        return "You seem happy!"
    elif sentiment < 0:
        return "You seem upset. How can I help?"
    else:
        return "You seem neutral."
def get_weather(city):
    api_key = "eca75c577415432fb58130804240112" 
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}q={city}&appid={api_key}"

    response = requests.get(complete_url)
    data = response.json()

    if data.get("cod") != "404" and data.get("main"):
        main = data["main"]
        weather_description = data["weather"][0]["description"]
        temperature = main["temp"] - 273.15 
        return f"The weather in {city} is {weather_description} with a temperature of {temperature:.2f}°C."
    else:
        return "Sorry, I couldn't fetch the weather data. Please check the city name or try again later."
def chatbot_response(user_input, user_name=""):
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I assist you today?"
    elif "how are you" in user_input:
        return "I'm doing great, thank you for asking!"
    elif "name" in user_input:
        if user_name:
            return f"My name is Chatbot. But I see your name is {user_name}!"
        else:
            return "My name is Chatbot. What's your name?"
    elif "weather" in user_input:
        city = input("Which city would you like the weather for? ")
        return get_weather(city)
    elif "joke" in user_input:
        return "Why don't scientists trust atoms? Because they make up everything!"
    elif "bye" in user_input:
        return "Goodbye! Have a great day!"
    elif "Thank you" in user_input:
        return "You are most welcome"
    else:
        sentiment_response = sentiment_analysis(user_input)
        return f"I'm sorry, I didn't understand that. {sentiment_response}"
def start_chat():
    print("Chatbot: Hello! Type 'bye' to exit.")
    user_name = ""
    
    while True:
        user_input = input("You: ")
    
        if user_input.lower() == "bye":
            print("Chatbot: Goodbye!")
            break
        
        response = chatbot_response(user_input, user_name)
        print(f"Chatbot: {response}")
        
        if "What's your name?" in response:
            user_name = input("You: ")

start_chat()
