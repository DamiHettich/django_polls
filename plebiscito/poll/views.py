from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse
from .models import Question, Poll, Choice

# Create your views here.
def index(request):
    return HttpResponse('<h1> Página principal Aplicación Encuestas </h1>')

def poll_details(request, poll_id):
    poll_obj = get_object_or_404(Poll, pk = poll_id)
    questions = poll_obj.question_set.all()
    print(questions)
    my_context = {
        'poll':poll_obj,
        'question_list':questions
    }
    return render(request, 'polls/details.html', context = my_context)

def poll_results(request, poll_id):
    return HttpResponse(f'<h1> Resultados para la Encuesta {poll_id} </h1>')

def question_details(request, question_id):
    return HttpResponse(f'<h1> Detalle pregunta:{question_id} </h1>')

def question_results(request, question_id):
    return HttpResponse(f'<h1> Resultados para la pregunta {question_id} </h1>')

def question_vote(request, question_id):
    return HttpResponse(f'<h1> Votando en {question_id} </h1>')