from django.db import models
from django.contrib.auth.models import AbstractUser

# Дочерний класс от AbstractUser (от Django - auth.models)
class User(AbstractUser):
    # Добавляем новое поле - фото (будут хранятся в media/users_images)
    image = models.ImageField(upload_to="users_images", blank=True)

