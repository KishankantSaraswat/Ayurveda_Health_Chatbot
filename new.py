class DoshaCalculator:
    def __init__(self):
        self.user_age = ''
        self.user_gender = ''
        self.user_name = ''
        self.user_build = ''
        self.user_skin_complexion = ''
        self.user_hair_type = ''
        self.user_energy_levels = ''
        self.user_activity_times = ''
        self.user_sleep_hours = ''
        self.user_sleep_trouble = ''
        self.user_appetite = ''
        self.user_food_cravings = ''

        self.user_attributes = [
            'user_age', 'user_gender', 'user_name', 'user_build', 'user_skin_complexion',
            'user_hair_type', 'user_energy_levels', 'user_activity_times', 'user_sleep_hours',
            'user_sleep_trouble', 'user_appetite', 'user_food_cravings'
        ]

    def get_user_attributes(self):
        user_attribute_values = {attr: getattr(self, attr) for attr in self.user_attributes}
        return user_attribute_values

    def update_user_attributes(self, attribute_values):
        for attr, value in attribute_values.items():
            setattr(self, attr, value)

    def calculate_dosha_scores(self):
        dosha_scores = {
            "Vata": 0,
            "Pitta": 0,
            "Kapha": 0
        }

        # Assign scores based on user responses
        for dosha, attributes in [("Vata", vata_attributes), ("Pitta", pitta_attributes), ("Kapha", kapha_attributes)]:
            for attribute, value in attributes.items():
                response = getattr(self, attribute)
                dosha_scores[dosha] += value.get(response, 0)

        # Find the dosha with the highest score
        max_dosha = max(dosha_scores, key=dosha_scores.get)

        return dosha_scores, max_dosha

# Define scores for each dosha attribute
vata_attributes = {
    "user_build": {"slim": -1, "medium": 0, "heavy": 1},
    "user_skin_complexion": {"fair": -1, "medium": 0, "dark": 1},
    "user_hair_type": {"thin": -1, "medium": 0, "thick": 1},
    "user_energy_levels": {"low": -1, "medium": 0, "high": 1},
    "user_activity_times": {"more active in the evening": -1, "no specific pattern": 0, "more active in the morning": 1},
    "user_sleep_hours": {"trouble falling asleep/staying asleep": -1, "normal sleep": 0, "sound sleeper": 1},
    "user_sleep_trouble": {"variable": -1, "moderate": 0, "strong": 1},
    "user_appetite": {"craving warm, spicy foods": -1, "no specific cravings": 0, "craving sweet, cold foods": 1},
    "user_food_cravings": {"craving warm, spicy foods": -1, "no specific cravings": 0, "craving sweet, cold foods": 1}
}

pitta_attributes = {
    "user_build": {"slim": 0, "medium": 0, "heavy": -1},
    "user_skin_complexion": {"fair": 0, "medium": 0, "dark": -1},
    "user_hair_type": {"thin": 0, "medium": 0, "thick": -1},
    "user_energy_levels": {"low": 0, "medium": 0, "high": 1},
    "user_activity_times": {"more active in the evening": -1, "no specific pattern": 0, "more active in the morning": 1},
    "user_sleep_hours": {"trouble falling asleep/staying asleep": 1, "normal sleep": 0, "sound sleeper": -1},
    "user_sleep_trouble": {"variable": 0, "moderate": 0, "strong": 1},
    "user_appetite": {"craving warm, spicy foods": 1, "no specific cravings": 0, "craving sweet, cold foods": -1},
    "user_food_cravings": {"craving warm, spicy foods": 1, "no specific cravings": 0, "craving sweet, cold foods": -1}
}

kapha_attributes = {
    "user_build": {"slim": -1, "medium": 0, "heavy": 1},
    "user_skin_complexion": {"fair": -1, "medium": 0, "dark": 1},
    "user_hair_type": {"thin": -1, "medium": 0, "thick": 1},
    "user_energy_levels": {"low": -1, "medium": 0, "high": 1},
    "user_activity_times": {"more active in the evening": -1, "no specific pattern": 0, "more active in the morning": 1},
    "user_sleep_hours": {"trouble falling asleep/staying asleep": 1, "normal sleep": 0, "sound sleeper": -1},
    "user_sleep_trouble": {"variable": -1, "moderate": 0, "strong": 1},
    "user_appetite": {"craving warm, spicy foods": 1, "no specific cravings": 0, "craving sweet, cold foods": -1},
    "user_food_cravings": {"craving warm, spicy foods": 1, "no specific cravings": 0, "craving sweet, cold foods": -1}
}

# Testing the DoshaCalculator
if __name__ == "__main__":
    calculator = DoshaCalculator()

    user_attribute_values = {
        'user_age': '30',
        'user_gender': 'male',
        'user_name': 'John Doe',
        'user_build': 'heavy',
        'user_skin_complexion': 'dark',
        'user_hair_type': 'thick',
        'user_energy_levels': 'high',
        'user_activity_times': 'more active in the morning',
        'user_sleep_hours': 'trouble falling asleep/staying asleep',
        'user_sleep_trouble': 'strong',
        'user_appetite': 'craving warm, spicy foods',
        'user_food_cravings': 'craving warm, spicy foods'
    }

    calculator.update_user_attributes(user_attribute_values)

    print("User Attributes:")
    print(calculator.get_user_attributes())

    dosha_scores, dominant_dosha = calculator.calculate_dosha_scores()

    print("\nDosha Scores:")
    print(dosha_scores)
    
    print("\nDominant Dosha:")
    print(dominant_dosha)
