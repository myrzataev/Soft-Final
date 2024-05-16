from django.urls import path
from api.views.api_test_views import api_test_list_view, api_test_detail_view, api_test_pass_view
from api.views.api_answer_views import api_answer_list_view
from api.views.api_qeustion import api_question_list_view

app_name: str = 'api'

urlpatterns = [
    path('v1/answer_list/', api_answer_list_view, name='api_answer_list_view'),
    path('v1/question_list/', api_question_list_view, name='api_question_list_view'),
    path('v1/test_list/', api_test_list_view, name='test_list_view'),
    path('v1/test/<int:test_set_id>/', api_test_detail_view, name='test_detail_view'),
    path('v1/test/<int:test_set_id>/pass/', api_test_pass_view, name='test_pass_view'),
]
