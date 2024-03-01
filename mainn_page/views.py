from django.shortcuts import render,redirect
from global_page.models import PageGlobalVeraibles, PageTextVeraibles
from .models import Category,Comments,FruitCarts
# Create your views here.
def main_func(request):
    main_page_date = PageGlobalVeraibles.objects.all()
    main_page_text = PageTextVeraibles.objects.all()
    category_all = Category.objects.all()
    fruit = FruitCarts.objects.all() 
    context = {'date1': main_page_date, 'date2':main_page_text,  "fruit": fruit, "category_all": category_all}
    return render(request, 'home.html', context=context)



def category_fiter(request, id=None):
    main_page_date = PageGlobalVeraibles.objects.all()
    main_page_text = PageTextVeraibles.objects.all()
    category_all = Category.objects.all()
    category = Category.objects.get(id=id)
    fruit = FruitCarts.objects.filter(category = category)
    context = {'date1': main_page_date, 'date2':main_page_text,  "fruit": fruit, "category_all": category_all}
    return render(request, 'home.html', context=context)



def product_filter(request, data):
    main_page_date = PageGlobalVeraibles.objects.all()
    main_page_text = PageTextVeraibles.objects.all()
    category_all = Category.objects.all()
    fruit = FruitCarts.objects.all()
    if data == 'Expensive':
        fruit = fruit.order_by('-fruits_price')
    elif data == 'Cheap':
        fruit = fruit.order_by('fruits_price')
    elif data == 'Likes':
        fruit = fruit.order_by('-fruit_likes')
    elif data == 'All':
        fruit = fruit
    context = {'date1': main_page_date, 'date2':main_page_text,  "fruit": fruit, "category_all": category_all}
    return render(request, 'home.html', context=context)




def search_products(request):
    main_page_date = PageGlobalVeraibles.objects.all()
    main_page_text = PageTextVeraibles.objects.all()
    category_all = Category.objects.all()
    product_name = request.POST.get('product_name', '')
    
    if product_name: 
        fruit = FruitCarts.objects.filter(fruit_name__icontains=product_name)
    else:
        fruit = FruitCarts.objects.all()
    
    context = {'date1': main_page_date, 'date2':main_page_text,  "fruit": fruit, "category_all": category_all}
    return render(request, 'home.html', context=context)



def product_detail(request,id):
    main_page_date = PageGlobalVeraibles.objects.all()
    main_page_text = PageTextVeraibles.objects.all()
    category_all = Category.objects.all()
    fruit = FruitCarts.objects.get(id=id)
    fruits_comment = Comments.objects.filter(fruit_comment = fruit).order_by('-comment_time')
    related_products = FruitCarts.objects.filter(category = fruit.category)
    if related_products.count() > 4:
        related_products = related_products.order_by('-id')[:4]
        
    if request.method == 'POST':
        name = request.POST.get('ism')
        email = request.POST.get('email')
        comment_text = request.POST.get('text')
        Comments.objects.create(fruit_comment = fruit, user_name = name, user_email = email, text = comment_text)
        return redirect('product_detail', id=id)
    context = {"fruit": fruit, "fruits_comment":fruits_comment, 'related_products':related_products, 'date1': main_page_date, 'date2':main_page_text, "category_all": category_all}
    return render(request, 'detail.html', context=context)
