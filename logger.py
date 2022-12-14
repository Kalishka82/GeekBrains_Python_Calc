from datetime import datetime as dt


def logger(data):
    with open('List_of_all_countings.txt', 'a') as file:
        time = dt.now().strftime('%D  %H:%M')
        file.write('{}\n{}\n'.format(time, data))
        file.write('\n')
