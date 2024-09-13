from django.shortcuts import render, get_object_or_404

from .models import Drawing, Category


def drawing_gallery(request, category_id=None):
    request.session['last_viewed_category'] = category_id  # Store the category in session
    categories = Category.objects.all()
    if category_id:
        drawings = Drawing.objects.filter(category_id=category_id)
    else:
        drawings = Drawing.objects.all()
    drawings = drawings.order_by('-upload_date')
    return render(request, 'drawings/gallery.html', {'drawings': drawings, 'categories': categories})


def drawing_detail(request, pk):
    drawing = get_object_or_404(Drawing, pk=pk)
    last_viewed_category = request.session.get('last_viewed_category')  # Retrieve category from session
    return render(request, 'drawings/detail.html', {'drawing': drawing, 'last_viewed_category': last_viewed_category})
