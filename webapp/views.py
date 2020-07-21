from django.shortcuts import render
from webapp.models import Payment
from webapp.models import Application


def rental(request):
    return render(request, 'app/rental.html')


def application2(request):
    return render(request, 'app/Application2.html')


def singin(request):
    my_dict = {'insert_me1': "Hello I am from views.py"}
    return render(request, 'app/SingIn.html', context=my_dict)


def thankyou(request):
    my_dict = {'insert_me1': "Hello I am from Thank_you.py"}
    return render(request, 'app/Thankyou.html', context=my_dict)


def paymentForm(request):
    my_dict = {'insert_me1': "Hello I am from Payment_form.py"}
    return render(request, 'app/Pyment.html', context=my_dict)


def terms(request):
    my_dict = {'insert_me1': "Hello I am from Payment_form.py"}
    return render(request, 'app/terms.html', context=my_dict)


def payment_form_submission(request):
    full_name = request.POST["name"]
    email = request.POST["email"]
    address = request.POST["address"]
    city = request.POST["city"]
    state = request.POST["state"]
    zip_code = request.POST["zip"]
    card_number = request.POST["cardnum"]
    name_on_card = request.POST["cardname"]

    payment_info = Payment(full_name=full_name,
                           address=address,
                           email=email,
                           city=city,
                           state=state,
                           zip_code=zip_code,
                           card_num=card_number,
                           name_on_card=name_on_card)
    payment_info.save()
    return render(request, 'app/Thankyou.html')


def form_name_view(request):
    return render(request, 'app/form_page.html', {'form': form})


def application_form_submission(request):
    first_name = request.POST["firstname"]
    last_name = request.POST["lastname"]
    email = request.POST["email"]
    address = request.POST["address"]
    city = request.POST["city"]
    state = request.POST["state"]
    zip_code = request.POST["zip"]
    house_location = request.POST["location"]
    deposit = request.POST["deposit"]
    date = request.POST["date"]
    phone = request.POST["phone"]
    file = request.POST["file"]

    application_info = Application(first_name=first_name,
                                   last_name=last_name,
                                   email=email,
                                   address=address,
                                   city=city,
                                   state=state,
                                   zip_code=zip_code,
                                   date=date,
                                   phone=phone,
                                   house=house_location,
                                   deposit=deposit,
                                   file=file)
    application_info.save()
    return render(request, 'app/Thank_app.html')
