# for loop for multiple lists

names = ['james', 'john', 'jack']
email_domains = ['gmail', 'hotmail', 'yahoo']

for i, j in zip(names, email_domains):
    # print i, j
    print '{} {}'.format(i, j)