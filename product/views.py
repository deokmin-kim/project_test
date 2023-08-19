from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import Product, ImageUpload
from .forms import ImageUploadForm

def main_page(request):
    return render(request, 'product/home.html')

def product_list(request):
    products = Product.objects.all()
    return render(request, 'product/product_list.html', {'products': products})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product/product_detail.html', {'product': product})


def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = ImageUploadForm()
    return render(request, 'upload_image.html', {'form': form})

def main(request):
    # 이미지 모델에서 이미지 하나 가져오기 (실제로는 원하는 방식으로 이미지를 가져오세요)
    main_image = ImageUpload.objects.first()
    context = {'image_url': main_image.image.url if main_image else ''}
    return render(request, 'main.html', context)