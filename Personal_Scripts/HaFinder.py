#hahaha finder
#testing regex knowledge

import re
#hardcoded test input.


def get_Ha(text:str) -> list:
    pattern = re.compile(r"(?:Ha|ha)+")
    #(?:...)returns entire match
    
    return pattern.findall(text)  
    
    #making sure it doesnt break with  no input or text that has no humor
    
if __name__ == "__main__":
    raw_text = """Read it or don't; the procrastination gods prefer suspense. Hahahahahahahaha.

Procrastination is not just a habit; it’s a lifestyle choice wrapped in plausible deniability and sold with a free packet of excuses. You plan to do the thing. You schedule the thing. You ceremonially open the thing’s file and then immediately close it because the lighting in the room is wrong. Ha. You research whether succulents dream. Ha. You decide to “just check one video” and emerge three hours later smelling like regret and cheap chips. Hahahahahahahaha.

There’s a cynical efficiency to it, if you squint: deadlines compress time and convert chaos into action. In a pressure cooker, people write essays, patch code, and perform miracles they swore they were incapable of at 2 p.m. on a Tuesday. Hahaha. Of course, that miracle usually comes with shaky citations, an awkwardly contrived conclusion, and the faint whiff of “I did this in an adrenaline blur,” but it’s done. Hahahaha. That’s the economy of last-minute excellence: expensive emotionally, cheap in minutes.

Socially, procrastination is theater. Group projects are a morality play where three archetypes appear: the Doer (bless them), the Heroic Latecomer (says “I’ll pull an all-nighter”), and the Denialists (texting the group memes). Ha. You’ll get messages like “Almost done!” sent at 11:58 p.m., which translates to “I have discovered the art of illusion.” Hahahahaha. There’s camaraderie in shared panic; misery loves company and so does the three-speaker speakerphone of excuses. Ha ha ha.

Why do we do it? It’s rarely pure laziness. It’s fear dressed in casual clothes — fear of starting, fear of failing, fear that the first sentence will be irredeemably bad. Hahahaha. So instead of confronting the project you exist in a loop of planning to plan. You reorganize folders by year. You read an article titled “How to Start” and decide you’re now qualified to start later. Hahaha. That’s emotional hedging: pretend preparation to avoid actual risk.

Fixes? Tiny, ugly, practical things. Timers. Micro-goals. Remove the distractions that turn your attention into Swiss cheese. Break tasks into pieces so small that even a sleepy raccoon could finish one. Ha. Apply rewards that aren’t junk-food-level pathetic: a five-minute walk, a chapter of a good book, permission to breathe. Hahahaha. Also — and this is important — stop moralizing over procrastination. Shaming yourself until midnight doesn’t write paragraphs; it just makes the midnight snacks more desperate. Ha.

In conclusion (yes, the finale you definitely scribbled at the last second in your head), procrastination is both liar and truth-teller. It lies by pretending you’ll perform better if you wait. It tells the truth by revealing what you actually value when time dwindles. Learn the pattern. Build scaffolding. And if all else fails, at least make the panic entertaining. Hahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahaha."""
    print(get_Ha(raw_text))
    