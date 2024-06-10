import random

def turrets_generator():
    def shoot(self):
        print("Shooting")

    def search(self):
        print("Searching")

    def talk(self):
        print("Talking")
    
    # Динамическое создание класса Turret
    Turret = type('Turret', (object,), {
        'shoot': shoot,
        'search': search,
        'talk': talk
    })
    
    # Генерация личностных черт
    traits = ['neuroticism', 'openness', 'conscientiousness', 'extraversion', 'agreeableness']
    values = [random.randint(0, 100) for _ in range(5)]
    total = sum(values)
    normalized_values = [int(value / total * 100) for value in values]
    diff = 100 - sum(normalized_values)
    normalized_values[0] += diff

    # Создание экземпляра турели с личностными чертами
    turret_instance = Turret()
    for trait, value in zip(traits, normalized_values):
        setattr(turret_instance, trait, value)
    
    return turret_instance

turret = turrets_generator()
print(turret.neuroticism, turret.openness, turret.conscientiousness, turret.extraversion, turret.agreeableness)
turret.shoot()
turret.search()
turret.talk()

