from app1.views import a1_dhoni
from django.urls import path
app_name='app1'
urlpatterns = [
    path('a1_dhoni/',a1_dhoni,name='a1_dhoni'),
]
