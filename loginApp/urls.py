from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls), #COMENTAR EN CASO DE QUE SE QUIERA MIGRAR NUEVAMENTE LA APLICACION
    path('blog/', include('blog.urls')),
    path('accounts/', include('accounts.urls')), #  
]