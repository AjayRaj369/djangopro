from django.urls import path
from myapp.views import employee

from rest_framework.routers import DefaultRouter
from .views import EmployeeViewSet
from .views import EmployeeView


from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import RegisterView,AdminOnlyView



router = DefaultRouter()
router.register(r'employees', EmployeeViewSet)


urlpatterns = [

    path('home/',employee),

    path('employees/', EmployeeView.as_view(), name='employee'),

     #Registration
    path('register/', RegisterView.as_view(), name='register'),

    #Token obtain (Login)
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),

    #Token refresh
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    #admin only to view employers list
    path('admin-only/', AdminOnlyView.as_view(), name='admin_only'),


]+router.urls