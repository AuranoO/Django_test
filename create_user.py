import random
from helloworldapp.models import Person
from faker import Faker
fake = Faker()

#%%
Person.objects.all()
line = Person(name="ana les", age="15")
line.save()

#%%
for i in range(10):
    d = Person(name=fake.name(), age=random.randint(20, 80))
    print(d)
    d.save()
