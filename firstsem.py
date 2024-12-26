import random
import sys

assessment_criteria = []
questions = []
student_feedback = []

def add_question(question):
    questions.append(question)

def generate_random_assessment_data(num_criteria=3, num_questions=5):
    word_list = ["Analysis", "Creativity", "Communication", "Problem-solving", "Collaboration"]
    assessment_criteria.extend(random.sample(word_list, min(num_criteria, len(word_list))))

    sentence_list = [
        "Explain the importance of collaboration in a team.",
        "Discuss a situation where you demonstrated problem-solving skills.",
        "How do you approach a creative task?",
        "Describe a scenario where effective communication was crucial.",
        "Analyze the impact of technology on education."
    ]
    questions.extend(random.sample(sentence_list, min(num_questions, len(sentence_list))))

def generate_assessment():
    formatted_assessment = ""
    formatted_assessment += "Assessment Questions:\n"
    formatted_assessment += '\n'.join([f"{index}. {question}" for index, question in enumerate(questions, start=1)])
    return formatted_assessment

def collect_student_feedback(student_name, feedback):
    student_feedback.append(f"{student_name}: {feedback}")

def generate_feedback_report():
    feedback_report = "Student Feedback Report:\n"
    feedback_report += '\n'.join(student_feedback)
    return feedback_report


def display_menu():
    print("Welcome to the Continuous Internal Evaluation (CIE) Project!\n")
    while True:
        print("1. Generate Random Assessment Data")
        print("2. Add Question")
        print("3. View Assessment")
        print("4. Collect Student Feedback")
        print("5. View Feedback Report")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")
        process_choice(choice)

def process_choice(choice):
    if choice == '1':
        generate_random_assessment_data()
    elif choice == '2':
        question = input("Enter assessment question: ")
        add_question(question)
        print(f"Assessment question '{question}' added.\n")
    elif choice == '3':
        assessment_result = generate_assessment()
        print(assessment_result)
    elif choice == '4':
        student_name = input("Enter student name: ")
        feedback = input("Enter student feedback: ")
        collect_student_feedback(student_name, feedback)
        print(f"Feedback collected from {student_name}.\n")
    elif choice == '5':
        feedback_report_result = generate_feedback_report()
        print(feedback_report_result)
    elif choice == '6':
        print("Exiting the CIE Project. Goodbye!")
        sys.exit()
    else:
        print("Invalid choice. Please enter a number between 1 and 7.\n")

if __name__ == "__main__":
    display_menu()