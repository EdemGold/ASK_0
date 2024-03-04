from django.db import models

class ReferredDoctor(models.Model):
    name = models.CharField(max_length=100)
    telephone = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Service(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class Patient(models.Model):
    full_name = models.CharField(max_length=200)
    sex = models.CharField(max_length=10)
    age = models.IntegerField()
    telephone = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return self.full_name

class PatientRequisition(models.Model):
    date = models.DateField()
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, null=True, blank=True)
    referred_by = models.ForeignKey(ReferredDoctor, on_delete=models.CASCADE)
    requisitions = models.ManyToManyField(Service)
    discount = models.DecimalField(max_digits=5, decimal_places=2)  # Add the discount field here
    total_amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    total_amount_owed = models.DecimalField(max_digits=10, decimal_places=2, editable=False)

    @property
    def total_price(self):
        return sum(service.price for service in self.requisitions.all())

    @property
    def payable_amount(self):
        return self.total_price * (1 - self.discount / 100)

    def save(self, *args, **kwargs):
        if self.patient:
            self.patient.save()
        self.total_amount_owed = self.payable_amount - self.total_amount_paid
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Patient: {self.patient.full_name if self.patient else 'Unregistered'}, Date: {self.date}"
