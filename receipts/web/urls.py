import django.contrib.admin
from django.conf.urls.static import static
from django.urls import path

from receipts import settings
from receipts.web.views import index, about, product, service, gallery, contact,\
                                SignUpView, information, SignOutView, SignInView,\
                                ProfileUpdate, PasswordChange
urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('product/', product, name='product'),
    path('service/', service, name='service'),
    path('gallery/', gallery, name='gallery'),
    path('contact/', contact, name='contact'),
    path('sign-up/', SignUpView.as_view(), name='sign up'),
    path('information/', information, name='information'),
    path('sign-in/', SignInView.as_view(), name='sign in'),
    path('sign-out/', SignOutView.as_view(), name='sign-out'),
    path('profile/<slug:slug>', ProfileUpdate.as_view(), name='profile'),
    path('password/', PasswordChange.as_view(), name='password change'),
    path('admin/', django.contrib.admin.AdminSite, name='admin'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
