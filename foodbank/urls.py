from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from registration.backends.simple.views import RegistrationView
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('restaurants.urls')),
    path('accounts/', include('registration.backends.simple.urls')),
    path('accounts/register/', RegistrationView.as_view(), name='registration_register'),
    path('login/', LoginView.as_view(redirect_authenticated_user=True), name='auth_login'),
    path('login/', LoginView.as_view(), name='auth_login'),
    path('accounts/logout/', LogoutView.as_view(), name='auth_logout'),



]


handler404 = "helpers.views.handle_not_found"
handler500 = "helpers.views.handle_server_error"


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
