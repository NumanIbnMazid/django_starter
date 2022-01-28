from django.views.generic import View
from django.shortcuts import render


class HomeView(View):
    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return render(request, "pages/index.html", context=context)

    def get_context_data(self, **kwargs):
        context = {}
        context["meta_description"] = "Standard Django Starter template example. Email: numanibnmazid@gmail.com"
        context["meta_keywords"] = "numan ibn mazid, python, django, standard django starter template, \
            django best practices, django starter template"
        context["meta_author"] = "Numan Ibn Mazid"
        # page contexts
        context["head_title"] = "Home"
        return context
