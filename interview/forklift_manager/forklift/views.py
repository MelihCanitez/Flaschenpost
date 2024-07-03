from django.shortcuts import render
from django.http.request import HttpRequest
from django.http.response import HttpResponse, HttpResponseBadRequest, HttpResponseBase

from forklift.models import Forklift

#neu
from .models import Partner
from .models import Reparatur
from django.http import JsonResponse

# Create your views here.
def overview(request: HttpRequest) -> HttpResponseBase:
    return render(request, 'forklift/overview.html', {
        'forklifts': Forklift.objects.all(),
    })


def allow_operator(request: HttpRequest) -> HttpResponseBase:
    try:
        data = request.POST

        forklift = Forklift.objects.get(id=data['forklift_id'])
        operators = set(forklift.allowed_operators)

        if data['allowed'] == 'true':
            operators.add(int(data['operator_id']))
        elif data['operator_id'] in operators:
            operators.remove(int(data['operator_id']))

        forklift.allowed_operators = list(operators)
        forklift.save()
        return HttpResponse()
    except Exception as e:
        return HttpResponseBadRequest(e)
    
def can_operate(request: HttpRequest) -> HttpResponseBase:
    try:
        data = request.POST

        forklift = Forklift.objects.get(id=data.get('forklift_id'))

        if data.get('allowed') == 'true':
            forklift.can_operate = True
        else:
            forklift.can_operate = False
            
        forklift.save()
        return HttpResponse()
    except Exception as e:
        return HttpResponseBadRequest(e)
    
def update_hours(request: HttpRequest) -> HttpResponseBase:
    try:
        data = request.POST

        forklift = Forklift.objects.get(id=data.get('forklift_id'))

        forklift.hours_run = data.get('hours')
            
        forklift.save()
        return HttpResponse()
    except Exception as e:
        return HttpResponseBadRequest(e)
    
def add_partner(request: HttpRequest) -> HttpResponseBase:
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')

        new_partner = Partner(name=name, email=email)
        new_partner.save()

        return HttpResponse('Partner erfolgreich hinzugefügt')
    
    return HttpResponseBadRequest('kein POST')

def add_reparatur(request: HttpRequest) -> HttpResponseBase:
    if request.method == 'POST':
        schadeneintritt = request.POST.get('schadeneintritt')
        fertigstellung = request.POST.get('fertigstellung')
        forkliftid = request.POST.get('forkliftid')
        partnerid = request.POST.get('partnerid')

        forklift = Forklift.objects.get(serial_no=forkliftid)
        partner = Partner.objects.get(pid=partnerid)

        new_reparatur = Reparatur(schadeneintritt=schadeneintritt, fertigstellung=fertigstellung, forkliftid=forklift, partnerid=partner)
        new_reparatur.save()

        return HttpResponse('Reparatur erfolgreich hinzugefügt')
    
    return HttpResponseBadRequest('kein POST')

def get_partners(request):
    if request.method == 'GET':
        partners = Partner.objects.all()
        partners_list = list(partners.values())
        return JsonResponse(partners_list, safe=False)
    else:
        return JsonResponse({'kein GET'})
    
def get_forklifts(request):
    if request.method == 'GET':
        forklifts = Forklift.objects.all()
        forklifts_list = list(forklifts.values())
        return JsonResponse(forklifts_list, safe=False)
    else:
        return JsonResponse({'kein GET'})