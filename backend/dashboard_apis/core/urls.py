from django.urls import path
from . import views
from . import order_view


urlpatterns = [
    # test api
    path('', views.getData.as_view()),

    # product api
    path('product/<str:id>', order_view.order_detail.as_view()),
    path('product/<str:id>', order_view.order_image_update.as_view()),
    path('upload/', views.upload.as_view()),

    path('order/', views.order.as_view()),
    # rider api
    path('rider-rewards/', views.rider_rewards.as_view()),
    path('rider-management/', views.getRiderManagementMap.as_view()),
    path('orders/all', views.getOrder.as_view()),
    path('riders/all', views.getRider.as_view()),
    path('bags/all', views.getBags.as_view()),
]    
