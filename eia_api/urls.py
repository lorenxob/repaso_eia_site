from django.urls import path
from . import views

urlpatterns = [path(
    'create:machine/', views.Create_machine.as_view(), name="create_machine"
)]
