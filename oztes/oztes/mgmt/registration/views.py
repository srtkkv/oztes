from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from ..models import Emp,Policy, Cartificate
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def anonymous(request):
    if request.method == 'PUT':
        print(request.body)
        return HttpResponse(status=201)
    else:
        resp = Policy.objects.get(name='Default')
        return HttpResponse(f'{resp.xml}', content_type='text/xml')

def view_profile(request, pk):
    user = get_object_or_404(Emp, pk=pk)

    return HttpResponse(f'{user}',content_type='text/xml')