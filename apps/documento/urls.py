from django.urls import path
from .views import DocumentCreate, DocumentUpdate

urlpatterns = [
    path('novo/<int:funcionario_id>', DocumentCreate.as_view(), name='create_document'),
    path('editar/<int:pk>', DocumentUpdate.as_view(), name='update_funcionariio'),
]