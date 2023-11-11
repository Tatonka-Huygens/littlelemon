#define URL route for index() view
from django.urls import path, include
from . import views

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'tables', views.BookingViewSet)

'''
router1 = DefaultRouter(trailing_slash=False)
router1.register(r'users', views.UserViewSet, basename='users')
'''
   #path('restaurant/booking/', include(router.urls)),
   #path('', include(router1.urls)),
   #path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),


urlpatterns = [
    path('', views.index, name='index'),
    path('menu/', views.MenuItemsView.as_view()),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
    path('booking/', include(router.urls)),
]