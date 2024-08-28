import requests
from .models import Customer
import uuid
import logging
import requests
from django.utils.dateparse import parse_datetime
from .models import Customer
from celery import shared_task
import os
import requests
from .models import *
import uuid
import logging
from django.core.exceptions import MultipleObjectsReturned
logger = logging.getLogger(__name__)

def get_oauth_token():
    token_url = os.getenv("OAUTH_TOKEN_URL")
    client_id = os.getenv("OAUTH_CLIENT_ID")
    client_secret = os.getenv("OAUTH_CLIENT_SECRET")  
    data = {
        'grant_type': 'client_credentials',
        'client_id': client_id,
        'client_secret': client_secret,
        'scope': os.getenv("OAUTH_SCOPE")    
    }

    response = requests.post(token_url, data=data)
    
    if response.status_code == 200:
        token = response.json().get('access_token')
        return token
    else:
        logger.error(f"Failed to get OAuth token: {response.status_code} - {response.text}")
        return None
    
from django.core.exceptions import MultipleObjectsReturned

@shared_task
def fetch_and_store_itemsaleprice_data():
    token = get_oauth_token()
    if not token:
        return
    
    headers = {
        'Authorization': f'Bearer {token}'
    }
    
    url = os.getenv("ITEMSALEPRICE_API_URL")
    
    while url:
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            data = response.json()
            if 'value' in data:
                for item in data['value']:
                    item_data = {
                        'system_id': uuid.uuid4(),  # Assuming system_id should be generated
                        'srno': item['Srno'],
                        'salestype': item['salestype'],
                        'salecode': item['Salecode'],
                        'item_no': item['ItemNo'],
                        'unit_price': item['UnitPrice'],
                        'minimum_quantity': item['MinimumQuantity'],
                        'start_date': item['StartDate'],
                        'end_date': item['EndDate'],
                        'modified_datetime': item['ModifedDateTime'],
                        'odata_etag': item['@odata.etag'],
                    }

                    try:
                        # Attempt to retrieve the first record with the given 'srno'
                        obj = ItemSalePrice.objects.filter(salestype=item['salestype'], item_no=item['ItemNo'],salecode=item['Salecode'],minimum_quantity=item['MinimumQuantity']).first()

                        if obj:
                            # Update the existing record if 'odata_etag' has changed
                            if obj.odata_etag != item['@odata.etag']:
                                for key, value in item_data.items():
                                    setattr(obj, key, value)
                                obj.save()
                        else:
                            # If no record is found, create a new one
                            ItemSalePrice.objects.create(**item_data)

                    except Exception as e:
                        logger.error(f"Error processing item {item['Srno']}: {str(e)}")

            url = data.get('@odata.nextLink', None)
        else:
            logger.error(f"Failed to fetch data: {response.status_code} - {response.text}")
            break

@shared_task
def fetch_and_store_item_data():
    token = get_oauth_token()
    if not token:
        return
    
    headers = {
        'Authorization': f'Bearer {token}'
    }
    
    url = os.getenv("ITEM_API_URL")
    
    while url:
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            data = response.json()
            if 'value' in data:
                for item in data['value']:
                    item_data = {
                        'etag': item['@odata.etag'],
                        'system_id': uuid.UUID(item['SystemId']),
                        'item_id': uuid.UUID(item['ID']),
                        'item_no': item['ItemNo'],
                        'description': item['Description'],
                        'blocked': item['Blocked'],
                        'sales_blocked': item['SalesBlocked'],
                        'search_description': item['SearchDescription'],
                        'base_unit_of_measure': item['BaseUnitOfMeasure'],
                        'inventory': item['inventory'],
                        'parent_category': item['ParentCategory'],
                        'item_category_code': item['ItemCategoryCode'],
                        'item_sub_category_code': item['ItemSubCategoryCode'],
                        'brand': item['Brand'],
                        'net_weight': item['NetWeight'],
                        'packaging': item['Packaging'],
                        'weight_description': item['WeightDescription'],
                        'type': item['Type'],
                        'quantity': item['Quantity'],
                        'vat': item['VAT'],
                        'brand_link': item['BrandLink'] if item['BrandLink'] else None,
                        'gtin': item['GTIN'],
                        'vat_prod_posting_group': item['VATProdPostingGroup'],
                        'purchasing_code': item['PurchasingCode'] if item['PurchasingCode'] else None,
                        'sales_unit_of_measure': item['SalesUnitOfMeasure'],
                        'bar_code': item['BarCode'] if item['BarCode'] else None,
                        'last_datetime_modified': item['LastDateTimeModified'],
                    }
                    
                    # Update or create based on the 'item_id' field
                    obj, created = Item.objects.update_or_create(
                        item_id=item['ID'],
                        defaults=item_data
                    )

                    # Check if the existing record has changed, if not, skip updating
                    if not created:
                        if obj.etag != item['@odata.etag']:
                            for key, value in item_data.items():
                                setattr(obj, key, value)
                            obj.save()

            url = data.get('@odata.nextLink', None)
        else:
            logger.error(f"Failed to fetch data: {response.status_code} - {response.text}")
            break

@shared_task
def fetch_and_store_customer_data():
    token = get_oauth_token()
    if not token:
        return
    
    headers = {
        'Authorization': f'Bearer {token}'
    }
    
    url = os.getenv("CUSTOMER_API_URL")
    
    while url:
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            data = response.json()
            if 'value' in data:
                for item in data['value']:
                    system_id = uuid.uuid4()  # Assuming `system_id` needs to be generated
                    item_data = {
    'odataetag': item['@odata.etag'],
    'no': item['No'],
    'name': item['Name'],
    'search_name': item['SearchName'],
    'name2': item['Name2'],
    'address': item['Address'],
    'address2': item['Address2'],
    'city': item['City'],
    'contact': item['Contact'],
    'phone_no': item['PhoneNo'],
    'telex_no': item['TelexNo'],
    'status': item['Status'],
    'enterprise_no': item['EnterpriseNo'],
    'vat_registration_no': item['VATRegistrationNo'],
    'blocked': item['Blocked'],
    'document_sending_profile': item['DocumentSendingProfile'],
    'shipto_code': item['ShiptoCode'],
    'our_account_no': item['OurAccountNo'],
    'territory_code': item['TerritoryCode'],
    'global_dimension1_code': item['GlobalDimension1Code'],
    'global_dimension2_code': item['GlobalDimension2Code'],
    'chain_name': item['ChainName'],
    'budgeted_amount': item['BudgetedAmount'],
    'credit_limit_lcy': item['CreditLimitLCY'],
    'customer_posting_group': item['CustomerPostingGroup'],
    'currency_code': item['CurrencyCode'],
    'customer_price_group': item['CustomerPriceGroup'],
    'language_code': item['LanguageCode'],
    'registration_number': item['RegistrationNumber'],
    'statistics_group': item['StatisticsGroup'],
    'payment_terms_code': item['PaymentTermsCode'],
    'salesperson_code': item['SalespersonCode'],
    'shipment_method_code': item['ShipmentMethodCode'],
    'place_of_export': item['PlaceofExport'],
    'customer_disc_group': item['CustomerDiscGroup'],
    'country_region_code': item['CountryRegionCode'],
    'amount': item['Amount'],
    'debit_amount': item['DebitAmount'],
    'credit_amount': item['CreditAmount'],
    'invoice_amounts': item['InvoiceAmounts'],
    'other_amounts_lcy': item['OtherAmountsLCY'],
    'comment': item['Comment'],
    'last_statement_no': item['LastStatementNo'],
    'prepayment': item['Prepayment'],
    'partner_type': item['PartnerType'],
    'payments': item['Payments'],
    'post_code': item['PostCode'],
    'print_statements': item['PrintStatements'],
    'prices_including_vat': item['PricesIncludingVAT'],
    'profit_lcy': item['ProfitLCY'],
    'billto_customer_no': item['BilltoCustomerNo'],
    'priority': item['Priority'],
    'payment_method_code': item['PaymentMethodCode'],
    'last_modified_date_time': item['LastModifiedDateTime'],
    'global_dimension1_filter': item['GlobalDimension1Filter'],
    'global_dimension2_filter': item['GlobalDimension2Filter'],
    'balance': item['Balance'],
    'balance_lcy': item['BalanceLCY'],
    'balance_due': item['BalanceDue'],
    'net_change': item['NetChange'],
    'net_change_lcy': item['NetChangeLCY'],
    'sales_lcy': item['SalesLCY'],
    'inv_amounts_lcy': item['InvAmountsLCY'],
    'inv_discounts_lcy': item['InvDiscountsLCY'],
    'no_of_invoices': item['NoofInvoices'],
    'invoice_disc_code': item['InvoiceDiscCode'],
    'invoice_copies': item['InvoiceCopies'],
    'pmt_discounts_lcy': item['PmtDiscountsLCY'],
    'pmt_tolerance_lcy': item['PmtToleranceLCY'],
    'balance_due_lcy': item['BalanceDueLCY'],
    'payments_lcy': item['PaymentsLCY'],
    'cr_memo_amounts': item['CrMemoAmounts'],
    'cr_memo_amounts_lcy': item['CrMemoAmountsLCY'],
    'finance_charge_memo_amounts': item['FinanceChargeMemoAmounts'],
    'shipped_not_invoiced': item['ShippedNotInvoiced'],
    'shipped_not_invoiced_lcy': item['ShippedNotInvoicedLCY'],
    'shipping_agent_code': item['ShippingAgentCode'],
    'application_method': item['ApplicationMethod'],
    'location_code': item['LocationCode'],
    'fax_no': item['FaxNo'],
    'vat_bus_posting_group': item['VATBusPostingGroup'],
    'combine_shipments': item['CombineShipments'],
    'gen_bus_posting_group': item['GenBusPostingGroup'],
    'gln': item['GLN'],
    'county': item['County'],
    'email': item['EMail'],
    'eori_number': item['EORINumber'],
    'use_gln_in_electronic_document': item['UseGLNinElectronicDocument'],
    'reminder_terms_code': item['ReminderTermsCode'],
    'reminder_amounts': item['ReminderAmounts'],
    'reminder_amounts_lcy': item['ReminderAmountsLCY'],
    'tax_area_code': item['TaxAreaCode'],
    'tax_area_id': item['TaxAreaID'],
    'tax_liable': item['TaxLiable'],
    'currency_filter': item['CurrencyFilter'],
    'email_address1': item['EmailAddress1'],
    'email_address2': item['EmailAddress2'],
    'email_address3': item['EmailAddress3'],
    'email_address4': item['EmailAddress4'],
    'user_id': item['UserId'],
    'password': item['Password'],
}


                    # Check if the customer already exists in the database
                    existing_customer = Customer.objects.filter(no=item['No']).first()

                    if existing_customer:
                        # Check if the existing data differs from the new data
                        has_changed = any(getattr(existing_customer, key) != value for key, value in item_data.items())
                        if has_changed:
                            # Update the existing customer record
                            for key, value in item_data.items():
                                setattr(existing_customer, key, value)
                            existing_customer.save()
                    else:
                        # If customer doesn't exist, create a new record
                        Customer.objects.create(system_id=system_id, **item_data)
                    
            url = data.get('@odata.nextLink', None)
        else:
            logger.error(f"Failed to fetch data: {response.status_code} - {response.text}")
            break


