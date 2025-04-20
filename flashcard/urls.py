from django.urls import path
from .views import *

urlpatterns = [
    # Your URLs...
    path('create/', CreateFlashCardView.as_view(), name='create-flash-card'),
    path('update/<id>/', UpdateFlashCardView.as_view(), name='update-flash-card'),
    path('delete/<id>/', DeleteFlashCardView.as_view(), name='delete-flash-card'),
    path('mylist/<user_id>/', ListFlashCardView.as_view(), name='List-flash-card'),
]