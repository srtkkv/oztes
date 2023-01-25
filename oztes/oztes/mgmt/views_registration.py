from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse,JsonResponse
from .models import Emp,Policy, Cartificate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Agent, Emp
from .serializers import AgentSerializer, EmpSerializer

@csrf_exempt
def anonymous(request):
    if request.method == 'PUT':
        print(request.body)
        return HttpResponse(status=201)
    else:
        resp = Policy.objects.get(name='Default')
        return HttpResponse(f'{resp.xml}', content_type='text/xml')
@csrf_exempt
def agent_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        agents = Agent.objects.all()
        serializer = AgentSerializer(agents, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = AgentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
@csrf_exempt
def emp_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        emps = Emp.objects.all()
        serializer = EmpSerializer(emps, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = EmpSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

def agent_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        agent = Agent.objects.get(pk=pk)
    except Agent.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = AgentSerializer(agent)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = AgentSerializer(agent, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        agent.delete()
        return HttpResponse(status=204)


def view_profile(request, pk):
    user = get_object_or_404(Emp, pk=pk)

    return HttpResponse(f'{user}',content_type='text/xml')