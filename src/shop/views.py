from django.shortcuts import render
from .models import Laptop
import requests
import json
from .forms import CheckoutForm
from django.shortcuts import redirect
from django.conf import settings

from payments.payment import PayClass


def laptop_list(request):
    laptops = Laptop.objects.all()
    context = {
        "laptops": laptops,
    }

    template_name = "shop/laptop_list.html"
    return render(request, template_name, context)


def laptop_detail(request, pk):
    laptop = Laptop.objects.get(pk=pk)
    context = {"laptop": laptop}
    template_name = "shop/laptop_details.html"
    return render(request, template_name, context)


def checkout(request):
    if request.method == "POST":
        form = CheckoutForm(request.POST)
        if form.is_valid():
            phone_number = form.cleaned_data["phone_number"]
            amount = form.cleaned_data["amount"]
            print("####### some check out is going on")
            callPay = PayClass.momopay(
                amount, "EUR", "reftext", phone_number, "paylaptop"
            )
            print(callPay["response"])
            key = callPay["ref"]
            response = callPay["response"]
            # Verify the transaction
            verify = PayClass.verifymomo(key)

            print(verify)

            if response == 202:
                return redirect("payment-pending")
            else:
                return redirect("payment-failed")
    else:
        form = CheckoutForm()
    context = {"form": form}
    return render(request, "shop/checkout.html", context)


def payment_pending(request):
    return render(request, "shop/payment_pending.html")


def payment_failed(request):
    return render(request, "shop/payment_failed.html")
