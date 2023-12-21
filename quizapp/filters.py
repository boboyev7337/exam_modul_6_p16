from django_filters import FilterSet, CharFilter, NumberFilter, DateFilter
from django import forms

from quizapp.models import User


class ResultListFilter(FilterSet):
    total = NumberFilter(field_name='views', lookup_expr='gt', label='Start views',
                         widget=forms.NumberInput(attrs={'class': 'form-control'}))
    first_name = CharFilter(lookup_expr='icontains', label='Title',
                            widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = CharFilter(lookup_expr='icontains', label='Title',
                            widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['total', 'first_name', 'last_name']