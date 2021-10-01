# from django.http import HttpResponse
#page 58

from django.shortcuts import render
from django.template import loader, context
from django.views.generic.edit import CreateView

from .models import Bb, Rubric
from .forms import BbForm

class BbCreateViews(CreateView):
    template_name = "bboard/create.html"
    form_class = BbForm
    success_url = "/bboard/"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics'] = Rubric.objects.all()
        return context


def by_rubric(request, rubric_id):
    bbs = Bb.objects.filter(rubric=rubric_id)
    rubrics = Rubric.objects.all()
    current_rubric = Rubric.objects.get(pk = rubric_id)
    context = {'bbs':bbs, 'rubrics': rubrics, 'current_rubric' : current_rubric}
    return render(request, 'bboard/by_rubric.html', context)

def index(request):
    template = loader.get_template('bboard/index.html')
    bbs = Bb.objects.all()
    rubrics = Rubric.objects.all()

    context = {'bbs': bbs, 'rubrics': rubrics}
    return render(request, 'bboard/index.html', context)