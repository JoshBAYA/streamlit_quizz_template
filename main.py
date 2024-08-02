class PointSystem:
    def __init__(self):
        self.points = 0

    def earn_points(self, amount):
        if amount > 0:
            self.points += amount

    def spend_points(self, amount):
        if amount > 0:
            if self.points >= amount:
                self.points -= amount

    def check_points(self):
        print(f"Total points: {self.points}")

    def final_score(self):
        if self.points >= 100:
            recommendation = "Excellent! Keep up the great work!"
        elif self.points >= 50:
            recommendation = "Good job! You're doing well!"
        elif self.points >= 20:
            recommendation = "Not bad, but there's room for improvement."
        else:
            recommendation = "You need to work harder."

        return self.points, recommendation

def ask_question(question, choice1, choice2):
    print(question)
    print(f"1. {choice1}")
    print(f"2. {choice2}")
    print("3. Neither")
    while True:
        try:
            answer = int(input("Enter 1, 2, or 3: "))
            if answer in [1, 2, 3]:
                return answer
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def main():
    ps = PointSystem()
    questions = [
        ("Would you rather work with numbers or words?", "Numbers", "Words"),
        ("Would you rather work in a Lab or an Office?", "Lab", "Office"),
        ("Would you rather create an art masterpiece or write a novel?", "Art Masterpiece", "Novel"),
        ("Would you rather solve a complex math problem or conduct a scientific experiment?", "Math Problem", "Scientific Experiment"),
        ("Would you rather study ancient civilizations or learn about modern politics?", "Ancient Civilizations", "Modern Politics"),
        ("Would you rather design a building or create a software program?", "Design Building", "Create Software Program"),
        ("Would you rather work with animals or teach children?", "Work with Animals", "Teach Children"),
        ("Would you rather have early Mornings or late Nights?", "Early Mornings", "Late Nights"),
        ("Would you rather explore space or dive into the ocean's depths?", "Explore Space", "Dive into Ocean"),
        ("Would you rather study human behavior or understand how machines work?", "Human Behavior", "Machines"),
        ("Would you rather compose a piece of music or act in a play?", "Compose Music", "Act in a Play"),
        ("Would you rather manage a sports team or plan a corporate event?", "Manage Sports Team", "Plan Corporate Event"),
        ("Would you rather translate foreign languages or study the effects of globalization?", "Translate Languages", "Effects of Globalization"),
        ("Would you rather lead a team project or work independently on a research paper?", "Lead Team Project", "Work Independently"),
        ("Would you rather develop a new recipe or create a health fitness plan?", "New Recipe", "Health Fitness Plan"),
        ("Would you rather study law or explore philosophical ideas?", "Study Law", "Philosophical Ideas"),
        ("Would you rather work on environmental conservation or urban development?", "Environmental Conservation", "Urban Development"),
        ("Would you rather write code or study cybersecurity?", "Write Code", "Cybersecurity"),
        ("Would you rather analyze crime scenes or study social justice issues?", "Analyze Crime Scenes", "Social Justice Issues"),
        ("Would you rather focus on physical health or mental health?", "Physical Health", "Mental Health"),
        ("Would you rather work in a lab or in the field with a community?", "Lab", "Field"),
        ("Would you rather be involved in business startups or work on non-profit initiatives?", "Business Startups", "Non-profit Initiatives")
    ]

    for question, choice1, choice2 in questions:
        answer = ask_question(question, choice1, choice2)
        if answer == 1:
            ps.earn_points(5)
        elif answer == 2:
            ps.earn_points(3)
        else:
            ps.earn_points(1)

    score, recommendation = ps.final_score()
    print(f"Final score: {score}")
    print(f"Recommendation: {recommendation}")

if __name__ == "__main__":
    main()
