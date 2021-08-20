from rest_framework.routers import SimpleRouter

from app.pkg.shortener.api.views import ShortenerView, MostPopularView

router = SimpleRouter(trailing_slash=False)
router.register(r'shortener', ShortenerView, basename='shortener')
router.register(r'most-popular', MostPopularView, basename='most-popular')

urlpatterns = router.urls
