from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r'post', PostViewSet)
router.register(r'post/(?P<post_id>[0-9]+)/comment', CommentViewSet)
router.register(r'series', SeriesViewSet)
router.register(r'tag', TagViewSet)

urlpatterns = [
  path('', include(router.urls)),
]