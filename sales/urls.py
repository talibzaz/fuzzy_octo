from django.urls import path

from .views import AddCustomerDetailsView, SaleBillView, GetCustomersList,\
    PrintInvoiceView

app_name = 'sales'

urlpatterns = [
    path('billing/sale-bill/', SaleBillView.as_view(), name='sale-bill'),
    path('billing/print-invoice/', PrintInvoiceView.as_view(), name='print-invoice'),
    path('customer/add-customer-details/', AddCustomerDetailsView.as_view(), name='add-cus-details'),
    path('customer/list/', GetCustomersList.as_view(), name='customer-list'),
]

