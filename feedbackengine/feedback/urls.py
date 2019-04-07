from django.urls import path, include
from .views import HomePage

from rest_framework import routers
from .views import FeedbackView, ProductView


router = routers.DefaultRouter()
router.register('feedbacks', FeedbackView)
router.register('products', ProductView)


urlpatterns = [
    path('', HomePage.as_view(), name='feedback_url'),
    path('api/', include(router.urls))

]