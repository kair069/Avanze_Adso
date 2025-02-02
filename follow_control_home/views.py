from django.shortcuts import render

from follow_control_backlog.utils import get_current_month_dates
from follow_control_card.models import Card

def HomeCC(request):
    if not request.user.is_authenticated:
        return render(request, 'follow_control_home.html', {'cards': []})

    month_data = get_current_month_dates()

    cards = Card.objects.filter(
        user=request.user,
        date__range=(month_data['start_of_month'], month_data['end_of_month'])
    ).exclude(date__week_day=1)

    for card in cards:
        card.update_card_values()

    return render(request, 'home_cc.html', {
        'cards': cards,
        'empty_days': month_data['empty_days'],
        'days_in_month': month_data['days_in_month'],
    })
