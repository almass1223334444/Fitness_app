from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'trainers', views.TrainerViewSet)
router.register(r'gyms', views.GymViewSet)
router.register(r'schedules', views.ScheduleViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
