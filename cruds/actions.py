from rest_framework import exceptions


class StateAction:
    @staticmethod
    def validate_uppercase(data: dict):
        if not data.get('abbreviation').isupper():
            raise exceptions.ValidationError('O campo sigla deve ser maiúsculo')
        return data
