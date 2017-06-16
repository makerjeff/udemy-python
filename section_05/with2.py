def Main():
    user_input = raw_input('File you want to open (:q to quit) -> ')

    while user_input != ':q':
        try:
            with open(user_input, 'r') as file:
                print file.read()
                break

        except:
            print 'Error reading file. '
            user_input = raw_input('Try another file name (:q to quit) -> ')

if __name__ == '__main__':
    Main()