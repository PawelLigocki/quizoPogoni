
import random
from string import ascii_lowercase

print("Witamy w quizie o Pogoni Szczecin")

name = input("\nJak masz na imię? ")
wynik = 0

answer = input("\nKiedy został założony klub Pogoń Szczecin? ")
if answer == "1948":
    print("Brawo, poprawna odpowiedż")
    wynik += 1
else:
    print(f"Odpowiedz nieprawidłowa, klub nie został założony w {answer!r}")

questions = [
    ("Jaka jest pojemność nowego stadionu Pogoni Szczecin? ", "21163"),
    ("W którym roku Pogoń zadebiutowała w najwyższej klasie rozgrywkowej w Polsce? ", "1959"),
    ("Przy jakiej ulicy mieści się siedziba Pogoni Szczecin? ", "Karłowicza"),
]

for question, correct_answer in questions:
    answer = input(f"\n{question}")
    if answer == correct_answer:
        print("Brawo, poprawna odpowiedz.")
        wynik += 1
    else:
        print(f"Odpowiedz nieprawidłowa.")

print("W kolejnych pytaniach prosimy o wybór odpowiedzi i wpisanie od a do d.")

NUM_QUESTIONS_PER_QUIZ = 4
QUESTIONS = {
    "Który zawodnik Pogoni Szczecin gra z numer 11 na koszulce? ": [
        "Luka Zahović",
        "Pontus Almqvist",
        "Kamil Grosicki",
        "Damian Dąbrowski",
    ],
    "Jakim wynikiem skończył się mecz Pogoni z zespołem Rakowa Częstochowa w Pucharze Polski 2022/2023? ": [
        "0:2",
        "1:2",
        "0:1",
        "1:0",
    ],
    "Na którym miejscu Pogoń skończyła ligowe rozgrywki w sezonie 2021/2022? ": [
        "1",
        "2",
        "3",
        "4",
    ]
}

num_questions = min(NUM_QUESTIONS_PER_QUIZ, len(QUESTIONS))
questions = random.sample(list(QUESTIONS.items()), k=num_questions)

for num, (question, alternatives) in enumerate(questions, start=1):
    print(f"\nPytanie {num}: ")
    print(question)
    correct_answer = alternatives[2]
    labeled_alternatives = dict(
        zip(ascii_lowercase, random.sample(alternatives, k=len(alternatives))))
    for label, alternative in labeled_alternatives.items():
        print(f"  {label}) {alternative}")
    while (answer_label := input("\nJaki jest Twój wybór? ")) not in labeled_alternatives:
        print(f"Proszę o wybór jednej z poniżej odpowiedzi {', '.join(labeled_alternatives)}! ")

    answer = labeled_alternatives[answer_label]

    if answer == correct_answer:
        print("Brawo, poprawna odpowiedż!")
        wynik += 1
    else:
        print("Odpowiedz nieprawidłowa.")

if wynik == 7:
    print(f"\nBrawo {name}, perfekcyjny wynik - 100%.")
elif wynik > 5:
    print(f"\nBrawo {name}, świetny wynik, jednak trochę zabrakło do 100%. Uzyskałeś {wynik} punktów.")
elif wynik > 3:
    print(f"\nBrawo {name}, dobry wynik, poducz sie i wróc do quizu. Uzyskałeś {wynik} punktów.")
else:
    print(f"\n{name} nie możesz nazywać się fanem Pogoni Szczecin.")
