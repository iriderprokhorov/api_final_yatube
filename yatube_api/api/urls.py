from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CommentsViewSet, FollowViewSet, GroupViewSet, PostViewSet

router = DefaultRouter()

router.register(r"groups", GroupViewSet)
router.register(
    r"posts/(?P<post_id>\d+)/comments", CommentsViewSet, basename="comments"
)
router.register(r"posts", PostViewSet)
router.register(r"follow", FollowViewSet)


urlpatterns = [
    path("v1/", include("djoser.urls")),
    path("v1/", include("djoser.urls.jwt")),
    path("v1/", include(router.urls)),
]
