import random
import string
from django.db import models

class ShortenUrlManager(models.Manager):
    def code_generator(self, size=8, chars=string.ascii_lowercase + string.digits):
        return ''.join(random.choice(chars) for _ in range(size))
    
    def create_unique_code(self):
        new_code = self.code_generator()
        code_exists = self.filter(shortcode=new_code).exists()
        if code_exists:
            return self.create_unique_code()
        return new_code

    def create(self, *args, **kwargs):
        if 'shortcode' not in kwargs:
            shortcode = self.create_unique_code()
            kwargs['shortcode'] = shortcode
        return super(ShortenUrlManager, self).create(*args, **kwargs)