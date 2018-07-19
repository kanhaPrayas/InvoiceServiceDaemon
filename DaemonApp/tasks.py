from __future__ import absolute_import
from celery import shared_task
from DaemonApp.models import *
from OrderManagement.InvoiceEngine.InvoiceApp.CeleryTasks import generate_invoice
from django.forms.models import model_to_dict




def service():
	order_lines = OrderLine.objects.filter(invoice=null)
	for order_line in order_lines:
		generate_invoice.apply_async(args=[orderline.id])


service()



