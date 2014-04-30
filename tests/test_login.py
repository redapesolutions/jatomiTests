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
  def _test_Scenario_4 (self):
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
    
    time.sleep(20)
    #browser.click_link_by_partial_href('http://dev.jatomifitness.com.my/jatomi/myPHP/buytopup.php?Amount=50&amp;PaymentId=560&amp;UserEmail=jatomitest@gmail.com&amp;UserContact=856&amp;Email=jatomitest@gmail.com')
    #browser.find_link_by_text('Proceed').click()
    accept_button = browser.find_by_class('confirmation_proceed')
    print accept_button
    # accept_button = browser.find_link_by_partial_href('http://dev.jatomifitness.com.my/jatomi/myPHP/buytopup.php')
    accept_button.click()
    

    time.sleep(15)
    self.assertEqual(browser.url, 'https://www.mobile88.com/epayment/ConfirmationPage.asp') 
  
  
  @test_utilities.e2e.email_on_failure
  @test_utilities.e2e.snap_on_failure
  def _test_Scenario_5 (self):
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
    
    time.sleep(20)
    top_up_cancel_button = browser.find_by_value('Cancel')
    top_up_cancel_button.click()
    self.assertEqual(browser.url, '{0}/{1}'.format(base_url, 'jatomi/en/top_up'))  
  

  @test_utilities.e2e.email_on_failure
  @test_utilities.e2e.snap_on_failure
  def _test_Scenario_6 (self):
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
    
    time.sleep(15)
    browser.fill('last_name','Testing88888')
    browser.fill('email','Testing88888@gmail.com.my') 
    second_dropdown = browser.find_option_by_value('50')
    second_dropdown.select("value","50")
    top_up_submit_button = browser.find_by_id('edit-friendssubmit')
    top_up_submit_button.click()
    alert_button = browser.find_by_id('alertify-ok').click()

  
 
  @test_utilities.e2e.email_on_failure
  @test_utilities.e2e.snap_on_failure
  def _test_Scenario_7 (self):
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
    time.sleep(15)
    browser.fill('last_name','Testing88888')
    browser.fill('email','Testing88@gmail.com.my') 
    browser.select("amount","50").last
    top_up_submit_button = browser.find_by_id('edit-friendssubmit')
    top_up_submit_button.click()
    alert_button = browser.find_by_id('alertify-ok').click()


  @test_utilities.e2e.email_on_failure
  @test_utilities.e2e.snap_on_failure
  def _test_Scenario_8 (self):
    browser = self.browser
    browser.click_link_by_text("Login")
    
    time.sleep(18)
    browser.fill('name','jatomitest@gmail.com')
    browser.fill('pass','pleaseohplease')

    login_button = browser.find_by_id("edit-submit")[0]
    login_button.click()
    time.sleep(10) 
    self.assertEqual(browser.url, '{0}/{1}'.format(base_url, 'jatomi/en/dashboard/overview'))
    browser.click_link_by_text("Personal Settings")
    time.sleep(10)
    self.assertEqual(browser.url, '{0}/{1}'.format(base_url, 'jatomi/en/dashboard/settings'))
    browser.click_link_by_href("http://dev.jatomifitness.com.my/jatomi/en/change/email")
    self.assertEqual(browser.url, '{0}/{1}'.format(base_url, 'jatomi/en/change/email'))
    time.sleep(10)
    browser.fill('current_email','jatomitest@gmail.com')
    browser.fill('new_email','jatomitest@gmail.com')
    browser.fill('confirm_email','jatomitest@gmail.com')
    browser.click_link_by_id("edit-update")
    self.assertEqual(browser.url, '{0}/{1}'.format(base_url, 'jatomi/en/dashboard/settings'))

  
  
  @test_utilities.e2e.email_on_failure
  @test_utilities.e2e.snap_on_failure
  def _test_Scenario_9 (self):
    browser = self.browser
    browser.click_link_by_text("Login")
    
    time.sleep(18)
    browser.fill('name','jatomitest@gmail.com')
    browser.fill('pass','pleaseohplease')

    login_button = browser.find_by_id("edit-submit")[0]
    login_button.click()
    time.sleep(10) 
    self.assertEqual(browser.url, '{0}/{1}'.format(base_url, 'jatomi/en/dashboard/overview'))
    browser.click_link_by_text("Personal Settings")
    time.sleep(10)
    self.assertEqual(browser.url, '{0}/{1}'.format(base_url, 'jatomi/en/dashboard/settings'))
    browser.attach_file('photo', '/home/navid/Desktop/error/test.jpg')
    save_button = browser.find_by_id('edit-submit').click()
    ok_button = browser.find_by_id('alertify-ok').click()
    
    
  

  @test_utilities.e2e.email_on_failure
  @test_utilities.e2e.snap_on_failure
  def _test_Scenario_10 (self):
    browser = self.browser
    browser.click_link_by_text("Login")
    
    time.sleep(18)
    browser.fill('name','jatomitest@gmail.com')
    browser.fill('pass','pleaseohplease')

    login_button = browser.find_by_id("edit-submit")[0]
    login_button.click()
    time.sleep(10) 
    self.assertEqual(browser.url, '{0}/{1}'.format(base_url, 'jatomi/en/dashboard/overview'))
    browser.click_link_by_text("Personal Settings")
    time.sleep(10)
    self.assertEqual(browser.url, '{0}/{1}'.format(base_url, 'jatomi/en/dashboard/settings'))
 

  @test_utilities.e2e.email_on_failure
  @test_utilities.e2e.snap_on_failure
  def _test_Scenario_11 (self):
    browser = self.browser
    browser.click_link_by_text("Login")
    
    time.sleep(18)
    browser.fill('name','jatomitest@gmail.com')
    browser.fill('pass','pleaseohplease')

    login_button = browser.find_by_id("edit-submit")[0]
    login_button.click()
    time.sleep(10) 
    self.assertEqual(browser.url, '{0}/{1}'.format(base_url, 'jatomi/en/dashboard/overview'))
    browser.click_link_by_text("Personal Settings")
    time.sleep(10)
    self.assertEqual(browser.url, '{0}/{1}'.format(base_url, 'jatomi/en/dashboard/settings'))
    browser.click_link_by_value("Change Password")
    time.sleep(10)
    browser.fill('C-pass','pleaseohplease')
    browser.fill('N-pass','pleaseohplease')
    browser.click_link_by_id("um_Cancel20")
    browser.click_link_by_name("op")
    browser.click_link_by_text("OK")

  

  @test_utilities.e2e.email_on_failure
  @test_utilities.e2e.snap_on_failure
  def _test_Scenario_12 (self):
    browser = self.browser
    browser.click_link_by_text("Login")
    
    time.sleep(18)
    browser.fill('name','jatomitest@gmail.com')
    browser.fill('pass','pleaseohplease')

    login_button = browser.find_by_id("edit-submit")[0]
    login_button.click()
    
    time.sleep(10) 
    self.assertEqual(browser.url, '{0}/{1}'.format(base_url, 'jatomi/en/dashboard/overview'))
    browser.click_link_by_text("Manage Membership")
    
    time.sleep(10)
    self.assertEqual(browser.url, '{0}/{1}'.format(base_url, 'jatomi/en/dashboard/manage'))
    addon_button = browser.find_by_id('thirstybuster')
    addon_button.click()
    addon_upgrade_button = browser.find_by_id("edit-adonsubmit").click()
    
    time.sleep(10)
    addon_submit_button = browser.find_by_id("um_SubmitI").click()
    
    time.sleep(10)
    self.assertEqual(browser.url, 'https://www.mobile88.com/epayment/ConfirmationPage.asp') 

  

  @test_utilities.e2e.email_on_failure
  @test_utilities.e2e.snap_on_failure
  def _test_Scenario_13 (self):
    browser = self.browser
    browser.click_link_by_text("Login")
    
    time.sleep(18)
    browser.fill('name','jatomitest@gmail.com')
    browser.fill('pass','pleaseohplease')

    login_button = browser.find_by_id("edit-submit")[0]
    login_button.click()
    
    time.sleep(10) 
    self.assertEqual(browser.url, '{0}/{1}'.format(base_url, 'jatomi/en/dashboard/overview'))
    browser.click_link_by_text("Manage Membership")
    
    time.sleep(10)
    self.assertEqual(browser.url, '{0}/{1}'.format(base_url, 'jatomi/en/dashboard/manage'))
    freeze_button = browser.find_by_css(".um_Freeze").click()
    
    time.sleep(5)
    browser.select("Month","2")
    browser.select("Reason","Holiday")
    freez_date_button = browser.find_by_id('um_datepicker2').fill('Date','04/30/2014')

    freeze_submit_button = browser.find_by_id("um_FreezeSubmit")
    browser.click_link_by_value("Proceed")

  
 
  @test_utilities.e2e.email_on_failure
  @test_utilities.e2e.snap_on_failure
  def test_Scenario_13_13 (self):
    browser = self.browser
    browser.click_link_by_text("Login")
    
    time.sleep(18)
    browser.fill('name','jatomitest@gmail.com')
    browser.fill('pass','pleaseohplease')

    login_button = browser.find_by_id("edit-submit")[0]
    login_button.click()
    
    time.sleep(10) 
    self.assertEqual(browser.url, '{0}/{1}'.format(base_url, 'jatomi/en/dashboard/overview'))
    browser.click_link_by_text("Manage Membership")
    
    time.sleep(10)
    self.assertEqual(browser.url, '{0}/{1}'.format(base_url, 'jatomi/en/dashboard/manage'))
    leave_button = browser.find_by_css(".um_Cancel").click()
    
    time.sleep(10)
    leave_confirm_button = browser.find_by_id('um_SubmitQ').click()
    
    time.sleep(5)
    element8 = find_by_id(choices_8).check()
    leave_submit_button = browser.find_by_id('um_Submit2').click()
    leave_submit_OK_button = browser.find_by_id('alertify-ok').click()
    leave_submit_OK_button = browser.find_by_id('alertify-ok').click()
  
  
  @test_utilities.e2e.email_on_failure
  @test_utilities.e2e.snap_on_failure
  def _test_Scenario_14 (self):
    browser = self.browser
    browser.click_link_by_text("Login")
    
    time.sleep(18)
    browser.fill('name','jatomitest@gmail.com')
    browser.fill('pass','pleaseohplease')

    login_button = browser.find_by_id("edit-submit")[0]
    login_button.click()
    time.sleep(10) 
    self.assertEqual(browser.url, '{0}/{1}'.format(base_url, 'jatomi/en/dashboard/overview'))  
    browser.click_link_by_text("My Calendar")
    self.assertEqual(browser.url, '{0}/{1}'.format(base_url, 'jatomi/en/buy_pt_session')) 
    pt_section = browser.find_by_css('.views-row').click()
    #pt-image = row.find_by_css('.trainbody').clik()
    browser.click_link_by_text("Next")
    time.sleep(10)
    browser.click_link_by_text("Finish")
    time.sleep(10)
    self.assertEqual(browser.url, 'https://www.mobile88.com/epayment/ConfirmationPage.asp') 
  

  @test_utilities.e2e.email_on_failure
  @test_utilities.e2e.snap_on_failure
  def _test_Scenario_15 (self):
    browser = self.browser
    browser.click_link_by_text("Login")
    
    time.sleep(18)
    browser.fill('name','jatomitest@gmail.com')
    browser.fill('pass','pleaseohplease')

    login_button = browser.find_by_id("edit-submit")[0]
    login_button.click()
    time.sleep(10) 
    self.assertEqual(browser.url, '{0}/{1}'.format(base_url, 'jatomi/en/dashboard/overview'))  
    browser.click_link_by_text("My Calendar")
    self.assertEqual(browser.url, '{0}/{1}'.format(base_url, 'jatomi/en/buy_pt_session')) 
    browser.click_link_by_text("Book Personal Training")
    self.assertEqual(browser.url, '{0}/{1}'.format(base_url, 'jatomi/en/my_calendar/book_pt')) 
    time.sleep(10)
    browser.click_link_by_id("trainer_85")



 
  @test_utilities.e2e.email_on_failure
  @test_utilities.e2e.snap_on_failure
  def _test_Scenario_16 (self):
    browser = self.browser
    browser.click_link_by_text("Login")
    
    time.sleep(18)
    browser.fill('name','jatomitest@gmail.com')
    browser.fill('pass','pleaseohplease')

    login_button = browser.find_by_id("edit-submit")[0]
    login_button.click()
    time.sleep(10) 
    self.assertEqual(browser.url, '{0}/{1}'.format(base_url, 'jatomi/en/dashboard/overview')) 
    browser.click_link_by_text("Interest & Goals")
    self.assertEqual(browser.url, '{0}/{1}'.format(base_url, 'jatomi/en/interest_goals')) 
    time.sleep(10)
    browser.click_link_by_text("Spinning Classes") 
    browser.click_link_by_text("Get Fit") 
    browser.click_link_by_text("Interested In Group Classes") 
    browser.click_link_by_text("Lifestyle") 
    browser.click_link_by_text("Lose Weight") 
    browser.click_link_by_text("Socialize") 
    browser.click_link_by_text("Access To High Quality Equipment") 
    browser.click_link_by_text("Strength Training") 
    browser.click_link_by_text("Rehabilitation") 
    browser.click_link_by_text("Interested In Functional Training") 
    browser.click_link_by_text("Get Motivated") 
    browser.click_link_by_text("Get Access To Fitness Professionals") 
    browser.click_link_by_text("Fitness Program For Older Adults") 
    browser.click_link_by_id("udpate_goals")
    time.sleep(10)
    browser.click_link_by_id("OK")
    self.assertEqual(browser.url, '{0}/{1}'.format(base_url, 'jatomi/en/interest_goals')) 





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