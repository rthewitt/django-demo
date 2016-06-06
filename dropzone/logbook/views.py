from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .models import Jump
from .forms import JumpForm


def get_home_dz():
    return 'Lake Elsinore'


def index(request):
    recent_jumps = list(reversed( Jump.objects.order_by('-date')[:5] ))
    jump_no = Jump.objects.count() + 1
    initial_data = {
        'number': jump_no,
        'location': get_home_dz()
    }
    return render(request, 'logbook/index.html', { 'jumps': recent_jumps, 'JumpForm': JumpForm(initial=initial_data) })


def jumps(request):
    if request.method == 'GET':
        jumps = Jump.objects.all()
        return render(request, 'logbook/log.html', { 'jumps': jumps })
    elif request.method == 'POST':
        jump_form = JumpForm(request.POST)
        jump_form.save()
        if jump_form.is_valid():
            return HttpResponseRedirect('/')
        else:
            return HttpResponse('Bad form data...')
