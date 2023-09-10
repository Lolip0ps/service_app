from rest_framework.viewsets import ReadOnlyModelViewSet
from servises.models import Subscriptions
from servises.serializers import SubscriptionsSerializer


class SubscriptionsView(ReadOnlyModelViewSet):
    queryset = Subscriptions.objects.all()
    serializer_class = SubscriptionsSerializer
