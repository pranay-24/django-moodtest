from django.http import JsonResponse, HttpResponse
from django.core.paginator import Paginator
# from .models import Product
from .models import Transaction
from .models import Mood
#pagination ,filtering, sorting
 
# def filter (request):
#     category = request.GET.get("category")
#     if(category):
#         products = Product.objects.filter(category = category)
#     else:
#         products = Product.objects.all()
#     serialized_data = [{'id':item.id, 'name': item.name ,'price':item.price }for item in products]
#     return JsonResponse({'products': serialized_data})

# def filter_transaction(requests):
#     mood = Transaction.GET.get("mood")
    
#     if(mood):
#         transactions = Transaction.objects.filter(mood = mood)
#     else:
#         transactions = Transaction.objects.all()
        
#     serialized_data = [{'title':tx.title , 'value':tx.value , 'mood': tx.mood} for tx in transactions ]
#     return JsonResponse({'transactions': serialized_data})


# def paginated_result(request):
#     queryset = Transaction.objects.all()
#     per_page = 10
#     page_number = request.GET.get("page", 1)
    
#     paginator = Paginator(queryset, per_page)
#     try:
#         page_object = paginator.page(page_number)
    
#     except EmptyPage:
#         return JsonResponse({'data': [], 'message':'page is ot of range'}, status=404)
        
#     serialized_data = [{'title':item.title, 'value':item.value, 'mood':item.mood} for item in page_object]
#     return JsonResponse({'data':serialized_data , 'current_page': page_number, 'total_pages' : paginator.num_pages  })

# def sortTransactions(request):
#     sort_by = request.GET.get("sort_by",'date')
    
#     sort_order =   request.GET.get("sort_order","asc") if request.GET.get("sort_order",'asc') in ['asc','desc'] else 'asc'
#     sorted_transaction = Transaction.objects.all().order_by(f'{sort_by}' if sort_order == 'asc' else f'-{sort_by}')    
    
#     serialized_data =  [{'title':tx.title , 'value':tx.value , 'mood': tx.mood} for tx in sorted_transaction ]
#     return JsonResponse({'sorted_transactions': serialized_data})