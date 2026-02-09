from django.shortcuts import render, redirect
from .forms import FeedbackCreateForm
from .models import Feedback
from django.contrib.auth.decorators import login_required


def home(request):
    '''Домашняя страница'''
    return render(request, 'feedback/home.html')

def feedback_form(request):
    ''' Создать отзыв'''
    if request.method == 'POST':
        form = FeedbackCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('all_feedback')
    else:
        form = FeedbackCreateForm()
    return render(request, 'feedback/feedback_form.html', {'form': form})

@login_required
def all_feedback(request):
    '''Показать все отзывы'''
    feedbacks = Feedback.objects.all().order_by('-created_at')
    return render(request, 'feedback/all_feedback.html', {'feedbacks': feedbacks})


