from django.shortcuts import render, redirect

# Create your views here.

data = {}

def create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        value = request.POST.get('value')
        if name in data:
            data[name].add(value)
        else:
            data[name] = {value}
        # return redirect('/read')
    return render(request, 'create.html')

def read(request):
    return render(request, 'read.html', {'data': data})

def update(request):
    if request.method == 'POST':
        key_to_update = request.POST.get('key_to_update')
        new_value = request.POST.get('new_value')

        if key_to_update in data:
            data[key_to_update] = {new_value}
            return redirect('/read')

    return render(request, 'update.html', {'keys': data.keys()})

def delete(request):
    if request.method == 'POST':
        # Get the name from the form and delete from the dictionary
        name = request.POST.get('key_to_update')
        if name in data:
            del data[name]
    return render(request, 'delete.html',{'keys':data.keys()})
