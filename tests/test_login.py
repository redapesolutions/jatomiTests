import test_utilities.e2e
import django.test
import django.conf

base_url = django.conf.settings.BASE_URL

class LoginTest(test_utilities.e2e.E2ETestBigDesktop):
  def setUp(self):
    super(LoginTest, self).setUp()
    self.browser.visit('{0}/{1}'.format(base_url, ''))

  @test_utilities.e2e.email_on_failure
  @test_utilities.e2e.snap_on_failure
  def test_login(self):
    browser = self.browser
    browser.click_link_by_text("Login")
    browser.fill('name','mathieu')
    browser.fill('pass','abcd1234')

    login_button = browser.find_by_id("edit-submit")[0]

    login_button.click()

    self.assertTrue(browser.url, '{0}/{1}'.format(base_url, 'account.html'))