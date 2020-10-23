from django.db import models
from django.urls import reverse

from .data import jobs, companies, cities, specialties, level
from django.contrib.auth.models import User
from random import choice, shuffle
from .utils import skill_maker, user_maker


class Company(models.Model):
    name = models.CharField(max_length=32, verbose_name="Компания", unique=True)
    location = models.CharField(max_length=32, verbose_name="Город", blank=True, null=True)
    logo = models.ImageField(verbose_name="Логотип", upload_to="MEDIA_COMPANY_IMAGE_DIR", blank=True, null=True)
    description = models.TextField(verbose_name="Информация о компании", blank=True, null=True)
    employee_count = models.IntegerField(verbose_name="Количество сотрудников", null=True, blank=True)
    owner = models.OneToOneField(User, related_name="company", on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('company', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Компания"
        verbose_name_plural = "Компании"


class Specialty(models.Model):
    code = models.CharField(max_length=32, verbose_name="Код", unique=True)
    slug = models.SlugField(unique=True)
    title = models.CharField(max_length=32, verbose_name="Специализация")
    picture = models.ImageField(verbose_name="Картинка", upload_to="MEDIA_SPECIALITY_IMAGE_DIR", blank=True, null=True)

    def get_absolute_url(self):
        return reverse('specialties', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Специализация"
        verbose_name_plural = "Специализации"


class Vacancy(models.Model):
    title = models.CharField(max_length=64, verbose_name="Профессия")
    specialty = models.ForeignKey(Specialty, related_name="vacancies", on_delete=models.CASCADE)
    company = models.ForeignKey(Company, related_name="vacancies", on_delete=models.CASCADE)
    skills = models.TextField(verbose_name="Навыки")
    level = models.CharField(max_length=16, verbose_name="Уровень")
    description = models.TextField(verbose_name="Описание", blank=True, null=True)
    salary_min = models.IntegerField(verbose_name="Зарплата от")
    salary_max = models.IntegerField(verbose_name="Зарплата до")
    published_at = models.DateField(verbose_name="Опубликовано", auto_now_add=True)

    def get_absolute_url(self):
        return reverse('vacancy', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Вакансия"
        verbose_name_plural = "Вакансии"
        ordering = ['-published_at']


#                                                  --- week 4 ---

class Application(models.Model):
    written_username = models.CharField(max_length=32, verbose_name="Вас зовут")
    written_phone = models.CharField(max_length=32, verbose_name="Ваш телефон")
    written_cover_letter = models.TextField(verbose_name="Сопроводительное письмо")
    vacancy = models.ForeignKey(Vacancy, related_name="applications", on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name="applications", on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('application', kwargs={'pk': self.pk})

    def __str__(self):
        return self.written_username

    class Meta:
        ordering = ['written_username']
        verbose_name = "Отклик"
        verbose_name_plural = "Отклики"


class UserResume(models.Model):
    EducationChoices = {
        ('Отсутствует', 'Отсутствует'),
        ('Среднее', 'Среднее'),
        ('Средне-специальное', 'Средне-специальное'),
        ('Неполное высшее', 'Неполное высшее'),
        ('Высшее', 'Высшее'),
    }

    GradeChoices = {
        ('intern', 'intern'),
        ('junior', 'junior'),
        ('middle', 'middle'),
        ('senior', 'senior'),
        ('lead', 'lead'),
    }
    WorkStatusChoices = {
        ('Не ищу работу', 'Не ищу работу'),
        ('Рассматриваю предложения', 'Рассматриваю предложения'),
        ('Ищу работу', 'Ищу работу'),
    }

    user = models.OneToOneField(User, related_name="resume", on_delete=models.CASCADE, verbose_name="Юзер")
    first_name = models.CharField(max_length=32, verbose_name="Имя")
    last_name = models.CharField(max_length=32, verbose_name="Фамилия")
    readiness = models.CharField(
        max_length=32,
        choices=WorkStatusChoices, verbose_name="Готовность")
    salary = models.PositiveIntegerField(verbose_name="Хочу")
    specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE, verbose_name="Специализация")
    level = models.CharField(
        max_length=32,
        choices=GradeChoices, verbose_name="Крутость")
    education = models.CharField(
        max_length=32,
        choices=EducationChoices, verbose_name="Образование")
    experience = models.TextField(verbose_name="Опыт")
    portfolio = models.CharField(max_length=32)

    def get_absolute_url(self):
        return reverse('updresume', kwargs={'pk': self.pk})

    def __str__(self):
        return ' '.join((self.first_name, self.last_name))

    class Meta:
        verbose_name = "Резюме"
        verbose_name_plural = "Резюме"


def random_database():
    # число юзеров, компаний, специальностей, вакансий = ....
    num_users, num_companies, num_specialties, num_vacancies = 40, 8, 8, 40
    somelist = list(range(40))
    shuffle(somelist)

    if User.objects.count() < num_users:
        for i in range(num_users):
            name, mail, password = user_maker(i)
            User.objects.create_user(username=name, email=mail, password=password)

    c = 0
    for company in companies:
        c += 1
        if Company.objects.count() < num_companies:
            Company.objects.create(
                name=company['title'], location=choice(cities),
                employee_count=choice(list(range(1, 500))),
                owner=User.objects.get(username=str('username' + str(somelist[c])))
            )

    for specialty in specialties:
        if Specialty.objects.count() < num_specialties:
            Specialty.objects.create(code=specialty['code'], slug=specialty['code'], title=specialty['title'])

    for job in jobs:
        if Vacancy.objects.count() < num_vacancies:
            Vacancy.objects.create(
                title=job['title'],
                specialty=Specialty.objects.filter(code=job['cat'])[0],
                company=Company.objects.filter(name=job['company'])[0],
                skills=skill_maker(6), level=choice(level), description=job['desc'],
                salary_min=job['salary_from'], salary_max=job['salary_to'],
            )

# раскомментировать при создании базы данных до создания суперюзера:
# random_database()
