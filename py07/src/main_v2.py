# main_v2.py

import sys
import questions_loader_v2
import test_logic_v2

def main():
    if len(sys.argv) < 2:
        print("Usage: main_v2.py <command> [<file>]")
        sys.exit(1)
    
    command = sys.argv[1]

    if command == 'test':
        if len(sys.argv) != 3:
            print("Usage: main_v2.py test <questions_file>")
            sys.exit(1)
        
        questions_file = sys.argv[2]
        
        try:
            questions = questions_loader_v2.load_questions(questions_file)
        except Exception as e:
            print(f"Error loading questions: {e}")
            sys.exit(1)
        
        if not questions:
            print("The questions file is empty.")
            sys.exit(1)
        
        responses = []
        
        for question_data in questions:
            print(question_data['question'])
            for i, answer in enumerate(question_data['answers']):
                print(f"{i+1}. {answer}")
            
            while True:
                try:
                    answer_index = int(input("Choose an answer (number): ")) - 1
                    if answer_index < 0 or answer_index >= len(question_data['answers']):
                        raise ValueError("Invalid answer number.")
                    break
                except ValueError as e:
                    print(e)
                    print("Please enter a valid number corresponding to one of the answers.")

            while True:
                try:
                    respiration = float(input("Enter respiration (BPM): "))
                    if respiration <= 0:
                        raise ValueError("Respiration must be a positive number.")
                    break
                except ValueError as e:
                    print(e)
                    print("Please enter a valid respiration rate.")

            while True:
                try:
                    heart_rate = float(input("Enter heart rate (BPM): "))
                    if heart_rate <= 0:
                        raise ValueError("Heart rate must be a positive number.")
                    break
                except ValueError as e:
                    print(e)
                    print("Please enter a valid heart rate.")

            while True:
                try:
                    blushing_level = int(input("Enter blushing level (1-6): "))
                    if blushing_level < 1 or blushing_level > 6:
                        raise ValueError("Blushing level must be between 1 and 6.")
                    break
                except ValueError as e:
                    print(e)
                    print("Please enter a valid blushing level between 1 and 6.")

            while True:
                try:
                    pupillary_dilation = float(input("Enter pupillary dilation (mm): "))
                    if pupillary_dilation < 2 or pupillary_dilation > 8:
                        raise ValueError("Pupillary dilation must be between 2 and 8 mm.")
                    break
                except ValueError as e:
                    print(e)
                    print("Please enter a valid pupillary dilation between 2 and 8 mm.")
            
            responses.append({
                'answer': question_data['answers'][answer_index],
                'respiration': respiration,
                'heart_rate': heart_rate,
                'blushing_level': blushing_level,
                'pupillary_dilation': pupillary_dilation
            })
        
        result = test_logic_v2.analyze_responses(responses)
        print(f"The subject is determined to be a {result}.")
    
    else:
        print("Unknown command. Available commands: test")

if __name__ == '__main__':
    main()

