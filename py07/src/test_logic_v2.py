# test_logic_v2.py

def analyze_responses(responses):
    total_respiration = sum(response['respiration'] for response in responses)
    total_heart_rate = sum(response['heart_rate'] for response in responses)
    total_blushing = sum(response['blushing_level'] for response in responses)
    total_pupillary = sum(response['pupillary_dilation'] for response in responses)

    threshold = 800  # Задаем пороговое значение для определения
    
    score = total_respiration + total_heart_rate + total_blushing + total_pupillary

    return "Replicant" if score > threshold else "Human"

