from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'game_category'
        verbose_name = "category"
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name


class Game(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='media', null=True, blank=True) # We can use bucket for store media files
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='games'
    )

    class Meta:
        db_table = 'game'
        verbose_name = "game"
        verbose_name_plural = "games"

    def __str__(self):
        return self.name