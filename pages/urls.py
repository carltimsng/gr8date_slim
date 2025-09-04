from django.urls import path
from . import views

app_name = "pages"

urlpatterns = [
    # index + optional alias "home"
    path("", views.index, name="index"),
    path("", views.index, name="home"),  # <— optional alias, safe to keep

    path("dashboard/", views.dashboard, name="dashboard"),

    # TEMP alias so `{% url 'hot_dates' %}` (inside namespace) resolves
    path("hot-dates/", views.dashboard, name="hot_dates"),

    # Blog (namespaced)
    path("blog/", views.blog_list, name="blog_list"),
    path("blog/<slug:slug>/", views.blog_detail, name="blog_detail"),

    # Profiles
    path("profiles/<int:pk>/", views.profile_detail, name="profile_detail"),
    path("my-profile/", views.my_profile, name="my_profile"),
    path("my-profile-edit/", views.my_profile_edit, name="my_profile_edit"),  # <— ADD THIS

    # Auth / account
    path("login/", views.login_page, name="login"),
    path("signup/", views.signup_page, name="signup"),
    path("logout/", views.logout_view, name="logout"),

    # Footer/info pages (match your view names)
    path("about-us/", views.about_page, name="about"),
    path("privacy/", views.privacy_page, name="privacy"),
    path("terms/", views.terms_page, name="terms"),
    path("faq/", views.faq_page, name="faq"),
    path("contact/", views.contact_page, name="contact"),

    # Messages (renamed view to avoid clash)
    path("messages/", views.messages_page, name="messages"),

    # Actions
    path("toggle-favorite/<int:pk>/", views.toggle_favorite, name="toggle_favorite"),
    path("block-profile/<int:pk>/", views.block_profile, name="block_profile"),
    path("request-private-access/<int:pk>/", views.request_private_access, name="request_private_access"),
]

