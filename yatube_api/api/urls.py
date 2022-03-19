from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CommentsViewSet, FollowViewSet, GroupViewSet, PostViewSet

router1 = DefaultRouter()

router1.register(r"groups", GroupViewSet, basename="groups")
router1.register(
    r"posts/(?P<post_id>\d+)/comments", CommentsViewSet, basename="comments"
)
router1.register(r"posts", PostViewSet, basename="posts")
router1.register(r"follow", FollowViewSet, basename="follow")


urlpatterns = [
    path("v1/", include("djoser.urls.jwt")),
    path("v1/", include(router1.urls)),
]
