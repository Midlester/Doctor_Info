from django.conf import settings # type: ignore
from django.conf.urls.static import static # type: ignore
from django.contrib import admin # type: ignore
from django.urls import path, include # type: ignore
from django.contrib.auth import views as auth_views # type: ignore

urlpatterns = [
    path('', include('doctor_info.urls')),  # Show doctor_list as homepage
    path('login/', auth_views.LoginView.as_view(template_name='doctor_info/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('admin/', admin.site.urls),
    path('doctor_info/', include('doctor_info.urls')),  # Still allow /doctor_info/
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

