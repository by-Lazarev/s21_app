# test_logic.py

def analyze_responses(responses):
    # Пример простого анализа: суммируем показатели и сравниваем с порогом
    total_respiration = sum(response['respiration'] for response in responses)
    total_heart_rate = sum(response['heart_rate'] for response in responses)
    total_blushing = sum(response['blushing_level'] for response in responses)
    total_pupillary = sum(response['pupillary_dilation'] for response in responses)

    threshold = 300  # Задаем пороговое значение для определения
    
    # Используем простую логику для определения результата
    score = total_respiration + total_heart_rate + total_blushing + total_pupillary

    return "Replicant" if score > threshold else "Human"

