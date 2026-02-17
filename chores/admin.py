from django.contrib import admin
from .models import Manager, Chore, Day, ChoreAssignment

# Register your models here.

admin.site.register(Manager)
admin.site.register(Chore)
admin.site.register(Day)
admin.site.register(ChoreAssignment)
