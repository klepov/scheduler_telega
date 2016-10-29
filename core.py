from datetime import date, datetime

time_15_35 = '15:35-17:05'
time_17_15 = '17:15-18:45'
time_18_50 = '18:50-20:20'

week_number = date.today().isocalendar()[1]
delta = week_number % 2

math = {"name": "Математический анализ", "classroom": "206"}
math_disc = {"name": "Дискретная математика", "classroom": "201"}
info_tech = {"name": "Информационные технологии", "classroom": "617, 620"}
info_sys = {"name": "инфокоммуникационные системы и сети", "classroom": "617, 620"}
web = {"name": "Web-технологии на транспорте", "classroom": "602"}
proc_sys = {"name": "Теория информационных процессов и систем", "classroom": "710, 617"}
rand = {"name": "Теория принятия решений", "classroom": "713"}

days = ['понедельник',
        "вторник",
        "среда",
        "четверг",
        "пятница",
        "суббота",
        "воскресенье"]

schedules = []

# числитель
if delta == 1:
    schedules = [0,
                 [{'subject': math, 'time': time_17_15}, {'subject': info_tech, 'time': time_18_50}],
                 [{'subject': web, 'time': time_17_15}],
                 [{'subject': proc_sys, 'time': time_18_50}],
                 [{'subject': math_disc, 'time': time_15_35}, {'subject': info_sys, 'time': time_17_15}],
                 0,
                 0]
else:
    schedules = [0,
                 [{'subject': math, 'time': time_17_15}, {'subject': info_tech, 'time': time_18_50}],
                 [{'subject': web, 'time': time_17_15}],
                 [{'subject': proc_sys, 'time': time_18_50}],
                 [{'subject': math_disc, 'time': time_17_15}, {'subject': rand, 'time': time_18_50}],
                 0,
                 0]


# schedule_on_day = schedules[date.today().weekday()]
def get_scheduler(choose):
    if choose == 1:
        schedule_on_day = date.today().weekday()
    elif choose == 2:
        schedule_on_day = date.today().weekday() + 1
    elif choose == 3:
        return one_week()
    schedule_on_day = schedules[schedule_on_day]
    if schedule_on_day == 0:
        return 'это выходной, отдыхай. чо'
    else:
        return one_day(schedule_on_day)


def one_day(schedule_on_day):
    list_answer = []
    for schedule in schedule_on_day:
        time = schedule.get('time')
        schedule_get = schedule.get('subject')
        classroom = schedule_get.get('classroom')
        name = schedule_get.get('name')
        format = ("\n|{}|  |{}|  |{}|".format(name, time, classroom))
        list_answer.append(format)
    return ''.join(list_answer)


def one_week():
    list_answer = []
    for schedule_on_day in range(len(schedules)):
        if schedules[schedule_on_day] == 0:
            list_answer.append("\n{} - выходной ".format(days[schedule_on_day]))
            continue
        day = days[schedule_on_day]
        list_local_day = []
        for schedule in schedules[schedule_on_day]:
            time = schedule.get('time')
            schedule_get = schedule.get('subject')
            classroom = schedule_get.get('classroom')
            name = schedule_get.get('name')
            format = ("(|{}|  |{}|  |{}|) \n".format(name, time, classroom))
            list_local_day.append(format)
        full_format = "\n{} - {}".format(day,''.join(list_local_day))
        list_answer.append(full_format)
    return (''.join(list_answer))
