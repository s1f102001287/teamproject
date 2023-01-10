from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	path('', views.index, name='index'),
    path('<int:article_id>/delete', views.delete, name='delete'),
    path('<int:article_id>/update', views.update, name='update'),
    path('create', views.create, name='create'),
    path('<int:article_id>/like', views.like, name='like'),
    path('api/articles/<int:article_id>/like', views.api_like),
    path('<int:article_id>', views.detail, name='detail'),
]
urlpatterns += static(settings.IMAGE_URL, document_root=settings.IMAGE_ROOT)