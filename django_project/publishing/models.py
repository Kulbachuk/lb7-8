from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Author(models.Model):
    name = models.CharField(max_length=100, verbose_name="Ім'я автора")
    email = models.EmailField(unique=True, verbose_name="Email")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата реєстрації")

    class Meta:
        ordering = ['name']
        verbose_name = "Автор"
        verbose_name_plural = "Автори"

    def __str__(self):
        return self.name


class AuthorProfile(models.Model):
    author = models.OneToOneField(
        Author, 
        on_delete=models.CASCADE, 
        related_name='profile',
        verbose_name="Автор"
    )
    bio = models.TextField(blank=True, verbose_name="Біографія")
    rating = models.FloatField(
        default=5.0, 
        validators=[MinValueValidator(1.0), MaxValueValidator(5.0)],
        verbose_name="Рейтинг"
    )

    class Meta:
        ordering = ['-rating']
        verbose_name = "Профіль автора"
        verbose_name_plural = "Профілі авторів"

    def __str__(self):
        return f"Профіль: {self.author.name}"


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name="Тег")
    slug = models.SlugField(max_length=50, unique=True, verbose_name="Слаг")

    class Meta:
        ordering = ['name']
        verbose_name = "Тег"
        verbose_name_plural = "Теги"

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=150, verbose_name="Назва книги")
    price = models.DecimalField(
    max_digits=8, 
    decimal_places=2, 
    validators=[MinValueValidator(0)], 
    verbose_name="Ціна (грн)"
    )
    description = models.TextField(verbose_name="Опис")
    published_year = models.IntegerField(default=2026, verbose_name="Рік видання")
    is_available = models.BooleanField(default=True, verbose_name="Доступна")
    isbn = models.CharField(max_length=13, blank=True, null=True, verbose_name="ISBN")
    
    author = models.ForeignKey(
        Author, 
        on_delete=models.PROTECT, 
        related_name='books',
        verbose_name="Автор"
    )
    tags = models.ManyToManyField(Tag, related_name='books', blank=True, verbose_name="Теги")

    class Meta:
        ordering = ['-published_year', 'title']
        verbose_name = "Книга"
        verbose_name_plural = "Книги"

    def __str__(self):
        return f"{self.title} ({self.published_year})"