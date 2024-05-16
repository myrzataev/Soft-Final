from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from webapp.models import Answer


# Список ответов
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def api_answer_list_view(request):
    answers = Answer.objects.all()
    answer_data = [{'id': answer.id, 'text': answer.text, 'is_correct': answer.is_correct, 'question': answer.question_id} for answer in answers]
    return Response({'answers': answer_data})
