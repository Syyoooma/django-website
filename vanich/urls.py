from django.contrib import admin
from django.urls import path, include
from users import views as user_views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('reg', user_views.register, name='register'),
    path('user', auth_views.LoginView.as_view(template_name='users/user.html'), name='user'),
    path('exit', auth_views.LogoutView.as_view(template_name='users/exit.html'), name='exit'),
    path('', include('blog.urls')),
    path('pass-reset', auth_views.PasswordResetView.as_view(template_name='users/pass_reset.html'), name='pass-reset'),
    path('pass-reset/done', auth_views.PasswordResetDoneView.as_view(template_name='users/pass_reset_done.html'), name='password_reset_done'),
    path('pass-reset/confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='users/pass_reset_confirm.html'),
         name='password_reset_confirm'),
path('pass-reset/complete', auth_views.PasswordResetCompleteView.as_view(template_name='users/pass_reset_complete.html'),
         name='password_reset_complete'),

    path('profile', user_views.profile, name='profile'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
