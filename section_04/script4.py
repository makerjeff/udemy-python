emails = ['me@gmail.com', 'you@gmail.com', 'they@gmail.com', 'me@yahoo.com', 'you@yahoo.com', 'they@yahoo.com']


# very simple way to check if a string item matches.

user_input = raw_input('String to search: -> ')


while user_input != ':q':
    for email in emails:
        if  user_input in email:
            print email + ' matches.'

            user_input = raw_input('String to search: -> ')

        else:
            print 'not found. '
            user_input = raw_input('String to search: -> ')