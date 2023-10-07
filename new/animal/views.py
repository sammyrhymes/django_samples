from django.shortcuts import render
from .models import Dog, Horse, Cat
from django.http import HttpResponse
from django.views import View
from django.views.generic import ListView

# Create your views here.
class CatListView(View):
    model = Cat
    def get(self, request):
        model_name = self.model._meta.verbose_name.lower()
        list_objects = self.model.objects.all()
        context = {
            f"{model_name}s": list_objects,
        }
        return render(request, f'animal/{model_name}.html' ,context)

class HorseListView(ListView):
    model = Horse
    model_name = model._meta.verbose_name.title().lower()
    template_name =  "animal/"+ model_name + '.html'
    context_object_name = model_name + "s"


class DogListView(HorseListView):
    model = Dog