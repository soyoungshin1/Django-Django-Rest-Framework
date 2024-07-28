from django.shortcuts import render, redirect,get_object_or_404 # import redirect
from .models import Review
from .forms import ReviewForm # forms.py에서 ReviewForm 가져오기

# Create your views here.
def main(request):
    reviews = Review.objects
    return render(request,'main/reviews.html',{'reviews':reviews})

def create(request):
    if request.method == 'POST': # method가 post일때
        form = ReviewForm(request.POST) # form 에 ReviewForm 할당
        if form.is_valid(): # form 유효성 검증
            form.save() # 저장
            return redirect('main') # 다시 main으로
    else:
        form = ReviewForm() # 빈 form 열기
    return render(request, 'main/create.html',{'form' :form})

def detail(request, pk):
    review = get_object_or_404(Review,pk=pk)
    return render(request,'main/detail.html',{'review':review})

def update(request,pk):
    review = get_object_or_404(Review, pk=pk)
    if request.method == 'POST':
        form = ReviewForm(request.POST,instance=review) # review 객체 가져오기
        if form.is_valid():
            form.save()
            return redirect('main')
    else:
        form = ReviewForm(instance=review) # review 객체 가져와서 form을 생성
    return render(request,'main/update.html',{'form':form})


def delete(request,pk):
    review = Review.objects.get(pk=pk)
    review.delete() 
    return redirect('main')