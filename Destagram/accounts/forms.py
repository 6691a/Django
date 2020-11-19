from django.contrib.auth.models import User

from django import forms

# form : formTag = HTML의 태그 = 프론트에서 사용자의 입력을 받는 인터페이스
# 장고의 form : HTML의 폼 역할, DB에 저장할 내용을 형식, 제약조건


class RegisterForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Repeate Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

    # 비밀번호가 같은지 검색
    # cleaned_data 장고에서 검증이 끝난 안전한 데이터
    def clean_password2(self):
        cd = self.cleaned_data

        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Password not matched!')
        return cd['password2']
