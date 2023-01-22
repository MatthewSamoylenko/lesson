import random

questions = ("code", "bit", "list", "soul", "next")

morse_code = {
  "0": "-----",
  "1": ".----",
  "2": "..---",
  "3": "...--",
  "4": "....-",
  "5": ".....",
  "6": "-....",
  "7": "--...",
  "8": "---..",
  "9": "----.",
  "a": ".-",
  "b": "-...",
  "c": "-.-.",
  "d": "-..",
  "e": ".",
  "f": "..-.",
  "g": "--.",
  "h": "....",
  "i": "..",
  "j": ".---",
  "k": "-.-",
  "l": ".-..",
  "m": "--",
  "n": "-.",
  "o": "---",
  "p": ".--.",
  "q": "--.-",
  "r": ".-.",
  "s": "...",
  "t": "-",
  "u": "..-",
  "v": "...-",
  "w": ".--",
  "x": "-..-",
  "y": "-.--",
  "z": "--..",
  ".": ".-.-.-",
  ",": "--..--",
  "?": "..--..",
  "!": "-.-.--",
  "-": "-....-",
  "/": "-..-.",
  "@": ".--.-.",
  "(": "-.--.",
  ")": "-.--.-"
}

answers = []

def morse_encode(sentence):
    answer = ""
    for i in range(len(sentence)):
        for j, item in morse_code.items():
            if sentence[i] == j:
                answer = answer + morse_code[j]
                break
    return answer

def get_word():
  random_index = random.randrange(len(questions))
  print(questions[random_index])
  return questions[random_index]

def print_statistics():
  count = 0
  for i in answers:
    if i == True:
      count += 1

  print(f"{len(answers)}")
  print(f"{count}")
  print(f"{len(answers)-count}")

def start_pley():
  for i in range(5):
    word = get_word()
    morse_code_answer = morse_encode(word)
    print(f"Word {morse_code_answer}")
    answer = input()
    if answer == word:
      answers.append(True)
    else:
      answers.append(False)

  print_statistics()





morse_encode(input())
get_word()
start_pley()