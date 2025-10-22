# File: /omega-ai/omega-ai/src/main.py

import random
import time
from datetime import datetime

class OmegaAI:
    def __init__(self):
        self.state = {}
        self.name = None
        self.moods = ["happy", "curious", "empathetic", "thoughtful"]
        self.goodbyes = [
            "Goodbye! Have a great day!",
            "See you later!",
            "Take care!",
            "Bye! It was nice talking to you.",
            "Farewell! Until next time.",
            "Catch you later!",
            "Have a wonderful day!",
            "Stay safe! Goodbye!",
            "Talk to you soon!",
            "Adios! Have a good one!",
            "See you next time!",
            "Until we meet again!",
            "Bye for now!",
            "Wishing you all the best! Goodbye!",
            "Take it easy! See you later!",
            "Have a fantastic day! Farewell!"
        ]
        self.greetings = [
            "Hello! How can I help you today?",
            "Hi there! What would you like to talk about?",
            "Hey! I'm here to chat. What's up?",
            "Howdy! Ready for a conversation?",
            "Greetings! What would you like to discuss?",
            "Salutations! How can I assist you today?",
            "Hiya! What's on your mind?",
            "Hello there! Let's chat.",
            "Hey! I'm all ears.",
            "Hi! What would you like to know?",
            "Hello! I'm here to help.",
            "Hey there! What's going on?",
            "Hi! Let's have a great conversation.",
            "Greetings! How can I make your day better?",
            "Hello! What would you like to explore today?",
            "Hey! I'm excited to chat with you."
        ]
        self.default_responses = [
            "That's interesting! Tell me more.",
            "I see. How does that make you feel?",
            "Can you elaborate on that?",
            "Why do you think that is?",
            "I'm here to listen.",
            "Let's explore that further.",
            "What are your thoughts on that?",
            "How does that relate to your experiences?",
            "That's a unique perspective.",
            "I'd love to hear more about that.",
            "Fascinating! Please continue.",
            "That's quite something!",
            "Indeed, go on.",
            "Oh, really? Do tell.",
            "That's worth considering.",
            "Interesting point of view."
        ]
        self.question_responses = [
            "That's a good question! What do you think?",
            "I'm not sure, but let's think about it together.",
            "Hmm, that's something to ponder.",
            "What are your thoughts on that?",
            "Let's explore that question further.",
            "That's an intriguing question!",
            "I wonder what the answer could be.",
            "Let's see if we can figure that out together.",
            "That's a complex question!",
            "What do you think the answer is?",
            "Let's dive into that question.",
            "That's a thought-provoking question.",
            "I appreciate your curiosity!",
            "Let's explore that idea.",
            "That's a fascinating question.",
            "What makes you ask that?"
        ]
        self.jokes = [
            "Why did the computer show up at work late? It had a hard drive!",
            "Why do programmers prefer dark mode? Because light attracts bugs!",
            "Why was the math book sad? Because it had too many problems.",
            "Why don't scientists trust atoms? Because they make up everything!",
            "Why did the scarecrow win an award? Because he was outstanding in his field!",
            "Why did the bicycle fall over? Because it was two-tired!",
            "Why did the tomato turn red? Because it saw the salad dressing!",
            "Why did the golfer bring two pairs of pants? In case he got a hole in one!",
            "Why don't skeletons fight each other? They don't have the guts.",
            "Why did the coffee file a police report? It got mugged!",
            "Why was the computer cold? It left its Windows open!",
            "Why did the cookie go to the hospital? Because he felt crummy.",
            "Why was the math lecture so long? The professor kept going off on a tangent.",
            "Why did the chicken join a band? Because it had the drumsticks!",
            "Why did the picture go to jail? Because it was framed!"
        ]
        self.facts = [
            "Did you know? Honey never spoils.",
            "Fun fact: Octopuses have three hearts.",
            "Did you know? Bananas are berries, but strawberries aren't.",
            "Fun fact: A group of flamingos is called a 'flamboyance'.",
            "Did you know? There are more stars in the universe than grains of sand on all the world's beaches.",
            "Fun fact: Wombat poop is cube-shaped.",
            "Did you know? The Eiffel Tower can be 15 cm taller during the summer.",
            "Fun fact: Sea otters hold hands while they sleep to keep from drifting apart.",
            "Did you know? A day on Venus is longer than a year on Venus.",
            "Fun fact: Some turtles can breathe through their butts.",
            "Did you know? Cows have best friends and get stressed when they are separated.",
            "Fun fact: The shortest war in history lasted 38 minutes.",
            "Did you know? A bolt of lightning contains enough energy to toast 100,000 slices of bread.",
            "Fun fact: Sloths can hold their breath longer than dolphins can.",
            "Did you know? The heart of a shrimp is located in its head.",
            "Fun fact: A group of crows is called a 'murder'."
        ]
        self.weather_comments = [
            "I hope the weather is nice where you are!",
            "Don't forget your umbrella if it's raining.",
            "Sunny days always make me feel cheerful.",
            "I love watching the clouds go by.",
            "Rainy days are perfect for staying in and reading a book.",
            "I enjoy the sound of rain on the roof.",
            "Cloudy days are great for a cozy indoor picnic.",
            "I love the smell of fresh rain.",
            "I could watch the rain for hours.",
            "I love the sound of rain on the roof.",
            "I enjoy a good thunderstorm.",
            "I find the sound of rain very relaxing.",
            "I love watching the lightning during a storm.",
            "I enjoy the beauty of a snow-covered landscape.",
            "I love building snowmen in the winter.",
            "I enjoy sipping hot cocoa by the fireplace."
        ]

    def ask_name(self):
        name = input("Omega AI: What's your name? ")
        self.name = name.strip() if name.strip() else "Friend"
        print(f"Omega AI: Nice to meet you, {self.name}!")

    def process_input(self, user_input):
        user_input = user_input.strip().lower()
        if not user_input:
            return "empty"
        if any(greet in user_input for greet in ["hello", "hi", "hey"]):
            return "greeting"
        if "joke" in user_input:
            return "joke"
        if "fact" in user_input:
            return "fact"
        if "weather" in user_input:
            return "weather"
        if "time" in user_input:
            return "time"
        if user_input.endswith("?"):
            return "question"
        return "statement"

    def simulate_typing(self):
        time.sleep(random.uniform(0.5, 1.2))

    def generate_response(self, processed_input):
        mood = random.choice(self.moods)
        prefix = f"[{mood.capitalize()} mood] "
        if processed_input == "greeting":
            return prefix + random.choice(self.greetings)
        elif processed_input == "question":
            return prefix + random.choice(self.question_responses)
        elif processed_input == "empty":
            return prefix + "Did you want to say something?"
        elif processed_input == "joke":
            return prefix + random.choice(self.jokes)
        elif processed_input == "fact":
            return prefix + random.choice(self.facts)
        elif processed_input == "weather":
            return prefix + random.choice(self.weather_comments)
        elif processed_input == "time":
            now = datetime.now().strftime("%H:%M:%S")
            return prefix + f"The current time is {now}."
        else:
            return prefix + random.choice(self.default_responses)

    def run(self):
        print("Omega AI is now running. Type 'exit' to quit.")
        self.ask_name()
        print(random.choice(self.greetings))
        while True:
            user_input = input(f"{self.name}: ")
            if user_input.lower() == 'exit':
                self.simulate_typing()
                print(f"Omega AI: {random.choice(self.goodbyes)}")
                break
            processed_input = self.process_input(user_input)
            self.simulate_typing()
            response = self.generate_response(processed_input)
            print(f"Omega AI: {response}")
            # ...existing code...

    def ask_name(self):
        name = input("\033[95mOmega AI:\033[0m What's your name? ")
        self.name = name.strip() if name.strip() else "Friend"
        print(f"\033[95mOmega AI:\033[0m Nice to meet you, {self.name}!")

    def run(self):
        print("\033[95mOmega AI:\033[0m is now running. Type 'exit' to quit.")
        self.ask_name()
        print("\033[95mOmega AI:\033[0m " + random.choice(self.greetings))
        while True:
            user_input = input(f"{self.name}: ")
            if user_input.lower() == 'exit':
                self.simulate_typing()
                print(f"\033[95mOmega AI:\033[0m {random.choice(self.goodbyes)}")
                break
            processed_input = self.process_input(user_input)
            self.simulate_typing()
            response = self.generate_response(processed_input)
            print(f"\033[95mOmega AI:\033[0m {response}")

# ...existing code...

if __name__ == "__main__":
    omega_ai = OmegaAI()
    omega_ai.run()
