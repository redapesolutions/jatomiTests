import model_mommy.mommy
import django.contrib.auth

def create_user(**kwargs):
  user = model_mommy.mommy.make(django.contrib.auth.models.User, **kwargs)
  if kwargs.get('password', None) is not None:
    user.set_password(kwargs.get('password', None))
    user.save()

  return user

def create_matiboy(**kwargs):
  kwargs['username'] = 'matiboy'
  kwargs['password'] = 'abcd1234'
  kwargs['is_staff'] = False
  kwargs['email'] = 'mathieu@redapesolutions.com'

  return create_user(**kwargs)

def create_charlie(**kwargs):
  kwargs['username'] = 'charlie'
  kwargs['password'] = 'abcd12345'
  kwargs['is_staff'] = False
  kwargs['email'] = 'charles@redapesolutions.com'

  return create_user(**kwargs)

def create_admin(**kwargs):
  kwargs['username'] = 'admin'
  kwargs['password'] = 'Abcd1234$'
  kwargs['is_staff'] = True
  kwargs['email'] = 'hp@redapesolutions.com'

  return create_user(**kwargs)

def create_superadmin(**kwargs):
  kwargs['username'] = 'root'
  kwargs['password'] = 'supersecretpassword'
  kwargs['is_staff'] = True
  kwargs['is_superuser'] = True
  kwargs['email'] = 'apple@redapesolutions.com'

  return create_user(**kwargs)

