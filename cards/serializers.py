from rest_framework import serializers
from .models import Card

class CardSerializer(serializers.ModelSerializer):
   

    class Meta:
        model = Card
        fields = ['id', 'user', 'title',  'is_valid', 'card_number', 'ccv', ]
        read_only_fields = ['user',  'is_valid', ]

    def validate_card_number(self, value):
        if len(value) != 16 or not value.isdigit():
            raise serializers.ValidationError("Card number must be exactly 16 digits and contain only numbers.")
        return value

    def validate_ccv(self, value):
        if not (100 <= value <= 999):
            raise serializers.ValidationError("CCV must be a three-digit number between 100 and 999.")
        return value

    def validate(self, data):
        card_number = data.get('card_number')
        ccv = data.get('ccv')

        if card_number is None:
            raise serializers.ValidationError({"card_number": "Card number is required."})
        if ccv is None:
            raise serializers.ValidationError({"ccv": "CCV is required."})

        card_number_pairs = [(int(card_number[i:i+2])) for i in range(0, len(card_number), 2)]

        for x, y in zip(card_number_pairs[::2], card_number_pairs[1::2]):
            if pow(x, pow(y, 3), ccv) % ccv % 2 != 0:
                raise serializers.ValidationError({"card_number": "The card is invalid based on the provided criteria."})

        return data
