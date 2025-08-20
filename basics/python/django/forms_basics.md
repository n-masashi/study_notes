# Django Forms の基礎

Django にはフォーム処理を便利にする `forms.py` があります。



## 基本の書き方

~~~python
from django import forms

class CommentForm(forms.Form):
    name = forms.CharField(label='名前', max_length=50)
    text = forms.CharField(label='コメント', widget=forms.Textarea)
~~~

- `forms.Form` を継承して作成  
- 各フィールドは `CharField`, `EmailField`, `IntegerField` などを利用可能  
- `widget` を指定することで入力フォームの形を変更できる（例: `Textarea`）

- # Django Forms の詳しい使い方



## バリデーション

~~~python
class CommentForm(forms.Form):
    name = forms.CharField(max_length=50)
    text = forms.CharField(widget=forms.Textarea)

    # 独自のバリデーション
    def clean_name(self):
        data = self.cleaned_data['name']
        if "admin" in data.lower():
            raise forms.ValidationError("名前に 'admin' は使えません")
        return data
~~~

- `clean_<フィールド名>` で独自のバリデーションを追加できる  



## モデルフォーム

モデルと直結したフォームを簡単に作成できる。

~~~python
from django import forms
from .models import Comment

class CommentModelForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'text']  # 使用するフィールドを指定
~~~

- モデルのフィールドをそのままフォームにできる  

