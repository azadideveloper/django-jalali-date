from django.shortcuts import render
from.froms import TestForm

from django.views .generic.edit import CreateView
from.models import Test




class CreateView(CreateView):
    model = Test
    form_class = TestForm
    template_name = "test.html"
    success_url = '/'




