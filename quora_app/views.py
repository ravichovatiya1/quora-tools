from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from quora_app import models, forms
from django.contrib import messages
from django.urls import reverse
from django.http import JsonResponse

# Create your views here.

def index(request):
    questions_obj = models.Questions.objects.all().order_by('-updated_at')
    count = len(questions_obj)
    return render(request,'quora_app/index.html', 
        {'questions_obj': questions_obj, 'count': count})


@login_required
def post_questions_create(request):
    form = forms.QuestionsForm()
    if request.method == 'POST':
        form = forms.QuestionsForm(request.POST, request.FILES)
        if form.is_valid():
            form_obj = form.save(commit=False)
            form_obj.author = request.user
            form_obj.save()
            messages.success(request, f'Post added Successful !' )
            return redirect('questions:post_questions_view')
    context ={"form" : form}
    return render(request, 'quora_app/questions/post_create.html', context)


@login_required
def post_questions_update(request, question_id):
    question_obj = get_object_or_404(models.Questions, id=question_id)
    form = forms.QuestionsForm(instance=question_obj)
    if request.method == 'POST':
        form = forms.QuestionsForm(request.POST, request.FILES, instance=question_obj)
        if form.is_valid():
            form_obj = form.save()
            messages.success(request, f'Post Updated Successful !' )
            return redirect('questions:post_questions_view')
    context ={"form" : form, 'question_obj':question_obj}
    return render(request, 'quora_app/questions/post_create.html', context)


@login_required
def post_questions_delete(request, question_id):
    question_obj = models.Questions.objects.filter(
        id = question_id, author = request.user)

    if question_obj:
        question_obj.delete()
        messages.success(request, f'Post Deleted Successful !' )
    else:
        messages.error(request, f'Object not Found !' )
    return redirect('questions:post_questions_view')


@login_required
def post_questions_view(request):
    questions_obj = models.Questions.objects.filter(author=request.user)
    context={'questions_obj': questions_obj} 
    return render(request, 'quora_app/questions/post_view.html', context)


@login_required
def answer_add(request):
    if request.method == 'POST':
        question_reference = request.POST.get('question_reference')
        content = request.POST.get('content')

        questions_obj = get_object_or_404(models.Questions, id=question_reference)
        obj, created = models.Answers.objects.update_or_create(
            question=questions_obj, author=request.user )
        obj.content = content
        obj.save()

        if created:
            messages.success(request, f'Answer is Submitted successfully.')
        else:
            messages.success(request, f'Answer is Updated successfully.')

        url_with_fragment = f"{reverse('index:index')}#post_id_{questions_obj.id}"
        return redirect(url_with_fragment)
    
@login_required
def like_answer(request):
    if request.method == 'POST':
        print('enter hear in post')
        answer_id = request.POST.get('answer_id')
        answers_obj = get_object_or_404(models.Answers, id=answer_id)
        obj, created = models.Likes.objects.update_or_create(
            answer=answers_obj, author=request.user )
        obj.save()
        if obj:
            data = {
                'status': 'success',
                'message': 'Like added successfully.',
                'likes_count': 1 }
        else:
            data = {
                'status': 'error',
                'message': 'Failed to like the post.'}

        return JsonResponse(data)
    return JsonResponse({'status': 'error', 'message': 'Invalid request.'})
