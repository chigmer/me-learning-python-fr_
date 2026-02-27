import random
"""You're free to use this script if you feel like insulting people.. or yourself'"""
INSULTS = [
    "You're the human equivalent of a terms and conditions agreement ignored by everyone and full of fine print excuses.",
    "You have the energy of a dying laptop fan.",
    "Somewhere, a village is missing its mediocre person.",
    "You're not the sharpest tool in the shed. You're also not in the shed.",
    "Your personality has the depth of a parking lot puddle.",
    "You bring everyone so much joy when you leave the room.",
    "You're like a software update — nobody wants you, but you show up anyway.",
    "The strongest thing about you is your Wi-Fi password.",
    "You're proof that evolution has a sense of humor.",
    "You have the charisma of a damp paper bag.",
    "I've seen more spine in a jellyfish documentary.",
    "You're the biological equivalent of a placeholder.",
    "Your greatest achievement is being consistently forgettable.",
    "You have the decision-making skills of a Magic 8-Ball left in the sun.",
    "You're like decaf coffee — all the inconvenience, none of the payoff.",
    "Your face has a 'terms subject to change without notice' energy.",
    "You're the reason instruction manuals exist.",
    "If mediocrity were currency, you'd still somehow be in debt.",    "You have the ambition of a houseplant and the output to match.",
    "You're like a footnote in someone else's story.",
    "You have the self-awareness of a brick wall, but the brick wall is load-bearing.",
    "You're the human equivalent of a buffer loading screen.",
    "Your potential called — it's given up and moved on.",
    "You're like a participation trophy that somehow got worse over time.",
    "You have the conversational range of an out-of-office reply.",
    "Your presence is the social equivalent of Comic Sans.",
    "You're what happens when a bad idea refuses to die.",
    "You have all the spark of a wet match in a windstorm.",
    "You're like an umbrella with holes — technically there, functionally useless.",
    "You have the originality of a copy machine running low on toner.",
    "Your critical thinking is best described as 'decorative'.",
    "You're the expired coupon of human beings.",
    "You have the follow-through of a New Year's resolution.",
    "You're like elevator music — inoffensive only because everyone's ignoring you.",
    "Your best quality is being a cautionary tale.",
    "You have the staying power of a sand castle at high tide.",
    "You're the kind of person who brings store-bought to a potluck and still messes it up.",
    "You have all the charm of a Terms of Service update.",
    "You're like a broken clock — not even right twice a day.",
    "Your LinkedIn recommendations read like a hostage situation.",
    "You have the resilience of a wet napkin.",
    "You're like an FAQ page that answers none of the actual questions.",
    "Your ideas arrive late, underdressed, and leave nothing behind.",
    "You have the tact of an autocorrect feature with a grudge.",
    "You're the human equivalent of a 'Page Not Found' error.",
    "Your confidence is impressively disconnected from your ability.",
    "You're like a smoke alarm without batteries — present, but useless when it matters.",
    "You have the intellectual footprint of a rounding error.",
    "You're what a missed opportunity looks like from the inside.",
    "You're the sort of person who peaks during the introduction.",
]

def get_insult():
    return random.choice(INSULTS)

if __name__ == "__main__":
    print("just type nothing to leave. or not. try me.")
    while True:
        user = input(">")
        if not user.strip():
            break
        print(get_insult())
   
