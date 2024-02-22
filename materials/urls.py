from django.urls import path
from materials.apps import MaterialsConfig
from rest_framework.routers import DefaultRouter

from materials.views import CourseDetailAPIView, CourseListCreateAPIView, CourseViewSet, LessonCreateAPIView, LessonDestroyAPIView, LessonListAPIView, LessonRetrieveAPIView, LessonUpdateAPIView


app_name = MaterialsConfig.name

router = DefaultRouter(trailing_slash=False)
router.register(r'courses', CourseViewSet, basename='courses')


urlpatterns = [
    path('lesson/create/', LessonCreateAPIView.as_view(), name='lesson-create'),
    path('lesson/', LessonListAPIView.as_view(), name='lesson-list'),
    path('lesson/<int:pk>/', LessonRetrieveAPIView.as_view(), name='lesson-get'),
    path('lesson/update/<int:pk>/',
         LessonUpdateAPIView.as_view(), name='lesson-update'),
    path('lesson/delete/<int:pk>/',
         LessonDestroyAPIView.as_view(), name='lesson-delete'),
    path('courses/', CourseListCreateAPIView.as_view(), name='course-list'),
    path('courses/<int:pk>/', CourseDetailAPIView.as_view(), name='course-detail'),



] + router.urls
