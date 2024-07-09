# todo/urls.py
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import TodoItemViewSet

router = DefaultRouter()
router.register(r'todos', TodoItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # other urlpatterns if any
]
