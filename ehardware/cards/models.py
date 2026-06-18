from django.db import models
from users.models import User

# Create your models here.
class Card(models.Model):
    """
    Card Model.
    """

    # First and last name do not cover name patterns around the globe
    name = models.CharField(_("Name of User"), blank=True, max_length=255)
    expiration = models.CharField(_("expiration date"), blank=True, max_length=255)
    cvv = models.CharField(_("Name of User"), blank=True, max_length=255)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="cards")