from django.urls import path
from . import views


# URL config
urlpatterns = [
    # path("", views.menu, name="chores"),
    path("", views.calendar_view, name="calendar"),   #ex. /chores/1/
    path("events/", views.calendar_events, name="calendar_events"),
    path("update/<int:pk>/", views.update_event, name="update_event"),
]
