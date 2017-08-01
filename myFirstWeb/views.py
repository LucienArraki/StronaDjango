from django.shortcuts import render

# Create your views here.
from myFirstWeb.models import Animal_category, Animal_type


def base(request):
    query_category = Animal_category.objects.all()
    query_type = Animal_type.objects.all()
    context = {
        "object_list_category": query_category,
        "object_list_type": query_type
    }
    return render(request,'myFirstWeb/base.html',context)