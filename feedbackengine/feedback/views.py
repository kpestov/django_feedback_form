from django.shortcuts import render
from django.views.generic import View
from .forms import FeedbackForm
from django.shortcuts import redirect
from django.urls import reverse


class HomePage(View):
    def get(self, request):
        form = FeedbackForm()
        return render(request, 'feedback/fill_form.html', context={'form': form})

    def post(self, request):
        bound_form = FeedbackForm(request.POST)

        if bound_form.is_valid():
            bound_form.save()
            # return render(request, 'feedback/thanks.html')
            return redirect(reverse('feedback_url'))

        return render(request, 'feedback/fill_form.html', context={'form': bound_form})


