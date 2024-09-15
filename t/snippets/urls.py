from django.urls import path
from snippets import views
from django.http import JsonResponse

from ninja import NinjaAPI
from .models import Check


api = NinjaAPI()

@api.get("/checks")
def list_checks(request):
    checks = Check.objects.all()
    return JsonResponse([{
        "id": check.id,
        "type": check.type,
        "url": check.url,
      } for check in checks], safe=False)

urlpatterns = [
    path('snippets/', views.snippet_list),
    path('snippets/<int:pk>/', views.snippet_detail),
    path('api/', api.urls),
]
