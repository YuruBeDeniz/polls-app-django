from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.db.models import F


from .models import Choice, Question

def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    template = loader.get_template('index.html')
    context = { 'latest_question_list': latest_question_list }
    # return HttpResponse(template.render(context, request))
    return render(request, 'index.html', context)

def detail(request, question_id):
    # question = get_object_or_404(Question, pk=question_id)
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'detail.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
    
def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'results.html', {'question': question})
    


# The reverse function is called "reverse" because it reverses the normal URL-matching process, 
# finding a URL from a view name instead of finding a view from a URL.

# request.POST is a dictionary-like object that lets you access 
# submitted data by key name. In this case, request.POST['choice'] 
# returns the ID of the selected choice, as a string. request.POST values are always strings.

# Another useful benefit of F() is that having the database - rather than Python - 
# update a field’s value avoids a race condition.
# it will only ever update the field based on the value of the field in the database 
# when the save() or update() is executed, rather than based on its value when the instance was retrieved.