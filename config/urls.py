from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('info/', include('core.urls', namespace='core')),
    path('account/', include('account.urls', namespace='account')),
    path('', include('task.urls', namespace='task')),

]
