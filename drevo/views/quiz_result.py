from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from drevo.models import QuizResult
from users.models import User, MenuSections


def show_quiz_result(request,id):
    if request.method == 'GET':
        quiz_results = {}
        user = User.objects.get(id=id)
        if user == request.user:
            sections = [i.name for i in MenuSections.objects.all()]
            activity = [i.name for i in MenuSections.objects.all() if i.name.startswith('Мои') or
                        i.name.startswith('Моя')]
            link = "{% url 'users:myprofile' %}"
        else:
            sections = [i.name for i in user.sections.all()]
            activity = [i.name for i in user.sections.all() if i.name.startswith('Мои') or i.name.startswith('Моя')]
            link = "{% url 'public_human' pub_user.id %}"
        all_results = QuizResult.objects.filter(user=user)
        all_quizzes_name = all_results.values_list("quiz__name", flat=True).distinct()
        for quizzes in all_quizzes_name:
            questions_and_answers = {}
            all_questions_name = all_results.filter(quiz__name=quizzes).values_list("question__name", flat=True) \
                .distinct().order_by('-question__order')
            for questions in all_questions_name:
                questions_and_answers[questions] = all_results.filter(question__name=questions, quiz__name=quizzes) \
                    .values_list("answer__name", "answer__related__tr__name").order_by('-answer__order')
            date = str(all_results.filter(quiz__name=quizzes).values_list("date_time__day", "date_time__month",
                                                                          "date_time__year").first()).rstrip(')'). \
                lstrip('(').replace(' ', '')
            for_link = all_results.filter(quiz__name=quizzes).values_list("quiz__pk", flat=True).first()
            quiz_results[quizzes + ' ' + date.replace(',', '.') + ' ' + str(for_link)] = questions_and_answers
        return render(request, 'drevo/show_quiz_result.html', {'quiz_result': quiz_results, 'pub_user': user,
                                                               'sections': sections, 'activity': activity, 'link': link})