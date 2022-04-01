import datetime
from django.db.models import Sum,Avg,Count
from django.utils import timezone
def by_range(self ,start_date, end_date=None):
    if end_date is None:
        return self.filter(timestamp__gte=start_date)
    return self.filter(timestamp__gte=start_date).filter(timestamp__lte=end_date)

def by_weeks_range(self ,weeks_ago=1 ,numbers_of_weeks=1):
    if numbers_of_weeks >weeks_ago:
        numbers_of_weeks =weeks_ago
    days_ago_start =weeks_ago *7
    days_ago_end =days_ago_start -(numbers_of_weeks *7)
    print(days_ago_end)
    start_date = timezone.now() - datetime.timedelta(days=days_ago_start)
    end_date = timezone.now() - datetime.timedelta(days=days_ago_end)
    return self.by_range(start_date ,end_date=end_date)
    return by_weeks_range(weeks_ago=10,numbers_of_weeks=10)