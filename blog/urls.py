from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('base/',views.base, name='base'),
    path('add_post/',views.add_post, name='add_post'),
    path('login/',views.login, name='login'),
    path('blog/<blog_id>', views.view_post, name='view_post'),
    path('edit_post/<blog_id>', views.edit_post, name='edit_post'),
    path('delete/<blog_id>', views.delete, name='delete'),
    path('view_category/<slug>', views.view_category, name='view_category'),
    path('search/',views.search, name='search'),

]
