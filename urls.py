from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('contactus/',views.contactus,name='contactus'),
    path('login/',views.login,name='login'),
    path('signup/',views.signup,name='signup'),
    path('ministry/',views.ministry,name='ministry'),
    path('railway/',views.railway,name='railway'),
    path('tourism/',views.tourism,name='tourism'),
    path('education/',views.education,name='education'),
    path('agriculture/',views.agriculture,name='agriculture'),
]