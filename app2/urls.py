from app2.views import a2_malli
from django.urls import path
app_name='app2'
urlpatterns = [
    path('a2_malli/',a2_malli,name='a2_malli')
]
