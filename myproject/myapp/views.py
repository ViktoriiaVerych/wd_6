from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse


entities = [
    {'id': 1, 'name': 'Entity 1', 'description': 'Description for Entity 1'},
    {'id': 2, 'name': 'Entity 2', 'description': 'Description for Entity 2'},
]

def main_page(request):
    return render(request, 'myapp/main_page.html')

def entity_list(request):
    return render(request, 'myapp/entity_list.html', {'entities': entities})

def entity_profile(request, id):
    entity = next((e for e in entities if e['id'] == id), None)
    if entity:
        return render(request, 'myapp/entity_profile.html', {'entity': entity})
    else:
        return HttpResponse("Entity not found", status=404)

def create_entity(request):
    # This is a placeholder for your POST logic
    return JsonResponse({'message': 'Entity created'}, status=201)  # Example response

def delete_entity(request, id):
    # This is a placeholder for your DELETE logic
    return JsonResponse({'message': 'Entity deleted'}, status=204)  # Example response
