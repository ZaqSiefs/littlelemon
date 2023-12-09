from django.shortcuts import render
from django.urls import reverse
from django.utils import timezone
from django.views.generic.edit import FormView
from .forms import BookingForm
import json, requests

def index(request):
    return render(request, 'restaurant/index.html', {})


def about(request):
    return render(request, 'restaurant/about.html')


def menu(request):
    url = f"http://127.0.0.1:8000{reverse('api:menu-list')}"
    response = requests.get(url)
    return render(request, 'restaurant/menu.html', context={'menu_item': json.loads(response.text)})


def menu_item(request, pk):
    url = f"http://127.0.0.1:8000{reverse('api:menu-detail', kwargs={'pk': pk})}"
    response = requests.get(url)
    return render(request, 'restaurant/menu_item.html', context={'menu_item': json.loads(response.text)})


class Book(FormView):
    form_class = BookingForm
    template_name = 'restaurant/book.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def get_data_from_form(self, form):
        data = {
            'name': form.cleaned_data.get('name'),
            'no_of_guests': form.cleaned_data.get('no_of_guests'),
            'booking_date': form.cleaned_data.get('booking_date'),
        }
        return data

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            data = self.get_data_from_form(form)
            url = f"http://127.0.0.1:8000{reverse('api:book-detail')}"
            response = requests.post(url, data=data)
            if response.status_code == 201:
                context = {'form': BookingForm()}
                return render(request, 'restaurant/book.html', context)
        context = {'form': form}
        return render(request, 'restaurant/book.html', )


def bookings(request):
    if request.GET.get('date') is None:
        date = timezone.now().date()
    else:
        date = request.GET.get('date')
    url = f"http://127.0.0.1:8000{reverse('api:bookings-list')}?date={date}"
    response = requests.get(url)
    return render(request, 'restaurant/bookings.html', context={'bookings': response.text})