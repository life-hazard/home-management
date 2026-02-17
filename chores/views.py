from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.template import loader

from .models import Chore, Day, ChoreAssignment

from datetime import date

import json

# Create your views here.
def menu(request):
    return HttpResponse(request)

def calendar_view(request):
    return render(request, "chores/index.html")

def calendar_events(request):
    assignments = ChoreAssignment.objects.select_related("chore", "day")

    events = [
        {
            "id": assignment.id,
            "title": assignment.chore.chore_name,
            "start": assignment.day.date,
        }
        for assignment in assignments
    ]

    return JsonResponse(events, safe=False)

def update_event(request, pk):
    if request.method == "POST":
        data = json.loads(request.body)
        new_date = data.get("start")

        day, _ = Day.objects.get_or_create(date=new_date)

        assignment = ChoreAssignment.objects.get(pk=pk)
        assignment.day = day
        assignment.save()

        return JsonResponse({"status": "success"})

