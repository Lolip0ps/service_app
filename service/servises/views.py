from django.db.models import Prefetch
from rest_framework.viewsets import ReadOnlyModelViewSet

from clients.models import Client
from servises.models import Subscriptions
from servises.serializers import SubscriptionsSerializer


class SubscriptionsView(ReadOnlyModelViewSet):
    queryset = Subscriptions.objects.all().prefetch_related(
        'plan',
        Prefetch('client', queryset=Client.objects.all().select_related('user').only('company_name', 'user__email'))
    )
    serializer_class = SubscriptionsSerializer
