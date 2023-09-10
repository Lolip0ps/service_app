from rest_framework import serializers

from servises.models import Subscriptions


class SubscriptionsSerializer(serializers.ModelSerializer):
    client_name = serializers.CharField(source='client.company_name')
    email = serializers.CharField(source='client.user.email')

    class Meta:
        model = Subscriptions
        fields = ('id', 'plan_id', 'client_name', 'email')
