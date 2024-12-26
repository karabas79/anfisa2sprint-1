from django.shortcuts import render

from .forms import ContestForm


def proposal(request):
    form = ContestForm(request.GET or None)
    # birthday_countdown = None
    context = {'form': form}
    # if form.is_valid():
    #     # ...вызовем функцию подсчёта дней:
    #     birthday_countdown = calculate_birthday_countdown(
    #         # ...и передаём в неё дату из словаря cleaned_data.
    #         form.cleaned_data['birthday']
    #     )
    # context.update({'birthday_countdown': birthday_countdown})
    return render(request, 'contest/form.html', context=context)
