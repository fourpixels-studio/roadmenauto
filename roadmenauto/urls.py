from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("frontend.urls")),
    path("accounts/", include("accounts.urls")),
    path("activities/", include("activities.urls")),
    path("activities/", include("events.urls")),
    path("gallery/", include("gallery.urls")),
    path("help/", include("help.urls")),
    path("members/", include("members.urls")),
    path("membership/", include("membership.urls")),
    path("newsletter/", include("newsletter.urls")),
    path("notifications/", include("notifications.urls")),
    path("payments/", include('payments.urls')),
    path("shop/", include("products.urls")),
    path("services/", include("services.urls")),
    path("shop/", include("shop.urls")),
    path("tickets/", include("tickets.urls")),
    path("vehicles/", include("vehicles.urls")),
    path("summernote/", include('django_summernote.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = "Roadmen Auto - Admin"
admin.site.index_title = "Roadmen Auto - Admin"
