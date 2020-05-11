from django.urls import path
from .apiviews import PollViewSet, PollDetail, ChoiceList, CreateVote, \
    UserCreate, LoginView
from rest_framework.routers import DefaultRouter
from rest_framework_swagger.views import get_swagger_view


schema_view = get_swagger_view(title='Polls API')

router = DefaultRouter()
router.register('polls', PollViewSet, base_name='polls')

app_name = 'polls'
urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('users/', UserCreate.as_view(), name='user_create'),
    path('polls/<int:pk>/', PollDetail.as_view(), name='polls_detail'),
    path('polls/<int:pk>/choices/', ChoiceList.as_view(), name='choice_list'),
    path('polls/<int:pk>/choices/<int:choice_pk>/vote/', CreateVote.as_view(),
         name='create_vote'),
    path('swagger-docs/', schema_view),
]

urlpatterns += router.urls
