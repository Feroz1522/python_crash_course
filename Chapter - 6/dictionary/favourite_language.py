favorite_languages = {
                    'jen': 'python',
                    'sarah': 'c',
                    'edward': 'ruby',
                    'phil': 'python',
                    }
polls = ['feroz','anwar','phil','edward','rinald']

for poll in polls :
    if poll in favorite_languages.keys():
        print("thank you for responding",poll)
    elif poll not in favorite_languages.keys():
        print("inviting you for taking the poll",poll)


