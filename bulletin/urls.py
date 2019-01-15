from django.urls import path, include

from .views import BulletinListView, BulletinDetailView


bulletin_patterns = ([
    path('', BulletinListView.as_view(), name="list"),
    path('<int:pk>', BulletinDetailView.as_view(), name="detail"),
], 'bulletin')

urlpatterns = [
    path('', include(bulletin_patterns))
]
