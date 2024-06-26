from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse

data = {
    "programlama":"programlama kurs sayfasi",
    "web-gelistirme":"web gelistirme kurs sayfasi",
    "mobil":"mobil kurs sayfasi",
}

def kurslar(request):
    return HttpResponse('Kurslar Hakkinda: ')

def kurs_liste(request):
    return HttpResponse('Kurs Listesi: ')

def details(request, kurs_adi):
    return HttpResponse(f'{kurs_adi} kursu detay sayfasi')

def getCoursesByCategory(request, category_name): 
    try:
        category_text = data[category_name]
        return HttpResponse(category_text)
    except:
        return HttpResponseNotFound('Sayfa bulunamadi. E404')

def getCoursesByCategoryID(request, category_id):
    category_list = list(data.keys())

    if(category_id > len(category_list) or category_id < 1):
        return HttpResponseNotFound('Sayfa bulunamadi. E404')

    category_name = category_list[category_id - 1]

    redirect_url = reverse('course_by_category', args=[category_name])

    return redirect(redirect_url)
 