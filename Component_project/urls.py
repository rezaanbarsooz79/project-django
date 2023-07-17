from django.contrib import admin
from django.urls import path,include
from Component_table.views import post_list 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Component/',post_list,name='post_list') ,
    path('api/', include('Component_table.urls'))
]













