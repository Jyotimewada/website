from django.contrib import admin
from django.urls import path
from notes import views  # Import views properly
from django.conf import settings
from django.conf.urls.static import static
from notes import views
urlpatterns = [
    # Admin URLs
    path('admin/', admin.site.urls),
    path('admin/home/', views.admin_home, name='admin_home'),
    path('admin/login/', views.login_admin, name='login_admin'),
    path('admin/change-password/', views.change_passwordadmin, name='change_passwordadmin'),

    # User Authentication URLs
    path('login/', views.userlogin, name='login'),
    path('logout/', views.Logout, name='logout'),
    path('signup/', views.signup1, name='signup'),

    # Profile Management URLs
    path('profile/', views.profile, name='profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('profile/change-password/', views.changepassword, name='changepassword'),

    # Notes Management URLs
    path('notes/upload/', views.upload_notes, name='upload_notes'),
    path('notes/my/', views.view_mynotes, name='view_mynotes'),
    path('notes/delete/<int:pid>/', views.delete_mynotes, name='delete_mynotes'),
    path('notes/all/', views.view_allnotes, name='view_allnotes'),
    path('notes/pending/', views.pending_notes, name='pending_notes'),
    path('notes/accepted/', views.accepted_notes, name='accepted_notes'),
    path('notes/rejected/', views.rejected_notes, name='rejected_notes'),
    path('notes/status/<int:pid>/', views.assign_status, name='assign_status'),
    path('notes/delete-admin/<int:pid>/', views.delete_notes, name='delete_notes'),
    path('notes/viewall/', views.viewallnotes, name='viewallnotes'),
    # User Management URLs
    path('users/', views.view_users, name='view_users'),
    path('users/delete/<int:pid>/', views.delete_users, name='delete_users'),

    # Queries Management URLs
    path('queries/unread/', views.unread_queries, name='unread_queries'),
    path('queries/read/', views.read_queries, name='read_queries'),
    path('queries/view/<int:pid>/', views.view_queries, name='view_queries'),

    # Static Pages
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),

    #path('', views.note_list, name='note_list'),
    #path('create/', views.create_note, name='create_note'),


    # Fixing 'all_notes'
    path('all_notes/', views.all_notes, name='all_notes'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
