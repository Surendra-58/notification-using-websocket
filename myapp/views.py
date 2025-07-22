from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

@csrf_exempt
def admin_notify(request):
    if request.method == 'POST':
        username = request.POST['username']
        message = request.POST['message']
        group_name = f"user_{username}"
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            group_name,
            {
                'type': 'send_notification',
                'message': message
            }
        )
    return render(request, 'admin_notify.html')

def user_notification(request, username):
    return render(request, 'user_notification.html', {'username': username})
