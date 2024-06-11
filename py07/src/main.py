# main.py

import sys
import questions_loader
import test_logic

def main():
    if len(sys.argv) < 2:
        print("Usage: main.py <command> [<file>]")
        sys.exit(1)
    
    command = sys.argv[1]

    if command == 'test':
        if len(sys.argv) != 3:
            print("Usage: main.py test <questions_file>")
            sys.exit(1)
        
        questions_file = sys.argv[2]
        questions = questions_loader.load_questions(questions_file)
        
        responses = []
        
        for question_data in questions:
            print(question_data['question'])
            for i, answer in enumerate(question_data['answers']):
                print(f"{i+1}. {answer}")
            
            answer_index = int(input("Choose an answer (number): ")) - 1
            
            if answer_index < 0 or answer_index >= len(question_data['answers']):
                print("Invalid answer number. Exiting.")
                sys.exit(1)
            
            respiration = float(input("Enter respiration (BPM): "))
            heart_rate = float(input("Enter heart rate (BPM): "))
            blushing_level = int(input("Enter blushing level (1-6): "))
            pupillary_dilation = float(input("Enter pupillary dilation (mm): "))
            
            responses.append({
                'answer': question_data['answers'][answer_index],
                'respiration': respiration,
                'heart_rate': heart_rate,
                'blushing_level': blushing_level,
                'pupillary_dilation': pupillary_dilation
            })
        
        result = test_logic.analyze_responses(responses)
        print(f"The subject is determined to be a {result}.")
    
    else:
        print("Unknown command. Available commands: test")

if __name__ == '__main__':
    main()

