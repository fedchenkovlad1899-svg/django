import os
from django.db import models
from django.contrib import admin
from config.models import BaseModel
from django.db.models.signals import post_delete
from django.dispatch import receiver



class Attachments(BaseModel):
    name= models.CharField(
        max_length=64,
        unique=True,
        verbose_name= 'Наименование'
    )
    task = models.ForeignKey(
        to = "Tasks",
        related_name = "attachments",
        on_delete = models.CASCADE,
    )

    photo = models.ImageField(
        upload_to="attachments",
        null=True,
        blank=True,
        verbose_name="Фото"
    )

    file = models.FileField(
        upload_to="attachments",
        null=True,
        blank=True,
        verbose_name="Файл"
    )

    class Meta:
        ordering = ['name']
        db_table = "attachments"
        verbose_name= "Вложение"
        verbose_name_plural= "Вложения"

    def __str__(self):
        return self.name

    def delete(self, *args, **kwargs):

        if self.photo:
            self.photo.delete(save=False)

        if self.file:
            self.file.delete(save=False)

        super().delete(*args, **kwargs)

