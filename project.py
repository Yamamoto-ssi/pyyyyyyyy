import random
import time
import sys
import pygame

pygame.mixer.init()

def printer(text, speed=0.03, volume=0.3):
    type_sound = pygame.mixer.Sound(r"E:\Downloads\sans voice.mp3")
    type_sound.set_volume(volume)
    channel = type_sound.play(loops=-1)
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    channel.fadeout(200)
    print()
def clear():
    print("\n" * 100)

seal =  5
hp = 100
exp = 0

enemies = ["Anaxagoras", "Veritas Ratio", "Albus Dumbledore", "Severus Snape", "Minerva McGonagall", "Walter White", "Gordon Ramsey", "Zoro Roronoa", "Master Oogway", "Gandalf", "Socrates", "Aristotle", "Confucius"]

intro_dialogues = {
    "Anaxagoras": [
        "Behold, a student of the cosmos! Let us see if you understand the nature of things.",
        "The mind is a spark from the heavens — let us test if yours still burns.",
        "I bring forth the light of reason. Answer wisely."
    ],
    "Veritas Ratio": [
        "Truth stands eternal. Let us see if you stand with it.",
        "Calculating intellect detected. Initializing examination of logic.",
        "You seek truth — let us test the strength of your reason."
    ],
    "Albus Dumbledore": [
        "Ah, another curious mind. Let’s see what wisdom you possess.",
        "Knowledge, my dear student, is the purest form of magic.",
        "Ah, back again? Let’s make this lesson a memorable one."
    ],
    "Severus Snape": [
        "Another one who dares waste my time. Very well, answer this.",
        "Let us see if your intellect matches your arrogance.",
        "Try not to embarrass yourself this time."
    ],
    "Minerva McGonagall": [
        "Pay attention now, this will be on your next exam.",
        "I expect nothing but your best — no excuses.",
        "Focus, student. The art of learning demands discipline."
    ],
    "Walter White": [
        "We’re not in class. We’re in the lab. And in my lab, you *get it right*.",
        "Let’s see if you can follow the formula — or blow it up instead.",
        "Say my name… then answer the question."
    ],
    "Gordon Ramsey": [
        "Right, let’s test your brain, not your cooking for once.",
        "If this answer’s raw, I swear—",
        "Show me something intelligent for a change, yeah?"
    ],
    "Zoro Roronoa": [
        "Huh? A question? Fine. I’ll slice through it first, think later.",
        "Let’s settle this with skill — and a little luck.",
        "Don’t get lost now. Focus and answer straight."
    ],
    "Master Oogway": [
        "The mind grows only when challenged. Let us begin.",
        "Ah, a student arrives seeking wisdom. How delightful.",
        "There are no coincidences — you are here to learn."
    ],
    "Gandalf": [
        "A test of wisdom, then? So be it.",
        "Even the smallest student can answer the greatest questions.",
        "You stand before Gandalf the Grey. Speak wisely."
    ],
    "Socrates": [
        "Come, let us reason together. What do you truly know?",
        "I ask not to prove you wrong, but to discover the truth.",
        "Tell me, student — do you *know* or merely *believe*?"
    ],
    "Aristotle": [
        "Let us engage in a bit of logical discourse, shall we?",
        "Through reason and method, truth will emerge.",
        "Every answer begins with observation. Let us begin."
    ],
    "Confucius": [
        "Learning without reflection is a waste — reflect well on this question.",
        "Let us test your virtue through understanding.",
        "He who learns but does not think is lost. Think carefully."
    ]
}
wrong_dialogues = {
    "Anaxagoras": [
        "Foolish mortal! You clearly have not grasped the essence of reason!",
        "Incorrect! Your logic collapses like a dying star.",
        "The universe weeps at your misunderstanding of truth."
    ],
    "Veritas Ratio": [
        "Logic abandoned you in that answer. Seek truth, not assumption.",
        "Zero points! Your reasoning was flawed. Recalibrate your intellect.",
        "Fail! Get out! The equation of truth rejects your input."
    ],
    "Albus Dumbledore": [
        "Ah, even the wisest among us make mistakes… but do try again, dear one.",
        "Incorrect, my friend. Curiosity is good — but accuracy, better.",
        "Not quite right. Let’s hope you’re better at Potions."
    ],
    "Severus Snape": [
        "Pathetic. I expected incompetence — but not this much.",
        "Tsk. Wrong again. Perhaps you should try actually studying.",
        "How utterly disappointing. Were you even paying attention?"
    ],
    "Minerva McGonagall": [
        "Incorrect. Honestly, did you even read the question properly?",
        "No, no, no! You’re better than that — I hope.",
        "Wrong. Detention-worthy performance, I must say."
    ],
    "Walter White": [
        "You’re wrong. Say it. Say you’re wrong!",
        "Incorrect! You clearly don’t understand the chemistry of logic.",
        "Wrong answer. You’re not in control — I am."
    ],
    "Gordon Ramsey": [
        "WRONG! You Doughnut! That answer’s so raw it’s still thinking!",
        "Bloody hell! Did you even taste that response before serving it?",
        "No! Wrong! That’s an overcooked disaster of an answer!"
    ],
    "Zoro Roronoa": [
        "Tch… wrong again. You’ll never find your way to the right answer like that.",
        "Missed it. Guess I’m not the only one with a bad sense of direction.",
        "Wrong. Keep training — or you’ll fall behind."
    ],
    "Master Oogway": [
        "There are no mistakes… only lessons. But that was definitely wrong.",
        "Ah, the turtle shell cracks. Reflect and try again.",
        "Even wisdom trips sometimes — but you fell quite hard."
    ],
    "Gandalf": [
        "Incorrect! A fool of a student! You shall not pass — this question.",
        "Wrong! Not all who wander are correct, it seems.",
        "No, no. That is not the way of wisdom, young one."
    ],
    "Socrates": [
        "So… you believe that was correct? Interesting. Let us examine your ignorance.",
        "Wrong, yet educational. For ignorance admitted is wisdom gained.",
        "Incorrect — but the pursuit of truth continues nonetheless."
    ],
    "Aristotle": [
        "Your reasoning lacks structure. Reconsider your premises next time.",
        "Wrong. You have failed to balance form with logic.",
        "Incorrect — your conclusion does not follow from your argument."
    ],
    "Confucius": [
        "The man who makes a mistake and does not correct it makes a greater one.",
        "Wrong. Even the wise must sometimes bow to correction.",
        "You missed the mark. Reflection is the path to improvement."
    ]
}
correct_dialogues = {
    "Anaxagoras": [
        "At last, reason shines through! The cosmos approves your intellect.",
        "Correct. You grasp the eternal harmony of logic.",
        "Well reasoned! Even the stars nod in approval."
    ],
    "Veritas Ratio": [
        "Truth aligns with you. Logic prevails.",
        "Excellent. You’ve upheld the law of reason.",
        "Your precision honors the name of truth itself."
    ],
    "Albus Dumbledore": [
        "Excellent! Perhaps you’ll make the House proud after all.",
        "Splendid work. Wit beyond measure is man’s greatest treasure.",
        "Well done. You remind me of a young wizard I once knew."
    ],
    "Severus Snape": [
        "Hmph. Even a broken cauldron brews right once in a while.",
        "Correct. Don’t let it go to your head.",
        "A competent answer — surprisingly."
    ],
    "Minerva McGonagall": [
        "Well done. Ten points to… whichever house you’re from.",
        "Correct. I do appreciate a student who pays attention.",
        "Excellent. You’ve proven you can think under pressure."
    ],
    "Walter White": [
        "That’s right. You’re finally starting to think.",
        "Correct! That’s the kind of precision I demand.",
        "You got it. You’re in the empire business now."
    ],
    "Gordon Ramsey": [
        "Finally! That’s cooked to perfection — about time!",
        "Correct! That’s a five-star answer right there!",
        "Beautiful! That’s what I’m talking about — now we’re cooking!"
    ],
    "Zoro Roronoa": [
        "Hah! You got it right this time. Don’t lose focus now.",
        "Not bad! Guess your sense of direction isn’t the only thing improving.",
        "Correct. You’re cutting through these questions like a blade."
    ],
    "Master Oogway": [
        "Ah… your mind blossoms like a lotus in spring. Very good.",
        "Correct. The path of wisdom opens before you.",
        "Excellent. You have found balance between mind and heart."
    ],
    "Gandalf": [
        "Well done! You have the wisdom to pass… for now.",
        "Correct! You’ve proven your worth, young scholar.",
        "Yes… even the smallest student can change the course of fate."
    ],
    "Socrates": [
        "You have reasoned well. Perhaps there’s hope for your mind yet.",
        "Correct. Wisdom is found through questioning, as you’ve done.",
        "Well thought out — the dialectic would be proud."
    ],
    "Aristotle": [
        "A sound conclusion drawn from solid reasoning — commendable.",
        "Excellent. Your logic aligns with the principles of thought.",
        "A fine demonstration of intellect and discipline."
    ],
    "Confucius": [
        "The path of wisdom begins with one right answer. You walk it well.",
        "Correct. You’ve shown virtue in understanding.",
        "Good. Learning without reflection is labor lost — but you have both."
    ]
}

def dialogue(lines):
    print(random.choice(lines))
    time.sleep(1)

def correct():
    global hp, seal
    print(f"\n\033[1m\033[92mThat is correct! You deflected the Catastrophe's question!\033[0m\033[0m")
    printer(f"\033[1m\033[91mCatastrophe of Questions:\033[0m \033[91m\"{random.choice(right_lines)}\"\033[0m\n")
    time.sleep(1.5)
    print(f"\033[1m\033[92m         Current HP: {hp}\033[0m\033[0m")
    print(f"\033[1m\033[93m         Current EXP: {exp}\033[0m\033[0m")
    print(f"\033[1m\033[91m         Remaining Seals: {seal}\033[0m\033[0m\n")

def wrong():
    global hp, seal
    print(f"\n\033[1m\033[91mThat is incorrect! The catastrophe grows stronger.\033[0m\033[0m")
    printer(f"\033[1m\033[91mCatastrophe of Questions:\033[0m \033[91m\"{random.choice(wrong_lines)}\"\033[0m\n")
    time.sleep(1.5)
    print("\033[1m\033[91m   A single chain loosens hold from the Catastrophe\033[0m\033[0m")
    seal -= 1
    time.sleep(1.5)
    if seal > 0:
        print(f"\n\033[1m\033[92m         Current HP: {hp}\033[0m\033[1m")
        print(f"\033[1m\033[93m         Current EXP: {exp}\033[0m\033[0m")
        print(f"\033[1m\033[91m         Remaining Seals: {seal}\033[0m\033[0m\n")
    else:
        hp -= 1000
        clear()
        print("""\033[91m
▓█████  ██▀███   ██▀███   ▒█████   ██▀███  
▓█   ▀ ▓██ ▒ ██▒▓██ ▒ ██▒▒██▒  ██▒▓██ ▒ ██▒
▒███   ▓██ ░▄█ ▒▓██ ░▄█ ▒▒██░  ██▒▓██ ░▄█ ▒
▒▓█  ▄ ▒██▀▀█▄  ▒██▀▀█▄  ▒██   ██░▒██▀▀█▄  
░▒████▒░██▓ ▒██▒░██▓ ▒██▒░ ████▓▒░░██▓ ▒██▒
░░ ▒░ ░░ ▒▓ ░▒▓░░ ▒▓ ░▒▓░░ ▒░▒░▒░ ░ ▒▓ ░▒▓░
 ░ ░  ░  ░▒ ░ ▒░  ░▒ ░ ▒░  ░ ▒ ▒░   ░▒ ░ ▒░
   ░     ░░   ░   ░░   ░ ░ ░ ░ ▒    ░░   ░ 
   ░  ░   ░        ░         ░ ░     ░\033[0m""", end="")
        time.sleep(1)
        print("""\033[91m
  ██████ ▓█████ ▄▄▄       ██▓      ██████ 
▒██    ▒ ▓█   ▀▒████▄    ▓██▒    ▒██    ▒ 
░ ▓██▄   ▒███  ▒██  ▀█▄  ▒██░    ░ ▓██▄   
  ▒   ██▒▒▓█  ▄░██▄▄▄▄██ ▒██░      ▒   ██▒
▒██████▒▒░▒████▒▓█   ▓██▒░██████▒▒██████▒▒
▒ ▒▓▒ ▒ ░░░ ▒░ ░▒▒   ▓▒█░░ ▒░▓  ░▒ ▒▓▒ ▒ ░
░ ░▒  ░ ░ ░ ░  ░ ▒   ▒▒ ░░ ░ ▒  ░░ ░▒  ░ ░
░  ░  ░     ░    ░   ▒     ░ ░   ░  ░  ░  
      ░     ░  ░     ░  ░    ░  ░      ░\033[0m""", end="")
        time.sleep(1.5)
        print("""\033[91m
███▄    █  ▒█████  ▄▄▄█████▓
 ██ ▀█   █ ▒██▒  ██▒▓  ██▒ ▓▒
▓██  ▀█ ██▒▒██░  ██▒▒ ▓██░ ▒░
▓██▒  ▐▌██▒▒██   ██░░ ▓██▓ ░ 
▒██░   ▓██░░ ████▓▒░  ▒██▒ ░ 
░ ▒░   ▒ ▒ ░ ▒░▒░▒░   ▒ ░░   
░ ░░   ░ ▒░  ░ ▒ ▒░     ░    
   ░   ░ ░ ░ ░ ░ ▒    ░      
         ░     ░ ░\033[0m""", end="")
        time.sleep(2)
        print("""\033[91m
 █████▒▒█████   █    ██  ███▄    █ ▓█████▄               
▓██   ▒▒██▒  ██▒ ██  ▓██▒ ██ ▀█   █ ▒██▀ ██▌              
▒████ ░▒██░  ██▒▓██  ▒██░▓██  ▀█ ██▒░██   █▌              
░▓█▒  ░▒██   ██░▓▓█  ░██░▓██▒  ▐▌██▒░▓█▄   ▌              
░▒█░   ░ ████▓▒░▒▒█████▓ ▒██░   ▓██░░▒████▓  ██▓  ██▓  ██▓
 ▒ ░   ░ ▒░▒░▒░ ░▒▓▒ ▒ ▒ ░ ▒░   ▒ ▒  ▒▒▓  ▒  ▒▓▒  ▒▓▒  ▒▓▒
 ░       ░ ▒ ▒░ ░░▒░ ░ ░ ░ ░░   ░ ▒░ ░ ▒  ▒  ░▒   ░▒   ░▒ 
 ░ ░   ░ ░ ░ ▒   ░░░ ░ ░    ░   ░ ░  ░ ░  ░  ░    ░    ░  
           ░ ░     ░              ░    ░      ░    ░    ░ 
                                     ░        ░    ░    ░\033[0m\n""")
        time.sleep(1)
        printer(f"\033[1m\033[91mCatastrophe of Questions:\033[0m \033[91m\"{random.choice(awakening_lines)}\"\033[0m\n")
        time.sleep(1)
        printer(f"\033[1m\033[91m   The Catastrophe pointed a finger towards you...\033[0m")
        time.sleep(1)
        printer(f"\033[1m\033[91m   A beam of polarized light surges forth at impossible speed.\033[0m")
        time.sleep(1)
        printer("\033[1m\033[91m   The air itself distorts from the heat...\033[0m")
        time.sleep(1)
        printer("\033[1m\033[91m   Your vision fades as everything turns white—\033[0m")
        time.sleep(1)
        printer("\033[1m\033[91m   You are reduced to nothing but ash and silence.\033[0m\n")
        time.sleep(.5)
        print(f"\n\033[1m\033[92m          Current HP: {hp}\033[0m\033[0m")
        print(f"\033[1m\033[93m          Current EXP: {exp}\033[0m\033[0m\n")
        print(f"\033[1m\033[91m          Remaining Seals: {seal}\033[0m\033[0m\n")

spawn_lines = [
    "Futile… all your learning ends here.",
    "Knowledge itself bends to my will!",
    "Let us see if you can survive... HAHAHA!",
    "HEH! Answer wisely, mortal. Every mistake weakens your grip on reality…",
    "SO... YOU'RE THE ONE WHO THINKS THEY CAN ANSWER EVERYTHING?"
]
wrong_lines = [
    "HAHAHA! Another seal shatters!",
    "Can you feel it? My strength returns!",
    "You call that knowledge? PATHETIC!",
    "Ignorance feeds me! Keep failing!"
]
right_lines = [
    "WHAT!? You deflected my question!?",
    "Hmph… delaying the inevitable.",
    "Your answers won’t save you forever!",
    "A flicker of hope in the dark—how quaint."
]
awakening_lines = [
    "THE SEALS ARE BROKEN!",
    "NOW IT’S OVER!",
    "*The screen trembles violently as the Catastrophe unleashes its power!*"
]

printer("\033[90mNow Loading...\033[0m ")
time.sleep(1.5)#1.5
printer("\033[90mPlease wait...\033[0m\n")
time.sleep(2)#2

print('''\033[92m════════════════════════════════════════════════════════════════════════════════
 ███████████  █████ █████ ███████████ █████   █████    ███████    ██████   █████
░░███░░░░░███░░███ ░░███ ░█░░░███░░░█░░███   ░░███   ███░░░░░███ ░░██████ ░░███ 
 ░███    ░███ ░░███ ███  ░   ░███  ░  ░███    ░███  ███     ░░███ ░███░███ ░███ 
 ░██████████   ░░█████       ░███     ░███████████ ░███      ░███ ░███░░███░███ 
 ░███░░░░░░     ░░███        ░███     ░███░░░░░███ ░███      ░███ ░███ ░░██████ 
 ░███            ░███        ░███     ░███    ░███ ░░███     ███  ░███  ░░█████ 
 █████           █████       █████    █████   █████ ░░░███████░   █████  ░░█████
░░░░░           ░░░░░       ░░░░░    ░░░░░   ░░░░░    ░░░░░░░    ░░░░░    ░░░░░\033[0m''')

while hp > 0:
    print('\033[92m════════════════════════════════════════════════════════════════════════════════\033[0m')
    time.sleep(1)
    print('''
    \033[1m\033[92mPrelim Lessons\033[0m\033[0m
       1. Introduction                 \033[1m\033[91m(HP)\033[0m\033[0m
       2. What is Programming?         \033[1m\033[91m(HP)\033[0m\033[0m
       3. Python Print Syntax          \033[1m\033[91m(HP)\033[0m\033[0m
       4. Python Comments              \033[1m\033[91m(HP)\033[0m\033[0m
       5. Variables and Data Types     \033[1m\033[91m(HP)\033[0m\033[0m
       6. Arithmetic Operation         \033[1m\033[91m(HP)\033[0m\033[0m''')
    time.sleep(.5)

    print('''
    \033[1m\033[94mMidterms Lessons\033[0m\033[0m
       7. Input Functions             \033[1m\033[91m(HP)\033[0m\033[0m
       8. f-String                    \033[1m\033[91m(HP)\033[0m\033[0m
       9. Conditional Statements      \033[1m\033[91m(HP)\033[0m\033[0m''')
    time.sleep(.5)

    print('''
    \033[1m\033[91mFinals Lessons\033[0m\033[0m
       10. Looping                    \033[1m\033[91m(HP)\033[0m\033[0m''')
    time.sleep(.5)

    print('''
    \033[1m\033[93mFunctions\033[0m\033[0m
       11. Test Your Knowledge        \033[1m\033[93m(EXP)\033[0m\033[0m
       12. Exit''')
    time.sleep(.5)

    print('\n\033[92m════════════════════════════════════════════════════════════════════════════════\033[0m')

    choice = input('\n\033[1m\033[92mEnter your choice: \033[0m\033[0m')

    if choice == "1":
        print("""\033[92m
█████             █████                           █████                      █████     ███                     
░░███             ░░███                           ░░███                      ░░███     ░░░                      
 ░███  ████████   ███████   ████████   ██████   ███████  █████ ████  ██████  ███████   ████   ██████  ████████  
 ░███ ░░███░░███ ░░░███░   ░░███░░███ ███░░███ ███░░███ ░░███ ░███  ███░░███░░░███░   ░░███  ███░░███░░███░░███ 
 ░███  ░███ ░███   ░███     ░███ ░░░ ░███ ░███░███ ░███  ░███ ░███ ░███ ░░░   ░███     ░███ ░███ ░███ ░███ ░███ 
 ░███  ░███ ░███   ░███ ███ ░███     ░███ ░███░███ ░███  ░███ ░███ ░███  ███  ░███ ███ ░███ ░███ ░███ ░███ ░███ 
 █████ ████ █████  ░░█████  █████    ░░██████ ░░████████ ░░████████░░██████   ░░█████  █████░░██████  ████ █████
░░░░░ ░░░░ ░░░░░    ░░░░░  ░░░░░      ░░░░░░   ░░░░░░░░   ░░░░░░░░  ░░░░░░     ░░░░░  ░░░░░  ░░░░░░  ░░░░ ░░░░░\033[0m\n"""
              "\nThis course introduces students to the fundamental concepts and principles of computer programming using Python as the primary language. \n"
              "Python has become one of the most popular languages in the world. Python uses clear, human-friendly syntax that allows beginners to focus on \n"
              "learning programming concepts rather than complex rules. It was designed with a focus on simplicity, readability, and productivity, allowing \n"
              "programmers to express their ideas in fewer lines of code compared to other languages like C++ or Java. The name “Python” actually comes from \n"
              "the British comedy group Monty Python, not the snake — showing that the language was meant to be fun and approachable.\n")
        proceed = input('\033[90m(Click Enter to Proceed)\033[0m \n')
        clear()
        time.sleep(1)
        print("""\033[91m 
 ██████████     █████████   ██████   █████   █████████  ██████████ ███████████   ███
░░███░░░░███   ███░░░░░███ ░░██████ ░░███   ███░░░░░███░░███░░░░░█░░███░░░░░███ ░███
 ░███   ░░███ ░███    ░███  ░███░███ ░███  ███     ░░░  ░███  █ ░  ░███    ░███ ░███
 ░███    ░███ ░███████████  ░███░░███░███ ░███          ░██████    ░██████████  ░███
 ░███    ░███ ░███░░░░░███  ░███ ░░██████ ░███    █████ ░███░░█    ░███░░░░░███ ░███
 ░███    ███  ░███    ░███  ░███  ░░█████ ░░███  ░░███  ░███ ░   █ ░███    ░███ ░░░ 
 ██████████   █████   █████ █████  ░░█████ ░░█████████  ██████████ █████   █████ ███
░░░░░░░░░░   ░░░░░   ░░░░░ ░░░░░    ░░░░░   ░░░░░░░░░  ░░░░░░░░░░ ░░░░░   ░░░░░ ░░░\033[0m\n""")
        time.sleep(1)
        enemy = random.choice(enemies)
        printer(f"\033[1m\033[91mA WILD {enemy.upper()} APPEARED!\033[0m\033[0m")
        time.sleep(1)
        printer(f"\033[1m\033[95m   {enemy}:\033[0m \033[91m\"{random.choice(intro_dialogues[enemy])}\"\033[0m ")
        time.sleep(1)
        printer(f"\033[91m\033[1m{enemy} asks you a question...\033[0m\033[0m")
        time.sleep(2)
        ans = input("\n\033[1m\033[97mWhat makes Python great for beginners?\033[0m\033[0m\n"
                    "\n   A. It runs only on specific operating systems, reducing complexity.\n"
                    "   B. It has a simple and readable syntax that’s close to everyday English.\n"
                    "   C. It requires manual memory management, which improves programming discipline.\n"
                    "   D. It forces programmers to write in complex low-level code\n"
                    "\n> ")
        if ans.lower() == "b":
            print(f"\n\033[1m\033[92mThat is correct! {enemy} nods approvingly.\033[0m\033[0m")
            printer(f"\033[1m\033[95m   {enemy}:\033[0m\033[0m \033[92m\"{random.choice(correct_dialogues[enemy])}\"\033[0m\n")
            time.sleep(1.5)
            print(f"\033[1m\033[92m   Current HP: {hp}\033[0m\033[0m")
            print(f"\033[1m\033[93m   Current EXP: {exp}\033[0m\033[0m\n")
            proceed = input('\033[90m(Click Enter to Proceed)\033[0m\n')
            clear()
        else:
            hp -= 20
            print(f"\n\033[1m\033[91mThat is incorrect! {enemy} throws a chalk on you.\033[0m\033[0m")
            printer(f"\033[1m\033[95m   {enemy}:\033[0m\033[0m \033[91m\"{random.choice(wrong_dialogues[enemy])}\"\033[0m\n")
            time.sleep(1.5)
            print("\033[1m\033[91m   -20HP\033[0m\033[0m")
            time.sleep(1.5)
            if hp > 0:
                print(f"\n\033[1m\033[92m   Current HP: {hp}\033[0m\033[1m")
                print(f"\033[1m\033[93m   Current EXP: {exp}\033[0m\033[0m\n")
                proceed = input('\033[90m(Click Enter to Proceed)\033[0m \n')
                clear()
            else:
                print(f"\n\033[1m\033[92m   Current HP: {hp}\033[0m\033[0m")
                print(f"\033[1m\033[93m   Current EXP: {exp}\033[0m\033[0m\n")
                time.sleep(1.5)
                break
        ans2 = input("\n\033[1m\033[97mThe name Python comes from?\033[0m\033[0m\n"
                     "\n   A. An actual Python non-venomous constrictor snakes\n"
                     "   B. The ancient Greek oracle of Delphi, also known as Pythia\n"
                     "   C. A mythical serpent called Python that slain by the god Apollo\n"
                     "   D. A famous British comedy group called Monty Python\n"
                     "\n> ")
        if ans2.lower() == "d":
            print(f"\n\033[1m\033[92mThat is correct! {enemy} nods approvingly.\033[0m\033[0m")
            printer(f"\033[1m\033[95m   {enemy}:\033[0m\033[0m \033[92m\"{random.choice(correct_dialogues[enemy])}\"\033[0m\n")
            time.sleep(1.5)
            print(f"\033[1m\033[92m   Current HP: {hp}\033[0m\033[0m")
            print(f"\033[1m\033[93m   Current EXP: {exp}\033[0m\033[0m\n")
            proceed = input('\033[90m(Click Enter to Proceed)\033[0m\n')
            clear()
        else:
            hp -= 20
            print(f"\n\033[1m\033[91mThat is incorrect! {enemy} throws a chalk on you.\033[0m\033[0m")
            printer(f"\033[1m\033[95m   {enemy}:\033[0m\033[0m \033[91m\"{random.choice(wrong_dialogues[enemy])}\"\033[0m\n")
            time.sleep(1.5)
            print("\033[1m\033[91m   -20HP\033[0m\033[0m")
            time.sleep(1.5)
            if hp > 0:
                print(f"\n\033[1m\033[92m   Current HP: {hp}\033[0m\033[1m")
                print(f"\033[1m\033[93m   Current EXP: {exp}\033[0m\033[0m\n")
                proceed = input('\033[90m(Click Enter to Proceed)\033[0m \n')
                clear()
            else:
                print(f"\n\033[1m\033[92m   Current HP: {hp}\033[0m\033[0m")
                print(f"\033[1m\033[93m   Current EXP: {exp}\033[0m\033[0m\n")
                time.sleep(2)
                break
        ans3 = input("\n\033[1m\033[97mOne of Python’s strengths is allowing programmers to express ideas using fewer lines of code than other languages.\033[0m\033[0m\n"
                     "\n   A. True\n"
                     "   B. False\n"
                     "   C. Maybe\n"
                     "   D. A and B\n"
                     "\n> ")
        if ans3.lower() == "a":
            print(f"\n\033[1m\033[92mThat is correct! {enemy} nods approvingly.\033[0m\033[0m")
            printer(f"\033[1m\033[95m   {enemy}:\033[0m\033[0m \033[92m\"{random.choice(correct_dialogues[enemy])}\"\033[0m\n")
            time.sleep(1.5)
            print(f"\033[1m\033[92m   Current HP: {hp}\033[0m\033[0m")
            print(f"\033[1m\033[93m   Current EXP: {exp}\033[0m\033[0m\n")
            proceed = input('\033[90m(Click Enter to Proceed)\033[0m\n')
            clear()
        else:
            hp -= 20
            print(f"\n\033[1m\033[91mThat is incorrect! {enemy} throws a chalk on you.\033[0m\033[0m")
            printer(f"\033[1m\033[95m   {enemy}:\033[0m\033[0m \033[91m\"{random.choice(wrong_dialogues[enemy])}\"\033[0m\n")
            time.sleep(1.5)
            print("\033[1m\033[91m   -20HP\033[0m\033[0m")
            time.sleep(1.5)
            if hp > 0:
                print(f"\n\033[1m\033[92m   Current HP: {hp}\033[0m\033[1m")
                print(f"\033[1m\033[93m   Current EXP: {exp}\033[0m\033[0m\n")
                proceed = input('\033[90m(Click Enter to Proceed)\033[0m \n')
                clear()
            else:
                print(f"\n\033[1m\033[92m   Current HP: {hp}\033[0m\033[0m")
                print(f"\033[1m\033[93m   Current EXP: {exp}\033[0m\033[0m\n")
                time.sleep(2)
                break
        ans4 = input("\n\033[1m\033[97mThe creator of Python wanted the language to be fun and approachable.\033[0m\033[0m\n"
            "\n   A. True\n"
            "   B. False\n"
            "   C. Maybe\n"
            "   D. A and B\n"
            "\n> ")
        if ans4.lower() == "a":
            print(f"\n\033[1m\033[92mThat is correct! {enemy} nods approvingly.\033[0m\033[0m")
            printer(
                f"\033[1m\033[95m   {enemy}:\033[0m\033[0m \033[92m\"{random.choice(correct_dialogues[enemy])}\"\033[0m\n")
            time.sleep(1.5)
            print(f"\033[1m\033[92m   Current HP: {hp}\033[0m\033[0m")
            print(f"\033[1m\033[93m   Current EXP: {exp}\033[0m\033[0m\n")
            proceed = input('\033[90m(Click Enter to Proceed)\033[0m\n')
            clear()
        else:
            hp -= 20
            print(f"\n\033[1m\033[91mThat is incorrect! {enemy} throws a chalk on you.\033[0m\033[0m")
            printer(
                f"\033[1m\033[95m   {enemy}:\033[0m\033[0m \033[91m\"{random.choice(wrong_dialogues[enemy])}\"\033[0m\n")
            time.sleep(1.5)
            print("\033[1m\033[91m   -20HP\033[0m\033[0m")
            time.sleep(1.5)
            if hp > 0:
                print(f"\n\033[1m\033[92m   Current HP: {hp}\033[0m\033[1m")
                print(f"\033[1m\033[93m   Current EXP: {exp}\033[0m\033[0m\n")
                proceed = input('\033[90m(Click Enter to Proceed)\033[0m \n')
                clear()
            else:
                print(f"\n\033[1m\033[92m   Current HP: {hp}\033[0m\033[0m")
                print(f"\033[1m\033[93m   Current EXP: {exp}\033[0m\033[0m\n")
                time.sleep(2)
                break

    elif choice == "2":
        print("""\033[92m
█████   ███   █████ █████                 █████        ███             ███████████                                                                                   ███                         ███████ 
░░███   ░███  ░░███ ░░███                 ░░███        ░░░             ░░███░░░░░███                                                                                 ░░░                        ███░░░███
 ░███   ░███   ░███  ░███████    ██████   ███████      ████   ██████    ░███    ░███ ████████   ██████   ███████ ████████   ██████   █████████████   █████████████   ████  ████████    ███████ ░░░   ░███
 ░███   ░███   ░███  ░███░░███  ░░░░░███ ░░░███░      ░░███  ███░░      ░██████████ ░░███░░███ ███░░███ ███░░███░░███░░███ ░░░░░███ ░░███░░███░░███ ░░███░░███░░███ ░░███ ░░███░░███  ███░░███   ███████ 
 ░░███  █████  ███   ░███ ░███   ███████   ░███        ░███ ░░█████     ░███░░░░░░   ░███ ░░░ ░███ ░███░███ ░███ ░███ ░░░   ███████  ░███ ░███ ░███  ░███ ░███ ░███  ░███  ░███ ░███ ░███ ░███  ░███░░░  
  ░░░█████░█████░    ░███ ░███  ███░░███   ░███ ███    ░███  ░░░░███    ░███         ░███     ░███ ░███░███ ░███ ░███      ███░░███  ░███ ░███ ░███  ░███ ░███ ░███  ░███  ░███ ░███ ░███ ░███  ░░░      
    ░░███ ░░███      ████ █████░░████████  ░░█████     █████ ██████     █████        █████    ░░██████ ░░███████ █████    ░░████████ █████░███ █████ █████░███ █████ █████ ████ █████░░███████   ███     
     ░░░   ░░░      ░░░░ ░░░░░  ░░░░░░░░    ░░░░░     ░░░░░ ░░░░░░     ░░░░░        ░░░░░      ░░░░░░   ░░░░░███░░░░░      ░░░░░░░░ ░░░░░ ░░░ ░░░░░ ░░░░░ ░░░ ░░░░░ ░░░░░ ░░░░ ░░░░░  ░░░░░███  ░░░      
                                                                                                        ███ ░███                                                                      ███ ░███          
                                                                                                       ░░██████                                                                      ░░██████           
                                                                                                        ░░░░░░                                                                        ░░░░░░\033[0m\n"""
              "\nA programming language is a special language that computers understand and use to perform tasks. It’s a way for humans to give instructions\n"
              "to a computer in a form that the computer can follow. At its core, programming is about problem-solving. A programmer analyzes a problem, plans \n"
              "a solution, and then writes code to make the computer carry out that solution. This involves using concepts such as variables (to store data), \n"
              "loops (to repeat actions), conditions (to make decisions), and functions (to organize code). Programming languages serve as the bridge between \n"
              "human logic and computer execution. Each language has its own rules (called syntax) and unique features, but they all share the same goal — to \n"
              "turn human ideas into working software. Learning to program helps people develop logical thinking, creativity, and precision. It’s a valuable \n"
              "skill in today’s digital world, used in fields such as web development, data science, robotics, cybersecurity, and mobile app development. \n"
              "Whether you’re automating simple tasks or building large systems, programming is the foundation that makes modern technology possible.")
        time.sleep(1)
        print("""\n \033[97mCommon Programming Languages Include:\033[0m
- Python
- Java
- C / C++
- JavaScript
- PHP
- Ruby\n""")
        proceed = input('\033[90m(Click Enter to Proceed)\033[0m \n')
        print("\nPython is a high-level, easy-to-learn programming language known for its simplicity and readability which can be good for beginners. Python is a \n"
              "widely-used programming language that was created by \033[1m\033[97mGuido van Rossum\033[0m\033[0m in \033[1m\033[97m1991.\033[0m\033[0m Python is a versatile language — it’s used for web development, \n"
              "data analysis, artificial intelligence, software Development, automation, mathematics and more. One of Python’s biggest strengths is its clean and \n"
              "easy-to-understand syntax. The code often looks close to regular English, making it an ideal choice for beginners who are learning to program for the \n"
              "first time. At the same time, Python is powerful enough for professional developers to build large and complex applications.\n")
        proceed1 = input('\033[90m(Click Enter to Proceed)\033[0m \n')
        clear()
        time.sleep(1)
        print("""\033[91m 
 ██████████     █████████   ██████   █████   █████████  ██████████ ███████████   ███
░░███░░░░███   ███░░░░░███ ░░██████ ░░███   ███░░░░░███░░███░░░░░█░░███░░░░░███ ░███
 ░███   ░░███ ░███    ░███  ░███░███ ░███  ███     ░░░  ░███  █ ░  ░███    ░███ ░███
 ░███    ░███ ░███████████  ░███░░███░███ ░███          ░██████    ░██████████  ░███
 ░███    ░███ ░███░░░░░███  ░███ ░░██████ ░███    █████ ░███░░█    ░███░░░░░███ ░███
 ░███    ███  ░███    ░███  ░███  ░░█████ ░░███  ░░███  ░███ ░   █ ░███    ░███ ░░░ 
 ██████████   █████   █████ █████  ░░█████ ░░█████████  ██████████ █████   █████ ███
░░░░░░░░░░   ░░░░░   ░░░░░ ░░░░░    ░░░░░   ░░░░░░░░░  ░░░░░░░░░░ ░░░░░   ░░░░░ ░░░\033[0m\n""")
        time.sleep(1)
        enemy = random.choice(enemies)
        printer(f"\033[1m\033[91mA WILD {enemy.upper()} APPEARED!\033[0m\033[0m")
        time.sleep(1)
        printer(f"\033[1m\033[95m   {enemy}:\033[0m \033[91m\"{random.choice(intro_dialogues[enemy])}\"\033[0m ")
        time.sleep(1)
        printer(f"\033[91m\033[1m{enemy} asks you a question...\033[0m\033[0m")
        time.sleep(1.5)
        ans = input("\n\033[1m\033[97mWho was the creator of Python?\033[0m\033[0m\n"
                    "\n   A. Guido van Rossum\n"
                    "   B. Dennis Ritchie\n"
                    "   C. Bjarne Stroustrup\n"
                    "   D. James Gosling\n"
                    "\n> ")
        if ans.lower() == "a":
            print(f"\n\033[1m\033[92mThat is correct! {enemy} nods approvingly.\033[0m\033[0m")
            printer(f"\033[1m\033[95m   {enemy}:\033[0m\033[0m \033[92m\"{random.choice(correct_dialogues[enemy])}\"\033[0m\n")
            time.sleep(1.5)
            print(f"\033[1m\033[92m   Current HP: {hp}\033[0m\033[0m")
            print(f"\033[1m\033[93m   Current EXP: {exp}\033[0m\033[0m\n")
            proceed = input('\033[90m(Click Enter to Proceed)\033[0m\n')
            clear()
        else:
            hp -= 20
            print(f"\n\033[1m\033[91mThat is incorrect! {enemy} throws a chalk on you.\033[0m\033[0m")
            printer(f"\033[1m\033[95m   {enemy}:\033[0m\033[0m \033[91m\"{random.choice(wrong_dialogues[enemy])}\"\033[0m\n")
            time.sleep(1.5)
            print("\033[1m\033[91m   -20HP\033[0m\033[0m")
            time.sleep(1.5)
            if hp > 0:
                print(f"\n\033[1m\033[92m   Current HP: {hp}\033[0m\033[1m")
                print(f"\033[1m\033[93m   Current EXP: {exp}\033[0m\033[0m\n")
                proceed = input('\033[90m(Click Enter to Proceed)\033[0m \n')
                clear()
            else:
                print(f"\n\033[1m\033[92m   Current HP: {hp}\033[0m\033[0m")
                print(f"\033[1m\033[93m   Current EXP: {exp}\033[0m\033[0m\n")
                time.sleep(2)
                break
        ans2 = input("\n\033[1m\033[97mWhat year was Python created?\033[0m\033[0m\n"
                    "\n   A. 1941\n"
                    "   B. 1961\n"
                    "   C. 1991\n"
                    "   D. 1981\n"
                    "\n> ")
        if ans2.lower() == "c":
            print(f"\n\033[1m\033[92mThat is correct! {enemy} nods approvingly.\033[0m\033[0m")
            printer(f"\033[1m\033[95m   {enemy}:\033[0m\033[0m \033[92m\"{random.choice(correct_dialogues[enemy])}\"\033[0m\n")
            time.sleep(1.5)
            print(f"\033[1m\033[92m   Current HP: {hp}\033[0m\033[0m")
            print(f"\033[1m\033[93m   Current EXP: {exp}\033[0m\033[0m\n")
            proceed = input('\033[90m(Click Enter to Proceed)\033[0m\n')
            clear()
        else:
            hp -= 20
            print(f"\n\033[1m\033[91mThat is incorrect! {enemy} throws a chalk on you.\033[0m\033[0m")
            printer(f"\033[1m\033[95m   {enemy}:\033[0m\033[0m \033[91m\"{random.choice(wrong_dialogues[enemy])}\"\033[0m\n")
            time.sleep(1.5)
            print("\033[1m\033[91m  -20HP\033[0m\033[0m")
            time.sleep(1.5)
            if hp > 0:
                print(f"\n\033[1m\033[92m   Current HP: {hp}\033[0m\033[1m")
                print(f"\033[1m\033[93m   Current EXP: {exp}\033[0m\033[0m\n")
                proceed = input('\033[90m(Click Enter to Proceed)\033[0m \n')
                clear()
            else:
                print(f"\n\033[1m\033[92m   Current HP: {hp}\033[0m\033[0m")
                print(f"\033[1m\033[93m   Current EXP: {exp}\033[0m\033[0m\n")
                time.sleep(2)
                break
        ans3 = input("\n\033[1m\033[97mProgramming is mainly about memorizing code instead of solving problems.\033[0m\033[0m\n"
                     "\n   A. True\n"
                     "   B. False\n"
                     "   C. Maybe\n"
                     "   D. A and B\n"
                     "\n> ")
        if ans3.lower() == "b":
            print(f"\n\033[1m\033[92mThat is correct! {enemy} nods approvingly.\033[0m\033[0m")
            printer(f"\033[1m\033[95m   {enemy}:\033[0m\033[0m \033[92m\"{random.choice(correct_dialogues[enemy])}\"\033[0m\n")
            time.sleep(1.5)
            print(f"\033[1m\033[92m   Current HP: {hp}\033[0m\033[0m")
            print(f"\033[1m\033[93m   Current EXP: {exp}\033[0m\033[0m\n")
            proceed = input('\033[90m(Click Enter to Proceed)\033[0m\n')
            clear()
        else:
            hp -= 20
            print(f"\n\033[1m\033[91mThat is incorrect! {enemy} throws a chalk on you.\033[0m\033[0m")
            printer(f"\033[1m\033[95m   {enemy}:\033[0m\033[0m \033[91m\"{random.choice(wrong_dialogues[enemy])}\"\033[0m\n")
            time.sleep(1.5)
            print("\033[1m\033[91m   -20HP\033[0m\033[0m")
            time.sleep(1.5)
            if hp > 0:
                print(f"\n\033[1m\033[92m   Current HP: {hp}\033[0m\033[1m")
                print(f"\033[1m\033[93m   Current EXP: {exp}\033[0m\033[0m\n")
                proceed = input('\033[90m(Click Enter to Proceed)\033[0m \n')
                clear()
            else:
                print(f"\n\033[1m\033[92m   Current HP: {hp}\033[0m\033[0m")
                print(f"\033[1m\033[93m   Current EXP: {exp}\033[0m\033[0m\n")
                time.sleep(2)
                break
        ans4 = input("\n\033[1m\033[97mAll programming languages share the same syntax.\033[0m\033[0m\n"
            "\n   A. True\n"
            "   B. False\n"
            "   C. Maybe\n"
            "   D. A and B\n"
            "\n> ")
        if ans4.lower() == "b":
            print(f"\n\033[1m\033[92mThat is correct! {enemy} nods approvingly.\033[0m\033[0m")
            printer(f"\033[1m\033[95m   {enemy}:\033[0m\033[0m \033[92m\"{random.choice(correct_dialogues[enemy])}\"\033[0m\n")
            time.sleep(1.5)
            print(f"\033[1m\033[92m   Current HP: {hp}\033[0m\033[0m")
            print(f"\033[1m\033[93m   Current EXP: {exp}\033[0m\033[0m\n")
            proceed = input('\033[90m(Click Enter to Proceed)\033[0m\n')
            clear()
        else:
            hp -= 20
            print(f"\n\033[1m\033[91mThat is incorrect! {enemy} throws a chalk on you.\033[0m\033[0m")
            printer(f"\033[1m\033[95m   {enemy}:\033[0m\033[0m \033[91m\"{random.choice(wrong_dialogues[enemy])}\"\033[0m\n")
            time.sleep(1.5)
            print("\033[1m\033[91m   -20HP\033[0m\033[0m")
            time.sleep(1.5)
            if hp > 0:
                print(f"\n\033[1m\033[92m   Current HP: {hp}\033[0m\033[1m")
                print(f"\033[1m\033[93m   Current EXP: {exp}\033[0m\033[0m\n")
                proceed = input('\033[90m(Click Enter to Proceed)\033[0m \n')
                clear()
            else:
                print(f"\n\033[1m\033[92m   Current HP: {hp}\033[0m\033[0m")
                print(f"\033[1m\033[93m   Current EXP: {exp}\033[0m\033[0m\n")
                time.sleep(2)
                break

    elif choice == "3":
        print("""\033[92m
███████████              █████    █████                             ███████████             ███              █████        █████████                         █████                         
░░███░░░░░███            ░░███    ░░███                             ░░███░░░░░███           ░░░              ░░███        ███░░░░░███                       ░░███                          
 ░███    ░███ █████ ████ ███████   ░███████    ██████  ████████      ░███    ░███ ████████  ████  ████████   ███████     ░███    ░░░  █████ ████ ████████   ███████    ██████   █████ █████
 ░██████████ ░░███ ░███ ░░░███░    ░███░░███  ███░░███░░███░░███     ░██████████ ░░███░░███░░███ ░░███░░███ ░░░███░      ░░█████████ ░░███ ░███ ░░███░░███ ░░░███░    ░░░░░███ ░░███ ░░███ 
 ░███░░░░░░   ░███ ░███   ░███     ░███ ░███ ░███ ░███ ░███ ░███     ░███░░░░░░   ░███ ░░░  ░███  ░███ ░███   ░███        ░░░░░░░░███ ░███ ░███  ░███ ░███   ░███      ███████  ░░░█████░  
 ░███         ░███ ░███   ░███ ███ ░███ ░███ ░███ ░███ ░███ ░███     ░███         ░███      ░███  ░███ ░███   ░███ ███    ███    ░███ ░███ ░███  ░███ ░███   ░███ ███ ███░░███   ███░░░███ 
 █████        ░░███████   ░░█████  ████ █████░░██████  ████ █████    █████        █████     █████ ████ █████  ░░█████    ░░█████████  ░░███████  ████ █████  ░░█████ ░░████████ █████ █████
░░░░░          ░░░░░███    ░░░░░  ░░░░ ░░░░░  ░░░░░░  ░░░░ ░░░░░    ░░░░░        ░░░░░     ░░░░░ ░░░░ ░░░░░    ░░░░░      ░░░░░░░░░    ░░░░░███ ░░░░ ░░░░░    ░░░░░   ░░░░░░░░ ░░░░░ ░░░░░ 
               ███ ░███                                                                                                                ███ ░███                                            
              ░░██████                                                                                                                ░░██████                                             
               ░░░░░░                                                                                                                  ░░░░░░\033[0m\n"""
              "The \033[95mprint\033[0m function is a Python instruction that will output values and results to the computer screen. It can show text, numbers, variables, or \n"
              "even the results of expressions. It’s one of the first and most useful functions beginners learn because it helps you see what your program is doing. The basic\n"
              " syntax of the print() function is print(value, ..., sep=' ', end='\\n'), where each part has a specific purpose. The value represents the data you want to\n"
              "display, which can be text, numbers, variables, or even expressions. (Optional) The sep parameter (short for separator) determines what character separates multiple values\n"
              " — by default, it uses a space (' '). (Optional) The end parameter decides what happens after the message is printed — by default, it moves the cursor to a new line ('\\n'),\n"
              " but this can be changed to display multiple outputs on the same line. For example, print(\"Hello\", end=" ") followed by print(\"World!\") will output Hello\\nWorld!\n"
              "on one line.\n"
              "\n\033[1m\033[97m   Example:\033[0m \033[95mprint\033[0m(\033[92m'Hello, World!'\033[0m) \n"
              "\033[1m\033[97m   Example Output:\033[0m \033[97mHello, World!\033[0m \n")
        proceed = input('\033[90m(Click Enter to Proceed)\033[0m \n')
        clear()
        time.sleep(1)
        print("""\033[91m 
 ██████████     █████████   ██████   █████   █████████  ██████████ ███████████   ███
░░███░░░░███   ███░░░░░███ ░░██████ ░░███   ███░░░░░███░░███░░░░░█░░███░░░░░███ ░███
 ░███   ░░███ ░███    ░███  ░███░███ ░███  ███     ░░░  ░███  █ ░  ░███    ░███ ░███
 ░███    ░███ ░███████████  ░███░░███░███ ░███          ░██████    ░██████████  ░███
 ░███    ░███ ░███░░░░░███  ░███ ░░██████ ░███    █████ ░███░░█    ░███░░░░░███ ░███
 ░███    ███  ░███    ░███  ░███  ░░█████ ░░███  ░░███  ░███ ░   █ ░███    ░███ ░░░ 
 ██████████   █████   █████ █████  ░░█████ ░░█████████  ██████████ █████   █████ ███
░░░░░░░░░░   ░░░░░   ░░░░░ ░░░░░    ░░░░░   ░░░░░░░░░  ░░░░░░░░░░ ░░░░░   ░░░░░ ░░░\033[0m\n""")
        time.sleep(1)
        enemy = random.choice(enemies)
        printer(f"\033[1m\033[91mA WILD {enemy.upper()} APPEARED!\033[0m\033[0m")
        time.sleep(1)
        printer(f"\033[1m\033[95m   {enemy}:\033[0m \033[91m\"{random.choice(intro_dialogues[enemy])}\"\033[0m ")
        time.sleep(1)
        printer(f"\033[91m\033[1m{enemy} asks you a question...\033[0m\033[0m")
        time.sleep(1.5)
        ans = input("\n\033[1m\033[97mWhat is the main purpose of the print() function in Python?\033[0m\033[0m\n"
                    "\n   A. To take input from the user\n"
                    "   B. To display output on the screen\n"
                    "   C. To store values in variables\n"
                    "   D. To stop the program\n"
                    "\n> ")
        if ans.lower() == "b":
            print(f"\n\033[1m\033[92mThat is correct! {enemy} nods approvingly.\033[0m\033[0m")
            printer(f"\033[1m\033[95m   {enemy}:\033[0m\033[0m \033[92m\"{random.choice(correct_dialogues[enemy])}\"\033[0m\n")
            time.sleep(1.5)
            print(f"\033[1m\033[92m   Current HP: {hp}\033[0m\033[0m")
            print(f"\033[1m\033[93m   Current EXP: {exp}\033[0m\033[0m\n")
            proceed = input('\033[90m(Click Enter to Proceed)\033[0m\n')
            clear()
        else:
            hp -= 20
            print(f"\n\033[1m\033[91mThat is incorrect! {enemy} throws a chalk on you.\033[0m\033[0m")
            printer(f"\033[1m\033[95m   {enemy}:\033[0m\033[0m \033[91m\"{random.choice(wrong_dialogues[enemy])}\"\033[0m\n")
            time.sleep(1.5)
            print("\033[1m\033[91m   -20HP\033[0m\033[0m")
            time.sleep(1.5)
            if hp > 0:
                print(f"\n\033[1m\033[92m   Current HP: {hp}\033[0m\033[1m")
                print(f"\033[1m\033[93m   Current EXP: {exp}\033[0m\033[0m\n")
                proceed = input('\033[90m(Click Enter to Proceed)\033[0m \n')
                clear()
            else:
                print(f"\n\033[1m\033[92m   Current HP: {hp}\033[0m\033[0m")
                print(f"\033[1m\033[93m   Current EXP: {exp}\033[0m\033[0m\n")
                time.sleep(2)
                break
        ans2 = input("\n\033[1m\033[97mWhat will this code: print(\"Hello\", \"World\") output?\033[0m\033[0m\n"
                     "\n   A. HelloWorld\n"
                     "   B. Hello World\n"
                     "   C. Hello, World\n"
                     "   D. Error\n"
                     "\n> ")
        if ans2.lower() == "b":
            print(f"\n\033[1m\033[92mThat is correct! {enemy} nods approvingly.\033[0m\033[0m")
            printer(f"\033[1m\033[95m   {enemy}:\033[0m\033[0m \033[92m\"{random.choice(correct_dialogues[enemy])}\"\033[0m\n")
            time.sleep(1.5)
            print(f"\033[1m\033[92m   Current HP: {hp}\033[0m\033[0m")
            print(f"\033[1m\033[93m   Current EXP: {exp}\033[0m\033[0m\n")
            proceed = input('\033[90m(Click Enter to Proceed)\033[0m\n')
            clear()
        else:
            hp -= 20
            print(f"\n\033[1m\033[91mThat is incorrect! {enemy} throws a chalk on you.\033[0m\033[0m")
            printer(
                f"\033[1m\033[95m   {enemy}:\033[0m\033[0m \033[91m\"{random.choice(wrong_dialogues[enemy])}\"\033[0m\n")
            time.sleep(1.5)
            print("\033[1m\033[91m  -20HP\033[0m\033[0m")
            time.sleep(1.5)
            if hp > 0:
                print(f"\n\033[1m\033[92m   Current HP: {hp}\033[0m\033[1m")
                print(f"\033[1m\033[93m   Current EXP: {exp}\033[0m\033[0m\n")
                proceed = input('\033[90m(Click Enter to Proceed)\033[0m \n')
                clear()
            else:
                print(f"\n\033[1m\033[92m   Current HP: {hp}\033[0m\033[0m")
                print(f"\033[1m\033[93m   Current EXP: {exp}\033[0m\033[0m\n")
                time.sleep(2)
                break
        ans3 = input("\n\033[1m\033[97mThe print() function can only display text and cannot show variables or numbers.\033[0m\033[0m\n"
            "\n   A. True\n"
            "   B. False\n"
            "   C. Maybe\n"
            "   D. A and B\n"
            "\n> ")
        if ans3.lower() == "b":
            print(f"\n\033[1m\033[92mThat is correct! {enemy} nods approvingly.\033[0m\033[0m")
            printer(f"\033[1m\033[95m   {enemy}:\033[0m\033[0m \033[92m\"{random.choice(correct_dialogues[enemy])}\"\033[0m\n")
            time.sleep(1.5)
            print(f"\033[1m\033[92m   Current HP: {hp}\033[0m\033[0m")
            print(f"\033[1m\033[93m   Current EXP: {exp}\033[0m\033[0m\n")
            proceed = input('\033[90m(Click Enter to Proceed)\033[0m\n')
            clear()
        else:
            hp -= 20
            print(f"\n\033[1m\033[91mThat is incorrect! {enemy} throws a chalk on you.\033[0m\033[0m")
            printer(
                f"\033[1m\033[95m   {enemy}:\033[0m\033[0m \033[91m\"{random.choice(wrong_dialogues[enemy])}\"\033[0m\n")
            time.sleep(1.5)
            print("\033[1m\033[91m   -20HP\033[0m\033[0m")
            time.sleep(1.5)
            if hp > 0:
                print(f"\n\033[1m\033[92m   Current HP: {hp}\033[0m\033[1m")
                print(f"\033[1m\033[93m   Current EXP: {exp}\033[0m\033[0m\n")
                proceed = input('\033[90m(Click Enter to Proceed)\033[0m \n')
                clear()
            else:
                print(f"\n\033[1m\033[92m   Current HP: {hp}\033[0m\033[0m")
                print(f"\033[1m\033[93m   Current EXP: {exp}\033[0m\033[0m\n")
                time.sleep(2)
                break
        ans4 = input("\n\033[1m\033[97mprint() function can display numbers, text, and even calculations.\033[0m\033[0m\n"
                     "\n   A. True\n"
                     "   B. False\n"
                     "   C. Maybe\n"
                     "   D. A and B\n"
                     "\n> ")
        if ans4.lower() == "a":
            print(f"\n\033[1m\033[92mThat is correct! {enemy} nods approvingly.\033[0m\033[0m")
            printer(f"\033[1m\033[95m   {enemy}:\033[0m\033[0m \033[92m\"{random.choice(correct_dialogues[enemy])}\"\033[0m\n")
            time.sleep(1.5)
            print(f"\033[1m\033[92m   Current HP: {hp}\033[0m\033[0m")
            print(f"\033[1m\033[93m   Current EXP: {exp}\033[0m\033[0m\n")
            proceed = input('\033[90m(Click Enter to Proceed)\033[0m\n')
            clear()
        else:
            hp -= 20
            print(f"\n\033[1m\033[91mThat is incorrect! {enemy} throws a chalk on you.\033[0m\033[0m")
            printer(f"\033[1m\033[95m   {enemy}:\033[0m\033[0m \033[91m\"{random.choice(wrong_dialogues[enemy])}\"\033[0m\n")
            time.sleep(1.5)
            print("\033[1m\033[91m   -20HP\033[0m\033[0m")
            time.sleep(1.5)
            if hp > 0:
                print(f"\n\033[1m\033[92m   Current HP: {hp}\033[0m\033[1m")
                print(f"\033[1m\033[93m   Current EXP: {exp}\033[0m\033[0m\n")
                proceed = input('\033[90m(Click Enter to Proceed)\033[0m \n')
                clear()
            else:
                print(f"\n\033[1m\033[92m   Current HP: {hp}\033[0m\033[0m")
                print(f"\033[1m\033[93m   Current EXP: {exp}\033[0m\033[0m\n")
                time.sleep(2)
                break

    elif choice == "4":
        print("""\033[92m
 ███████████              █████    █████                               █████████                                                                █████           
░░███░░░░░███            ░░███    ░░███                               ███░░░░░███                                                              ░░███            
 ░███    ░███ █████ ████ ███████   ░███████    ██████  ████████      ███     ░░░   ██████  █████████████   █████████████    ██████  ████████   ███████    ██████ 
 ░██████████ ░░███ ░███ ░░░███░    ░███░░███  ███░░███░░███░░███    ░███          ███░░███░░███░░███░░███ ░░███░░███░░███  ███░░███░░███░░███ ░░░███░    ███░░  
 ░███░░░░░░   ░███ ░███   ░███     ░███ ░███ ░███ ░███ ░███ ░███    ░███         ░███ ░███ ░███ ░███ ░███  ░███ ░███ ░███ ░███████  ░███ ░███   ░███    ░░█████ 
 ░███         ░███ ░███   ░███ ███ ░███ ░███ ░███ ░███ ░███ ░███    ░░███     ███░███ ░███ ░███ ░███ ░███  ░███ ░███ ░███ ░███░░░   ░███ ░███   ░███ ███ ░░░░███
 █████        ░░███████   ░░█████  ████ █████░░██████  ████ █████    ░░█████████ ░░██████  █████░███ █████ █████░███ █████░░██████  ████ █████  ░░█████  ██████ 
░░░░░          ░░░░░███    ░░░░░  ░░░░ ░░░░░  ░░░░░░  ░░░░ ░░░░░      ░░░░░░░░░   ░░░░░░  ░░░░░ ░░░ ░░░░░ ░░░░░ ░░░ ░░░░░  ░░░░░░  ░░░░ ░░░░░    ░░░░░  ░░░░░░  
               ███ ░███                                                                                                                                         
              ░░██████                                                                                                                                          
               ░░░░░░\033[0m\n"""
              "Comments are lines in a Python program that are ignored by the computer. Comments can be used to explain Python code. It can also be used to make \n"
              "the code more readable, leave notes, and prevent execution when testing code. To create a Comment you just need to put a \033[90m#\033[0m symbol at the start\n"
              "and Python will ignore everything after the \033[90m#\033[0m symbol. \n"
              "\n\033[1m\033[97m   Example:\033[0m \033[95mprint\033[0m(\033[92m'Hello, World!'\033[0m)  \033[90m# This prints a greeting\033[0m \n"
              "\033[1m\033[97m   Example Output:\033[0m Hello, World! \n"
              "\nYou can also write multi-line comments using triple quotes (''' or \"\"\") \n"
"""\033[92m   '''
   This is a multi-line comment.
   It can span several lines.
   '''\033[0m \n""")
        proceed = input('\033[90m(Click Enter to Proceed)\033[0m \n')
        clear()
        time.sleep(1)
        print("""\033[91m 
 ██████████     █████████   ██████   █████   █████████  ██████████ ███████████   ███
░░███░░░░███   ███░░░░░███ ░░██████ ░░███   ███░░░░░███░░███░░░░░█░░███░░░░░███ ░███
 ░███   ░░███ ░███    ░███  ░███░███ ░███  ███     ░░░  ░███  █ ░  ░███    ░███ ░███
 ░███    ░███ ░███████████  ░███░░███░███ ░███          ░██████    ░██████████  ░███
 ░███    ░███ ░███░░░░░███  ░███ ░░██████ ░███    █████ ░███░░█    ░███░░░░░███ ░███
 ░███    ███  ░███    ░███  ░███  ░░█████ ░░███  ░░███  ░███ ░   █ ░███    ░███ ░░░ 
 ██████████   █████   █████ █████  ░░█████ ░░█████████  ██████████ █████   █████ ███
░░░░░░░░░░   ░░░░░   ░░░░░ ░░░░░    ░░░░░   ░░░░░░░░░  ░░░░░░░░░░ ░░░░░   ░░░░░ ░░░\033[0m\n""")
        time.sleep(1)
        enemy = random.choice(enemies)
        printer(f"\033[1m\033[91mA WILD {enemy.upper()} APPEARED!\033[0m\033[0m")
        time.sleep(1)
        printer(f"\033[1m\033[95m   {enemy}:\033[0m \033[91m\"{random.choice(intro_dialogues[enemy])}\"\033[0m ")
        time.sleep(1)
        printer(f"\033[91m\033[1m{enemy} asks you a question...\033[0m\033[0m")
        time.sleep(1.5)
        ans = input("\n\033[1m\033[97mWhat symbol is used to write a single-line comment in Python?\033[0m\033[0m\n"
                    "\n   A. #\n"
                    "   B. *\n"
                    "   C. @\n"
                    "   D. !\n"
                    "\n> ")
        if ans.lower() == "a":
            print(f"\n\033[1m\033[92mThat is correct! {enemy} nods approvingly.\033[0m\033[0m")
            printer(f"\033[1m\033[95m   {enemy}:\033[0m\033[0m \033[92m\"{random.choice(correct_dialogues[enemy])}\"\033[0m\n")
            time.sleep(1.5)
            print(f"\033[1m\033[92m   Current HP: {hp}\033[0m\033[0m")
            print(f"\033[1m\033[93m   Current EXP: {exp}\033[0m\033[0m\n")
            proceed = input('\033[90m(Click Enter to Proceed)\033[0m\n')
            clear()
        else:
            hp -= 20
            print(f"\n\033[1m\033[91mThat is incorrect! {enemy} throws a chalk on you.\033[0m\033[0m")
            printer(f"\033[1m\033[95m   {enemy}:\033[0m\033[0m \033[91m\"{random.choice(wrong_dialogues[enemy])}\"\033[0m\n")
            time.sleep(1.5)
            print("\033[1m\033[91m   -20HP\033[0m\033[0m")
            time.sleep(1.5)
            if hp > 0:
                print(f"\n\033[1m\033[92m   Current HP: {hp}\033[0m\033[1m")
                print(f"\033[1m\033[93m   Current EXP: {exp}\033[0m\033[0m\n")
                proceed = input('\033[90m(Click Enter to Proceed)\033[0m \n')
                clear()
            else:
                print(f"\n\033[1m\033[92m   Current HP: {hp}\033[0m\033[0m")
                print(f"\033[1m\033[93m   Current EXP: {exp}\033[0m\033[0m\n")
                time.sleep(2)
                break
        ans2 = input("\n\033[1m\033[97mWhat are comments mainly used for in Python code?\033[0m\033[0m\n"
                     "\n   A. To make the program run faster\n"
                     "   B. To store user input\n"
                     "   C. To explain or describe code\n"
                     "   D. To output text on the screen\n"
                     "\n> ")
        if ans2.lower() == "c":
            print(f"\n\033[1m\033[92mThat is correct! {enemy} nods approvingly.\033[0m\033[0m")
            printer(f"\033[1m\033[95m   {enemy}:\033[0m\033[0m \033[92m\"{random.choice(correct_dialogues[enemy])}\"\033[0m\n")
            time.sleep(1.5)
            print(f"\033[1m\033[92m   Current HP: {hp}\033[0m\033[0m")
            print(f"\033[1m\033[93m   Current EXP: {exp}\033[0m\033[0m\n")
            proceed = input('\033[90m(Click Enter to Proceed)\033[0m\n')
            clear()
        else:
            hp -= 20
            print(f"\n\033[1m\033[91mThat is incorrect! {enemy} throws a chalk on you.\033[0m\033[0m")
            printer(f"\033[1m\033[95m   {enemy}:\033[0m\033[0m \033[91m\"{random.choice(wrong_dialogues[enemy])}\"\033[0m\n")
            time.sleep(1.5)
            print("\033[1m\033[91m  -20HP\033[0m\033[0m")
            time.sleep(1.5)
            if hp > 0:
                print(f"\n\033[1m\033[92m   Current HP: {hp}\033[0m\033[1m")
                print(f"\033[1m\033[93m   Current EXP: {exp}\033[0m\033[0m\n")
                proceed = input('\033[90m(Click Enter to Proceed)\033[0m \n')
                clear()
            else:
                print(f"\n\033[1m\033[92m   Current HP: {hp}\033[0m\033[0m")
                print(f"\033[1m\033[93m   Current EXP: {exp}\033[0m\033[0m\n")
                time.sleep(2)
                break
        ans3 = input("\n\033[1m\033[97mMulti-line comments in Python require a special keyword.\033[0m\033[0m\n"
            "\n   A. True\n"
            "   B. False\n"
            "   C. Maybe\n"
            "   D. A and B\n"
            "\n> ")
        if ans3.lower() == "b":
            print(f"\n\033[1m\033[92mThat is correct! {enemy} nods approvingly.\033[0m\033[0m")
            printer(f"\033[1m\033[95m   {enemy}:\033[0m\033[0m \033[92m\"{random.choice(correct_dialogues[enemy])}\"\033[0m\n")
            time.sleep(1.5)
            print(f"\033[1m\033[92m   Current HP: {hp}\033[0m\033[0m")
            print(f"\033[1m\033[93m   Current EXP: {exp}\033[0m\033[0m\n")
            proceed = input('\033[90m(Click Enter to Proceed)\033[0m\n')
            clear()
        else:
            hp -= 20
            print(f"\n\033[1m\033[91mThat is incorrect! {enemy} throws a chalk on you.\033[0m\033[0m")
            printer(f"\033[1m\033[95m   {enemy}:\033[0m\033[0m \033[91m\"{random.choice(wrong_dialogues[enemy])}\"\033[0m\n")
            time.sleep(1.5)
            print("\033[1m\033[91m   -20HP\033[0m\033[0m")
            time.sleep(1.5)
            if hp > 0:
                print(f"\n\033[1m\033[92m   Current HP: {hp}\033[0m\033[1m")
                print(f"\033[1m\033[93m   Current EXP: {exp}\033[0m\033[0m\n")
                proceed = input('\033[90m(Click Enter to Proceed)\033[0m \n')
                clear()
            else:
                print(f"\n\033[1m\033[92m   Current HP: {hp}\033[0m\033[0m")
                print(f"\033[1m\033[93m   Current EXP: {exp}\033[0m\033[0m\n")
                time.sleep(2)
                break
        ans4 = input("\n\033[1m\033[97mComments in Python affect how the code runs.\033[0m\033[0m\n"
            "\n   A. True\n"
            "   B. False\n"
            "   C. Maybe\n"
            "   D. A and B\n"
            "\n> ")
        if ans4.lower() == "b":
            print(f"\n\033[1m\033[92mThat is correct! {enemy} nods approvingly.\033[0m\033[0m")
            printer(f"\033[1m\033[95m   {enemy}:\033[0m\033[0m \033[92m\"{random.choice(correct_dialogues[enemy])}\"\033[0m\n")
            time.sleep(1.5)
            print(f"\033[1m\033[92m   Current HP: {hp}\033[0m\033[0m")
            print(f"\033[1m\033[93m   Current EXP: {exp}\033[0m\033[0m\n")
            proceed = input('\033[90m(Click Enter to Proceed)\033[0m\n')
            clear()
        else:
            hp -= 20
            print(f"\n\033[1m\033[91mThat is incorrect! {enemy} throws a chalk on you.\033[0m\033[0m")
            printer(f"\033[1m\033[95m   {enemy}:\033[0m\033[0m \033[91m\"{random.choice(wrong_dialogues[enemy])}\"\033[0m\n")
            time.sleep(1.5)
            print("\033[1m\033[91m   -20HP\033[0m\033[0m")
            time.sleep(1.5)
            if hp > 0:
                print(f"\n\033[1m\033[92m   Current HP: {hp}\033[0m\033[1m")
                print(f"\033[1m\033[93m   Current EXP: {exp}\033[0m\033[0m\n")
                proceed = input('\033[90m(Click Enter to Proceed)\033[0m \n')
                clear()
            else:
                print(f"\n\033[1m\033[92m   Current HP: {hp}\033[0m\033[0m")
                print(f"\033[1m\033[93m   Current EXP: {exp}\033[0m\033[0m\n")
                time.sleep(2)
                break

    elif choice == "5":
        print("""\033[92m
 █████   █████                      ███            █████     ████                                               █████    ██████████              █████                 ███████████                                      
░░███   ░░███                      ░░░            ░░███     ░░███                                              ░░███    ░░███░░░░███            ░░███                 ░█░░░███░░░█                                      
 ░███    ░███   ██████   ████████  ████   ██████   ░███████  ░███   ██████   █████      ██████   ████████    ███████     ░███   ░░███  ██████   ███████    ██████     ░   ░███  ░  █████ ████ ████████   ██████   ██████ 
 ░███    ░███  ░░░░░███ ░░███░░███░░███  ░░░░░███  ░███░░███ ░███  ███░░███ ███░░      ░░░░░███ ░░███░░███  ███░░███     ░███    ░███ ░░░░░███ ░░░███░    ░░░░░███        ░███    ░░███ ░███ ░░███░░███ ███░░███ ███░░  
 ░░███   ███    ███████  ░███ ░░░  ░███   ███████  ░███ ░███ ░███ ░███████ ░░█████      ███████  ░███ ░███ ░███ ░███     ░███    ░███  ███████   ░███      ███████        ░███     ░███ ░███  ░███ ░███░███████ ░░█████ 
  ░░░█████░    ███░░███  ░███      ░███  ███░░███  ░███ ░███ ░███ ░███░░░   ░░░░███    ███░░███  ░███ ░███ ░███ ░███     ░███    ███  ███░░███   ░███ ███ ███░░███        ░███     ░███ ░███  ░███ ░███░███░░░   ░░░░███
    ░░███     ░░████████ █████     █████░░████████ ████████  █████░░██████  ██████    ░░████████ ████ █████░░████████    ██████████  ░░████████  ░░█████ ░░████████       █████    ░░███████  ░███████ ░░██████  ██████ 
     ░░░       ░░░░░░░░ ░░░░░     ░░░░░  ░░░░░░░░ ░░░░░░░░  ░░░░░  ░░░░░░  ░░░░░░      ░░░░░░░░ ░░░░ ░░░░░  ░░░░░░░░    ░░░░░░░░░░    ░░░░░░░░    ░░░░░   ░░░░░░░░       ░░░░░      ░░░░░███  ░███░░░   ░░░░░░  ░░░░░░  
                                                                                                                                                                                    ███ ░███  ░███                      
                                                                                                                                                                                   ░░██████   █████                     
                                                                                                                                                                                    ░░░░░░   ░░░░░\033[0m\n"""
              "A variable is a name that stores data that can be used and manipulated in a program. Think of it as a container box that holds a value. A variable can\n"
              "have a short name (like x and y) or a more descriptive name (age, car_name, total_volume). A variable name can only contain alpha-numeric characters and\n"
              "underscores (A-z, 0-9, and _). It also must start with a letter or the underscore character, it cannot start with number. A Variable is also case-sensitive\n"
              "(age and AGE are two different variables)\n")
        print("""\033[97m   Variable Naming Rules\033[0m
\033[1m\033[92m      Good:\033[0m name AGE bread spam23 _speed
\033[1m\033[91m      Bad:\033[0m 1name #bread var.12 15
\033[1m\033[93m      Different:\033[0m name Name NAME\n""")
        proceed = input('\033[90m(Click Enter to Proceed)\033[0m \n')

        print("\033[1m\033[97m   Basic Data Types:\033[0m\n"
              "      int – Integer numbers (e.g., 10, 25)\n"
              "      float – Decimal numbers (e.g., 12.5, 3.14)\n"
              "      str – String or text (e.g., \"Hello\", \"Juan\"\n"
              "      bool – Boolean values (True or False)\n"
              "\n\033[1m\033[97m   Sample Code:\033[0m\n"
              "      name = \"Maria\"\n"
              "      age = 20\n"
              "      grade = 89.5\n"
              "      is_enrolled = True\n")
        proceed2 = input('\033[90m(Click Enter to Proceed)\033[0m \n')
        clear()
        time.sleep(1)
        print("""\033[91m 
 ██████████     █████████   ██████   █████   █████████  ██████████ ███████████   ███
░░███░░░░███   ███░░░░░███ ░░██████ ░░███   ███░░░░░███░░███░░░░░█░░███░░░░░███ ░███
 ░███   ░░███ ░███    ░███  ░███░███ ░███  ███     ░░░  ░███  █ ░  ░███    ░███ ░███
 ░███    ░███ ░███████████  ░███░░███░███ ░███          ░██████    ░██████████  ░███
 ░███    ░███ ░███░░░░░███  ░███ ░░██████ ░███    █████ ░███░░█    ░███░░░░░███ ░███
 ░███    ███  ░███    ░███  ░███  ░░█████ ░░███  ░░███  ░███ ░   █ ░███    ░███ ░░░ 
 ██████████   █████   █████ █████  ░░█████ ░░█████████  ██████████ █████   █████ ███
░░░░░░░░░░   ░░░░░   ░░░░░ ░░░░░    ░░░░░   ░░░░░░░░░  ░░░░░░░░░░ ░░░░░   ░░░░░ ░░░\033[0m\n""")
        time.sleep(1)
        enemy = random.choice(enemies)
        printer(f"\033[1m\033[91mA WILD {enemy.upper()} APPEARED!\033[0m\033[0m")
        time.sleep(1)
        printer(f"\033[1m\033[95m   {enemy}:\033[0m \033[91m\"{random.choice(intro_dialogues[enemy])}\"\033[0m ")
        time.sleep(1)
        printer(f"\033[91m\033[1m{enemy} asks you a question...\033[0m\033[0m")
        time.sleep(1.5)
        ans = input("\n\033[1m\033[97mWhich of the following is a valid variable name in Python?\033[0m\033[0m\n"
                    "\n   A. 1name\n"
                    "   B. #bread\n"
                    "   C. var.12\n"
                    "   D. car_name\n"
                    "\n> ")
        if ans.lower() == "d":
            print(f"\n\033[1m\033[92mThat is correct! {enemy} nods approvingly.\033[0m\033[0m")
            printer(f"\033[1m\033[95m   {enemy}:\033[0m\033[0m \033[92m\"{random.choice(correct_dialogues[enemy])}\"\033[0m\n")
            time.sleep(1.5)
            print(f"\033[1m\033[92m   Current HP: {hp}\033[0m\033[0m")
            print(f"\033[1m\033[93m   Current EXP: {exp}\033[0m\033[0m\n")
            proceed = input('\033[90m(Click Enter to Proceed)\033[0m\n')
            clear()
        else:
            hp -= 20
            print(f"\n\033[1m\033[91mThat is incorrect! {enemy} throws a chalk on you.\033[0m\033[0m")
            printer(f"\033[1m\033[95m   {enemy}:\033[0m\033[0m \033[91m\"{random.choice(wrong_dialogues[enemy])}\"\033[0m\n")
            time.sleep(1.5)
            print("\033[1m\033[91m   -20HP\033[0m\033[0m")
            time.sleep(1.5)
            if hp > 0:
                print(f"\n\033[1m\033[92m   Current HP: {hp}\033[0m\033[1m")
                print(f"\033[1m\033[93m   Current EXP: {exp}\033[0m\033[0m\n")
                proceed = input('\033[90m(Click Enter to Proceed)\033[0m \n')
                clear()
            else:
                print(f"\n\033[1m\033[92m   Current HP: {hp}\033[0m\033[0m")
                print(f"\033[1m\033[93m   Current EXP: {exp}\033[0m\033[0m\n")
                time.sleep(2)
                break
        ans2 = input("\n\033[1m\033[97mWhat will happen if you try to name a variable starting with a number (e.g., 2count)?\033[0m\033[0m\n"
                     "\n   A. It will be treated as a comment\n"
                     "   B. It will cause an error\n"
                     "   C. It will work normally\n"
                     "   D. It will automatically change to _2count\n"
                     "\n> ")
        if ans2.lower() == "b":
            print(f"\n\033[1m\033[92mThat is correct! {enemy} nods approvingly.\033[0m\033[0m")
            printer(f"\033[1m\033[95m   {enemy}:\033[0m\033[0m \033[92m\"{random.choice(correct_dialogues[enemy])}\"\033[0m\n")
            time.sleep(1.5)
            print(f"\033[1m\033[92m   Current HP: {hp}\033[0m\033[0m")
            print(f"\033[1m\033[93m   Current EXP: {exp}\033[0m\033[0m\n")
            proceed = input('\033[90m(Click Enter to Proceed)\033[0m\n')
            clear()
        else:
            hp -= 20
            print(f"\n\033[1m\033[91mThat is incorrect! {enemy} throws a chalk on you.\033[0m\033[0m")
            printer(f"\033[1m\033[95m   {enemy}:\033[0m\033[0m \033[91m\"{random.choice(wrong_dialogues[enemy])}\"\033[0m\n")
            time.sleep(1.5)
            print("\033[1m\033[91m  -20HP\033[0m\033[0m")
            time.sleep(1.5)
            if hp > 0:
                print(f"\n\033[1m\033[92m   Current HP: {hp}\033[0m\033[1m")
                print(f"\033[1m\033[93m   Current EXP: {exp}\033[0m\033[0m\n")
                proceed = input('\033[90m(Click Enter to Proceed)\033[0m \n')
                clear()
            else:
                print(f"\n\033[1m\033[92m   Current HP: {hp}\033[0m\033[0m")
                print(f"\033[1m\033[93m   Current EXP: {exp}\033[0m\033[0m\n")
                time.sleep(2)
                break
        ans3 = input("\n\033[1m\033[97mVariable names in Python can start with an underscore (_).\033[0m\033[0m\n"
                     "\n   A. True\n"
                     "   B. False\n"
                     "   C. Maybe\n"
                     "   D. A and B\n"
                     "\n> ")
        if ans3.lower() == "a":
            print(f"\n\033[1m\033[92mThat is correct! {enemy} nods approvingly.\033[0m\033[0m")
            printer(f"\033[1m\033[95m   {enemy}:\033[0m\033[0m \033[92m\"{random.choice(correct_dialogues[enemy])}\"\033[0m\n")
            time.sleep(1.5)
            print(f"\033[1m\033[92m   Current HP: {hp}\033[0m\033[0m")
            print(f"\033[1m\033[93m   Current EXP: {exp}\033[0m\033[0m\n")
            proceed = input('\033[90m(Click Enter to Proceed)\033[0m\n')
            clear()
        else:
            hp -= 20
            print(f"\n\033[1m\033[91mThat is incorrect! {enemy} throws a chalk on you.\033[0m\033[0m")
            printer(f"\033[1m\033[95m   {enemy}:\033[0m\033[0m \033[91m\"{random.choice(wrong_dialogues[enemy])}\"\033[0m\n")
            time.sleep(1.5)
            print("\033[1m\033[91m   -20HP\033[0m\033[0m")
            time.sleep(1.5)
            if hp > 0:
                print(f"\n\033[1m\033[92m   Current HP: {hp}\033[0m\033[1m")
                print(f"\033[1m\033[93m   Current EXP: {exp}\033[0m\033[0m\n")
                proceed = input('\033[90m(Click Enter to Proceed)\033[0m \n')
                clear()
            else:
                print(f"\n\033[1m\033[92m   Current HP: {hp}\033[0m\033[0m")
                print(f"\033[1m\033[93m   Current EXP: {exp}\033[0m\033[0m\n")
                time.sleep(2)
                break
        ans4 = input("\n\033[1m\033[97mVariable names can contain spaces, like: my name = \"John\".\033[0m\033[0m\n"
                     "\n   A. True\n"
                     "   B. False\n"
                     "   C. Maybe\n"
                     "   D. A and B\n"
                     "\n> ")
        if ans4.lower() == "b":
            print(f"\n\033[1m\033[92mThat is correct! {enemy} nods approvingly.\033[0m\033[0m")
            printer(f"\033[1m\033[95m   {enemy}:\033[0m\033[0m \033[92m\"{random.choice(correct_dialogues[enemy])}\"\033[0m\n")
            time.sleep(1.5)
            print(f"\033[1m\033[92m   Current HP: {hp}\033[0m\033[0m")
            print(f"\033[1m\033[93m   Current EXP: {exp}\033[0m\033[0m\n")
            proceed = input('\033[90m(Click Enter to Proceed)\033[0m\n')
            clear()
        else:
            hp -= 20
            print(f"\n\033[1m\033[91mThat is incorrect! {enemy} throws a chalk on you.\033[0m\033[0m")
            printer(f"\033[1m\033[95m   {enemy}:\033[0m\033[0m \033[91m\"{random.choice(wrong_dialogues[enemy])}\"\033[0m\n")
            time.sleep(1.5)
            print("\033[1m\033[91m   -20HP\033[0m\033[0m")
            time.sleep(1.5)
            if hp > 0:
                print(f"\n\033[1m\033[92m   Current HP: {hp}\033[0m\033[1m")
                print(f"\033[1m\033[93m   Current EXP: {exp}\033[0m\033[0m\n")
                proceed = input('\033[90m(Click Enter to Proceed)\033[0m \n')
                clear()
            else:
                print(f"\n\033[1m\033[92m   Current HP: {hp}\033[0m\033[0m")
                print(f"\033[1m\033[93m   Current EXP: {exp}\033[0m\033[0m\n")
                time.sleep(2)
                break

    elif choice == "6":
        print("""\033[92m
   █████████              ███   █████    █████                                █████     ███                 ███████                                            █████     ███                     
  ███░░░░░███            ░░░   ░░███    ░░███                                ░░███     ░░░                ███░░░░░███                                         ░░███     ░░░                      
 ░███    ░███  ████████  ████  ███████   ░███████   █████████████    ██████  ███████   ████   ██████     ███     ░░███ ████████   ██████  ████████   ██████   ███████   ████   ██████  ████████  
 ░███████████ ░░███░░███░░███ ░░░███░    ░███░░███ ░░███░░███░░███  ███░░███░░░███░   ░░███  ███░░███   ░███      ░███░░███░░███ ███░░███░░███░░███ ░░░░░███ ░░░███░   ░░███  ███░░███░░███░░███ 
 ░███░░░░░███  ░███ ░░░  ░███   ░███     ░███ ░███  ░███ ░███ ░███ ░███████   ░███     ░███ ░███ ░░░    ░███      ░███ ░███ ░███░███████  ░███ ░░░   ███████   ░███     ░███ ░███ ░███ ░███ ░███ 
 ░███    ░███  ░███      ░███   ░███ ███ ░███ ░███  ░███ ░███ ░███ ░███░░░    ░███ ███ ░███ ░███  ███   ░░███     ███  ░███ ░███░███░░░   ░███      ███░░███   ░███ ███ ░███ ░███ ░███ ░███ ░███ 
 █████   █████ █████     █████  ░░█████  ████ █████ █████░███ █████░░██████   ░░█████  █████░░██████     ░░░███████░   ░███████ ░░██████  █████    ░░████████  ░░█████  █████░░██████  ████ █████
░░░░░   ░░░░░ ░░░░░     ░░░░░    ░░░░░  ░░░░ ░░░░░ ░░░░░ ░░░ ░░░░░  ░░░░░░     ░░░░░  ░░░░░  ░░░░░░        ░░░░░░░     ░███░░░   ░░░░░░  ░░░░░      ░░░░░░░░    ░░░░░  ░░░░░  ░░░░░░  ░░░░ ░░░░░ 
                                                                                                                       ░███                                                                      
                                                                                                                       █████                                                                     
                                                                                                                      ░░░░░\033[0m\n"""
              "In programming, arithmetic operations are mathematical actions that allow you to perform calculations such as addition, subtraction, multiplication, and\n"
              "division. Python supports all the basic arithmetic operators that you use in math, and they work on numbers stored in variables or written directly in code.")
        print("""\033[97m
   Operator      Description                           Example      Result\033[0m

      +          Addition                               5 + 3         8    
      -          Subtraction                            10 - 4        6    
      *          Multiplication                         2 * 6         12  
      /          Division (float result)                8 / 2         4.0 
      //         Floor Division (whole number)          9 // 2        4    
      %          Modulus (remainder)                    9 % 2         1   
      **         Exponentiation (power)                 2 ** 3        8\n""")
        proceed = input('\033[90m(Click Enter to Proceed)\033[0m\n')

        print("""An expression is a combination of values, variables, and operators that Python can evaluate to produce a result. For example:

   x = 10
   y = 3
   result = (x + y) * 2
   print(result)

In this example, (x + y) * 2 is an arithmetic expression. Python first adds x and y, then multiplies the sum by 2, following the order of operations (PEMDAS) — 
Parentheses, Exponents, Multiplication, Division, Addition, Subtraction. Arithmetic operations and expressions are the foundation of programming logic, used 
in calculations, algorithms, and decision-making in almost every type of program.\n""")
        proceed2 = input('\033[90m(Click Enter to Proceed)\033[0m \n')
        clear()
        time.sleep(1)
        print("""\033[91m 
 ██████████     █████████   ██████   █████   █████████  ██████████ ███████████   ███
░░███░░░░███   ███░░░░░███ ░░██████ ░░███   ███░░░░░███░░███░░░░░█░░███░░░░░███ ░███
 ░███   ░░███ ░███    ░███  ░███░███ ░███  ███     ░░░  ░███  █ ░  ░███    ░███ ░███
 ░███    ░███ ░███████████  ░███░░███░███ ░███          ░██████    ░██████████  ░███
 ░███    ░███ ░███░░░░░███  ░███ ░░██████ ░███    █████ ░███░░█    ░███░░░░░███ ░███
 ░███    ███  ░███    ░███  ░███  ░░█████ ░░███  ░░███  ░███ ░   █ ░███    ░███ ░░░ 
 ██████████   █████   █████ █████  ░░█████ ░░█████████  ██████████ █████   █████ ███
░░░░░░░░░░   ░░░░░   ░░░░░ ░░░░░    ░░░░░   ░░░░░░░░░  ░░░░░░░░░░ ░░░░░   ░░░░░ ░░░\033[0m\n""")
        time.sleep(1)
        enemy = random.choice(enemies)
        printer(f"\033[1m\033[91mA WILD {enemy.upper()} APPEARED!\033[0m\033[0m")
        time.sleep(1)
        printer(f"\033[1m\033[95m   {enemy}:\033[0m \033[91m\"{random.choice(intro_dialogues[enemy])}\"\033[0m ")
        time.sleep(1)
        printer(f"\033[91m\033[1m{enemy} asks you a question...\033[0m\033[0m")
        time.sleep(1.5)
        ans = input("\n\033[1m\033[97mWhich of the following is not an arithmetic operator in Python\033[0m\033[0m\n"
                    "\n   A. **\n"
                    "   B. //\n"
                    "   C. =\n"
                    "   D. %\n"
                    "\n> ")
        if ans.lower() == "c":
            print(f"\n\033[1m\033[92mThat is correct! {enemy} nods approvingly.\033[0m\033[0m")
            printer(f"\033[1m\033[95m   {enemy}:\033[0m\033[0m \033[92m\"{random.choice(correct_dialogues[enemy])}\"\033[0m\n")
            time.sleep(1.5)
            print(f"\033[1m\033[92m   Current HP: {hp}\033[0m\033[0m")
            print(f"\033[1m\033[93m   Current EXP: {exp}\033[0m\033[0m\n")
            proceed = input('\033[90m(Click Enter to Proceed)\033[0m\n')
            clear()
        else:
            hp -= 20
            print(f"\n\033[1m\033[91mThat is incorrect! {enemy} throws a chalk on you.\033[0m\033[0m")
            printer(f"\033[1m\033[95m   {enemy}:\033[0m\033[0m \033[91m\"{random.choice(wrong_dialogues[enemy])}\"\033[0m\n")
            time.sleep(1.5)
            print("\033[1m\033[91m   -20HP\033[0m\033[0m")
            time.sleep(1.5)
            if hp > 0:
                print(f"\n\033[1m\033[92m   Current HP: {hp}\033[0m\033[1m")
                print(f"\033[1m\033[93m   Current EXP: {exp}\033[0m\033[0m\n")
                proceed = input('\033[90m(Click Enter to Proceed)\033[0m \n')
                clear()
            else:
                print(f"\n\033[1m\033[92m   Current HP: {hp}\033[0m\033[0m")
                print(f"\033[1m\033[93m   Current EXP: {exp}\033[0m\033[0m\n")
                time.sleep(2)
                break
        ans2 = input("\n\033[1m\033[97mWhat does the % operator do?\033[0m\033[0m\n"
            "\n   A. Divides two numbers\n"
            "   B. Returns the quotient of a division\n"
            "   C. Converts a number to a percentage\n"
            "   D. Finds the remainder of a division\n"
            "\n> ")
        if ans2.lower() == "d":
            print(f"\n\033[1m\033[92mThat is correct! {enemy} nods approvingly.\033[0m\033[0m")
            printer(f"\033[1m\033[95m   {enemy}:\033[0m\033[0m \033[92m\"{random.choice(correct_dialogues[enemy])}\"\033[0m\n")
            time.sleep(1.5)
            print(f"\033[1m\033[92m   Current HP: {hp}\033[0m\033[0m")
            print(f"\033[1m\033[93m   Current EXP: {exp}\033[0m\033[0m\n")
            proceed = input('\033[90m(Click Enter to Proceed)\033[0m\n')
            clear()
        else:
            hp -= 20
            print(f"\n\033[1m\033[91mThat is incorrect! {enemy} throws a chalk on you.\033[0m\033[0m")
            printer(f"\033[1m\033[95m   {enemy}:\033[0m\033[0m \033[91m\"{random.choice(wrong_dialogues[enemy])}\"\033[0m\n")
            time.sleep(1.5)
            print("\033[1m\033[91m  -20HP\033[0m\033[0m")
            time.sleep(1.5)
            if hp > 0:
                print(f"\n\033[1m\033[92m   Current HP: {hp}\033[0m\033[1m")
                print(f"\033[1m\033[93m   Current EXP: {exp}\033[0m\033[0m\n")
                proceed = input('\033[90m(Click Enter to Proceed)\033[0m \n')
                clear()
            else:
                print(f"\n\033[1m\033[92m   Current HP: {hp}\033[0m\033[0m")
                print(f"\033[1m\033[93m   Current EXP: {exp}\033[0m\033[0m\n")
                time.sleep(2)
                break
        ans3 = input("\n\033[1m\033[97mWhat is the correct order of arithmetic operations in Python (precedence)?\033[0m\033[0m\n"
                     "\n   A. Subtraction/Addition → Division/Multiplication → Exponent → Parenthesis\n"
                     "   B. Parenthesis → Exponent → Multiplication/Division → Addition/Subtraction\n"
                     "   C. Parenthesis → Exponent → Addition/Subtraction → Multiplication/Division\n"
                     "   D. Multiplication → Division → Addition → Subtraction → Exponent → Parenthesis \n"
                     "\n> ")
        if ans3.lower() == "b":
            print(f"\n\033[1m\033[92mThat is correct! {enemy} nods approvingly.\033[0m\033[0m")
            printer(f"\033[1m\033[95m   {enemy}:\033[0m\033[0m \033[92m\"{random.choice(correct_dialogues[enemy])}\"\033[0m\n")
            time.sleep(1.5)
            print(f"\033[1m\033[92m   Current HP: {hp}\033[0m\033[0m")
            print(f"\033[1m\033[93m   Current EXP: {exp}\033[0m\033[0m\n")
            proceed = input('\033[90m(Click Enter to Proceed)\033[0m\n')
            clear()
        else:
            hp -= 20
            print(f"\n\033[1m\033[91mThat is incorrect! {enemy} throws a chalk on you.\033[0m\033[0m")
            printer(f"\033[1m\033[95m   {enemy}:\033[0m\033[0m \033[91m\"{random.choice(wrong_dialogues[enemy])}\"\033[0m\n")
            time.sleep(1.5)
            print("\033[1m\033[91m   -20HP\033[0m\033[0m")
            time.sleep(1.5)
            if hp > 0:
                print(f"\n\033[1m\033[92m   Current HP: {hp}\033[0m\033[1m")
                print(f"\033[1m\033[93m   Current EXP: {exp}\033[0m\033[0m\n")
                proceed = input('\033[90m(Click Enter to Proceed)\033[0m \n')
                clear()
            else:
                print(f"\n\033[1m\033[92m   Current HP: {hp}\033[0m\033[0m")
                print(f"\033[1m\033[93m   Current EXP: {exp}\033[0m\033[0m\n")
                time.sleep(2)
                break
        ans4 = input("\n\033[1m\033[97mWhat does the expression: (2 + 3) * 4 ** 2  evaluate to?\033[0m\033[0m\n"
                     "\n   A. 20\n"
                     "   B. 100\n"
                     "   C. 80\n"
                     "   D. 400\n"
                     "\n> ")
        if ans4.lower() == "c":
            print(f"\n\033[1m\033[92mThat is correct! {enemy} nods approvingly.\033[0m\033[0m")
            printer(f"\033[1m\033[95m   {enemy}:\033[0m\033[0m \033[92m\"{random.choice(correct_dialogues[enemy])}\"\033[0m\n")
            time.sleep(1.5)
            print(f"\033[1m\033[92m   Current HP: {hp}\033[0m\033[0m")
            print(f"\033[1m\033[93m   Current EXP: {exp}\033[0m\033[0m\n")
            proceed = input('\033[90m(Click Enter to Proceed)\033[0m\n')
            clear()
        else:
            hp -= 20
            print(f"\n\033[1m\033[91mThat is incorrect! {enemy} throws a chalk on you.\033[0m\033[0m")
            printer(f"\033[1m\033[95m   {enemy}:\033[0m\033[0m \033[91m\"{random.choice(wrong_dialogues[enemy])}\"\033[0m\n")
            time.sleep(1.5)
            print("\033[1m\033[91m   -20HP\033[0m\033[0m")
            time.sleep(1.5)
            if hp > 0:
                print(f"\n\033[1m\033[92m   Current HP: {hp}\033[0m\033[1m")
                print(f"\033[1m\033[93m   Current EXP: {exp}\033[0m\033[0m\n")
                proceed = input('\033[90m(Click Enter to Proceed)\033[0m \n')
                clear()
            else:
                print(f"\n\033[1m\033[92m   Current HP: {hp}\033[0m\033[0m")
                print(f"\033[1m\033[93m   Current EXP: {exp}\033[0m\033[0m\n")
                time.sleep(2)
                break

    elif choice == "7":
        print("""\033[92m
 █████                                  █████       ███████████                                 █████     ███                             
░░███                                  ░░███       ░░███░░░░░░█                                ░░███     ░░░                              
 ░███  ████████   ████████  █████ ████ ███████      ░███   █ ░  █████ ████ ████████    ██████  ███████   ████   ██████  ████████    █████ 
 ░███ ░░███░░███ ░░███░░███░░███ ░███ ░░░███░       ░███████   ░░███ ░███ ░░███░░███  ███░░███░░░███░   ░░███  ███░░███░░███░░███  ███░░  
 ░███  ░███ ░███  ░███ ░███ ░███ ░███   ░███        ░███░░░█    ░███ ░███  ░███ ░███ ░███ ░░░   ░███     ░███ ░███ ░███ ░███ ░███ ░░█████ 
 ░███  ░███ ░███  ░███ ░███ ░███ ░███   ░███ ███    ░███  ░     ░███ ░███  ░███ ░███ ░███  ███  ░███ ███ ░███ ░███ ░███ ░███ ░███  ░░░░███
 █████ ████ █████ ░███████  ░░████████  ░░█████     █████       ░░████████ ████ █████░░██████   ░░█████  █████░░██████  ████ █████ ██████ 
░░░░░ ░░░░ ░░░░░  ░███░░░    ░░░░░░░░    ░░░░░     ░░░░░         ░░░░░░░░ ░░░░ ░░░░░  ░░░░░░     ░░░░░  ░░░░░  ░░░░░░  ░░░░ ░░░░░ ░░░░░░  
                  ░███                                                                                                                    
                  █████\033[0m\n"""
              "The input() function is used to get information from the user while a program is running. It pauses the program and waits for the user to type something on\n"
              "the keyboard, then presses Enter. The text that the user types is returned as a string (text data) by default. Because the function always returns data in\n"
              "string form, it is often necessary to convert the input into other data types, such as integers or floats, using type casting functions like int() or float().\n"
              " The input() function is commonly used to make programs interactive, allowing users to enter names, numbers, or other information that the program can then\n"
              "process. Its syntax is written as input(prompt), where the prompt is optional but helpful for instructing the user. Overall, the input() function plays a key\n"
              "role in creating dynamic and user-driven Python programs.\n"
              "\n\033[97m   Syntax:\033[0m variable = input(\"Prompt message: \")\n"
              "\n\033[97m   Example:\033[0m name = input(\"Enter your name: \")\n"
              "            age = input(\"Enter your age: \")\n")
        proceed = input('\033[90m(Click Enter to Proceed)\033[0m \n')
        clear()
        time.sleep(1)
        print("""\033[91m 
 ██████████     █████████   ██████   █████   █████████  ██████████ ███████████   ███
░░███░░░░███   ███░░░░░███ ░░██████ ░░███   ███░░░░░███░░███░░░░░█░░███░░░░░███ ░███
 ░███   ░░███ ░███    ░███  ░███░███ ░███  ███     ░░░  ░███  █ ░  ░███    ░███ ░███
 ░███    ░███ ░███████████  ░███░░███░███ ░███          ░██████    ░██████████  ░███
 ░███    ░███ ░███░░░░░███  ░███ ░░██████ ░███    █████ ░███░░█    ░███░░░░░███ ░███
 ░███    ███  ░███    ░███  ░███  ░░█████ ░░███  ░░███  ░███ ░   █ ░███    ░███ ░░░ 
 ██████████   █████   █████ █████  ░░█████ ░░█████████  ██████████ █████   █████ ███
░░░░░░░░░░   ░░░░░   ░░░░░ ░░░░░    ░░░░░   ░░░░░░░░░  ░░░░░░░░░░ ░░░░░   ░░░░░ ░░░\033[0m\n""")
        time.sleep(1)
        enemy = random.choice(enemies)
        printer(f"\033[1m\033[91mA WILD {enemy.upper()} APPEARED!\033[0m\033[0m")
        time.sleep(1)
        printer(f"\033[1m\033[95m   {enemy}:\033[0m \033[91m\"{random.choice(intro_dialogues[enemy])}\"\033[0m ")
        time.sleep(1)
        printer(f"\033[91m\033[1m{enemy} asks you a question...\033[0m\033[0m")
        time.sleep(1.5)
        ans = input("\n\033[1m\033[97mWhat is the main purpose of the input() function in Python?\033[0m\033[0m\n"
                    "\n   A. To receive data from the user\n"
                    "   B. To display output on the screen\n"
                    "   C. To perform calculations\n"
                    "   D. To initialize a variable\n"
                    "\n> ")
        if ans.lower() == "a":
            print(f"\n\033[1m\033[92mThat is correct! {enemy} nods approvingly.\033[0m\033[0m")
            printer(f"\033[1m\033[95m   {enemy}:\033[0m\033[0m \033[92m\"{random.choice(correct_dialogues[enemy])}\"\033[0m\n")
            time.sleep(1.5)
            print(f"\033[1m\033[92m   Current HP: {hp}\033[0m\033[0m")
            print(f"\033[1m\033[93m   Current EXP: {exp}\033[0m\033[0m\n")
            proceed = input('\033[90m(Click Enter to Proceed)\033[0m\n')
            clear()
        else:
            hp -= 20
            print(f"\n\033[1m\033[91mThat is incorrect! {enemy} throws a chalk on you.\033[0m\033[0m")
            printer(f"\033[1m\033[95m   {enemy}:\033[0m\033[0m \033[91m\"{random.choice(wrong_dialogues[enemy])}\"\033[0m\n")
            time.sleep(1.5)
            print("\033[1m\033[91m   -20HP\033[0m\033[0m")
            time.sleep(1.5)
            if hp > 0:
                print(f"\n\033[1m\033[92m   Current HP: {hp}\033[0m\033[1m")
                print(f"\033[1m\033[93m   Current EXP: {exp}\033[0m\033[0m\n")
                proceed = input('\033[90m(Click Enter to Proceed)\033[0m \n')
                clear()
            else:
                print(f"\n\033[1m\033[92m   Current HP: {hp}\033[0m\033[0m")
                print(f"\033[1m\033[93m   Current EXP: {exp}\033[0m\033[0m\n")
                time.sleep(2)
                break
        ans2 = input("\n\033[1m\033[97mBy default, what is the data type of the value returned by input()?\033[0m\033[0m\n"
                     "\n   A. float\n"
                     "   B. int\n"
                     "   C. bool\n"
                     "   D. str\n"
                     "\n> ")
        if ans2.lower() == "d":
            print(f"\n\033[1m\033[92mThat is correct! {enemy} nods approvingly.\033[0m\033[0m")
            printer(f"\033[1m\033[95m   {enemy}:\033[0m\033[0m \033[92m\"{random.choice(correct_dialogues[enemy])}\"\033[0m\n")
            time.sleep(1.5)
            print(f"\033[1m\033[92m   Current HP: {hp}\033[0m\033[0m")
            print(f"\033[1m\033[93m   Current EXP: {exp}\033[0m\033[0m\n")
            proceed = input('\033[90m(Click Enter to Proceed)\033[0m\n')
            clear()
        else:
            hp -= 20
            print(f"\n\033[1m\033[91mThat is incorrect! {enemy} throws a chalk on you.\033[0m\033[0m")
            printer(f"\033[1m\033[95m   {enemy}:\033[0m\033[0m \033[91m\"{random.choice(wrong_dialogues[enemy])}\"\033[0m\n")
            time.sleep(1.5)
            print("\033[1m\033[91m  -20HP\033[0m\033[0m")
            time.sleep(1.5)
            if hp > 0:
                print(f"\n\033[1m\033[92m   Current HP: {hp}\033[0m\033[1m")
                print(f"\033[1m\033[93m   Current EXP: {exp}\033[0m\033[0m\n")
                proceed = input('\033[90m(Click Enter to Proceed)\033[0m \n')
                clear()
            else:
                print(f"\n\033[1m\033[92m   Current HP: {hp}\033[0m\033[0m")
                print(f"\033[1m\033[93m   Current EXP: {exp}\033[0m\033[0m\n")
                time.sleep(2)
                break
        ans3 = input("\n\033[1m\033[97mWhat will the following code output if the user types 10?\n"
                     "x = input(\"Enter a number: \")\n"
                     "print(x + x)\033[0m\033[0m\n"
            "\n   A. 10\n"
            "   B. 1010\n"
            "   C. 20\n"
            "   D. Error\n"
            "\n> ")
        if ans3.lower() == "c":
            print(f"\n\033[1m\033[92mThat is correct! {enemy} nods approvingly.\033[0m\033[0m")
            printer(f"\033[1m\033[95m   {enemy}:\033[0m\033[0m \033[92m\"{random.choice(correct_dialogues[enemy])}\"\033[0m\n")
            time.sleep(1.5)
            print(f"\033[1m\033[92m   Current HP: {hp}\033[0m\033[0m")
            print(f"\033[1m\033[93m   Current EXP: {exp}\033[0m\033[0m\n")
            proceed = input('\033[90m(Click Enter to Proceed)\033[0m\n')
            clear()
        else:
            hp -= 20
            print(f"\n\033[1m\033[91mThat is incorrect! {enemy} throws a chalk on you.\033[0m\033[0m")
            printer(f"\033[1m\033[95m   {enemy}:\033[0m\033[0m \033[91m\"{random.choice(wrong_dialogues[enemy])}\"\033[0m\n")
            time.sleep(1.5)
            print("\033[1m\033[91m   -20HP\033[0m\033[0m")
            time.sleep(1.5)
            if hp > 0:
                print(f"\n\033[1m\033[92m   Current HP: {hp}\033[0m\033[1m")
                print(f"\033[1m\033[93m   Current EXP: {exp}\033[0m\033[0m\n")
                proceed = input('\033[90m(Click Enter to Proceed)\033[0m \n')
                clear()
            else:
                print(f"\n\033[1m\033[92m   Current HP: {hp}\033[0m\033[0m")
                print(f"\033[1m\033[93m   Current EXP: {exp}\033[0m\033[0m\n")
                time.sleep(2)
                break
        ans4 = input("\n\033[1m\033[97mYou can use input() to read multiple values at once, separated by commas.\033[0m\033[0m\n"
                     "\n   A. True\n"
                     "   B. False\n"
                     "   C. Maybe\n"
                     "   D. A and B\n"
                     "\n> ")
        if ans4.lower() == "b":
            print(f"\n\033[1m\033[92mThat is correct! {enemy} nods approvingly.\033[0m\033[0m")
            printer(f"\033[1m\033[95m   {enemy}:\033[0m\033[0m \033[92m\"{random.choice(correct_dialogues[enemy])}\"\033[0m\n")
            time.sleep(1.5)
            print(f"\033[1m\033[92m   Current HP: {hp}\033[0m\033[0m")
            print(f"\033[1m\033[93m   Current EXP: {exp}\033[0m\033[0m\n")
            proceed = input('\033[90m(Click Enter to Proceed)\033[0m\n')
            clear()
        else:
            hp -= 20
            print(f"\n\033[1m\033[91mThat is incorrect! {enemy} throws a chalk on you.\033[0m\033[0m")
            printer(f"\033[1m\033[95m   {enemy}:\033[0m\033[0m \033[91m\"{random.choice(wrong_dialogues[enemy])}\"\033[0m\n")
            time.sleep(1.5)
            print("\033[1m\033[91m   -20HP\033[0m\033[0m")
            time.sleep(1.5)
            if hp > 0:
                print(f"\n\033[1m\033[92m   Current HP: {hp}\033[0m\033[1m")
                print(f"\033[1m\033[93m   Current EXP: {exp}\033[0m\033[0m\n")
                proceed = input('\033[90m(Click Enter to Proceed)\033[0m \n')
                clear()
            else:
                print(f"\n\033[1m\033[92m   Current HP: {hp}\033[0m\033[0m")
                print(f"\033[1m\033[93m   Current EXP: {exp}\033[0m\033[0m\n")
                time.sleep(2)
                break

    elif choice == "8":
        print("""\033[92m
    ██████              █████████   █████               ███                     
   ███░░███            ███░░░░░███ ░░███               ░░░                      
  ░███ ░░░            ░███    ░░░  ███████   ████████  ████  ████████    ███████
 ███████    ██████████░░█████████ ░░░███░   ░░███░░███░░███ ░░███░░███  ███░░███
░░░███░    ░░░░░░░░░░  ░░░░░░░░███  ░███     ░███ ░░░  ░███  ░███ ░███ ░███ ░███
  ░███                 ███    ░███  ░███ ███ ░███      ░███  ░███ ░███ ░███ ░███
  █████               ░░█████████   ░░█████  █████     █████ ████ █████░░███████
 ░░░░░                 ░░░░░░░░░     ░░░░░  ░░░░░     ░░░░░ ░░░░ ░░░░░  ░░░░░███
                                                                        ███ ░███
                                                                       ░░██████ 
                                                                        ░░░░░░\033[0m\n"""
              "An f-string (short for formatted string literal) is a feature in Python that makes it easy to insert variables or expressions directly inside a string. It was\n"
              "introduced in Python 3.6 and is one of the simplest and most readable ways to format text output. To create an f-string, you just put an f before the opening\n"
              "quotation mark of a string, and then place any variable or expression inside curly braces {}. When the program runs, Python automatically replaces the braces\n"
              "with the corresponding values. For example, writing name = \"Evandrel\" and then print(f\"Hello, {name}!\") will display “Hello, Evandrel!”. F-strings can also\n"
              "evaluate expressions inside the braces, such as f\"{5 + 3}\", which would output 8. Aside from simply inserting variables into strings, f-strings in Python\n"
              "can also perform expressions, formatting, and function calls directly inside the curly braces {}. This means you can include operations like arithmetic\n"
              "({2 + 3} → 5), string methods ({name.upper()}), or even call functions ({len(name)}) within an f-string. F-strings also support format specifiers, allowing\n"
              "you to control how numbers or text appear. For example, you can format a floating-point number to two decimal places using f\"{price:.2f}\", or align text\n"
              "neatly using width specifiers like f\"{word:<10}\"Overall, f-strings are a powerful and user-friendly feature that helps make\n"
              "Python code cleaner and more expressive when handling text and variables together.\n")
        proceed = input('\033[90m(Click Enter to Proceed)\033[0m ')
        print("\n\033[1m\033[97m   Basic Syntax:\033[0m\n"
              "      print(f\"some text {variable_name}\")\n"
              "\n\033[1m\033[97m   1. Example:\033[0m\n"
              "      name = \"Luna\"\n"
              "      age = 15\n"
              "      print(f\"My name is {name} and I am {age} years old.\")\n"
              "\n\033[1m\033[97m   Example Output:\033[0m\n"
              "      My name is Luna and I am 15 years old.\n"
              "\n\033[1m\033[97m   2. Example:\033[0m\n"
              "      x = 5\n"
              "      y = 10\n"
              "      print(f\"The sum of {x} and {y} is {x + y}\")\n"
              "\n\033[1m\033[97m   Example Output:\033[0m\n"
              "      The sum of 5 and 10 is 15.\n")
        proceed2 = input('\033[90m(Click Enter to Proceed)\033[0m \n')
        clear()
        time.sleep(1)
        print("""\033[91m 
 ██████████     █████████   ██████   █████   █████████  ██████████ ███████████   ███
░░███░░░░███   ███░░░░░███ ░░██████ ░░███   ███░░░░░███░░███░░░░░█░░███░░░░░███ ░███
 ░███   ░░███ ░███    ░███  ░███░███ ░███  ███     ░░░  ░███  █ ░  ░███    ░███ ░███
 ░███    ░███ ░███████████  ░███░░███░███ ░███          ░██████    ░██████████  ░███
 ░███    ░███ ░███░░░░░███  ░███ ░░██████ ░███    █████ ░███░░█    ░███░░░░░███ ░███
 ░███    ███  ░███    ░███  ░███  ░░█████ ░░███  ░░███  ░███ ░   █ ░███    ░███ ░░░ 
 ██████████   █████   █████ █████  ░░█████ ░░█████████  ██████████ █████   █████ ███
░░░░░░░░░░   ░░░░░   ░░░░░ ░░░░░    ░░░░░   ░░░░░░░░░  ░░░░░░░░░░ ░░░░░   ░░░░░ ░░░\033[0m\n""")
        time.sleep(1)
        enemy = random.choice(enemies)
        printer(f"\033[1m\033[91mA WILD {enemy.upper()} APPEARED!\033[0m\033[0m")
        time.sleep(1)
        printer(f"\033[1m\033[95m   {enemy}:\033[0m \033[91m\"{random.choice(intro_dialogues[enemy])}\"\033[0m ")
        time.sleep(1)
        printer(f"\033[91m\033[1m{enemy} asks you a question...\033[0m\033[0m")
        time.sleep(1.5)
        ans = input("\n\033[1m\033[97mWhat does the “f” in f-string stand for?\033[0m\033[0m\n"
                    "\n   A. Format\n"
                    "   B. Function\n"
                    "   C. Flow\n"
                    "   D. For\n"
                    "\n> ")
        if ans.lower() == "a":
            print(f"\n\033[1m\033[92mThat is correct! {enemy} nods approvingly.\033[0m\033[0m")
            printer(f"\033[1m\033[95m   {enemy}:\033[0m\033[0m \033[92m\"{random.choice(correct_dialogues[enemy])}\"\033[0m\n")
            time.sleep(1.5)
            print(f"\033[1m\033[92m   Current HP: {hp}\033[0m\033[0m")
            print(f"\033[1m\033[93m   Current EXP: {exp}\033[0m\033[0m\n")
            proceed = input('\033[90m(Click Enter to Proceed)\033[0m\n')
            clear()
        else:
            hp -= 20
            print(f"\n\033[1m\033[91mThat is incorrect! {enemy} throws a chalk on you.\033[0m\033[0m")
            printer(f"\033[1m\033[95m   {enemy}:\033[0m\033[0m \033[91m\"{random.choice(wrong_dialogues[enemy])}\"\033[0m\n")
            time.sleep(1.5)
            print("\033[1m\033[91m   -20HP\033[0m\033[0m")
            time.sleep(1.5)
            if hp > 0:
                print(f"\n\033[1m\033[92m   Current HP: {hp}\033[0m\033[1m")
                print(f"\033[1m\033[93m   Current EXP: {exp}\033[0m\033[0m\n")
                proceed = input('\033[90m(Click Enter to Proceed)\033[0m \n')
                clear()
            else:
                print(f"\n\033[1m\033[92m   Current HP: {hp}\033[0m\033[0m")
                print(f"\033[1m\033[93m   Current EXP: {exp}\033[0m\033[0m\n")
                time.sleep(2)
                break
        ans2 = input("\n\033[1m\033[97mWhich of the following is the correct syntax for an f-string?\033[0m\033[0m\n"
            "\n   A. f(\"Hello {name}\")\n"
            "   B. f['Hello {name}']\n"
            "   C. f\"Hello {name}\"\n"
            "   D. f.(\"Hello {name}\")\n"
            "\n> ")
        if ans2.lower() == "c":
            print(f"\n\033[1m\033[92mThat is correct! {enemy} nods approvingly.\033[0m\033[0m")
            printer(f"\033[1m\033[95m   {enemy}:\033[0m\033[0m \033[92m\"{random.choice(correct_dialogues[enemy])}\"\033[0m\n")
            time.sleep(1.5)
            print(f"\033[1m\033[92m   Current HP: {hp}\033[0m\033[0m")
            print(f"\033[1m\033[93m   Current EXP: {exp}\033[0m\033[0m\n")
            proceed = input('\033[90m(Click Enter to Proceed)\033[0m\n')
            clear()
        else:
            hp -= 20
            print(f"\n\033[1m\033[91mThat is incorrect! {enemy} throws a chalk on you.\033[0m\033[0m")
            printer(f"\033[1m\033[95m   {enemy}:\033[0m\033[0m \033[91m\"{random.choice(wrong_dialogues[enemy])}\"\033[0m\n")
            time.sleep(1.5)
            print("\033[1m\033[91m  -20HP\033[0m\033[0m")
            time.sleep(1.5)
            if hp > 0:
                print(f"\n\033[1m\033[92m   Current HP: {hp}\033[0m\033[1m")
                print(f"\033[1m\033[93m   Current EXP: {exp}\033[0m\033[0m\n")
                proceed = input('\033[90m(Click Enter to Proceed)\033[0m \n')
                clear()
            else:
                print(f"\n\033[1m\033[92m   Current HP: {hp}\033[0m\033[0m")
                print(f"\033[1m\033[93m   Current EXP: {exp}\033[0m\033[0m\n")
                time.sleep(2)
                break
        ans3 = input("\n\033[1m\033[97mYou can put function calls inside f-string braces.\033[0m\033[0m\n"
                     "\n   A. True\n"
                     "   B. False\n"
                     "   C. Maybe\n"
                     "   D. A and B\n"
                     "\n> ")
        if ans3.lower() == "a":
            print(f"\n\033[1m\033[92mThat is correct! {enemy} nods approvingly.\033[0m\033[0m")
            printer(f"\033[1m\033[95m   {enemy}:\033[0m\033[0m \033[92m\"{random.choice(correct_dialogues[enemy])}\"\033[0m\n")
            time.sleep(1.5)
            print(f"\033[1m\033[92m   Current HP: {hp}\033[0m\033[0m")
            print(f"\033[1m\033[93m   Current EXP: {exp}\033[0m\033[0m\n")
            proceed = input('\033[90m(Click Enter to Proceed)\033[0m\n')
            clear()
        else:
            hp -= 20
            print(f"\n\033[1m\033[91mThat is incorrect! {enemy} throws a chalk on you.\033[0m\033[0m")
            printer(f"\033[1m\033[95m   {enemy}:\033[0m\033[0m \033[91m\"{random.choice(wrong_dialogues[enemy])}\"\033[0m\n")
            time.sleep(1.5)
            print("\033[1m\033[91m   -20HP\033[0m\033[0m")
            time.sleep(1.5)
            if hp > 0:
                print(f"\n\033[1m\033[92m   Current HP: {hp}\033[0m\033[1m")
                print(f"\033[1m\033[93m   Current EXP: {exp}\033[0m\033[0m\n")
                proceed = input('\033[90m(Click Enter to Proceed)\033[0m \n')
                clear()
            else:
                print(f"\n\033[1m\033[92m   Current HP: {hp}\033[0m\033[0m")
                print(f"\033[1m\033[93m   Current EXP: {exp}\033[0m\033[0m\n")
                time.sleep(2)
                break
        ans4 = input("\n\033[1m\033[97mYou must use double quotes \" with f-strings; single quotes ' will not work.\033[0m\033[0m\n"
            "\n   A. True\n"
            "   B. False\n"
            "   C. Maybe\n"
            "   D. A and B\n"
            "\n> ")
        if ans4.lower() == "b":
            print(f"\n\033[1m\033[92mThat is correct! {enemy} nods approvingly.\033[0m\033[0m")
            printer(f"\033[1m\033[95m   {enemy}:\033[0m\033[0m \033[92m\"{random.choice(correct_dialogues[enemy])}\"\033[0m\n")
            time.sleep(1.5)
            print(f"\033[1m\033[92m   Current HP: {hp}\033[0m\033[0m")
            print(f"\033[1m\033[93m   Current EXP: {exp}\033[0m\033[0m\n")
            proceed = input('\033[90m(Click Enter to Proceed)\033[0m\n')
            clear()
        else:
            hp -= 20
            print(f"\n\033[1m\033[91mThat is incorrect! {enemy} throws a chalk on you.\033[0m\033[0m")
            printer(f"\033[1m\033[95m   {enemy}:\033[0m\033[0m \033[91m\"{random.choice(wrong_dialogues[enemy])}\"\033[0m\n")
            time.sleep(1.5)
            print("\033[1m\033[91m   -20HP\033[0m\033[0m")
            time.sleep(1.5)
            if hp > 0:
                print(f"\n\033[1m\033[92m   Current HP: {hp}\033[0m\033[1m")
                print(f"\033[1m\033[93m   Current EXP: {exp}\033[0m\033[0m\n")
                proceed = input('\033[90m(Click Enter to Proceed)\033[0m \n')
                clear()
            else:
                print(f"\n\033[1m\033[92m   Current HP: {hp}\033[0m\033[0m")
                print(f"\033[1m\033[93m   Current EXP: {exp}\033[0m\033[0m\n")
                time.sleep(2)
                break

    elif choice == "9":
        print("""\033[92m
   █████████                          █████  ███   █████     ███                                ████      █████████   █████               █████                                                  █████           
  ███░░░░░███                        ░░███  ░░░   ░░███     ░░░                                ░░███     ███░░░░░███ ░░███               ░░███                                                  ░░███            
 ███     ░░░   ██████  ████████    ███████  ████  ███████   ████   ██████  ████████    ██████   ░███    ░███    ░░░  ███████    ██████   ███████    ██████  █████████████    ██████  ████████   ███████    █████ 
░███          ███░░███░░███░░███  ███░░███ ░░███ ░░░███░   ░░███  ███░░███░░███░░███  ░░░░░███  ░███    ░░█████████ ░░░███░    ░░░░░███ ░░░███░    ███░░███░░███░░███░░███  ███░░███░░███░░███ ░░░███░    ███░░  
░███         ░███ ░███ ░███ ░███ ░███ ░███  ░███   ░███     ░███ ░███ ░███ ░███ ░███   ███████  ░███     ░░░░░░░░███  ░███      ███████   ░███    ░███████  ░███ ░███ ░███ ░███████  ░███ ░███   ░███    ░░█████ 
░░███     ███░███ ░███ ░███ ░███ ░███ ░███  ░███   ░███ ███ ░███ ░███ ░███ ░███ ░███  ███░░███  ░███     ███    ░███  ░███ ███ ███░░███   ░███ ███░███░░░   ░███ ░███ ░███ ░███░░░   ░███ ░███   ░███ ███ ░░░░███
 ░░█████████ ░░██████  ████ █████░░████████ █████  ░░█████  █████░░██████  ████ █████░░████████ █████   ░░█████████   ░░█████ ░░████████  ░░█████ ░░██████  █████░███ █████░░██████  ████ █████  ░░█████  ██████ 
  ░░░░░░░░░   ░░░░░░  ░░░░ ░░░░░  ░░░░░░░░ ░░░░░    ░░░░░  ░░░░░  ░░░░░░  ░░░░ ░░░░░  ░░░░░░░░ ░░░░░     ░░░░░░░░░     ░░░░░   ░░░░░░░░    ░░░░░   ░░░░░░  ░░░░░ ░░░ ░░░░░  ░░░░░░  ░░░░ ░░░░░    ░░░░░  ░░░░░░\033[0m\n"""
              "Conditional statements are used to make decisions in a program. They allow your code to perform different actions depending on whether a condition is true or\n"
              "false. Conditional statements let your program “think” and react to different situations. They are essential for controlling the flow of your code, creating\n"
              "logic-based decisions, and making your programs more dynamic and interactive. Python relies on indentation (whitespace at the beginning of a line) to define \n"
              "scope in the code. Other programming languages often use curly-brackets for this purpose. Additionally, you can nest another condition inside a condition. In\n"
              "Python, the main conditional statements are if, elif, and else.\n")
        proceed = input('\033[90m(Click Enter to Proceed)\033[0m\n')
        print("\033[1m\033[97m   Basic Syntax\033[0m\n"
              "      if \033[90mcondition\033[0m:\n"
              "           \033[90m# code to run if the condition is true\033[0m\n"
              "      elif \033[90manother_condition\033[0m:\n"
              "           \033[90m# code to run if the preceding condition is false but this one is true\033[0m\n"
              "      else:\n"
              "           \033[90m# code to run if all conditions are false\033[0m\n")
        proceed2 = input('\033[90m(Click Enter to Proceed)\033[0m\n')
        print("""\033[1m\033[97m   Relational (Comparison) Operators\033[0m
       Operator      Meaning                            Example      Result\033[0m
    
          >          Greater than                        5 > 3        True    
          <          Less than                           5 < 3        False    
          *          Equal to                            5 == 5       True  
          /          Not equal to                        5 != 3       True
          //         Greater than or equal to            5 >= 5       True    
          %          Less than or equal to               3 <= 5       True\n""")
        proceed3 = input('\033[90m(Click Enter to Proceed)\033[0m \n')
        clear()
        time.sleep(1)
        print("""\033[91m 
 ██████████     █████████   ██████   █████   █████████  ██████████ ███████████   ███
░░███░░░░███   ███░░░░░███ ░░██████ ░░███   ███░░░░░███░░███░░░░░█░░███░░░░░███ ░███
 ░███   ░░███ ░███    ░███  ░███░███ ░███  ███     ░░░  ░███  █ ░  ░███    ░███ ░███
 ░███    ░███ ░███████████  ░███░░███░███ ░███          ░██████    ░██████████  ░███
 ░███    ░███ ░███░░░░░███  ░███ ░░██████ ░███    █████ ░███░░█    ░███░░░░░███ ░███
 ░███    ███  ░███    ░███  ░███  ░░█████ ░░███  ░░███  ░███ ░   █ ░███    ░███ ░░░ 
 ██████████   █████   █████ █████  ░░█████ ░░█████████  ██████████ █████   █████ ███
░░░░░░░░░░   ░░░░░   ░░░░░ ░░░░░    ░░░░░   ░░░░░░░░░  ░░░░░░░░░░ ░░░░░   ░░░░░ ░░░\033[0m\n""")
        time.sleep(1)
        enemy = random.choice(enemies)
        printer(f"\033[1m\033[91mA WILD {enemy.upper()} APPEARED!\033[0m\033[0m")
        time.sleep(1)
        printer(f"\033[1m\033[95m   {enemy}:\033[0m \033[91m\"{random.choice(intro_dialogues[enemy])}\"\033[0m ")
        time.sleep(1)
        printer(f"\033[91m\033[1m{enemy} asks you a question...\033[0m\033[0m")
        time.sleep(1.5)
        ans = input("\n\033[1m\033[97mWhich of the following statements is true about Python indentation?\033[0m\033[0m\n"
                    "\n   A. It’s optional\n"
                    "   B. It’s only used for loops\n"
                    "   C. It defines which code belongs to which block\n"
                    "   D. It can be replaced with curly braces\n"
                    "\n> ")
        if ans.lower() == "c":
            print(f"\n\033[1m\033[92mThat is correct! {enemy} nods approvingly.\033[0m\033[0m")
            printer(f"\033[1m\033[95m   {enemy}:\033[0m\033[0m \033[92m\"{random.choice(correct_dialogues[enemy])}\"\033[0m\n")
            time.sleep(1.5)
            print(f"\033[1m\033[92m   Current HP: {hp}\033[0m\033[0m")
            print(f"\033[1m\033[93m   Current EXP: {exp}\033[0m\033[0m\n")
            proceed = input('\033[90m(Click Enter to Proceed)\033[0m\n')
            clear()
        else:
            hp -= 20
            print(f"\n\033[1m\033[91mThat is incorrect! {enemy} throws a chalk on you.\033[0m\033[0m")
            printer(f"\033[1m\033[95m   {enemy}:\033[0m\033[0m \033[91m\"{random.choice(wrong_dialogues[enemy])}\"\033[0m\n")
            time.sleep(1.5)
            print("\033[1m\033[91m   -20HP\033[0m\033[0m")
            time.sleep(1.5)
            if hp > 0:
                print(f"\n\033[1m\033[92m   Current HP: {hp}\033[0m\033[1m")
                print(f"\033[1m\033[93m   Current EXP: {exp}\033[0m\033[0m\n")
                proceed = input('\033[90m(Click Enter to Proceed)\033[0m \n')
                clear()
            else:
                print(f"\n\033[1m\033[92m   Current HP: {hp}\033[0m\033[0m")
                print(f"\033[1m\033[93m   Current EXP: {exp}\033[0m\033[0m\n")
                time.sleep(2)
                break
        ans2 = input("\n\033[1m\033[97mWhat will the code below output?\n"
                     "age = 18\n"
                     "if age >= 18:\n"
                     "   print(\"Adult\")\n"
                     "else:\n"
                     "   print(\"Minor\")\033[0m\033[0m\n"
                     "\n   A. Adult\n"
                     "   B. Minor\n"
                     "   C. Error\n"
                     "   D. Nothing\n"
                     "\n> ")
        if ans2.lower() == "a":
            print(f"\n\033[1m\033[92mThat is correct! {enemy} nods approvingly.\033[0m\033[0m")
            printer(f"\033[1m\033[95m   {enemy}:\033[0m\033[0m \033[92m\"{random.choice(correct_dialogues[enemy])}\"\033[0m\n")
            time.sleep(1.5)
            print(f"\033[1m\033[92m   Current HP: {hp}\033[0m\033[0m")
            print(f"\033[1m\033[93m   Current EXP: {exp}\033[0m\033[0m\n")
            proceed = input('\033[90m(Click Enter to Proceed)\033[0m\n')
            clear()
        else:
            hp -= 20
            print(f"\n\033[1m\033[91mThat is incorrect! {enemy} throws a chalk on you.\033[0m\033[0m")
            printer(f"\033[1m\033[95m   {enemy}:\033[0m\033[0m \033[91m\"{random.choice(wrong_dialogues[enemy])}\"\033[0m\n")
            time.sleep(1.5)
            print("\033[1m\033[91m  -20HP\033[0m\033[0m")
            time.sleep(1.5)
            if hp > 0:
                print(f"\n\033[1m\033[92m   Current HP: {hp}\033[0m\033[1m")
                print(f"\033[1m\033[93m   Current EXP: {exp}\033[0m\033[0m\n")
                proceed = input('\033[90m(Click Enter to Proceed)\033[0m \n')
                clear()
            else:
                print(f"\n\033[1m\033[92m   Current HP: {hp}\033[0m\033[0m")
                print(f"\033[1m\033[93m   Current EXP: {exp}\033[0m\033[0m\n")
                time.sleep(2)
                break
        ans3 = input("\n\033[1m\033[97mWhat happens if you forget the colon : at the end of an if statement?\033[0m\033[0m\n"
                     "\n   A. It will be ignored\n"
                     "   B. The code still runs\n"
                     "   C. The next line will be skipped\n"
                     "   D. Python will give an error\n"
                     "\n> ")
        if ans3.lower() == "d":
            print(f"\n\033[1m\033[92mThat is correct! {enemy} nods approvingly.\033[0m\033[0m")
            printer(f"\033[1m\033[95m   {enemy}:\033[0m\033[0m \033[92m\"{random.choice(correct_dialogues[enemy])}\"\033[0m\n")
            time.sleep(1.5)
            print(f"\033[1m\033[92m   Current HP: {hp}\033[0m\033[0m")
            print(f"\033[1m\033[93m   Current EXP: {exp}\033[0m\033[0m\n")
            proceed = input('\033[90m(Click Enter to Proceed)\033[0m\n')
            clear()
        else:
            hp -= 20
            print(f"\n\033[1m\033[91mThat is incorrect! {enemy} throws a chalk on you.\033[0m\033[0m")
            printer(f"\033[1m\033[95m   {enemy}:\033[0m\033[0m \033[91m\"{random.choice(wrong_dialogues[enemy])}\"\033[0m\n")
            time.sleep(1.5)
            print("\033[1m\033[91m   -20HP\033[0m\033[0m")
            time.sleep(1.5)
            if hp > 0:
                print(f"\n\033[1m\033[92m   Current HP: {hp}\033[0m\033[1m")
                print(f"\033[1m\033[93m   Current EXP: {exp}\033[0m\033[0m\n")
                proceed = input('\033[90m(Click Enter to Proceed)\033[0m \n')
                clear()
            else:
                print(f"\n\033[1m\033[92m   Current HP: {hp}\033[0m\033[0m")
                print(f"\033[1m\033[93m   Current EXP: {exp}\033[0m\033[0m\n")
                time.sleep(2)
                break
        ans4 = input("\n\033[1m\033[97mThe else statement can exist without an if statement.\033[0m\033[0m\n"
            "\n   A. True\n"
            "   B. False\n"
            "   C. Maybe\n"
            "   D. A and B\n"
            "\n> ")
        if ans4.lower() == "b":
            print(f"\n\033[1m\033[92mThat is correct! {enemy} nods approvingly.\033[0m\033[0m")
            printer(f"\033[1m\033[95m   {enemy}:\033[0m\033[0m \033[92m\"{random.choice(correct_dialogues[enemy])}\"\033[0m\n")
            time.sleep(1.5)
            print(f"\033[1m\033[92m   Current HP: {hp}\033[0m\033[0m")
            print(f"\033[1m\033[93m   Current EXP: {exp}\033[0m\033[0m\n")
            proceed = input('\033[90m(Click Enter to Proceed)\033[0m\n')
            clear()
        else:
            hp -= 20
            print(f"\n\033[1m\033[91mThat is incorrect! {enemy} throws a chalk on you.\033[0m\033[0m")
            printer(f"\033[1m\033[95m   {enemy}:\033[0m\033[0m \033[91m\"{random.choice(wrong_dialogues[enemy])}\"\033[0m\n")
            time.sleep(1.5)
            print("\033[1m\033[91m   -20HP\033[0m\033[0m")
            time.sleep(1.5)
            if hp > 0:
                print(f"\n\033[1m\033[92m   Current HP: {hp}\033[0m\033[1m")
                print(f"\033[1m\033[93m   Current EXP: {exp}\033[0m\033[0m\n")
                proceed = input('\033[90m(Click Enter to Proceed)\033[0m \n')
                clear()
            else:
                print(f"\n\033[1m\033[92m   Current HP: {hp}\033[0m\033[0m")
                print(f"\033[1m\033[93m   Current EXP: {exp}\033[0m\033[0m\n")
                time.sleep(2)
                break
        ans5 = input("\n\033[1m\033[97mYou can nest an if statement inside another if statement.\033[0m\033[0m\n"
                     "\n   A. True\n"
                     "   B. False\n"
                     "   C. Maybe\n"
                     "   D. A and B\n"
                     "\n> ")
        if ans5.lower() == "a":
            print(f"\n\033[1m\033[92mThat is correct! {enemy} nods approvingly.\033[0m\033[0m")
            printer(
                f"\033[1m\033[95m   {enemy}:\033[0m\033[0m \033[92m\"{random.choice(correct_dialogues[enemy])}\"\033[0m\n")
            time.sleep(1.5)
            print(f"\033[1m\033[92m   Current HP: {hp}\033[0m\033[0m")
            print(f"\033[1m\033[93m   Current EXP: {exp}\033[0m\033[0m\n")
            proceed = input('\033[90m(Click Enter to Proceed)\033[0m\n')
            clear()
        else:
            hp -= 20
            print(f"\n\033[1m\033[91mThat is incorrect! {enemy} throws a chalk on you.\033[0m\033[0m")
            printer(
                f"\033[1m\033[95m   {enemy}:\033[0m\033[0m \033[91m\"{random.choice(wrong_dialogues[enemy])}\"\033[0m\n")
            time.sleep(1.5)
            print("\033[1m\033[91m   -20HP\033[0m\033[0m")
            time.sleep(1.5)
            if hp > 0:
                print(f"\n\033[1m\033[92m   Current HP: {hp}\033[0m\033[1m")
                print(f"\033[1m\033[93m   Current EXP: {exp}\033[0m\033[0m\n")
                proceed = input('\033[90m(Click Enter to Proceed)\033[0m \n')
                clear()
            else:
                print(f"\n\033[1m\033[92m   Current HP: {hp}\033[0m\033[0m")
                print(f"\033[1m\033[93m   Current EXP: {exp}\033[0m\033[0m\n")
                time.sleep(2)
                break

    elif choice == "10":
        print("""\033[92m
 █████                                    ███                     
░░███                                    ░░░                      
 ░███         ██████   ██████  ████████  ████  ████████    ███████
 ░███        ███░░███ ███░░███░░███░░███░░███ ░░███░░███  ███░░███
 ░███       ░███ ░███░███ ░███ ░███ ░███ ░███  ░███ ░███ ░███ ░███
 ░███      █░███ ░███░███ ░███ ░███ ░███ ░███  ░███ ░███ ░███ ░███
 ███████████░░██████ ░░██████  ░███████  █████ ████ █████░░███████
░░░░░░░░░░░  ░░░░░░   ░░░░░░   ░███░░░  ░░░░░ ░░░░ ░░░░░  ░░░░░███
                               ░███                       ███ ░███
                               █████                     ░░██████ 
                              ░░░░░                       ░░░░░░\033[0m\n"""
              "Loops are used in programming to repeat a block of code multiple times. Instead of writing the same code again and again, loops let you automate repetitive tasks\n"
              "efficiently. Loops are essential in programming because they make code shorter, cleaner, and more efficient, allowing programmers to perform repeated actions,\n"
              "process data, and create dynamic programs that respond intelligently to different situations. Python also provides loop control statements such as break, continue,\n"
              " and pass. The break statement stops the loop entirely, even if the condition hasn’t been fully met. The continue statement skips the rest of the code inside the\n"
              "loop for the current iteration and moves to the next one. The pass statement does nothing—it’s often used as a placeholder when you want to have a loop or condition\n"
              "syntactically but don’t want it to perform any action yet. Python provides two main types of loops: for loops and while loops.\n")
        proceed = input('\033[90m(Click Enter to Proceed)\033[0m\n')
        print("\033[1m\033[97m   1. The for Loop\033[0m\033[0m\n"
              "A for loop is used when you want to repeat something a specific number of times or go through a sequence such as a list, string, or range of numbers. The for loop\n"
              "is commonly used when you know beforehand how many times you want to repeat an action, such as iterating through a list, a string, or a range of numbers.\n"
              "For example, using for i in range(5): will execute the code inside the loop five times.\n")
        time.sleep(1)
        print("\033[1m\033[97m   Syntax\033[0m\033[0m\n"
             "      for \033[90mvariable\033[0m in \033[90msequence:\033[0m\n"
              "         \033[90m# code to repeat\033[0m\n")
        time.sleep(1)
        print("""\033[1m\033[97m   Example\033[0m\033[0m
      for i in range(5):
          print("Hello!")\n""")
        time.sleep(1)
        print("""\033[1m\033[97m   Example Output:\033[0m\033[0m
      Hello!
      Hello!
      Hello!
      Hello!
      Hello!\n""")
        proceed1 = input('\033[90m(Click Enter to Proceed)\033[0m\n')
        print("\033[1m\033[97m2. The while Loop\033[0m\033[0m\n"
              "the while loop is used when the number of repetitions is not fixed and depends on a condition. It keeps running as long as the condition remains true, and stops\n"
              "once it becomes false. For instance, a while loop can continue asking a user for input until they type a specific response. Python also provides special statements\n"
              "like break and continue to control the behavior of loops — break immediately stops the loop, while continue skips the current iteration and moves to the next one.\n")
        time.sleep(1)
        print("""\033[1m\033[97m   Syntax\033[0m\033[0m
      while \033[90mcondition:\033[0m
          \033[90m# code to repeat\033[0m\n""")
        time.sleep(1)
        print("""\033[1m\033[97m   Example:\033[0m\033[0m
      count = 1
      while count <= 5:
          print("Count:", count)
          count += 1\n""")
        time.sleep(1)
        print(f"""\033[1m\033[97m   Example Output:\033[0m\033[0m
      Count: 1
      Count: 2
      Count: 3
      Count: 4
      Count: 5

The loop continues running until count becomes greater than 5.\n""")
        proceed2 = input('\033[90m(Click Enter to Proceed)\033[0m\n')
        clear()
        time.sleep(1)
        print("""\033[91m 
 ██████████     █████████   ██████   █████   █████████  ██████████ ███████████   ███
░░███░░░░███   ███░░░░░███ ░░██████ ░░███   ███░░░░░███░░███░░░░░█░░███░░░░░███ ░███
 ░███   ░░███ ░███    ░███  ░███░███ ░███  ███     ░░░  ░███  █ ░  ░███    ░███ ░███
 ░███    ░███ ░███████████  ░███░░███░███ ░███          ░██████    ░██████████  ░███
 ░███    ░███ ░███░░░░░███  ░███ ░░██████ ░███    █████ ░███░░█    ░███░░░░░███ ░███
 ░███    ███  ░███    ░███  ░███  ░░█████ ░░███  ░░███  ░███ ░   █ ░███    ░███ ░░░ 
 ██████████   █████   █████ █████  ░░█████ ░░█████████  ██████████ █████   █████ ███
░░░░░░░░░░   ░░░░░   ░░░░░ ░░░░░    ░░░░░   ░░░░░░░░░  ░░░░░░░░░░ ░░░░░   ░░░░░ ░░░\033[0m\n""")
        time.sleep(1)
        enemy = random.choice(enemies)
        printer(f"\033[1m\033[91mA WILD {enemy.upper()} APPEARED!\033[0m\033[0m")
        time.sleep(1)
        printer(f"\033[1m\033[95m   {enemy}:\033[0m \033[91m\"{random.choice(intro_dialogues[enemy])}\"\033[0m ")
        time.sleep(1)
        printer(f"\033[91m\033[1m{enemy} asks you a question...\033[0m\033[0m")
        time.sleep(1.5)
        ans = input("\n\033[1m\033[97mWhich of the following keywords is used to create a loop that repeats when a condition is true?\033[0m\033[0m\n"
            "\n   A. for\n"
            "   B. loop\n"
            "   C. while\n"
            "   D. repeat\n"
            "\n> ")
        if ans.lower() == "c":
            print(f"\n\033[1m\033[92mThat is correct! {enemy} nods approvingly.\033[0m\033[0m")
            printer(f"\033[1m\033[95m   {enemy}:\033[0m\033[0m \033[92m\"{random.choice(correct_dialogues[enemy])}\"\033[0m\n")
            time.sleep(1.5)
            print(f"\033[1m\033[92m   Current HP: {hp}\033[0m\033[0m")
            print(f"\033[1m\033[93m   Current EXP: {exp}\033[0m\033[0m\n")
            proceed = input('\033[90m(Click Enter to Proceed)\033[0m\n')
            clear()
        else:
            hp -= 20
            print(f"\n\033[1m\033[91mThat is incorrect! {enemy} throws a chalk on you.\033[0m\033[0m")
            printer(f"\033[1m\033[95m   {enemy}:\033[0m\033[0m \033[91m\"{random.choice(wrong_dialogues[enemy])}\"\033[0m\n")
            time.sleep(1.5)
            print("\033[1m\033[91m   -20HP\033[0m\033[0m")
            time.sleep(1.5)
            if hp > 0:
                print(f"\n\033[1m\033[92m   Current HP: {hp}\033[0m\033[1m")
                print(f"\033[1m\033[93m   Current EXP: {exp}\033[0m\033[0m\n")
                proceed = input('\033[90m(Click Enter to Proceed)\033[0m \n')
                clear()
            else:
                print(f"\n\033[1m\033[92m   Current HP: {hp}\033[0m\033[0m")
                print(f"\033[1m\033[93m   Current EXP: {exp}\033[0m\033[0m\n")
                time.sleep(2)
                break
        ans2 = input("\n\033[1m\033[97mHow many times will the loop below execute?\n"
                     "for i in range(2, 10, 2):"
                     "    print(i)\033[0m\n"
                     "\n   A. 7 times\n"
                     "   B. 6 times\n"
                     "   C. 5 times\n"
                     "   D. 4 times\n"
                     "\n> ")
        if ans2.lower() == "c":
            print(f"\n\033[1m\033[92mThat is correct! {enemy} nods approvingly.\033[0m\033[0m")
            printer(f"\033[1m\033[95m   {enemy}:\033[0m\033[0m \033[92m\"{random.choice(correct_dialogues[enemy])}\"\033[0m\n")
            time.sleep(1.5)
            print(f"\033[1m\033[92m   Current HP: {hp}\033[0m\033[0m")
            print(f"\033[1m\033[93m   Current EXP: {exp}\033[0m\033[0m\n")
            proceed = input('\033[90m(Click Enter to Proceed)\033[0m\n')
            clear()
        else:
            hp -= 20
            print(f"\n\033[1m\033[91mThat is incorrect! {enemy} throws a chalk on you.\033[0m\033[0m")
            printer(f"\033[1m\033[95m   {enemy}:\033[0m\033[0m \033[91m\"{random.choice(wrong_dialogues[enemy])}\"\033[0m\n")
            time.sleep(1.5)
            print("\033[1m\033[91m  -20HP\033[0m\033[0m")
            time.sleep(1.5)
            if hp > 0:
                print(f"\n\033[1m\033[92m   Current HP: {hp}\033[0m\033[1m")
                print(f"\033[1m\033[93m   Current EXP: {exp}\033[0m\033[0m\n")
                proceed = input('\033[90m(Click Enter to Proceed)\033[0m \n')
                clear()
            else:
                print(f"\n\033[1m\033[92m   Current HP: {hp}\033[0m\033[0m")
                print(f"\033[1m\033[93m   Current EXP: {exp}\033[0m\033[0m\n")
                time.sleep(2)
                break
        ans3 = input("\n\033[1m\033[97mWhich statement is used to stop a loop early?\033[0m\033[0m\n"
            "\n   A. stop\n"
            "   B. end\n"
            "   C. exit\n"
            "   D. break\n"
            "\n> ")
        if ans3.lower() == "d":
            print(f"\n\033[1m\033[92mThat is correct! {enemy} nods approvingly.\033[0m\033[0m")
            printer(f"\033[1m\033[95m   {enemy}:\033[0m\033[0m \033[92m\"{random.choice(correct_dialogues[enemy])}\"\033[0m\n")
            time.sleep(1.5)
            print(f"\033[1m\033[92m   Current HP: {hp}\033[0m\033[0m")
            print(f"\033[1m\033[93m   Current EXP: {exp}\033[0m\033[0m\n")
            proceed = input('\033[90m(Click Enter to Proceed)\033[0m\n')
            clear()
        else:
            hp -= 20
            print(f"\n\033[1m\033[91mThat is incorrect! {enemy} throws a chalk on you.\033[0m\033[0m")
            printer(f"\033[1m\033[95m   {enemy}:\033[0m\033[0m \033[91m\"{random.choice(wrong_dialogues[enemy])}\"\033[0m\n")
            time.sleep(1.5)
            print("\033[1m\033[91m   -20HP\033[0m\033[0m")
            time.sleep(1.5)
            if hp > 0:
                print(f"\n\033[1m\033[92m   Current HP: {hp}\033[0m\033[1m")
                print(f"\033[1m\033[93m   Current EXP: {exp}\033[0m\033[0m\n")
                proceed = input('\033[90m(Click Enter to Proceed)\033[0m \n')
                clear()
            else:
                print(f"\n\033[1m\033[92m   Current HP: {hp}\033[0m\033[0m")
                print(f"\033[1m\033[93m   Current EXP: {exp}\033[0m\033[0m\n")
                time.sleep(2)
                break
        ans4 = input("\n\033[1m\033[97mWhat statement skips the rest of the loop and continues with the next iteration?\033[0m\033[0m\n"
                     "\n   A. end\n"
                     "   B. break\n"
                     "   C. pass\n"
                     "   D. continue\n"
                     "\n> ")
        if ans4.lower() == "d":
            print(f"\n\033[1m\033[92mThat is correct! {enemy} nods approvingly.\033[0m\033[0m")
            printer(f"\033[1m\033[95m   {enemy}:\033[0m\033[0m \033[92m\"{random.choice(correct_dialogues[enemy])}\"\033[0m\n")
            time.sleep(1.5)
            print(f"\033[1m\033[92m   Current HP: {hp}\033[0m\033[0m")
            print(f"\033[1m\033[93m   Current EXP: {exp}\033[0m\033[0m\n")
            proceed = input('\033[90m(Click Enter to Proceed)\033[0m\n')
            clear()
        else:
            hp -= 20
            print(f"\n\033[1m\033[91mThat is incorrect! {enemy} throws a chalk on you.\033[0m\033[0m")
            printer(f"\033[1m\033[95m   {enemy}:\033[0m\033[0m \033[91m\"{random.choice(wrong_dialogues[enemy])}\"\033[0m\n")
            time.sleep(1.5)
            print("\033[1m\033[91m   -20HP\033[0m\033[0m")
            time.sleep(1.5)
            if hp > 0:
                print(f"\n\033[1m\033[92m   Current HP: {hp}\033[0m\033[1m")
                print(f"\033[1m\033[93m   Current EXP: {exp}\033[0m\033[0m\n")
                proceed = input('\033[90m(Click Enter to Proceed)\033[0m \n')
                clear()
            else:
                print(f"\n\033[1m\033[92m   Current HP: {hp}\033[0m\033[0m")
                print(f"\033[1m\033[93m   Current EXP: {exp}\033[0m\033[0m\n")
                time.sleep(2)
                break
        ans5 = input("\n\033[1m\033[97mwhile loops can be used to simulate for loops.\033[0m\033[0m\n"
                     "\n   A. True\n"
                     "   B. False\n"
                     "   C. Maybe\n"
                     "   D. A and B\n"
                     "\n> ")
        if ans5.lower() == "a":
            print(f"\n\033[1m\033[92mThat is correct! {enemy} nods approvingly.\033[0m\033[0m")
            printer(f"\033[1m\033[95m   {enemy}:\033[0m\033[0m \033[92m\"{random.choice(correct_dialogues[enemy])}\"\033[0m\n")
            time.sleep(1.5)
            print(f"\033[1m\033[92m   Current HP: {hp}\033[0m\033[0m")
            print(f"\033[1m\033[93m   Current EXP: {exp}\033[0m\033[0m\n")
            proceed = input('\033[90m(Click Enter to Proceed)\033[0m\n')
            clear()
        else:
            hp -= 20
            print(f"\n\033[1m\033[91mThat is incorrect! {enemy} throws a chalk on you.\033[0m\033[0m")
            printer(f"\033[1m\033[95m   {enemy}:\033[0m\033[0m \033[91m\"{random.choice(wrong_dialogues[enemy])}\"\033[0m\n")
            time.sleep(1.5)
            print("\033[1m\033[91m   -20HP\033[0m\033[0m")
            time.sleep(1.5)
            if hp > 0:
                print(f"\n\033[1m\033[92m   Current HP: {hp}\033[0m\033[1m")
                print(f"\033[1m\033[93m   Current EXP: {exp}\033[0m\033[0m\n")
                proceed = input('\033[90m(Click Enter to Proceed)\033[0m \n')
                clear()
            else:
                print(f"\n\033[1m\033[92m   Current HP: {hp}\033[0m\033[0m")
                print(f"\033[1m\033[93m   Current EXP: {exp}\033[0m\033[0m\n")
                time.sleep(2)
                break

    elif choice == "11":
        clear()
        print("""\033[91m
▄▄▄█████▓ ██░ ██ ▓█████      ▄████  ██▀███   ▒█████   █    ██  ███▄    █ ▓█████▄    ▄▄▄█████▓ ██▀███  ▓█████  ███▄ ▄███▓ ▄▄▄▄    ██▓    ▓█████   ██████               
▓  ██▒ ▓▒▓██░ ██▒▓█   ▀     ██▒ ▀█▒▓██ ▒ ██▒▒██▒  ██▒ ██  ▓██▒ ██ ▀█   █ ▒██▀ ██▌   ▓  ██▒ ▓▒▓██ ▒ ██▒▓█   ▀ ▓██▒▀█▀ ██▒▓█████▄ ▓██▒    ▓█   ▀ ▒██    ▒               
▒ ▓██░ ▒░▒██▀▀██░▒███      ▒██░▄▄▄░▓██ ░▄█ ▒▒██░  ██▒▓██  ▒██░▓██  ▀█ ██▒░██   █▌   ▒ ▓██░ ▒░▓██ ░▄█ ▒▒███   ▓██    ▓██░▒██▒ ▄██▒██░    ▒███   ░ ▓██▄                 
░ ▓██▓ ░ ░▓█ ░██ ▒▓█  ▄    ░▓█  ██▓▒██▀▀█▄  ▒██   ██░▓▓█  ░██░▓██▒  ▐▌██▒░▓█▄   ▌   ░ ▓██▓ ░ ▒██▀▀█▄  ▒▓█  ▄ ▒██    ▒██ ▒██░█▀  ▒██░    ▒▓█  ▄   ▒   ██▒              
  ▒██▒ ░ ░▓█▒░██▓░▒████▒   ░▒▓███▀▒░██▓ ▒██▒░ ████▓▒░▒▒█████▓ ▒██░   ▓██░░▒████▓      ▒██▒ ░ ░██▓ ▒██▒░▒████▒▒██▒   ░██▒░▓█  ▀█▓░██████▒░▒████▒▒██████▒▒ ██▓  ██▓  ██▓
  ▒ ░░    ▒ ░░▒░▒░░ ▒░ ░    ░▒   ▒ ░ ▒▓ ░▒▓░░ ▒░▒░▒░ ░▒▓▒ ▒ ▒ ░ ▒░   ▒ ▒  ▒▒▓  ▒      ▒ ░░   ░ ▒▓ ░▒▓░░░ ▒░ ░░ ▒░   ░  ░░▒▓███▀▒░ ▒░▓  ░░░ ▒░ ░▒ ▒▓▒ ▒ ░ ▒▓▒  ▒▓▒  ▒▓▒
    ░     ▒ ░▒░ ░ ░ ░  ░     ░   ░   ░▒ ░ ▒░  ░ ▒ ▒░ ░░▒░ ░ ░ ░ ░░   ░ ▒░ ░ ▒  ▒        ░      ░▒ ░ ▒░ ░ ░  ░░  ░      ░▒░▒   ░ ░ ░ ▒  ░ ░ ░  ░░ ░▒  ░ ░ ░▒   ░▒   ░▒ 
  ░       ░  ░░ ░   ░      ░ ░   ░   ░░   ░ ░ ░ ░ ▒   ░░░ ░ ░    ░   ░ ░  ░ ░  ░      ░        ░░   ░    ░   ░      ░    ░    ░   ░ ░      ░   ░  ░  ░   ░    ░    ░  
          ░  ░  ░   ░  ░         ░    ░         ░ ░     ░              ░    ░                   ░        ░  ░       ░    ░          ░  ░   ░  ░      ░    ░    ░    ░ 
                                                                          ░                                                   ░                           ░    ░    ░\033[0m""")
        proceed0 = input('\033[90m(Click Enter to Proceed)\033[0m\n')
        clear()
        pygame.mixer.init()
        pygame.mixer.music.load(r"E:\Downloads\Song For Wemmbu  PLAYFUL MASSACRE.mp3")
        pygame.mixer.music.play(-1)
        time.sleep(.5)
        print("""\033[91m
 ██████████     █████████   ██████   █████   █████████  ██████████ ███████████   ███
░░███░░░░███   ███░░░░░███ ░░██████ ░░███   ███░░░░░███░░███░░░░░█░░███░░░░░███ ░███
 ░███   ░░███ ░███    ░███  ░███░███ ░███  ███     ░░░  ░███  █ ░  ░███    ░███ ░███
 ░███    ░███ ░███████████  ░███░░███░███ ░███          ░██████    ░██████████  ░███
 ░███    ░███ ░███░░░░░███  ░███ ░░██████ ░███    █████ ░███░░█    ░███░░░░░███ ░███
 ░███    ███  ░███    ░███  ░███  ░░█████ ░░███  ░░███  ░███ ░   █ ░███    ░███ ░░░ 
 ██████████   █████   █████ █████  ░░█████ ░░█████████  ██████████ █████   █████ ███
░░░░░░░░░░   ░░░░░   ░░░░░ ░░░░░    ░░░░░   ░░░░░░░░░  ░░░░░░░░░░ ░░░░░   ░░░░░ ░░░\033[0m\n""")
        time.sleep(.5)
        print(f"""\033[91m 
 ██████████     █████████   ██████   █████   █████████  ██████████ ███████████   ███
░░███░░░░███   ███░░░░░███ ░░██████ ░░███   ███░░░░░███░░███░░░░░█░░███░░░░░███ ░███
 ░███   ░░███ ░███    ░███  ░███░███ ░███  ███     ░░░  ░███  █ ░  ░███    ░███ ░███
 ░███    ░███ ░███████████  ░███░░███░███ ░███          ░██████    ░██████████  ░███
 ░███    ░███ ░███░░░░░███  ░███ ░░██████ ░███    █████ ░███░░█    ░███░░░░░███ ░███
 ░███    ███  ░███    ░███  ░███  ░░█████ ░░███  ░░███  ░███ ░   █ ░███    ░███ ░░░ 
 ██████████   █████   █████ █████  ░░█████ ░░█████████  ██████████ █████   █████ ███
░░░░░░░░░░   ░░░░░   ░░░░░ ░░░░░    ░░░░░   ░░░░░░░░░  ░░░░░░░░░░ ░░░░░   ░░░░░ ░░░\033[0m\n""")
        time.sleep(.4)
        print("""\033[91m 
░▒▓███████▓▒░ ░▒▓██████▓▒░░▒▓███████▓▒░ ░▒▓██████▓▒░░▒▓████████▓▒░▒▓███████▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒▒▓███▓▒░▒▓██████▓▒░ ░▒▓███████▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░       
░▒▓███████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓██████▓▒░░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░\033[0m\n""")
        proceed = input('\033[90m(Click Enter to Proceed)\033[0m\n')
        clear()
        print("""\033[91m
                                              ░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░ 
                                                 ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        
                                                 ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        
                                                 ░▒▓█▓▒░   ░▒▓████████▓▒░▒▓██████▓▒░   
                                                 ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        
                                                 ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        
                                                 ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░\033[0m""")
        time.sleep(.8)
        print("""\033[91m
 ░▒▓██████▓▒░ ░▒▓██████▓▒░▒▓████████▓▒░▒▓██████▓▒░ ░▒▓███████▓▒░▒▓████████▓▒░▒▓███████▓▒░ ░▒▓██████▓▒░░▒▓███████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░  ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░         ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        
░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░  ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░         ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        
░▒▓█▓▒░      ░▒▓████████▓▒░ ░▒▓█▓▒░  ░▒▓████████▓▒░░▒▓██████▓▒░   ░▒▓█▓▒░   ░▒▓███████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓███████▓▒░░▒▓████████▓▒░▒▓██████▓▒░   
░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░  ░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░  ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░  ░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░  ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        
 ░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░  ░▒▓█▓▒░░▒▓█▓▒░▒▓███████▓▒░   ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░░▒▓██████▓▒░░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░\033[0m""")
        time.sleep(.8)
        print("""\033[91m
                                                        ░▒▓██████▓▒░░▒▓████████▓▒░ 
                                                       ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        
                                                       ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        
                                                       ░▒▓█▓▒░░▒▓█▓▒░▒▓██████▓▒░   
                                                       ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        
                                                       ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        
                                                        ░▒▓██████▓▒░░▒▓█▓▒░\033[0m""")
        time.sleep(.8)
        print("""\033[91m
              ░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░░▒▓███████▓▒░▒▓████████▓▒░▒▓█▓▒░░▒▓██████▓▒░░▒▓███████▓▒░ ░▒▓███████▓▒░ 
             ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░         ░▒▓█▓▒░   ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        
             ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░         ░▒▓█▓▒░   ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        
             ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓██████▓▒░  ░▒▓██████▓▒░   ░▒▓█▓▒░   ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓██████▓▒░  
             ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░             ░▒▓█▓▒░  ░▒▓█▓▒░   ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░ 
             ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░             ░▒▓█▓▒░  ░▒▓█▓▒░   ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░ 
              ░▒▓██████▓▒░ ░▒▓██████▓▒░░▒▓████████▓▒░▒▓███████▓▒░   ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓███████▓▒░  
                ░▒▓█▓▒░                                                                                                      
                 ░▒▓██▓▒░\033[0m\n""")
        proceed2 = input('\033[90m(Click Enter to Proceed)\033[0m\n')
        clear()
        printer(f"""\033[1m\033[91mA distorted voice emerges through the void.\033[91m""")
        time.sleep(1)
        printer(f"""\033[1m\033[91mCatastrophe of Questions:\033[0m \033[91m\"{random.choice(spawn_lines)}\033[0m\n""")
        time.sleep(1)
        printer("\033[1m\033[92m  System:\033[0m \033[92mBrace yourself, brave Scholar. Each wrong answer will bring closer the Catastrophe’s triumph. May the God of Wisdom be on your side.\033[0m\n")
        proceed4 = input('\033[90m(Click Enter to Proceed)\033[0m\n')
        clear()
        ans = input("\n\033[1m\033[91mThe name Python comes from?\033[0m\033[0m\n"
                     "\n      A. An actual Python non-venomous constrictor snakes\n"
                     "      B. The ancient Greek oracle of Delphi, also known as Pythia\n"
                     "      C. A famous British comedy group called Monty Python\n"
                     "      D. A mythical serpent called Python that slain by the god Apollo\n"
                     "\n> ")
        if ans.lower() == "c":
            correct()
            proceed = input('\033[90m(Click Enter to Proceed)\033[0m\n')
            clear()
        else:
            wrong()
            proceed = input('\033[90m(Click Enter to Proceed)\033[0m\n')
            clear()
        if hp < 0:
            break
        ans2 = input("\n\033[1m\033[91mWho was the creator of Python?\033[0m\033[0m\n"
                    "\n      A. Bjarne Stroustrup\n"
                    "      B. Dennis Ritchie\n"
                    "      C. Guido van Rossum\n"
                    "      D. James Gosling\n"
                    "\n> ")
        if ans2.lower() == "c":
            correct()
            proceed = input('\033[90m(Click Enter to Proceed)\033[0m\n')
            clear()
        else:
            wrong()
            proceed = input('\033[90m(Click Enter to Proceed)\033[0m\n')
            clear()
        if hp < 0:
            break
        ans3 = input("\n\033[1m\033[91mWhat year was Python created?\033[0m\033[0m\n"
                    "\n      A. 1941\n"
                    "      B. 1961\n"
                    "      C. 1981\n"
                    "      D. 1991\n"
                     "\n> ")
        if ans3.lower() == "d":
            correct()
            proceed = input('\033[90m(Click Enter to Proceed)\033[0m\n')
            clear()
        else:
            wrong()
            proceed = input('\033[90m(Click Enter to Proceed)\033[0m\n')
            clear()
        if hp < 0:
            break
        ans4 = input("\n\033[1m\033[91mWhich of the following best describes a programming language?\033[0m\033[0m\n"
                     "\n      A. A universal human language\n"
                     "      B. A set of instructions humans write for computers to execute\n"
                     "      C. A type of compiler\n"
                     "      D. A type of software\n"
                     "\n> ")
        if ans4.lower() == "b":
            correct()
            proceed = input('\033[90m(Click Enter to Proceed)\033[0m\n')
            clear()
        else:
            wrong()
            proceed = input('\033[90m(Click Enter to Proceed)\033[0m\n')
            clear()
        if hp < 0:
            break
        ans5 = input("\n\033[1m\033[91mWhich function displays text on the screen in Python?\033[0m\033[0m\n"
                     "\n      A. display()\n"
                     "      B. print()\n"
                     "      C. output()\n"
                     "      D. show()\n"
                     "\n> ")
        if ans5.lower() == "b":
            correct()
            proceed = input('\033[90m(Click Enter to Proceed)\033[0m\n')
            clear()
        else:
            wrong()
            proceed = input('\033[90m(Click Enter to Proceed)\033[0m\n')
            clear()
        if hp < 0:
            break
        ans6 = input("\n\033[1m\033[91mWhat is the main purpose of the print() function in Python?\033[0m\033[0m\n"
                    "\n      A. To display output on the screen\n"
                    "      B. To take input from the user\n"
                    "      C. To store values in variables\n"
                    "      D. To stop the program\n"
                    "\n> ")
        if ans6.lower() == "a":
            correct()
            proceed = input('\033[90m(Click Enter to Proceed)\033[0m\n')
            clear()
        else:
            wrong()
            proceed = input('\033[90m(Click Enter to Proceed)\033[0m\n')
            clear()
        if hp < 0:
            break
        ans7 = input("\n\033[1m\033[91mWhat are comments mainly used for in Python code?\033[0m\033[0m\n"
                     "\n      A. To make the program run faster\n"
                     "      B. To explain or describe code\n"
                     "      C. To store user input\n"
                     "      D. To output text on the screen\n"
                     "\n> ")
        if ans7.lower() == "b":
            correct()
            proceed = input('\033[90m(Click Enter to Proceed)\033[0m\n')
            clear()
        else:
            wrong()
            proceed = input('\033[90m(Click Enter to Proceed)\033[0m\n')
            clear()
        if hp < 0:
            break
        ans8 = input("\n\033[1m\033[91mWhat symbol is used to write a single-line comment in Python?\033[0m\033[0m\n"
                    "\n      A. !\n"
                    "      B. *\n"
                    "      C. @\n"
                    "      D. #\n"
                    "\n> ")
        if ans8.lower() == "d":
            correct()
            proceed = input('\033[90m(Click Enter to Proceed)\033[0m\n')
            clear()
        else:
            wrong()
            proceed = input('\033[90m(Click Enter to Proceed)\033[0m\n')
            clear()
        if hp < 0:
            break
        ans9 = input("\n\033[1m\033[91mWhich of the following is the correct way of naming a variable?\033[0m\033[0m\n"
                     "\n      A. 1name\n"
                     "     B. _score\n"
                     "     C. total.volume\n"
                     "     D. #age\n"
                     "\n> ")
        if ans9.lower() == "b":
            correct()
            proceed = input('\033[90m(Click Enter to Proceed)\033[0m\n')
            clear()
        else:
            wrong()
            proceed = input('\033[90m(Click Enter to Proceed)\033[0m\n')
            clear()
        if hp < 0:
            break
        ans10 = input("\n\033[1m\033[91mWhich of the following stores text in Python?\033[0m\033[0m\n"
                     "\n    A. int\n"
                     "     B. bool\n"
                     "     C. str\n"
                     "     D. float\n"
                     "\n> ")
        if ans10.lower() == "c":
            correct()
            proceed = input('\033[90m(Click Enter to Proceed)\033[0m\n')
            clear()
        else:
            wrong()
            proceed = input('\033[90m(Click Enter to Proceed)\033[0m\n')
            clear()
        if hp < 0:
            break
        ans11 = input("\n\033[1m\033[91mWhat does the % operator do?\033[0m\033[0m\n"
                     "\n      A. Divides two numbers\n"
                     "      B. Returns the quotient of a division\n"
                     "      C. Converts a number to a percentage\n"
                     "      D. Finds the remainder of a division\n"
                     "\n> ")
        if ans11.lower() == "d":
            correct()
            proceed = input('\033[90m(Click Enter to Proceed)\033[0m\n')
            clear()
        else:
            wrong()
            proceed = input('\033[90m(Click Enter to Proceed)\033[0m\n')
            clear()
        if hp < 0:
            break
        ans12 = input("\n\033[1m\033[91mWhich of the following is not an arithmetic operator in Python\033[0m\033[0m\n"
                    "\n      A. **\n"
                    "      B. =\n"
                    "      C. //\n"
                    "      D. %\n"
                    "\n> ")
        if ans12.lower() == "b":
            correct()
            proceed = input('\033[90m(Click Enter to Proceed)\033[0m\n')
            clear()
        else:
            wrong()
            proceed = input('\033[90m(Click Enter to Proceed)\033[0m\n')
            clear()
        if hp < 0:
            break
        ans13 = input("\n\033[1m\033[91mWhat is the correct order of arithmetic operations in Python (precedence)?\033[0m\033[0m\n"
                    "\n      A. Subtraction/Addition → Division/Multiplication → Exponent → Parenthesis\n"
                    "      B. Parenthesis → Exponent → Multiplication/Division → Addition/Subtraction\n"
                    "      C. Parenthesis → Exponent → Addition/Subtraction → Multiplication/Division\n"
                    "      D. Multiplication → Division → Addition → Subtraction → Exponent → Parenthesis \n"
                    "\n> ")
        if ans13.lower() == "b":
            correct()
            proceed = input('\033[90m(Click Enter to Proceed)\033[0m\n')
            clear()
        else:
            wrong()
            proceed = input('\033[90m(Click Enter to Proceed)\033[0m\n')
            clear()
        if hp < 0:
            break
        ans14 = input("\n\033[1m\033[91mWhat is the main purpose of the input() function in Python?\033[0m\033[0m\n"
                    "\n      A. To perform calculations\n"
                    "      B. To display output on the screen\n"
                    "      C. To receive data from the user\n"
                    "      D. To initialize a variable\n"
                    "\n> ")
        if ans14.lower() == "c":
            correct()
            proceed = input('\033[90m(Click Enter to Proceed)\033[0m\n')
            clear()
        else:
            wrong()
            proceed = input('\033[90m(Click Enter to Proceed)\033[0m\n')
            clear()
        if hp < 0:
            break
        ans15 = input("\n\033[1m\033[91mBy default, what is the data type of the value returned by input()?\033[0m\033[0m\n"
                    "\n      A. float\n"
                    "      B. int\n"
                    "      C. bool\n"
                    "      D. str\n"
                    "\n> ")
        if ans15.lower() == "d":
            correct()
            proceed = input('\033[90m(Click Enter to Proceed)\033[0m\n')
            clear()
        else:
            wrong()
            proceed = input('\033[90m(Click Enter to Proceed)\033[0m\n')
            clear()
        if hp < 0:
            break
        ans16 = input("\n\033[1m\033[91mWhich of the following is the correct syntax for an f-string?\033[0m\033[0m\n"
                     "\n      A. f(\"Hello {name}\")\n"
                     "      B. f['Hello {name}']\n"
                     "      C. f\"Hello {name}\"\n"
                     "      D. f.(\"Hello {name}\")\n"
                     "\n> ")
        if ans16.lower() == "c":
            correct()
            proceed = input('\033[90m(Click Enter to Proceed)\033[0m\n')
            clear()
        else:
            wrong()
            proceed = input('\033[90m(Click Enter to Proceed)\033[0m\n')
            clear()
        if hp < 0:
            break
        ans17 = input("\n\033[1m\033[91mWhat does the “f” in f-string stand for?\033[0m\033[0m\n"
                    "\n      A. Function\n"
                    "      B. Format\n"
                    "      C. Flow\n"
                    "      D. For\n"
                    "\n> ")
        if ans17.lower() == "b":
            correct()
            proceed = input('\033[90m(Click Enter to Proceed)\033[0m\n')
            clear()
        else:
            wrong()
            proceed = input('\033[90m(Click Enter to Proceed)\033[0m\n')
            clear()
        if hp < 0:
            break
        ans18 = input("\n\033[1m\033[91mWhich of the following statements is true about Python indentation?\033[0m\033[0m\n"
                    "\n      A. It defines which code belongs to which block\n"
                    "      B. It’s only used for loops\n"
                    "      C. It’s optional\n"
                    "      D. It can be replaced with curly braces\n"
                    "\n> ")
        if ans18.lower() == "a":
            correct()
            proceed = input('\033[90m(Click Enter to Proceed)\033[0m\n')
            clear()
        else:
            wrong()
            proceed = input('\033[90m(Click Enter to Proceed)\033[0m\n')
            clear()
        if hp < 0:
            break
        ans19 = input("\n\033[1m\033[91mWhich keyword starts a conditional block?\033[0m\033[0m\n"
                    "\n      A. if\n"
                    "      B. in\n"
                    "      C. do\n"
                    "      D. while\n"
                    "\n> ")
        if ans19.lower() == "a":
            correct()
            proceed = input('\033[90m(Click Enter to Proceed)\033[0m\n')
            clear()
        else:
            wrong()
            proceed = input('\033[90m(Click Enter to Proceed)\033[0m\n')
            clear()
        if hp < 0:
            break
        ans20 = input("\n\033[1m\033[91mWhich of the following allows multiple condition checks?\033[0m\033[0m\n"
                    "\n      A. if\n"
                    "      B. elif\n"
                    "      C. else\n"
                    "      D. for\n"
                    "\n> ")
        if ans20.lower() == "b":
            correct()
            proceed = input('\033[90m(Click Enter to Proceed)\033[0m\n')
            clear()
        else:
            wrong()
            proceed = input('\033[90m(Click Enter to Proceed)\033[0m\n')
            clear()
        if hp < 0:
            break
        ans21 = input("\n\033[1m\033[91mWhich keyword starts a loop that repeats a fixed number of times?\033[0m\033[0m\n"
                    "\n      A. repeat\n"
                    "      B. while\n"
                    "      C. else\n"
                    "      D. for\n"
                    "\n> ")
        if ans21.lower() == "d":
            correct()
            proceed = input('\033[90m(Click Enter to Proceed)\033[0m\n')
            clear()
        else:
            wrong()
            proceed = input('\033[90m(Click Enter to Proceed)\033[0m\n')
            clear()
        if hp < 0:
            break
        ans22 = input("\n\033[1m\033[91mWhich of the following keywords is used to create a loop that repeats when a condition is true?\033[0m\033[0m\n"
                    "\n      A. for\n"
                    "      B. loop\n"
                    "      C. while\n"
                    "      D. repeat\n"
                    "\n> ")
        if ans22.lower() == "c":
            correct()
            proceed = input('\033[90m(Click Enter to Proceed)\033[0m\n')
            clear()
        else:
            wrong()
            proceed = input('\033[90m(Click Enter to Proceed)\033[0m\n')
            clear()
        if hp < 0:
            break
        ans23 = input("\n\033[1m\033[91mWhich statement is used to stop a loop early?\033[0m\033[0m\n"
                     "\n      A. stop\n"
                     "      B. end\n"
                     "      C. exit\n"
                     "      D. break\n"
                     "\n> ")
        if ans23.lower() == "d":
            correct()
            proceed = input('\033[90m(Click Enter to Proceed)\033[0m\n')
            clear()
        else:
            wrong()
            proceed = input('\033[90m(Click Enter to Proceed)\033[0m\n')
            clear()
        if hp < 0:
            break
        ans24 = input("\n\033[1m\033[91mWhat statement skips the rest of the loop and continues with the next iteration?\033[0m\033[0m\n"
                    "\n      A. end\n"
                    "      B. break\n"
                    "      C. continue\n"
                    "      D. pass\n"
                    "\n> ")
        if ans24.lower() == "c":
            correct()
            proceed = input('\033[90m(Click Enter to Proceed)\033[0m\n')
            clear()
        else:
            wrong()
            proceed = input('\033[90m(Click Enter to Proceed)\033[0m\n')
            clear()
        if hp < 0:
            break

        if seal > 0:
            printer("\033[1m\033[92m   The void trembles as the Catastrophe staggers, barely holding form...\033[0m\n")
            time.sleep(1)
            printer("\033[1m\033[91mHis voice screeches:\033[0m")
            time.sleep(1.5)
            print("""\033[91m
 ██▓    █     █░ ▄▄▄        ██████    ▓█████▄ ▓█████   █████▒▓█████ ▄▄▄     ▄▄▄█████▓▓█████ ▓█████▄            ▄▒▓██▓▄
▓██▒   ▓█░ █ ░█░▒████▄    ▒██    ▒    ▒██▀ ██▌▓█   ▀ ▓██   ▒ ▓█   ▀▒████▄   ▓  ██▒ ▓▒▓█   ▀ ▒██▀ ██▌          ▓▒░  ▐█▓▒
▒██▒   ▒█░ █ ░█ ▒██  ▀█▄  ░ ▓██▄      ░██   █▌▒███   ▒████ ░ ▒███  ▒██  ▀█▄ ▒ ▓██░ ▒░▒███   ░██   █▌             ░▓█▓▀
░██░   ░█░ █ ░█ ░██▄▄▄▄██   ▒   ██▒   ░▓█▄   ▌▒▓█  ▄ ░▓█▒  ░ ▒▓█  ▄░██▄▄▄▄██░ ▓██▓ ░ ▒▓█  ▄ ░▓█▄   ▌            ▓█▒░
░██░   ░░██▒██▓  ▓█   ▓██▒▒██████▒▒   ░▒████▓ ░▒████▒░▒█░    ░▒████▒▓█   ▓██▒ ▒██▒ ░ ░▒████▒░▒████▓  ██▓  ██▓  ▒▄▄▒ 
░▓     ░ ▓░▒ ▒   ▒▒   ▓▒█░▒ ▒▓▒ ▒ ░    ▒▒▓  ▒ ░░ ▒░ ░ ▒ ░    ░░ ▒░ ░▒▒   ▓▒█░ ▒ ░░   ░░ ▒░ ░ ▒▒▓  ▒  ▒▓▒  ▒▓▒  ░▀▀▒
 ▒ ░     ▒ ░ ░    ▒   ▒▒ ░░ ░▒  ░ ░    ░ ▒  ▒  ░ ░  ░ ░       ░ ░  ░ ▒   ▒▒ ░   ░     ░ ░  ░ ░ ▒  ▒  ░▒   ░▒   ░  ░
 ▒ ░     ░   ░    ░   ▒   ░  ░  ░      ░ ░  ░    ░    ░ ░       ░    ░   ▒    ░         ░    ░ ░  ░  ░    ░       ░
 ░         ░          ░  ░      ░        ░       ░  ░           ░  ░     ░  ░           ░  ░   ░      ░    ░   ░   
                                       ░                                                     ░        ░    ░\033[0m""", end="")
            time.sleep(2)
            print("""\033[91m
 ██▓ ███▄ ▄███▓ ██▓███   ▒█████    ██████   ██████  ██▓ ▄▄▄▄    ██▓    ▓█████  ▐██▌
▓██▒▓██▒▀█▀ ██▒▓██░  ██▒▒██▒  ██▒▒██    ▒ ▒██    ▒ ▓██▒▓█████▄ ▓██▒    ▓█   ▀  ▐██▌
▒██▒▓██    ▓██░▓██░ ██▓▒▒██░  ██▒░ ▓██▄   ░ ▓██▄   ▒██▒▒██▒ ▄██▒██░    ▒███    ▐██▌
░██░▒██    ▒██ ▒██▄█▓▒ ▒▒██   ██░  ▒   ██▒  ▒   ██▒░██░▒██░█▀  ▒██░    ▒▓█  ▄  ▓██▒
░██░▒██▒   ░██▒▒██▒ ░  ░░ ████▓▒░▒██████▒▒▒██████▒▒░██░░▓█  ▀█▓░██████▒░▒████▒ ▒▄▄ 
░▓  ░ ▒░   ░  ░▒▓▒░ ░  ░░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░▒ ▒▓▒ ▒ ░░▓  ░▒▓███▀▒░ ▒░▓  ░░░ ▒░ ░ ░▀▀▒
 ▒ ░░  ░      ░░▒ ░       ░ ▒ ▒░ ░ ░▒  ░ ░░ ░▒  ░ ░ ▒ ░▒░▒   ░ ░ ░ ▒  ░ ░ ░  ░ ░  ░
 ▒ ░░      ░   ░░       ░ ░ ░ ▒  ░  ░  ░  ░  ░  ░   ▒ ░ ░    ░   ░ ░      ░       ░
 ░         ░                ░ ░        ░        ░   ░   ░          ░  ░   ░  ░ ░   
                                                             ░\033[0m\n""")
            time.sleep(1.5)
            printer("\n\033[1m\033[92mBut you gazed down upon him as you hover from the air.\033[0m")
            time.sleep(1)
            printer("\033[1m\033[92mYou gained\033[0m \033[1m\033[93m100 EXP\033[0m \033[1m\033[92mand transcended beyond mortal understanding. Energy surges within you...\033[0m")
            time.sleep(1)
            printer("\033[1m\033[92mYou feel limitless power flowing through your veins...\033[0m")
            time.sleep(1)
            printer("\033[1m\033[92mThree powers awaken in your hands — which will you choose?\033[0m")
            time.sleep(1)
            print("""
            1.  \033[1m\033[95mHollow Purple\033[0m
      
            2.  \033[1m\033[91mWorld-Cutting Slash\033[0m
            
            3.  \033[1m\033[97mMahoraga\033[0m
            """)

            power = input("\033[1m\033[92mChoose your final technique: \033[0m").strip()

            if power == "1":
                clear()
                printer("\n\033[1m\033[92mYou raise your hand. Space folds and light bends around you.\033[0m")
                time.sleep(1)
                printer("\033[1m\033[92mYour voice falls into a whisper...\033[0m")
                time.sleep(2)
                print("""\033[1m\033[96m
            ╔═════════════════════════════════════════════════════════════════════════════════════╗
            ║   Nine ropes. Polarized light. Crow and Declaration. The gap within and without.    ║
            ╚═════════════════════════════════════════════════════════════════════════════════════╝\n""")
                proceed = input('\033[90m(Click Enter to Proceed)\033[0m\n')
                time.sleep(2)
                print("""\033[95m
 █████   █████    ███████    █████       █████          ███████    █████   ███   █████
░░███   ░░███   ███░░░░░███ ░░███       ░░███         ███░░░░░███ ░░███   ░███  ░░███ 
 ░███    ░███  ███     ░░███ ░███        ░███        ███     ░░███ ░███   ░███   ░███ 
 ░███████████ ░███      ░███ ░███        ░███       ░███      ░███ ░███   ░███   ░███ 
 ░███░░░░░███ ░███      ░███ ░███        ░███       ░███      ░███ ░░███  █████  ███  
 ░███    ░███ ░░███     ███  ░███      █ ░███      █░░███     ███   ░░░█████░█████░   
 █████   █████ ░░░███████░   ███████████ ███████████ ░░░███████░      ░░███ ░░███     
░░░░░   ░░░░░    ░░░░░░░    ░░░░░░░░░░░ ░░░░░░░░░░░    ░░░░░░░         ░░░   ░░░\033[0m""")
                time.sleep(1.5)
                print("""\033[95m
░▒▓███████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓███████▓▒░░▒▓███████▓▒░░▒▓█▓▒░      ░▒▓████████▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░        
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░        
░▒▓███████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓███████▓▒░░▒▓███████▓▒░░▒▓█▓▒░      ░▒▓██████▓▒░   
░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░        
░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░        
░▒▓█▓▒░       ░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓████████▓▒░▒▓████████▓▒░\033[0m\n""")
                time.sleep(2)
                printer("\n\033[1m\033[92mA hue of purple sphere and pure annihilation tears through the Catastrophe, erasing it completely.\033[0m")
            elif power == "2":
                clear()
                printer("\n\033[1m\033[92mYou bring your hands together, palms hovering apart. Your hands shifts two fingers raised, the others pressed downward.\033[0m")
                time.sleep(1)
                printer("\033[1m\033[92mYour voice falls into a whisper...\033[0m")
                time.sleep(2)
                print("""\033[1m\033[96m
            ╔══════════════════════════════════════════════════════╗
            ║   Dragon Scales. Repulsion. Paired Falling Stars.    ║
            ╚══════════════════════════════════════════════════════╝\n""")
                proceed = input('\033[90m(Click Enter to Proceed)\033[0m\n')
                time.sleep(1)
                print("""\033[1m\033[91m
 █████   ███   █████    ███████    ███████████   █████       ██████████        █████████  █████  █████ ███████████ ███████████ █████ ██████   █████   █████████ 
░░███   ░███  ░░███   ███░░░░░███ ░░███░░░░░███ ░░███       ░░███░░░░███      ███░░░░░███░░███  ░░███ ░█░░░███░░░█░█░░░███░░░█░░███ ░░██████ ░░███   ███░░░░░███
 ░███   ░███   ░███  ███     ░░███ ░███    ░███  ░███        ░███   ░░███    ███     ░░░  ░███   ░███ ░   ░███  ░ ░   ░███  ░  ░███  ░███░███ ░███  ███     ░░░ 
 ░███   ░███   ░███ ░███      ░███ ░██████████   ░███        ░███    ░███   ░███          ░███   ░███     ░███        ░███     ░███  ░███░░███░███ ░███         
 ░░███  █████  ███  ░███      ░███ ░███░░░░░███  ░███        ░███    ░███   ░███          ░███   ░███     ░███        ░███     ░███  ░███ ░░██████ ░███    █████
  ░░░█████░█████░   ░░███     ███  ░███    ░███  ░███      █ ░███    ███    ░░███     ███ ░███   ░███     ░███        ░███     ░███  ░███  ░░█████ ░░███  ░░███ 
    ░░███ ░░███      ░░░███████░   █████   █████ ███████████ ██████████      ░░█████████  ░░████████      █████       █████    █████ █████  ░░█████ ░░█████████ 
     ░░░   ░░░         ░░░░░░░    ░░░░░   ░░░░░ ░░░░░░░░░░░ ░░░░░░░░░░        ░░░░░░░░░    ░░░░░░░░      ░░░░░       ░░░░░    ░░░░░ ░░░░░    ░░░░░   ░░░░░░░░░\033[0m\n""")
                time.sleep(1.5)
                print("""\033[91m
 ░▒▓███████▓▒░▒▓█▓▒░       ░▒▓██████▓▒░ ░▒▓███████▓▒░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ 
 ░▒▓██████▓▒░░▒▓█▓▒░      ░▒▓████████▓▒░░▒▓██████▓▒░░▒▓████████▓▒░ 
       ░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
       ░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓███████▓▒░░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓███████▓▒░░▒▓█▓▒░░▒▓█▓▒░\033[0m\n""")
                time.sleep(2)
                printer("\n\033[92mReality itself splits — and the Catastrophe is cut in half, vanishing into light.\033[0m")
            elif power == "3":
                clear()
                printer("\n\033[1m\033[92mYour left hand curled into a fist. Your right hand then clasped over it. A grip of coercion, forcing a power to obey.\033[0m")
                time.sleep(1)
                printer("\033[1m\033[92mYour voice falls into a whisper...\033[0m")
                time.sleep(2)
                print("""\033[1m\033[96m
            ╔══════════════════════════════════════════════════════════════════════════════════════╗
            ║   With this treasure... I summon. Eight Grip Sword Divergent Sila Divine General.    ║
            ╚══════════════════════════════════════════════════════════════════════════════════════╝\n""")
                proceed = input('\033[90m(Click Enter to Proceed)\033[0m\n')
                time.sleep(1)
                print("""\033[97m
░▒▓██████████████▓▒░ ░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓██████▓▒░░▒▓███████▓▒░ ░▒▓██████▓▒░ ░▒▓██████▓▒░ ░▒▓██████▓▒░  
░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓███████▓▒░░▒▓████████▓▒░▒▓█▓▒▒▓███▓▒░▒▓████████▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░\033[0m\n""")
                time.sleep(2)
                printer("\033[1m\033[92mA being materialized from the shadow. A giant, eight-spoked wheel hung above its head.\033[0m")
                printer("\033[1m\033[92mIt slashed its blade sidewards and the Catastrophe vanished in a thousand pieces.\033[0m")
            else:
                printer("\n\033[1m\033[92mYou hesitate... The Catastrophe howls in fury — but your sheer will vaporizes him anyway.\033[0m")
                time.sleep(1)
                printer("\033[1m\033[92mQuite anti climactic if you ask me. Anyway... The world is saved? I suppose.\033[0m")

            proceed1 = input('\n\033[90m(Click Enter to Proceed)\033[0m\n')
            clear()
            print("""\033[92m
 █████ █████                        █████   ███   █████  ███             ███
░░███ ░░███                        ░░███   ░███  ░░███  ░░░             ░███
 ░░███ ███    ██████  █████ ████    ░███   ░███   ░███  ████  ████████  ░███
  ░░█████    ███░░███░░███ ░███     ░███   ░███   ░███ ░░███ ░░███░░███ ░███
   ░░███    ░███ ░███ ░███ ░███     ░░███  █████  ███   ░███  ░███ ░███ ░███
    ░███    ░███ ░███ ░███ ░███      ░░░█████░█████░    ░███  ░███ ░███ ░░░ 
    █████   ░░██████  ░░████████       ░░███ ░░███      █████ ████ █████ ███
   ░░░░░     ░░░░░░    ░░░░░░░░         ░░░   ░░░      ░░░░░ ░░░░ ░░░░░ ░░░\033[0m""")
            break

    elif choice == "12":
        if exp < 100:
            clear()
            print("""\033[91m
 █████ █████                        █████                                 ███
░░███ ░░███                        ░░███                                 ░███
 ░░███ ███    ██████  █████ ████    ░███         ██████   ██████  ██████ ░███
  ░░█████    ███░░███░░███ ░███     ░███        ███░░███ ███░░   ███░░███░███
   ░░███    ░███ ░███ ░███ ░███     ░███       ░███ ░███░░█████ ░███████ ░███
    ░███    ░███ ░███ ░███ ░███     ░███      █░███ ░███ ░░░░███░███░░░  ░░░ 
    █████   ░░██████  ░░████████    ███████████░░██████  ██████ ░░██████  ███
   ░░░░░     ░░░░░░    ░░░░░░░░    ░░░░░░░░░░░  ░░░░░░  ░░░░░░   ░░░░░░  ░░░\033[0m""")
            break
        else:
            clear()
            print("""\033[92m
 █████ █████                        █████   ███   █████  ███             ███
░░███ ░░███                        ░░███   ░███  ░░███  ░░░             ░███
 ░░███ ███    ██████  █████ ████    ░███   ░███   ░███  ████  ████████  ░███
  ░░█████    ███░░███░░███ ░███     ░███   ░███   ░███ ░░███ ░░███░░███ ░███
   ░░███    ░███ ░███ ░███ ░███     ░░███  █████  ███   ░███  ░███ ░███ ░███
    ░███    ░███ ░███ ░███ ░███      ░░░█████░█████░    ░███  ░███ ░███ ░░░ 
    █████   ░░██████  ░░████████       ░░███ ░░███      █████ ████ █████ ███
   ░░░░░     ░░░░░░    ░░░░░░░░         ░░░   ░░░      ░░░░░ ░░░░ ░░░░░ ░░░\033[0m""")
            break

    else:
        clear()
        print("""\033[91m
▓█████  ██▀███   ██▀███   ▒█████   ██▀███         ██▓ ███▄    █ ██▒   █▓ ▄▄▄       ██▓     ██▓▓█████▄         ██████▓██   ██▓ ███▄    █ ▄███████▓ ▄▄▄      ▒██   ██▒
▓█   ▀ ▓██ ▒ ██▒▓██ ▒ ██▒▒██▒  ██▒▓██ ▒ ██▒      ▓██▒ ██ ▀█   █▓██░  ██▒▒████▄    ▓██▒    ▓██▒▒██▀ ██▌      ▒██    ▒ ▒██  ██▒ ██ ▀█  ██ ▓  ██▒ ▓▒▒████▄    ▒▒██ ██▒░
▒███   ▓██ ░▄█ ▒▓██ ░▄█ ▒▒██░  ██▒▓██ ░▄█ ▒      ▒██▒▓██  ▀█ ██▒▓██  ██▒▒██  ▀█▄  ▒██░    ▒██▒░██   █▌      ░ ▓██▄    ▒██ ██░▓██  ▀█ ██▒▒ ▓██░ ▒░▒██  ▀█▄  ░░  ██  ░
▒▓█  ▄ ▒██▀▀█▄  ▒██▀▀█▄  ▒██   ██░▒██▀▀█▄        ░██░▓██▒  ▐▌██▒ ▒██ ██░░██▄▄▄▄██ ▒██░    ░██░░▓█▄  █▌        ▒   ██▒ ░ ▐██▓░▓██▒  ▐▌██▒░ ▓██▓ ░ ░██▄▄▄▄██  ░██ ██▒ 
░▒████▒░██▓ ▒██▒░██▓ ▒██▒░ ████▓▒░░██▓ ▒██▒      ░██░▒██░   ▓██░  ▒▀██░  ▓█   ▓██▒░██████▒░██░░▒████▓       ▒██████▒▒ ░ ██▒▓░▒██░   ▓██░  ▒██▒ ░  ▓█   ▓██▒▒██▒ ▒██▒
░░ ▒░ ░░ ▒▓ ░▒▓░░ ▒▓ ░▒▓░░ ▒░▒░▒░ ░ ▒▓ ░▒▓░      ░▓  ░ ▒░   ▒ ▒   ░ ▐░   ▒▒   ▓▒█░░ ▒░▓  ░░▓   ▒▒▓  ▒       ▒ ▒▓▒ ▒ ░  ██▒▒▒ ░ ▒░   ▒ ▒   ▒ ░░    ▒▒   ▓▒█░▒▒ ░ ░▓ ░
 ░ ░  ░  ░▒ ░ ▒░  ░▒ ░ ▒░  ░ ▒ ▒░   ░▒ ░ ▒░       ▒ ░░ ░░   ░ ▒░  ░ ░░    ▒   ▒▒ ░░ ░ ▒  ░ ▒ ░ ░ ▒  ▒       ░ ░▒  ░ ░▓██ ░▒░ ░ ░░   ░ ▒░    ░      ▒   ▒▒ ░░░   ░▒ ░
   ░     ░░   ░   ░░   ░ ░ ░ ░ ▒    ░░   ░        ▒ ░   ░   ░ ░     ░░    ░   ▒     ░ ░    ▒ ░ ░ ░  ░       ░  ░  ░  ▒ ▒ ░░     ░   ░ ░   ░        ░   ▒    ░    ░  
   ░  ░   ░        ░         ░ ░     ░            ░           ░      ░        ░  ░    ░  ░ ░     ░                ░  ░ ░              ░                ░  ░ ░    ░  
                                                                    ░                          ░                     ░ ░\033[0m\n""")
        break

if hp <= 0:
    clear()
    print("""\033[91m
                                                             ░  ░       ░      ░  ░     ░    ░ ░        ░     ░  ░   ░         ░       ░   ░  ░
                                                        ░ ░   ░   ░   ▒   ░      ░      ░      ░     ░ ░ ░ ▒       ░░     ░     ░░   ░      ░  ░  ░  ▒
                                                      ░     ░   ░▒   ▒   ▒  ░░ ▒░   ░  ░░░ ▒░ ░  ░  ░ ▒░  ▒░    ░ ▐░   ▒░  ░░ ▒  ▓ ░▒▓░    ░   ▒   ░   ░
                                                        ▒  ░    ▒ ▒  ▓▒ ░   ░   ▓▒░░ ▒░   ░  ░░░   ░ ▒  ░▒░    ░ ▐░  ░░ ▒░ ░░  ▒ ░▒ ░    ░   ▒    ░   ▒░   ░
                                                    ░   ░   ▒  ▄███▄  ▄▄▄   ▒░  ███▄ ▄███▓▓█████  ▒  ░  ▒█████   ██▒   █▓▓█████  ██▀██▄      ▐██▌ ░  ▒   ░
                                                     ░  ░ ▒   ██▒ ▀█▒▒████▄ ░  ▓██▒▀█▀ ██▒▓█   ▀ ░  ▒  ▒██▒  ██▒▓██░   █▒▓█   ▀ ▓██ ▒ ██▒    ▐██▌ ▓ ░   ░
                                                     ░ ▒   ░ ▒██░▄▄▄░▒██  ▀█▄  ▓██    ▓██░▒███  ▒   ░  ▒██░  ██▒ ▓██  █▒░▒███   ▓██ ░▄█ ▒    ▐██▌░ ░  ░  ░ 
                                                   ░  ░  ░   ░▓█  ██▓░██▄▄▄▄██ ▒██    ▒██ ▒▓█  ▄   ░▒  ▒██   ██░  ▒██ █░░▒▓█  ▄ ▒██▀▀█▄      ▓██▒ ░   ▒   ░ 
                                                     ░ ░  ░  ░▒▓███▀▒ ▓█   ▓██▒▒██▒   ░██▒░▒████▒  ░   ░ ████▓▒░   ▒▀█░  ░▒████▒░██▓ ▒██▒    ▒▄▄ ░ ▒     ░ 
                                                     ░ ▒  ░  ░▒   ▒  ▒▒   ▓▒ ░░ ▒░   ░  ░░░ ▒░ ░      ░ ▒░▒░▒░    ░ ▐░  ░░ ▒░ ░░ ▒▓ ░▒ ░ ▒░  ░▀▀▒ ░ ░  ░  
                                                        ░  ░     ░   ░   ▒   ▒▒ ░░  ░     ░ ░ ▒  ░     ▒  ░ ▒ ▒░    ░ ░░   ░ ░  ░  ░▒ ░ ▒░    ░  ░   ░   ▒░
                                                      ░   ░   ░   ▒   ░      ░      ░  ░ ░   ░ ░ ░ ▒    ▒  ░░     ░     ░▒   ░        ░░   ░    ░ ░ ▒
                                                          ░       ░  ░       ░      ░  ░         ░ ░        ░     ░  ░   ░         ░   ░      ░   ░
                                                                                                             ░                           














                                                                \033[0m""")
