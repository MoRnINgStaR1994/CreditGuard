from django.db import models
from django.contrib.auth.models import User

class Card(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cards')
    title = models.CharField(max_length=250, unique=True)
    is_valid = models.BooleanField(default=True)
    card_number = models.CharField(max_length=16, unique=True, editable=True)
    ccv = models.PositiveBigIntegerField(editable=True)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.censored_number = self.card_number[:6] + '*' * 6 + self.card_number[-4:]
        self.is_valid = self.check_validity()
        super().save(*args, **kwargs)

    def check_validity(self):
        card_number_pairs = [(int(self.card_number[i:i+2])) for i in range(0, len(self.card_number), 2)]
        for x, y in zip(card_number_pairs[::2], card_number_pairs[1::2]):
            if pow(x, pow(y, 3), self.ccv) % self.ccv % 2 != 0:
                return False
        return True

    def __str__(self):
        return self.title
