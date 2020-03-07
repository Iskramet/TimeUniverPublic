from datetime import datetime, timedelta

from .models import User, Group

def func_day_week(day):                                 # Определяет день недели по дате
    day_week = int(day.strftime('%w'))
    return day_week

def func_parity_week(day):                              # Определяет четность недели по дате
    if (int(day.strftime('%V')) - 1) % 2 == 0 :
        parity_week = 2
    else:
        parity_week = 1
    return parity_week

def func_student_group(request):                        # Определяет группу пользователя
    username = request.user.username
    user = User.objects.get(username = username)
    id_group = user.student.group
    return id_group

#def func_add_lesson(request):