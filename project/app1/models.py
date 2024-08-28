from django.db import models
import uuid
from django.contrib.auth.models import AbstractUser


class Customer(models.Model):
    # customer_user = models.OneToOneField(Customer, on_delete=models.CASCADE, related_name='user')

    odataetag = models.CharField(max_length=255, verbose_name="OData ETag", blank=True, null=True)
    system_id = models.UUIDField(primary_key=True, verbose_name="System ID", default=uuid.uuid4)
    no = models.CharField(max_length=50, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    search_name = models.CharField(max_length=255, blank=True, null=True)
    name2 = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    address2 = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    contact = models.CharField(max_length=255, blank=True, null=True)
    phone_no = models.CharField(max_length=50, blank=True, null=True)
    telex_no = models.CharField(max_length=50, blank=True, null=True)
    status = models.BooleanField(default=False, null=True)
    enterprise_no = models.CharField(max_length=50, blank=True, null=True)
    vat_registration_no = models.CharField(max_length=50, blank=True, null=True)
    blocked = models.CharField(max_length=50, blank=True, null=True)
    document_sending_profile = models.CharField(max_length=50, blank=True, null=True)
    shipto_code = models.CharField(max_length=50, blank=True, null=True)
    our_account_no = models.CharField(max_length=50, blank=True, null=True)
    territory_code = models.CharField(max_length=50, blank=True, null=True)
    global_dimension1_code = models.CharField(max_length=50, blank=True, null=True)
    global_dimension2_code = models.CharField(max_length=50, blank=True, null=True)
    chain_name = models.CharField(max_length=255, blank=True, null=True)
    budgeted_amount = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    credit_limit_lcy = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    customer_posting_group = models.CharField(max_length=50, blank=True, null=True)
    currency_code = models.CharField(max_length=10, blank=True, null=True)
    customer_price_group = models.CharField(max_length=50, blank=True, null=True)
    language_code = models.CharField(max_length=10, blank=True, null=True)
    registration_number = models.CharField(max_length=50, blank=True, null=True)
    statistics_group = models.IntegerField(blank=True, null=True)
    payment_terms_code = models.CharField(max_length=50, blank=True, null=True)
    salesperson_code = models.CharField(max_length=50, blank=True, null=True)
    shipment_method_code = models.CharField(max_length=50, blank=True, null=True)
    place_of_export = models.CharField(max_length=255, blank=True, null=True)
    customer_disc_group = models.CharField(max_length=50, blank=True, null=True)
    country_region_code = models.CharField(max_length=10, blank=True, null=True)
    amount = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    debit_amount = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    credit_amount = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    invoice_amounts = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    other_amounts_lcy = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    comment = models.BooleanField(default=False, null=True)
    last_statement_no = models.IntegerField(blank=True, null=True)
    prepayment = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    partner_type = models.CharField(max_length=50, blank=True, null=True)
    payments = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    post_code = models.CharField(max_length=20, blank=True, null=True)
    print_statements = models.BooleanField(default=False, null=True)
    prices_including_vat = models.BooleanField(default=False, null=True)
    profit_lcy = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    billto_customer_no = models.CharField(max_length=50, blank=True, null=True)
    priority = models.IntegerField(blank=True, null=True)
    payment_method_code = models.CharField(max_length=50, blank=True, null=True)
    last_modified_date_time = models.DateTimeField(blank=True, null=True)
    global_dimension1_filter = models.CharField(max_length=50, blank=True, null=True)
    global_dimension2_filter = models.CharField(max_length=50, blank=True, null=True)
    balance = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    balance_lcy = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    balance_due = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    net_change = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    net_change_lcy = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    sales_lcy = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    inv_amounts_lcy = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    inv_discounts_lcy = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    no_of_invoices = models.IntegerField(blank=True, null=True)
    invoice_disc_code = models.CharField(max_length=50, blank=True, null=True)
    invoice_copies = models.IntegerField(blank=True, null=True)
    pmt_discounts_lcy = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    pmt_tolerance_lcy = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    balance_due_lcy = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    payments_lcy = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    cr_memo_amounts = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    cr_memo_amounts_lcy = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    finance_charge_memo_amounts = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    shipped_not_invoiced = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    shipped_not_invoiced_lcy = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    shipping_agent_code = models.CharField(max_length=50, blank=True, null=True)
    application_method = models.CharField(max_length=50, blank=True, null=True)
    location_code = models.CharField(max_length=50, blank=True, null=True)
    fax_no = models.CharField(max_length=50, blank=True, null=True)
    vat_bus_posting_group = models.CharField(max_length=50, blank=True, null=True)
    combine_shipments = models.BooleanField(default=False, null=True)
    gen_bus_posting_group = models.CharField(max_length=50, blank=True, null=True)
    gln = models.CharField(max_length=50, blank=True, null=True)
    county = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    eori_number = models.CharField(max_length=50, blank=True, null=True)
    use_gln_in_electronic_document = models.BooleanField(default=False, null=True)
    reminder_terms_code = models.CharField(max_length=50, blank=True, null=True)
    reminder_amounts = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    reminder_amounts_lcy = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    tax_area_code = models.CharField(max_length=50, blank=True, null=True)
    tax_area_id = models.UUIDField(blank=True, null=True)
    tax_liable = models.BooleanField(default=False, null=True)
    currency_filter = models.CharField(max_length=10, blank=True, null=True)
    email_address1 = models.EmailField(blank=True, null=True)
    email_address2 = models.EmailField(blank=True, null=True)
    email_address3 = models.EmailField(blank=True, null=True)
    email_address4 = models.EmailField(blank=True, null=True)
    

    user_id = models.CharField(max_length=50, blank=True,null=True)
    password = models.CharField(max_length=255, blank=True,null=True)

    def __str__(self):
        return format(self.name )
    

# models.py
from django.db import models

class ItemSalePrice(models.Model):
    system_id = models.UUIDField(primary_key=True, editable=False, db_column='SystemId')
    srno = models.IntegerField(db_column='Srno')
    salestype = models.CharField(max_length=255, db_column='salestype')
    salecode = models.CharField(max_length=255, db_column='Salecode')
    item_no = models.CharField(max_length=255, db_column='ItemNo')
    unit_price = models.DecimalField(max_digits=10, decimal_places=6, db_column='UnitPrice')
    minimum_quantity = models.IntegerField(db_column='MinimumQuantity')
    start_date = models.DateField(db_column='StartDate')
    end_date = models.DateField(db_column='EndDate')
    modified_datetime = models.DateTimeField(db_column='ModifedDateTime')
    odata_etag = models.CharField(max_length=255, db_column='odata_etag')  # Renamed field

    class Meta:
        verbose_name = 'Item Sale Price'
        verbose_name_plural = 'Item Sale Prices'
        db_table = 'item_sale_price'


from django.db import models

class Item(models.Model):
    etag = models.CharField(max_length=255, db_column="@odata.etag")
    system_id = models.UUIDField()
    item_id = models.UUIDField()
    item_no = models.CharField(max_length=20)
    description = models.TextField()
    blocked = models.BooleanField()
    sales_blocked = models.BooleanField()
    search_description = models.TextField()
    base_unit_of_measure = models.CharField(max_length=10)
    inventory = models.IntegerField()
    parent_category = models.CharField(max_length=100)
    item_category_code = models.CharField(max_length=100)
    item_sub_category_code = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    net_weight = models.DecimalField(max_digits=10, decimal_places=3)
    packaging = models.CharField(max_length=50)
    weight_description = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    quantity = models.IntegerField()
    vat = models.DecimalField(max_digits=5, decimal_places=2)
    brand_link = models.URLField(blank=True, null=True)
    gtin = models.CharField(max_length=20)
    vat_prod_posting_group = models.CharField(max_length=50)
    purchasing_code = models.CharField(max_length=50, blank=True, null=True)
    sales_unit_of_measure = models.CharField(max_length=10)
    bar_code = models.CharField(max_length=50, blank=True, null=True)
    last_datetime_modified = models.DateTimeField()
    

    def __str__(self):
        return self.item_no



class User(AbstractUser):
   customer = models.OneToOneField(Customer, on_delete=models.CASCADE, related_name='user',null=True,blank=True)
   username = models.CharField(max_length=50, blank=True, null=True, unique=True)
   email = models.EmailField(unique=True)
   
   
   USERNAME_FIELD = 'email'
   REQUIRED_FIELDS = ['username']

   def __str__(self):
       return "{}".format(self.email)
