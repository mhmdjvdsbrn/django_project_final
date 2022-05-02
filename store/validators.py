from django.core.exceptions import ValidationError

def validate_size_kb(file):
    max_size_kb =50

    if file.size > max_size_kb *1024 :
        raise ValidationError(f'file cannot be large than {max_size_kb}KB')