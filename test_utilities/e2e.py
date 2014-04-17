import splinter
import django.test
import os
import inspect
import datetime
import django.conf
import django.core.mail
import django.test.utils

class E2ETest(django.test.TestCase):
  def setUp(self):
    try:
      driver = django.conf.settings.E2E_TESTS['BROWSER']['DRIVER']
    except:
      driver = 'chrome'
    self.browser = splinter.Browser(driver)
    self.browser.driver.set_window_size(*self.size)

  @property
  def size(self):
    raise NotImplementedError("Subclasses must define expected browser size")


class E2ETestiPhone(E2ETest):
  @property
  def size(self):
    return (320,500)

class E2ETestXS(E2ETest):
  @property
  def size(self):
    return (480,700)

class E2ETestTabletPortait(E2ETest):
  @property
  def size(self):
    return (768, 1024)

class E2ETestTabletLandscape(E2ETest):
  @property
  def size(self):
    return (1024, 768)

class E2ETestBigDesktop(E2ETest):
  @property
  def size(self):
    return (1200, 1680)

def image_folder_path():
  try:
    path = django.conf.settings.E2E_TESTS['SNAPPER']['FOLDER_PATH']
  except AttributeError:
    path = os.getcwd()

  return path

def image_path(self, caller):
  return '{base}/{now}__{callingclass}__{caller}.png'.format(base=image_folder_path(), now=datetime.datetime.now().isoformat(), caller=caller, callingclass=self.__class__.__name__)

def email_on_failure(original_function):
  @django.test.utils.override_settings(EMAIL_BACKEND='django.core.mail.backends.smtp.EmailBackend')
  def new_function(*args):
    self = args[0]
    caller = 'TODO'
    try:
      original_function(*args)
    except Exception, e:
      mail = django.core.mail.EmailMessage('Test failed: {callingclass} - {caller}'.format(  caller=caller, callingclass=self.__class__.__name__ ), 'Test has failed at {0}'.format(datetime.datetime.now().isoformat()), 'hp@redapesolutions.com', django.conf.settings.E2E_TESTS['RECIPIENTS'])
      if self._path_to_image:
        with open(self._path_to_image, 'r') as f:
          mail.attach('error.png', f.read(), 'image/png')
      mail.send()
      raise e
      
  return new_function

def snap_on_failure(original_function):
  def new_function(*args):
    self = args[0]
    caller = original_function.func_name
    self._name_of_test = caller
    try:
      original_function(*args)
    except Exception, e:
      self._path_to_image = image_path(self, caller)
      self._name_of_test = caller
      self.browser.driver.save_screenshot(self._path_to_image)
      raise e

  return new_function