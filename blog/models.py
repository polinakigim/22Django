from django.db import models


class Blog(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name="Заголовок",
        help_text="Введите заголовок",
    )
    content = models.TextField(blank=True, null=True, verbose_name="Содержимое")
    image = models.ImageField(
        upload_to="blog/image",
        blank=True,
        null=True,
        verbose_name="Фото",
        help_text="Загрузите фото",
    )
    number_of_views = models.PositiveIntegerField(
        verbose_name="Колличество просмотров", default=0
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name="Дата последнего изменения"
    )

    is_publication = models.BooleanField(verbose_name="Признак публикации")

    class Meta:
        verbose_name = "Блог"
        verbose_name_plural = "Блоги"
        ordering = ["title", "number_of_views", "created_at"]

    def __str__(self):
        return f"{self.title}"
