# with statments automatically close opened files.

def open_with_read():
    filename = raw_input('Enter the text file name ->  ')

    while filename != ':q':
        try:
            with open(filename, 'r') as file:
                print file.read()

            print 'Finished reading file. Goodbye!'
            break

        except :
            print 'Errored out.'

            filename = raw_input('No file by that name. Try again -> ')


def main():
    open_with_read()


if __name__ == '__main__':
    main()
