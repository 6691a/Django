from django.shortcuts import render

from .forms import RegisterForm
# Create your views here.

# CRUD Create, Update


def register(request):

    if request.method == "POST":
        # 회원 가입 데이터 입력 완료
        user_form = RegisterForm(request.POST)
        # Data가 올바른지 확인
        if user_form.is_valid():
            # DB에 user_from에서 받은 정보를 저장하지 않는다
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            # 가입한 유저의 정보를 html에서 확인 할 수 있도록 {'new_user1': new_user} 지정
            return render(request, 'registration/register_done.html', {'new_user1': new_user})
    else:
        # 회원 가입 내용을 입력 하는 상황
        # 빈 폼을 만들어 준다
        user_form = RegisterForm()
    return render(request, 'registration/register.html', {'form': user_form})
