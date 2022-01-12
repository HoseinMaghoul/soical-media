from django.contrib.auth.models import BaseUserManager



class MyUserManager(BaseUserManager):
    
    def crate_user(self, email, full_name, pasword):
        if not email:
            raise ValueError('user must have email!', 'danger')
        if not full_name:
            raise ValueError('user must have fullname', 'danger')

        
        user = self.model(email=self.normalize_email(email), full_name=full_name)
        user.set_password(pasword)
        user.save(using=self._db)
        return user 

    
    def create_superuser(self, email, full_name, password):
        user = self.create_user(email, full_name, password)
        user.is_admin = True
        user.save(using=self._db)
        return user 