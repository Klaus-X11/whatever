from django.urls import path,include
from allauth.account.views import ConfirmEmailView
from django.conf.urls import url
from .views import null_view,complete_view
urlpatterns = [
        path('auth/registration/account-email-verification-sent/', null_view, name='account_email_verification_sent'),
        url(r'^auth/registration/account-confirm-email/(?P<key>[-:\w]+)/$', ConfirmEmailView.as_view(), name='account_confirm_email'),
        url(r'^auth/registration/complete/$', complete_view, name='account_confirm_complete'),
        url(r'^auth/password-reset/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', null_view, name='password_reset_confirm'),
        path('auth/', include('rest_auth.urls')),
        path('auth/registration/', include('rest_auth.registration.urls')),
]
