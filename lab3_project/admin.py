from django.contrib import admin

from .models import Posts
admin.site.register(Posts)


from .models import Categories
admin.site.register(Categories)

from .models import Student
admin.site.register(Student)

