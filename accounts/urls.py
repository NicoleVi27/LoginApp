#from django.urls import path
#from django.contrib.auth.views import LoginView, LogoutView
#from django.views.generic import CreateView    # postscript
#from django.contrib.auth.forms import UserCreationForm    # postscript


#urlpatterns = [
#    path('signup/', CreateView.as_view(
#        template_name='accounts/signup.html',
#        form_class=UserCreationForm,
#        success_url='/accounts/login',
#    ), name='signup'),    # postscript
#    path('login/', LoginView.as_view(
#        redirect_authenticated_user=True,
#        template_name='accounts/login.html'
#    ), name='login'),
#    path('logout/', LogoutView.as_view(), name='logout'),
#]

from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import UserCreateAndLoginView, UserDetail, UserUpdate, PasswordChange, PasswordChangeDone, UserDelete   

urlpatterns = [
    path('signup/', UserCreateAndLoginView.as_view(), name='signup'),
    path('login/', LoginView.as_view(
        redirect_authenticated_user=True,
        template_name='accounts/login.html'
    ), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('user_detail/<int:pk>/', UserDetail.as_view(), name='user_detail'),
    path('user_update/<int:pk>/', UserUpdate.as_view(), name='user_update'),
    path('password_change/', PasswordChange.as_view(), name='password_change'),   
    path('password_change/done/', PasswordChangeDone.as_view(), name='password_change_done'),   
    path('user_delete/<int:pk>/', UserDelete.as_view(), name='user_delete'),   
]
