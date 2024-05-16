from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from webapp.models import TestSet, Question, Answer


# Список тестов
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def api_test_list_view(request):

    test_sets = TestSet.objects.all()
    test_sets_data = [{'id': test_set.id, 'title': test_set.title, 'description': test_set.description} for test_set in
                      test_sets]

    return Response({'test_sets': test_sets_data})


# Детальный просмотров тестов
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def api_test_detail_view(request, test_set_id):

    test_set = get_object_or_404(TestSet, pk=test_set_id)
    test_set_data = {'id': test_set.id, 'title': test_set.title, 'description': test_set.description}

    return Response({'test_set': test_set_data})


# Пройти тест
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def api_test_pass_view(request, test_set_id):

    test_set = get_object_or_404(TestSet, pk=test_set_id)
    questions = Question.objects.filter(test_set=test_set)

    correct_answers_count = 0
    total_questions = questions.count()

    for question in questions:
        correct_answers = [int(answer_id) for answer_id in
                           Answer.objects.filter(question=question, is_correct=True).values_list('id', flat=True)]
        submitted_answers = [int(answer.strip()) for answer in request.data.get(f'answer_{question.id}', [])]

        if any(answer in correct_answers for answer in submitted_answers):
            correct_answers_count += 1

    correct_percentage = (correct_answers_count / total_questions) * 100

    return Response({
        'test_set': {'id': test_set.id, 'title': test_set.title, 'description': test_set.description},
        'correct_percentage': correct_percentage,
        'correct_answers_count': correct_answers_count,
        'total_questions': total_questions
    })
