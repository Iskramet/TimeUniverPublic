from django.shortcuts import render, redirect
from datetime import datetime, timedelta
from django.db.models import Q
from django.contrib.auth.decorators import login_required 

from .forms import GroupForm
from .models import shedule
from .utils import *

class Shedule():

    day_week_all = {
                1:'Понедельник',
                2:'Вторник',
                3:'Среда',
                4:'Четверг',
                5:'Пятница',
                6:'Суббота'
                }
    
    parity_week_all = {
                1:'Нечетная',
                2:'Четная'
                }


def promo(request):
    if request.method == "POST":
        form = GroupForm(request.POST)
        if form.is_valid():
            group = form.cleaned_data.get('group').group_id
            return redirect('group', group)
    else:
        form = GroupForm()

    data = {
        "form": form,
    }
    return render(request, 'main/group.html', data) 

def shedule_view(request, group):
    
    lessons_all = shedule.objects.filter(group = group).order_by('start_time') 

    data = {
            'lessons_today': lessons_all.filter(Q(day_week = func_day_week(datetime.now())), Q(parity_week = func_parity_week(datetime.now())) | Q(parity_week = 3)),
            'lessons_tomorrow': lessons_all.filter(Q(day_week = func_day_week(datetime.now() + timedelta(days=1))), Q(parity_week = func_parity_week(datetime.now() + timedelta(days=1))) | Q(parity_week = 3)),
            'lessons_all': lessons_all,
            'day_week_all': Shedule.day_week_all,
            'parity_week_all': Shedule.parity_week_all,
            'day_week': func_day_week(datetime.now()),
            'title': 'Расписание',
            'group': group,
            }
    return render(request, 'main/shedule.html', data)

def day_week(request, group, pk):

    data ={
        'lessons': shedule.objects.filter(day_week = pk, group = group),
        'title': Shedule.day_week_all.get(pk),
        'group': group,
        }
    return render(request, 'main/day_week.html', data)

def lesson(request, group, pk):
    lesson_full = shedule.objects.get(lesson_id = pk)
    data ={
        'lesson': lesson_full,
        'id': pk,
        'group': group,
        'parity_week': Shedule.parity_week_all.get(lesson_full.parity_week, "Каждую неделю"),
        'day_week': Shedule.day_week_all.get(lesson_full.day_week),
        }
    return render(request, 'main/lesson.html', data)

@login_required(redirect_field_name='my_redirect_field')
def remove_lesson(request, group, lesson):
    shedule.objects.get(lesson_id = lesson).delete()
    return redirect('group', group)