# bite_22.py
# Write a decorator with argument

from functools import wraps


def make_html(tag):
    # Takes tag argument
    def add_tag(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Adds HTML tag to text
            return f'<{tag}>{func(*args, **kwargs)}</{tag}>'
        return wrapper
    return add_tag


@make_html('p')
@make_html('strong')
def get_text(text='I code with PyBites'):
    return text


print(get_text())
