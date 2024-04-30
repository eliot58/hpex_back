from django.db import models


class Text(models.Model):
    text = models.TextField(verbose_name='Текст')


    def __str__(self) -> str:
        return str(self.id)

    class Meta:
        verbose_name = 'Текст'
        verbose_name_plural = 'Тексты'

class Agent(models.Model):
    tg_id = models.IntegerField(primary_key=True, verbose_name = "telegram id агента")
    fullName = models.CharField(max_length=256, verbose_name = "ФИО агента")
    date_of_birth = models.DateField(verbose_name = "Дата рождения")
    phone = models.CharField(max_length=256, verbose_name = "Номер телефона")
    username = models.CharField(max_length=256, null = True, blank = True, verbose_name = "telegram username")
    city = models.CharField(max_length=256, verbose_name = "Город")
    transport = models.CharField(max_length=256, verbose_name = "Адрес доставки (ТК)")
    qr_code = models.FileField(upload_to="qr_code", null=True, blank=True, verbose_name = "Qr code агента")
    code = models.CharField(max_length=256, unique=True, verbose_name = "Код агента")
    created = models.DateTimeField(auto_now_add=True, verbose_name = "Дата регистрации")

    def __str__(self) -> str:
        return self.fullName + ' ' + self.code


    class Meta:
        verbose_name = 'Агент'
        verbose_name_plural = 'Агенты'


class Client(models.Model):
    user = models.ForeignKey(Agent, on_delete=models.CASCADE, verbose_name = "Агент клиента")
    fullName = models.CharField(max_length=256, verbose_name = "ФИО клиента")
    phone = models.CharField(max_length=256, verbose_name = "Телефон клиента")
    code = models.CharField(max_length=256, unique=True, verbose_name = "Код клиента")
    city = models.CharField(max_length=256, verbose_name = "Город клиента")
    created = models.DateTimeField(auto_now_add=True, verbose_name = "Дата регистрации")


    def __str__(self) -> str:
        return self.fullName + ' ' + self.code

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


class Track(models.Model):
    file = models.FileField(upload_to="track")

    def __str__(self) -> str:
        return str(self.id)

    class Meta:
        verbose_name = 'Контроль таблица'
        verbose_name_plural = 'Контроль таблицы'


class Ransom(models.Model):
    file = models.FileField(upload_to="ransom")

    def __str__(self) -> str:
        return str(self.id)

    class Meta:
        verbose_name = 'Выкуп таблица'
        verbose_name_plural = 'Выкуп таблицы'