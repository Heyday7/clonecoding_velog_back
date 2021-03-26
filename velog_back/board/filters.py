from django_filters import rest_framework as filters
from .models import *
from django.db.models import Q

class PostFilter(filters.FilterSet):
  query = filters.CharFilter(method='filter_query')

  def filter_query(self, queryset, name, value):
    qs = queryset.filter(
      Q(title__icontains=value) | Q(content__icontains=value)
    )
    return qs



  class Meta:
    model = Post 
    fields = ['query']

