from django.shortcuts import render

def handler404(request, exception):

    context = {
        'error': '404',
        'message': 'The page you are looking for does not exist.',
    }

    response = render(request, 'exception.html', context)
    return response


def handler500(request):

    context = {
        'error': '500',
        'message': 'Something went wrong...',
    }
    
    response = render(request, 'exception.html', context)
    return response


def handler403(request, exception):

    context = {
        'error': '403',
        'message': 'Permission denied.',
    }
    
    response = render(request, 'exception.html', context)
    return response


def handler400(request, exception):

    context = {
        'error': '400',
        'message': 'Bad request, try again later.',
    }
    
    response = render(request, 'exception.html', context)
    return response