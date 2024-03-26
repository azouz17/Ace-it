from django.contrib import admin
from .models import *


admin.site.register(Table)
admin.site.register(Column)
admin.site.register(Row)
admin.site.register(Cell)
admin.site.register(Expert)
admin.site.register(Field)

# Register your models here.
