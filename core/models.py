from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


# Create your models here.

class AbstractModel(models.Model):
    updated_date = models.DateTimeField(
        blank=True,
        auto_now=True,
        verbose_name='Updated Date',
        help_text='',
    )
    created_date = models.DateTimeField(
        blank=True,
        auto_now_add=True,
        verbose_name='Created Date',
        help_text='',
    )

    class Meta:
        abstract = True


class GeneralSetting(AbstractModel):
    name = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Name',
        help_text='',
    )
    description = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Description',
        help_text='',
    )
    parameter = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Parameter',
        help_text='',
    )

    def __str__(self):
        return f'General Setting {self.name}'

    class Meta:
        verbose_name = 'General Setting'
        verbose_name_plural = 'General Settings'
        ordering = ('id',)


class ImageSetting(AbstractModel):
    name = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Name',
        help_text='',
    )
    description = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Description',
        help_text='',
    )
    file = models.ImageField(
        default='',
        verbose_name='Image',
        help_text='',
        blank=True,
        upload_to='images/',
    )

    def __str__(self):
        return f'Image Setting {self.name}'

    class Meta:
        verbose_name = 'Image Setting'
        verbose_name_plural = 'Image Settings'
        ordering = ('id',)


class Skill(AbstractModel):
    order = models.IntegerField(
        default=0,
        verbose_name='Order'
    )
    name = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name='Name',
        help_text='',
    )
    percentage = models.IntegerField(
        default=50,
        verbose_name='Percentage',
        validators=[MinValueValidator(0), MaxValueValidator(100)],
    )

    def __str__(self):
        return f'Skill: {self.name}'

    class Meta:
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'
        ordering = ('order',)


class Experience(AbstractModel):
    company_name = models.CharField(
        default="",
        max_length=254,
        blank=True,
        verbose_name='Company Name'
    )
    job_title = models.CharField(
        default="",
        max_length=254,
        blank=True,
        verbose_name='Job Title',
    )
    job_location = models.CharField(
        default="",
        max_length=254,
        blank=True,
        verbose_name='Job Location',
    )
    start_date = models.DateField(
        verbose_name='Start Date',
    )
    end_date = models.DateField(
        default=None,
        null=True,
        blank=True,
        verbose_name='End Date',
    )

    def __str__(self):
        return f'Experience: {self.company_name}'

    class Meta:
        verbose_name = 'Experience'
        verbose_name_plural = 'Experiences'
        ordering = ('start_date',)


class Education(AbstractModel):
    school_name = models.CharField(
        default="",
        max_length=254,
        blank=True,
        verbose_name='School Name'
    )
    major = models.CharField(
        default="",
        max_length=254,
        blank=True,
        verbose_name='Major',
    )
    department = models.CharField(
        default="",
        max_length=254,
        blank=True,
        verbose_name='Department',
    )
    start_date = models.DateField(
        verbose_name='Start Date',
    )
    end_date = models.DateField(
        default=None,
        null=True,
        blank=True,
        verbose_name='End Date',
    )

    def __str__(self):
        return f'Experience: {self.school_name}'

    class Meta:
        verbose_name = 'Education'
        verbose_name_plural = 'Education'
        ordering = ('start_date',)


class SocialMedia(AbstractModel):
    order = models.IntegerField(
        default=0,
        verbose_name='Order'
    )
    link = models.URLField(
        default="",
        max_length=254,
        blank=True,
        verbose_name='Link',
    )
    icon = models.CharField(
        default="",
        max_length=254,
        blank=True,
        verbose_name='Icon',
    )

    def __str__(self):
        return f'Experience: {self.link}'

    class Meta:
        verbose_name = 'Social Media'
        verbose_name_plural = 'SocialMedia'
        ordering = ('order',)

class Document(AbstractModel):
    order = models.IntegerField(
        default=0,
        verbose_name='Order'
    )
    slug = models.SlugField(
        default="",
        max_length=254,
        blank=True,
        verbose_name='Slug',
    )
    button_text = models.CharField(
        default="",
        max_length=254,
        blank=True,
        verbose_name='Button Text',
    )
    file = models.FileField(
        default="",
        verbose_name='File',
        blank=True,
        upload_to='documents/',
    )

    def __str__(self):
        return f'Document: {self.slug}'

    class Meta:
        verbose_name = 'Document'
        verbose_name_plural = 'Documents'
        ordering = ('order',)
