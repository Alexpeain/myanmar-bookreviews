from books.models import Genre

def genres_processor(request):
    all_genres = Genre.objects.all()
    return {'genres': all_genres}