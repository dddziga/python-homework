from django import template

register = template.Library()

translations = {
    'This field is required.': 'Это поле обязательно для заполнения.',
    'Enter a valid email address.': 'Введите действительный адрес электронной почты.',
    'The two password fields didn’t match.': 'Пароли не совпадают.',
    'This password is too short. It must contain at least 8 characters.': 'Этот пароль слишком короткий. Он должен содержать не менее 8 символов.',
    'This password is too common.': 'Этот пароль слишком распространен.',
    'This password is entirely numeric.': 'Этот пароль состоит только из цифр.'
}

@register.filter
def translate_error(error):
    return translations.get(error, error)
