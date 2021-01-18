

    

def result(bot_id,date,start_time, finish_time, time_list, revenue_list, file_name):

    file = open('bot'+str(bot_id)+'.txt')

    average_time = sum(time_list) / len(time_list)
    average_revenue_RUB = sum(revenue_list) / len(revenue_list)
    time_work = finish_time - start_time

def cycle_log(bot_id, time_work):

    file = open('bot'+str(bot_id)+'.txt')

def create_log(bot_id, date, start_time):

    bot_id = str(bot_id)
    file_name = 'bot'+ bot_id + '.txt'

    file = open(file_name, 'w')

    file.write('Bot id: ' + bot_id + '\n' + 'Date: '+ str(date) + '\n' + 'Start time: ' + start_time)
    #print(file.tell())



create_log(bot_id = 1, date = '12.1.2020', start_time = '19:40')