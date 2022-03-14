from django.urls import path, include

urlpatterns = [
    # Djoser создаст набор необходимых эндпоинтов.
    # базовые, для управления пользователями в Django:
    path("v1/", include("djoser.urls")),
    # JWT-эндпоинты, для управления JWT-токенами:
    path("v1/", include("djoser.urls.jwt")),
]
