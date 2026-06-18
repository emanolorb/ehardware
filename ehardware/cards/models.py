from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Card(models.Model):
    """
    Card Model.
    """

    # First and last name do not cover name patterns around the globe
    name = models.CharField(_("Name of User"), blank=True, max_length=255)
    card_number = models.CharField(_("Card Number"), blank=True, max_length=255)
    expiration = models.CharField(_("Expiration Date"), blank=True, max_length=255)
    cvv = models.CharField(_("CVV"), blank=True, max_length=255)
    user_id = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="cards")