# Definition der Klasse
import sys


class Quiz:
    def __init__(self, qaa_list):
        self.questions = qaa_list
        self.currentQuestionIndex = 0
        self.points = 0

    def showQuestion(self):
        currentQuestion = self.questions[self.currentQuestionIndex]
        print(f"Frage {self.currentQuestionIndex + 1}: {currentQuestion['question']}\n")
        for i, choice in enumerate(currentQuestion['choice']):
            print(f"{i + 1}. {choice}")

    def checkAnswer(self, user_answer):
        correctAnswer = self.questions[self.currentQuestionIndex]['answer']
        if user_answer.lower() == correctAnswer.lower():
            self.points += 1
            print("\nKorrekt!\n")
        else:
            print("\nDas war leider falsch\n")
        self.currentQuestionIndex += 1

    def showFinalResult(self):
        print(f"Deine Punktzahl ist: {self.points} von {len(self.questions)}")

# Hauptprogramm

qaa_list = [
    {
        'question' : "Aus welchem Anime ist Rimuru Tempest?",
        'choice'   : ["A: Dragon Ball Z", "B: That Time I got Reincarnated as a Slime", "C: Bleach", "D: Toradora"],
        'answer'   : "B"
    },
    {
        'question' : "Wie heiß das Schwert von Ichigo Kurosaki?",
        'choice'   : ["A: Tenseiga", "B: Tenken", "C: Zangetsu", "D: Sanemi"],
        'answer'   : "C"
    },
    {
        'question' : "Wie hieß die Droge, mit der Shinichi Kudo geschrumpft wurde?",
        'choice'   : ["A: Apoptoxin 4869", "B: Apotoxin 4869,", "C: Apoptoxien 4869", "D: Dextotoxin 3755"],
        'answer'   : "A"
    },
    {
        'question': "Welche Nationalität hat Money D. Ruffy?",
        'choice': ["A: Spanien", "B: Brazilien", "C: Portugal", "D: Mexiko"],
        'answer': "B"
    },
    {
        'question': "Welcher Charakter benutzt den Detroit Smash?",
        'choice': ["A: Son Goku", "B: Gon", "C: Sukuna", "D: Izuku Midoriya"],
        'answer': "D"
    },
    {
        'question': "Wie alt war Shinichi Kudo als er geschrumpft wurde?",
        'choice': ["A: 16", "B: 17", "C: 15", "D: 19"],
        'answer': "B"
    },
    {
        'question': "Welcher ist keiner der drei Göttermonster aus Yu-Gi-Oh?",
        'choice': ["A: Slifer der Himmelsdrache", "B: Der geflügelte Drache von Ra", "C: Obelisk der Peiniger", "D: Raviel, Herr der Phantome"],
        'answer': "D"
    },
    {
        'question': "Wonach werden die Kriegerinnen von 'Sailor Moon' benannt?",
        'choice': ["A: Planeten", "B: Asteroiden", "C: Sternen", "D: Monden"],
        'answer': "A"
    },
    {
        'question': "Wie heißt der Wunschdrache von Namek in Dragon Ball Z?",
        'choice': ["A: Shenlong", "B: Super Shenlong", "C: Polunga", "D: Omega Shenlong"],
        'answer': "C"
    },
    {
        'question': "Wie werden die Probleme in der welt von No Game No gelöst?",
        'choice': ["A: durch Kriege", "B: durch Spiele", "C: durch Kämpfe", "D: durch Rätsel"],
        'answer': "B"
    },
    {
        'question': "Wie heißt Yugis alter Ego?",
        'choice': ["A: Atem", "B: Anubis", "C: Aknamkanon", "D: Bakura"],
        'answer': "A"
    },
    {
        'question': "Wie lautet Natsu Dragneel eigendlich vollständigen Name?",
        'choice': ["A: Etherious Natsu Dragneel", "B: Athenos Natsu Dragneel", "C: Atreus Natsu Dragneel", "D: Deloria Natsu Dragneel"],
        'answer': "A"
    },
    {
        'question': "Wie heißt der zweite Kira im Anime Death Note mit richtigen Namen?",
        'choice': ["A: Ruri Asada", "B: Lori Misami", "C: Yuna Kisara", "D: Misa Amane"],
        'answer': "D"
    },
    {
        'question': "Welcher Animefilm hat einen Oscar gewonnen?",
        'choice': ["A: Das wandelnde Schloss", "B: Chihiros Reise ins Zauberland", "C: Your Name", "D: Suzume"],
        'answer': "B"
    },
    {
        'question': "Wer aus Attack on Titan kann ich in einen Titanen verwandeln?",
        'choice': ["A: Armin Alert", "B: Reiner Braun", "C: Eren Jäger", "D: Misaka Ackermann"],
        'answer': "C"
    }
]

# Erstellen einer Instanz für die Quiz Klasse

quiz = Quiz(qaa_list)

# Durchführen des Quiz

while quiz.currentQuestionIndex < len(quiz.questions):
    quiz.showQuestion()
    user_answer = input("\nDeine Antwort (A/B/C/D): ")
    quiz.checkAnswer(user_answer)

# Anzeigen des Endergenisses

quiz.showFinalResult()