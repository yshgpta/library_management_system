from django.urls import path
from library import views

urlpatterns = [
    path('home/', views.index, name='home'),
    path('register',views.register,name='register'),
    path('std_login/',views.std_login,name='std_login'),
    path('user_login/',views.user_login_success, name='user_login'),
    path('logout',views.std_logout,name='logout'),
    path('search_b/',views.search_book,name='search_b'),
    path('issue_book/',views.issue_book,name='issue_book'),
    path('delete_issue/',views.delete_issue,name='delete_issue'),
    path('renewal/',views.renewal, name = 'renewal'),
    path('get_all_user/',views.get_all_user, name='get_all_user'),
    path('checkout/',views.checkout,name='checkout'),
    path('book_detail/',views.book_detail,name='book_detail'),
    path('return_book',views.return_book, name='return_book'),
    path('superuser_login', views.superuser_login, name='superuser_login'),
    path('admin_login',views.admin_login_success, name='admin_login'),
    path('admin_logout',views.admin_logout, name ='admin_logout')
]