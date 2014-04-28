import test_utilities.e2e
import django.test
import django.conf
import django.test.utils
import time

base_url = django.conf.settings.BASE_URL

class LoginTest(test_utilities.e2e.E2ETestBigDesktop):
  def setUp(self):
    super(LoginTest, self).setUp()
    self.browser.visit('{0}/{1}'.format(base_url, ''))

  @test_utilities.e2e.email_on_failure
  @test_utilities.e2e.snap_on_failure
  def _test_failed_login(self):
    browser = self.browser
    browser.click_link_by_text("Login")
    time.sleep(18)
    browser.fill('name','mathieu')
    browser.fill('pass','abcd1234')

    login_button = browser.find_by_id("edit-submit")[0]

    login_button.click()

    self.assertEqual(browser.url, '{0}/{1}'.format(base_url, 'en/user'))

    message_box = browser.find_by_css('.messages')[0]
    self.assertTrue(message_box.has_class('error'))
    self.assertTrue('Sorry' in message_box.text)
  
  @test_utilities.e2e.email_on_failure
  @test_utilities.e2e.snap_on_failure
  def _test_success_login(self):
    browser = self.browser
    browser.click_link_by_text("Login")

    browser.fill('name','jatomitest@gmail.com')
    browser.fill('pass','pleaseohplease')

    login_button = browser.find_by_id("edit-submit")[0]

    login_button.click()

    self.assertEqual(browser.url, '{0}/{1}'.format(base_url, 'jatomi/en/dashboard/overview'))

  @test_utilities.e2e.email_on_failure
  @test_utilities.e2e.snap_on_failure
  def _test_Scenario_1_2_3 (self):
    browser = self.browser
    browser.click_link_by_text("Login")
    
    time.sleep(18)
    browser.fill('name','jatomitest@gmail.com')
    browser.fill('pass','pleaseohplease')

    login_button = browser.find_by_id("edit-submit")[0]
    login_button.click()

    self.assertEqual(browser.url, '{0}/{1}'.format(base_url, 'jatomi/en/dashboard/overview'))
    
    time.sleep(15)
    overview_button = browser.find_by_id('SS')
    overview_button.click()

    Ok_button = browser.find_by_id('Okay')
    Ok_button.click()
  
    download_button = browser.find_by_css('.membershipOverview .pdf')
    download_button.click()
    self.assertEqual(browser.url, '{0}/{1}'.format(base_url, 'jatomi/sites/all/modules/jatomi/user_dashboard/templates/Contractpdf/examples/pdf/Tom.pdf'))
    browser.back()

    time.sleep(15)
    topUp_button = browser.find_by_id('topUp')
    topUp_button.click()
    self.assertEqual(browser.url, '{0}/{1}'.format(base_url, 'jatomi/en/top_up'))
  
  @test_utilities.e2e.email_on_failure
  @test_utilities.e2e.snap_on_failure
  def test_Scenario_4 (self):
    browser = self.browser
    browser.click_link_by_text("Login")
    
    time.sleep(18)
    browser.fill('name','jatomitest@gmail.com')
    browser.fill('pass','pleaseohplease')

    login_button = browser.find_by_id("edit-submit")[0]
    login_button.click()

    self.assertEqual(browser.url, '{0}/{1}'.format(base_url, 'jatomi/en/dashboard/overview'))
    
    time.sleep(10)
    topUp_button = browser.find_by_id('topUp')
    topUp_button.click()
    self.assertEqual(browser.url, '{0}/{1}'.format(base_url, 'jatomi/en/top_up'))
    
    time.sleep(10)
    browser.select("amount","50")
    top_up_submit_button = browser.find_by_id('edit-topupsubmit')
    top_up_submit_button.click()
    time.sleep(10)
    browser.click_link_by_href('http://dev.jatomifitness.com.my/jatomi/myPHP/buytopup.php?Amount=50&amp;PaymentId=330&amp;UserEmail=jatomitest@gmail.com&amp;UserContact=856&amp;Email=jatomitest@gmail.com')
    # top_up_accept_button.click()
    # top_up_cancel_button = browser.find_by_value('Cancel')
    # top_up_cancel_button.click()

    time.sleep(15)
    self.assertEqual(browser.url, 'https://www.mobile88.com/epayment/ConfirmationPage.asp') 
    
    
    



  @test_utilities.e2e.email_on_failure
  @test_utilities.e2e.snap_on_failure
  def _test_list_clubs(self):
    browser = self.browser
    browser.click_link_by_text('Find a Club')
    self.assertEqual(browser.url, '{0}/{1}'.format(base_url, 'jatomi/en/fitness-clubs'))
    # self.assertTrue("Clubs" in browser.title)
    four_rows = browser.find_by_css(".views-row")
    self.assertEqual(four_rows.__len__(), 4)

    for row in four_rows:
      self.assertTrue(row.find_by_tag("img")[0].visible)
      the_button = row.find_by_css(".get-your-guest-pass")
      self.assertEqual(the_button.__len__(), 1)

  @test_utilities.e2e.email_on_failure
  @test_utilities.e2e.snap_on_failure
  def _test_registration_toggle_images(self):
    browser = self.browser  
    browser.click_link_by_text('Sign up')
    time.sleep(18)
    four_rows = browser.find_by_css('.pageRow')
    for row in four_rows:
      four_images = row.find_by_css('img.rowImg')
      for image in four_images:
        if image.has_class("activeImg"):
          self.assertFalse(image.visible)
        else:
          self.assertTrue(image.visible)

      # Click on first col. expect color on first column only
      four_images[0].click()
      time.sleep(0.1)
      self.assertTrue(four_images[1].visible)
      self.assertFalse(four_images[3].visible)

      four_images[2].click()
      time.sleep(0.1)
      self.assertFalse(four_images[1].visible)
      self.assertTrue(four_images[3].visible)

      four_images[0].click()
      time.sleep(0.1)
      self.assertTrue(four_images[1].visible)
      self.assertFalse(four_images[3].visible)


  def tearDown(self):
    self.browser.quit()