from django.contrib import admin
from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static     


urlpatterns = [
	url(r'', include("pages.urls")),
    url(r'^listings/', include("listings.urls")),
    url(r'^message/', include("message.urls")),
    url(r'^blog/', include("blog.urls")),
    url(r'^news/', include("news.urls")),
    url(r'^admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
