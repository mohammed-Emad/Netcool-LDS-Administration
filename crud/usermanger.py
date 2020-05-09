from django.utils import timezone
from django.contrib.auth.models import BaseUserManager

def update_last_login(sender, user, **kwargs):
	user.last_login = timezone.now()
	user.save(update_fields=['last_login'])


class UserManager(BaseUserManager):

	def create_user(self,  username, email, password=None, is_admin=False, is_staff=False, is_active=True):

		if not username:
			raise ValueError('Users must have a username ')
		if not email:
			raise ValueError('Users must have an emaill.')
		if not password:
			raise ValueError('Users must have a password')

		user_obj =	self.model(username=username,
			email=self.normalize_email(email),
			)
		user_obj.set_password(password)
		user_obj.admin  = is_admin
		user_obj.staff  = is_staff
		user_obj.active = is_active
		user_obj.save(using=self._db)

		return user_obj
	def create_staffuser(self, email, username, password=None):
		user = self.create_user(email=email, username=username, password=password, is_staff=True)
		return user

	def create_superuser(self, email, username, password=None):
		user = self.create_user(email=email, username=username, password=password)
		user.is_staff=True
		user.is_admin=True
		user.save(using=self._db)
		return user