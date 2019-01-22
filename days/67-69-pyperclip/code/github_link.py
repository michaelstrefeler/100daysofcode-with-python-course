import pyperclip


def get_link():
    answer = input('Would you like my github link? (Y/N) ')

    if answer.lower().startswith('y'):
        pyperclip.copy('https://github.com/michaelstrefeler')
        print('My link has been copied to your clipboard')
    else:
        print('Ok, bye')
        exit()


if __name__ == "__main__":
    get_link()
