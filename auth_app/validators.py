from django.core.exceptions import ValidationError
from django.core import validators
import re

def password_validator(value):
    '''
        1. Validates the password has min 8 char.
        2. Has special charactors in it.
        3. Has numeric in it.
    '''
    if not len(value) >= 8 or not len(value) <= 50:
        raise ValidationError(
            'Password should be between 8-50 characters long.'
        )
    if not re.search('[A-Z]', value) or not re.search('[a-z]', value) \
            or not re.search('[0-9]', value) or not re.search('[^A-Za-z0-9]', value):
        raise ValidationError(
            'Password should contain at least one numeric, uppercase, lowercase and special letter.'
        )
