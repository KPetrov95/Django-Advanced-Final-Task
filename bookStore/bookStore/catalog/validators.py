from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible
@deconstructible
class ExactLengthValidator:
    def __init__(self, message=None):
        self.message = message

    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, value):
        if value is None:
            value = 'Your ISBN must be exactly 13 digits!'
        self.__message = value

    def __call__(self, value: str, *args, **kwargs):
        if not (value.isdigit() and len(value) == 13):
            raise ValidationError(self.message)
