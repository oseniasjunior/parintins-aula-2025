from rest_framework import exceptions


class StateAction:
    @staticmethod
    def validate_uppercase(data: dict):
        if not data.get('abbreviation').isupper():
            raise exceptions.ValidationError('O campo sigla deve ser maiúsculo')
        return data

    @staticmethod
    def create_state_file(state_id: int):
        with open('/tmp/states.txt', 'w+') as file:
            for item in range(10000):
                file.write(f'{state_id} - {item}\n')
