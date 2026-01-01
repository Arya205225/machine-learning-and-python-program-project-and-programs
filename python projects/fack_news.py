import random

subject = [
    "Shah Rukh Khan",
    "virat Kohli",
    "nirmeala sitharaman",
    "Narendra Modi",
    "Rahul Gandhi",
    "Sonia Gandhi",
    "Amit Shah",
    "Yogi Adityanath",
    "Arvind Kejriwal",
    "Smriti Irani",
    "Piyush Goyal",
    "Rajnath Singh",
]

action = [ 
    "is the best",
    "is the worst",
    "is a great leader",
    "is a bad leader",
    "is a honest person",
    "is a corrupt person",
    "is a genius",
    "is an idiot",
    "is a hero",
    "is a villain",
    "is a role model",
    "is a disgrace",
    "is a patriot",
    "is a traitor",
    "eat",
]

place_or_thing = [
    "India",
    "Pakistan",
    "China",
    "USA",
    "UK",
    "Russia",
    "Australia",
    "Canada",
    "Germany",
    "France",
    "Italy",
    "Japan",
    "South Korea",
    "Brazil",
]

while True:
    subject_choice = random.choice(subject)
    action_choice = random.choice(action)
    place_choice = random.choice(place_or_thing)
    
    headline = f"BREAKING NEWS: {subject_choice} {action_choice} {place_choice}"
    
    print("\n" + headline)
    user_input = input("Do you want to generate another headline? (yes/no): ").strip().lower()
    if user_input == "no":
        break

print("Thank you for using the Fake News Headline Generator! Have a fun day!") 
