from django.shortcuts import render, redirect
from .models import Farm, House, Cave, Casino


def index(request):
    if request.method == 'GET':
        if 'log' not in request.session:
            request.session['log'] = []
        if 'gold' not in request.session:
            request.session['gold'] = 0
        context = {
            'gold': request.session['gold'],
            'log': request.session['log']
        }
        return render(request, 'ninja_app/index.html', context)
    else:
        return process_money(request)


def process_money(request):
    locations = {
        'farm': Farm,
        'casino': Casino,
        'house': House,
        'cave': Cave,
    }
    building = locations[request.POST['building']]
    current_gold = request.session['gold']
    obj = building()
    gold = obj.value
    current_gold += gold
    request.session['gold'] = current_gold
    log = request.session['log']
    log.append(obj.new_log())
    request.session['log'] = log
    return redirect('/')
