from django.contrib import admin
from myapp.models import MyModel, MyModel2
# Register your models here.

admin.site.register(MyModel)
admin.site.register(MyModel2)
