from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator, MaxValueValidator, RegexValidator
# from django.utils.translation import gettext_lazy as _
#
# from .manager import CustomerManager, BusinessManager


class User(AbstractUser):

    # class Types(models.TextChoices):
    #     customer = "CUSTOMER", "Customer"
    #     business = "BUSINESS", "Business"
    #     both = "BOTH", "Both"
    #
    # base_type = Types.customer
    # type = models.CharField(_("Type of User"), max_length=50, choices=Types.choices, default=base_type)
    # USERNAME_FIELD = 'email'

    is_customer = models.BooleanField(default=True)
    is_business = models.BooleanField(default=False)


# class Customer(User):
#     base_type = User.Types.customer
#     objects = CustomerManager()
#
#     def save(self, *args, **kwargs):
#         if not self.id:
#             self.type = User.Types.customer
#         return super().save(*args, **kwargs)
#
#     class Meta:
#         proxy = True
#
#
# class Business(User):
#     base_type = User.Types.business
#     objects = BusinessManager()
#
#     def save(self, *args, **kwargs):
#         if not self.id:
#             self.type = self.base_type
#         return super().save(*args, **kwargs)
#
#     class Meta:
#         proxy = True


class MasterCountry(models.Model):
    name = models.CharField(max_length=150, unique=True)
    code = models.CharField(max_length=50, null=True, blank=True)
    dial_code = models.IntegerField(null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    update_on = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Countries"


class MasterState(models.Model):
    country = models.ForeignKey(MasterCountry, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    code = models.CharField(max_length=50, null=True, blank=True)
    tin = models.IntegerField(null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    update_on = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.country.name + " >> " + self.name

    class Meta:
        verbose_name_plural = "States"
        unique_together = (('country', 'name'), ('country', 'code'), ('country', 'tin'),)


class MasterCity(models.Model):
    state = models.ForeignKey(MasterState, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    code = models.CharField(max_length=50, null=True, blank=True)
    # Not unique across globe
    pincode = models.IntegerField(null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    update_on = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.state.country.name + " >> " + self.name

    class Meta:
        verbose_name_plural = "Cities"
        unique_together = (('state', 'name'), ('state', 'code'))


class MasterBusiness(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    country = models.ForeignKey(MasterCountry, on_delete=models.SET_NULL, null=True)
    state = models.ForeignKey(MasterState, on_delete=models.SET_NULL, null=True)
    city = models.ForeignKey(MasterCity, on_delete=models.SET_NULL, null=True)

    avatar = models.ImageField(null=True, blank=True)
    display_name = models.CharField(_("Business Name"), max_length=255)
    legal_name = models.CharField(_("Legal Business Name"), max_length=255, null=True, blank=True)
    # phone_regex = RegexValidator(regex=r"^\+?1?\d{8,15}$")
    # phoneNumber = models.CharField(validators=[phone_regex], max_length=16, unique=True)
    phone = models.IntegerField(unique=True, validators=[MinValueValidator(1111111111)])
    email = models.EmailField(_("Business Email"), null=True, blank=True)
    address = models.CharField(_("Address of User"), max_length=500, null=True, blank=True)
    gst = models.CharField(null=True, blank=True, max_length=50)
    pan = models.CharField(null=True, blank=True, max_length=50)
    created_on = models.DateTimeField(auto_now_add=True)
    update_on = models.DateTimeField(auto_now=True)
    # If not deactivated
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    # After certain bookings will not be visible to customers
    is_visible = models.BooleanField(default=True)
    is_banned = models.BooleanField(default=False)

    def __str__(self):
        return self.display_name

    class Meta:
        verbose_name_plural = "Businesses"


class MasterCustomer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    country = models.ForeignKey(MasterCountry, on_delete=models.SET_NULL, null=True)
    state = models.ForeignKey(MasterState, on_delete=models.SET_NULL, null=True)
    city = models.ForeignKey(MasterCity, on_delete=models.SET_NULL, null=True)

    # First & Last name do not cover global names
    avatar = models.ImageField(null=True, blank=True)
    name = models.CharField(max_length=255)
    phone = models.IntegerField(unique=True, validators=[MinValueValidator(1111111111)])
    email = models.EmailField(null=True, blank=True)
    dob = models.DateField(_('Customer Email'), null=True, blank=True)
    address = models.CharField(_("Address of User"), max_length=500, null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    update_on = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Customers"



