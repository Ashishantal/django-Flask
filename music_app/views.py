from django.shortcuts import render # type: ignore


from django.core.paginator import Paginator
from . models import Song



def index(request):
    paginator= Paginator(Song.objects.all(),1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    all_songs = Song.objects.all()
    context={"page_obj":page_obj, 'all_songs': all_songs}
    return render(request,"index.html",context)
