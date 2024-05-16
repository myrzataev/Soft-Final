from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from webapp.models import Question


# Список вопросов
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def api_question_list_view(request):
    questions = Question.objects.all()
    question_data = [{'id': question.id, 'text': question.text, 'photo': question.photo.url if question.photo else None,
                      'audio': question.audio.url if question.audio else None, 'test_set': question.test_set_id} for question in questions]
    return Response({'questions': question_data})
