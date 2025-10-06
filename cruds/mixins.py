from rest_framework import exceptions


class StateSerializerMixin:

    def validate(self, attrs: dict):
        if not attrs.get('abbreviation').isupper():
            raise exceptions.ValidationError('O campo sigla deve ser maiúsculo')
        return data
