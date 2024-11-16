from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible
@deconstructible
class PhoneDigitsValidator:
    def __init__(self, message = None):
        self.message = message

    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, value):
        if value is None:
            value = 'You phone number must consist only of digits!'
        self.__message = value

    def __call__(self, value, *args, **kwargs):
        if not value.isdigit():
            raise ValidationError(self.message)