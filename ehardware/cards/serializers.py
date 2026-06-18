from rest_framework import serializers

from ehardware.cards.models import Card


class CardSerializer(serializers.ModelSerializer[Card]):
    class Meta:
        model = Card
        fields = ["name", "card_number", "expiration", "cvv"]

