print("Select level difficulty")

easy = {"be": "быть", "do": "делать", "have": "иметь", "make": "делать", "go": "идти"}
medium = {"be": "быть", "do": "делать", "have": "иметь", "make": "делать", "go": "идти"}
hard = {"be": "быть", "do": "делать", "have": "иметь", "make": "делать", "go": "идти"}

levels = {
    0: "0",
    1: "1",
    2: "2",
    3: "3",
    4: "4",
    5: "5"
}

answers = {}

selected_level = input("easy, medium, hard \n")

if selected_level == "easy":
    for key, item in easy.items():
        len_words = len(item)
        print(f"{key},{len_words}, The first sing {item[0]}")
        answer = input()
        if answer != item:
            print(f" Error, {key} it's {item}")
        answers[key] = (answer == item)

if selected_level == "medium":
    for key, item in medium.items():
        len_words = len(item)
        print(f"{key},{len_words}, The first sing {item[0]}")
        answer = input()
        if answer != item:
            print(f" Error, {key} it's {item}")
        answers[key] = (answer == item)

if selected_level == "hard":
    for key, item in hard.items():
        len_words = len(item)
        print(f"{key},{len_words}, The first sing {item[0]}")
        answer = input()
        if answer != item:
            print(f" Error, {key} it's {item}")
        answers[key] = (answer == item)


print("True")
for key, item in answers.items():
    if item == True:
        print(key)

print("False")
for key, item in answers.items():
    if item == False:
        print(key)



count_answer = 0
for key, item in answers.items():
    if item == True:
       count_answer += 1


print(f"Your level {levels[count_answer]}")
