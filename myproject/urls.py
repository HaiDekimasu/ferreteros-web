
from django.contrib import admin
from django.urls import path
from Ferreteros.views import home  # Importamos la vista de tu nueva app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),  # La cadena vacía '' significa que es la página principal
]