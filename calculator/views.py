
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


# Static data for categories and features
CATEGORIES = {
    "E-commerce": {"Product Listing": 30, "Payment Integration": 25},
    "Social Media": {"User Profiles": 30, "Chat System": 40},
    "Cloud Kitchen": {"Menu Display": 25, "Online Ordering": 40},
}
HOURLY_RATE = 10

def index(request):
    return render(request, 'calculator/index.html', {'categories': CATEGORIES})

@csrf_exempt
def calculate_cost(request):
    if request.method == "POST":
        category = request.POST.get('category')
        features = request.POST.getlist('features[]')

        total_hours = sum([CATEGORIES[category][feature] for feature in features])
        total_cost = total_hours * HOURLY_RATE

        return JsonResponse({'total_cost': total_cost})
    return JsonResponse({'error': 'Invalid request'}, status=400)
