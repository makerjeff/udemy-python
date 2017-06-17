salary = 92000

def calculate(salary, work_weeks):
    print 'Base salary: {0:.2f}'.format(salary)
    print 'Work weeks: {0:.2f}'.format(work_weeks)
    print '\n'
    print 'Daily: {0:.2f}'.format(salary/work_weeks/5)
    print 'Weekly: {0:.2f}'.format(salary/work_weeks)
    print 'Quarterly: {0:.2f}'.format( (salary/work_weeks)*12)


def Main():
    calculate(salary, 50)

if __name__ == '__main__':
    Main()