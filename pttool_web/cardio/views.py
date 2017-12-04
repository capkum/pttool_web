from django.shortcuts import render


def index(request, pk):
    if request.method == 'POST':
        print(pk)
        pass

    else:
        print(pk)
        return render(request, 'cardio/time_table.html', {})
