# while loops

# diy password check
password = 'password12345'
input_password = ''
attempts = 0

while input_password != password:
    input_password = raw_input('Enter your password: ')

    if input_password == password:
        print 'Password accepted. You are logged in. '

    else:
        attempts += 1
        print 'Inccorect password, you\'ve attempted ' + str(attempts) + ' times.'
