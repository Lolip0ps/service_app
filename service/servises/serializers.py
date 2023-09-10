from rest_framework import serializers

from servises.models import Subscriptions, Plan


class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = ("__all__")


class SubscriptionsSerializer(serializers.ModelSerializer):
    plan = PlanSerializer()
    client_name = serializers.CharField(source='client.company_name')
    email = serializers.CharField(source='client.user.email')

    class Meta:
        model = Subscriptions
        fields = ('id', 'plan_id', 'client_name', 'email', 'plan')
