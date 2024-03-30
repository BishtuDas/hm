from django.db import models

class Customer(models.Model):
    Problem_Summary = models.TextField(blank=True)
    Why_Right_Provider = models.TextField(blank=True)
    Why_Come_To_You_Now = models.TextField(blank=True)
    What_Will_Be_Different = models.TextField(blank=True)
    Solution_Summary = models.TextField(blank=True)
    Patient_Demographics = models.TextField(blank=True)
    Unique_Value_Proposition = models.TextField(blank=True)
    Patients_Earn_Subset = models.TextField(blank=True)
    Opportunity_Problems_Solve = models.TextField(blank=True)
    Target_Patients = models.TextField(blank=True)
    Unique_Value_Proposition_Opportunity = models.TextField(blank=True)
    Earn_Opportunity = models.TextField(blank=True)
    Financial_Forecast = models.TextField(blank=True)
    Revenue = models.TextField(blank=True)
    Cash_Payers = models.TextField(blank=True)
    Insurance_Payers = models.TextField(blank=True)
    Offer_Products = models.TextField(blank=True)
    Cross_Sell = models.TextField(blank=True)
    Current_Patients = models.TextField(blank=True)
    Adequately_Funded = models.TextField(blank=True)
    Provide_Services = models.TextField(blank=True)
    Competitors = models.TextField(blank=True)
    Provide_Patients = models.TextField(blank=True)
    Unique = models.TextField(blank=True)
    Market_Size_Segments = models.TextField(blank=True)
    Key_Payers = models.TextField(blank=True)
    Desired = models.TextField(blank=True)
    Specific_Types_Patients = models.TextField(blank=True)
    Multiple_Groups = models.TextField(blank=True)
    Blanket_Outlook = models.TextField(blank=True)





class Company(models.Model):
    # Marketing Plan fields
    reaching_target_audience = models.TextField()
    marketing_channels = models.TextField()
    working_channels = models.TextField()
    tracking_platforms = models.TextField()

    # Sales Plan fields
    relies_on_salespeople = models.TextField()
    conversion_strategy = models.TextField()
    marketing_alignment = models.TextField()

    # Operations fields
    locations_description = models.TextField()
    available_space = models.TextField()
    future_plans_description = models.TextField() 

    # Technology fields
    software_description = models.TextField()
    emr = models.TextField()
    other_tools = models.TextField()

    # Milestones & Metrics fields
    milestones = models.TextField()
    success_definition = models.TextField()
    accomplished_milestones = models.TextField()
    key_metrics = models.TextField()
    roi = models.TextField()
    kpis = models.TextField()
    data_utilization = models.TextField()

    # Company fields
    owners = models.TextField()
    legal_structure = models.TextField()

    # Management Team fields
    team_members = models.TextField()
    team_description = models.TextField()

    # Financial Plan fields
    has_financial_plan = models.TextField()
    forecast_process = models.TextField()
    revenue_projection = models.TextField()
    growth_assumption = models.TextField()
    key_expenses = models.TextField()
    profit_expectation = models.TextField()
    revenue_expense_tracking = models.TextField()

    # Business fields
    business_evaluation = models.TextField()
    has_business_plan = models.TextField()
    has_budget = models.TextField()
    goals = models.TextField()
    benchmarks = models.TextField()

    # Strategic Partnerships fields
    coi_description = models.TextField()
    coi_support_strategy = models.TextField()
    coi_leverage = models.TextField()
    coi_challenges = models.TextField()
    coi_strategy = models.TextField()
    referral_network = models.TextField()
    coi_leverage_strategy = models.TextField()







class Website(models.Model):
    # Website Product
    website_product = models.CharField(max_length=100, choices=[
        ('Custom Website: 5 pages', 'Custom Website: 5 pages'),
        ('Custom Website: 10 pages', 'Custom Website: 10 pages'),
        ('Custom Website: 15 pages', 'Custom Website: 15 pages'),
        ('Custom Website: 20 pages', 'Custom Website: 20 pages'),
        ('Custom Website: 25 pages', 'Custom Website: 25 pages'),
        ('Custom Website: 25+ pages', 'Custom Website: 25+ pages'),
        ('Custom Website: Landing Page', 'Custom Website: Landing Page'),
    ])
    
    # Primary Goal
    inbound_leads = models.BooleanField(default=False)
    quote_requests = models.BooleanField(default=False)
    brand_awareness = models.BooleanField(default=False)
    education = models.BooleanField(default=False)
    other_primary_goal = models.CharField(max_length=100, blank=True)
    
    # Social Links
    facebook = models.URLField(max_length=200, blank=True)
    linkedin = models.URLField(max_length=200, blank=True)
    other_social_media = models.URLField(max_length=200, blank=True)
    
    # Domain Information
    domain_registration = models.CharField(max_length=100, choices=[
        ('I have a domain', 'I have a domain'),
        ('I do not have a domain, please purchase one on my behalf', 'I do not have a domain, please purchase one on my behalf'),
    ])
    domain_registrar = models.CharField(max_length=100, blank=True)
    current_website_url = models.URLField(max_length=200, blank=True)
    domain_username = models.CharField(max_length=100, blank=True)
    domain_password = models.CharField(max_length=100, blank=True)
    requested_website_url = models.URLField(max_length=200, blank=True)
    
    # Navigation
    navigation_structure = models.CharField(max_length=200, blank=True)
    navigation_notes = models.TextField(blank=True)
    navigation_assets = models.URLField(max_length=200, blank=True)
    
    # Images
    professional_images = models.BooleanField(default=False)
    related_to_business_images = models.BooleanField(default=False)
    fun_images = models.BooleanField(default=False)
    choose_for_me_images = models.BooleanField(default=False)
    other_images_demographics = models.CharField(max_length=200, blank=True)
    
    # Contact Information
    primary_contact_email = models.EmailField(max_length=100)
    secondary_contact_email = models.EmailField(max_length=100)
    email_cta = models.BooleanField(default=False)
    phone_cta = models.BooleanField(default=False)
    contact_form_email = models.EmailField(max_length=100)
    public_phone_number = models.CharField(max_length=20, blank=True)
    public_email = models.EmailField(max_length=100, blank=True)
    business_address = models.CharField(max_length=200, blank=True)
    hours_of_operation = models.CharField(max_length=100, blank=True)
    
    # Products
    products_doc_link = models.URLField(max_length=200, blank=True)
    product_csv_upload = models.FileField(upload_to='product_csv/', blank=True)
    product_images_link = models.URLField(max_length=200, blank=True)
    
    # Payment and Shipping
    payment_processor = models.CharField(max_length=100, blank=True)
    shipping_options = models.CharField(max_length=100, blank=True)
    
    # Additional Functionality
    additional_functionality = models.TextField(blank=True)
    embed_codes = models.TextField(blank=True)
    
    # Web Copy Options
    business_description = models.TextField(blank=True)
    slogans = models.CharField(max_length=100, blank=True)
    target_audience = models.CharField(max_length=100, blank=True)
    need_for_products_services = models.CharField(max_length=100, blank=True)
    business_history = models.TextField(blank=True)
    mission_statement = models.TextField(blank=True)
    contact_purpose = models.CharField(max_length=100, blank=True)
    product_service_description = models.CharField(max_length=100, blank=True)
    tone_of_voice = models.CharField(max_length=100, blank=True)
    additional_info = models.TextField(blank=True)
    missed_details = models.TextField(blank=True)
    
    # Problem Summary
    problem_summary = models.TextField(blank=True)

   
    def __str__(self):
        return f"Contact Form #{self.id}"
    




class Marketing(models.Model):
    cac = models.TextField(verbose_name="Customer Acquisition Cost")
    budget = models.TextField(verbose_name="Budget")
    process_description = models.TextField(verbose_name="Process Description")
    yearly_referrals = models.TextField(verbose_name="Yearly Referrals")
    referral_thanks = models.TextField(verbose_name="Referral Thanks")
    marketing_methods = models.TextField(verbose_name="Marketing Methods")
    landing_pages_count = models.TextField(verbose_name="Landing Pages Count")
    website_product = models.CharField(max_length=100, verbose_name="Website Product", choices=[
        ('Facebook Ads', 'Facebook Ads'),
        ('Google Ads', 'Google Ads'),
        ('Instagram ads', 'Instagram ads'),
        ('Twitter ads', 'Twitter ads'),
        ('3rd Party', '3rd Party'),
        ('Vitals', 'Vitals'),
        ('Billboards', 'Billboards'),
        ('Digital marketing', 'Digital marketing'),
        ('Healthgrades', 'Healthgrades'),
        ('ZocDoc.com', 'ZocDoc.com'),
        ('Docspot', 'Docspot'),
        ('EZdoctor', 'EZdoctor'),
        ('Caredash', 'Caredash'),
        ('Website', 'Website'),
        ('Bing Ads', 'Bing Ads'),
        ('Apple', 'Apple'),
        ('Other Social Media', 'Other Social Media'),
        ('Health.usnews.com', 'Health.usnews.com'),
        ('Youtube', 'Youtube'),
        ('Webmd.com', 'Webmd.com'),
        ('Do you host any social', 'Do you host any social'),
        ('Live events', 'Live events'),
        ('Reddit', 'Reddit'),
        ('Your blog', 'Your blog'),
        ('3rd Party Blogs', '3rd Party Blogs'),
        ('Yelp', 'Yelp'),
    ])
    patient_process = models.TextField(verbose_name="Patient Process")
    lifetime_customer_value = models.TextField(verbose_name="Lifetime Customer Value")
    follow_up_appointments = models.TextField(verbose_name="Follow-up Appointments")
    returning_patients_percentage = models.TextField(verbose_name="Returning Patients Percentage")
    communication_method = models.CharField(max_length=100, verbose_name="Communication Method", choices=[
        ('Email', 'Email'),
        ('Phone', 'Phone'),
        ('Text', 'Text'),
        ('Newsletter', 'Newsletter'),
        ('Blog', 'Blog'),
        ('Social Media', 'Social Media'),
        ('Media Communications', 'Media Communications'),
        ('Events', 'Events'),
        ('Combination', 'Combination'),
    ])
    proactive_or_reactive = models.TextField(verbose_name="Proactive or Reactive")
    reminders_method = models.TextField(verbose_name="Reminders Method")
    follow_up_confirmation = models.TextField(verbose_name="Follow-up Confirmation")
    reschedule_actions = models.TextField(verbose_name="Reschedule Actions")
    google_search_results_personal_name = models.TextField(verbose_name="Google Search Results (Personal Name)")
    google_search_results_clinic_name = models.TextField(verbose_name="Google Search Results (Clinic Name)")
    google_listing_info = models.TextField(verbose_name="Google Listing Info")
    information_accuracy = models.TextField(verbose_name="Is all of the information accurate?", help_text="Answer whether all of the information is accurate.", blank=True)
    reviews_count = models.TextField(verbose_name="Reviews Count")
    average_ratings = models.TextField(verbose_name="Average Ratings")
    online_reputation_importance = models.TextField(verbose_name="Online Reputation Importance")
    review_request_process = models.TextField(verbose_name="Review Request Process")
    correspondences_after_visit = models.TextField(verbose_name="Correspondences After Visit")
    challenges_as_practitioner = models.TextField(verbose_name="Challenges as a Practitioner")
    challenges_as_business_owner = models.TextField(verbose_name="Challenges as a Business Owner")
    industry_risks = models.TextField(verbose_name="Industry Risks")
    competitive_risks = models.TextField(verbose_name="Competitive Risks")

    # Add more fields as needed

    def __str__(self):
        return f"Medical Practice Survey #{self.pk}"


