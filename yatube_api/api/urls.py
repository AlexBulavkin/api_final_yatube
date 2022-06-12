from django.urls import include, path

from rest_framework.routers import DefaultRouter

from .views import CommentViewSet, GroupViewSet, FollowViewSet, PostViewSet

router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'follow', FollowViewSet, basename='follow')
router.register(
    r'^posts/(?P<post_id>[\d+]+)/comments', CommentViewSet, basename='comment'
)

urlpatterns = [
    path('', include(router.urls)),
    path('', include('djoser.urls.jwt')),
]
