from .views import TaskModelViewApiSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('tasks', TaskModelViewApiSet, base_name='task')
urlpatterns = router.urls
