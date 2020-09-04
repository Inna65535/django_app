from django import forms

class HelloForm(forms.Form):
    data=[
        ('ラーメン', '１：ラーメン'),
        ('うどん', '２：うどん'),
        ('そば', '３：そば'),
        ('パスタ', '４：パスタ'),
        ('チャーハン', '５：チャーハン'),
        ('すし', '６：すし'),
        ('ステーキ', '７：ステーキ'),
        ('うなぎ', '８：うなぎ'),
        ('とんかつ', '９：とんかつ'),
        ('焼肉', '１０：焼肉'),
        ('断食', '１１：断食')
    ]
    choice = forms.MultipleChoiceField(label='あながた食べたいのは', \
        choices=data, widget=forms.SelectMultiple(attrs={'size': 6}))
