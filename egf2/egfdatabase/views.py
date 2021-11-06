from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.core.mail import send_mail
from .models import CustomerInfo, GunInfo, WorkOrder, RecoilPadInfo, Evaluation, WorkOrderForm, Materials, Labor, JobCost, TaxRate, WorkOrderlabor
from django.db.models import Q, Sum
from django.core.paginator import Paginator
from .forms import Custinfoa, CustinfoB, GuninfoA, WorkOrderA, WorkOrderB, RecoilManChoiceField, RecoilStyleChoiceField, RecoilNumberChoiceField, WorkOrderC, Proposal, MaterialA, Evalue, Evalueprev
from django.views import View
from django.template.loader import get_template
from io import BytesIO
import xhtml2pdf.pisa as pisa
from django.http import HttpResponse


def index2(request):
    context = {}
    return render(request, 'egf/index2.html', context)

def home(request):
    return render(request, 'egf/home.html')


def index(request):
    return render(request, 'egf/index.html')


def base(request):
    return render(request, 'egf/base2.html')


def about(request):
    return render(request, 'egf/about.html')


def evaluation(request):
    return render(request, 'egf/evaluation.html')


def services(request):
    return render(request, 'egf/services.html')


def contact(request):
    if request.method == "POST":
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']

        # send an email
        send_mail(
            message_name,  # subject
            message,  # message
            message_email,  # from email
            ['elitegunfitting@gmail.com'],  # To Email
            )

        return render(request, 'egf/contact.html', {'message_name': message_name})

    else:
        return render(request, 'egf/contact.html', {})


def cust_info_existing(request):
    queryset = CustomerInfo.objects.all()
    search_term = ''
    if 'search' in request.GET:
        search_term = request.GET['search']
        queryset = queryset.filter(Q(id__icontains=search_term)
                                   | Q(custcompanytname__icontains=search_term)
                                   | Q(custfirstname__icontains=search_term)
                                   | Q(custlastname__icontains=search_term)
                                   | Q(custadd1__icontains=search_term)
                                   | Q(custadd2__icontains=search_term)
                                   | Q(custcity__icontains=search_term)
                                   | Q(custst__icontains=search_term)
                                   | Q(custzipcode__icontains=search_term)
                                   | Q(custwork1__icontains=search_term)
                                   | Q(custwork2__icontains=search_term)
                                   | Q(custcell1__icontains=search_term)
                                   | Q(custcell2__icontains=search_term)
                                   | Q(custhome__icontains=search_term)
                                   | Q(custemail1__icontains=search_term)
                                   | Q(custemail2__icontains=search_term))
    paginator = Paginator(queryset, 14)  # Show 6 contacts per page
    page = request.GET.get('page')
    queryset = paginator.get_page(page)
    context = {"object_list": queryset, "search_term": search_term}
    return render(request, 'egf/cust_info_existing.html', context)


def cust_info_new(request):
    if request.method == 'POST':
        form = CustinfoB(request.POST)
        if form.is_valid():
            form.save()
            a = CustomerInfo.objects.all()
            d = GunInfo.objects.all()
            instance2 = CustomerInfo.objects.order_by('id').last()
            b = a.values_list('id', flat=True).last()
            c = GunInfo.objects.create(id=b)
            instance3 = GunInfo.objects.order_by('gun_id').last()
            e = d.values_list('gun_id', flat=True).last()
            CustomerInfo.objects.filter(id=b).update(idA=b)
            GunInfo.objects.filter(gun_id=e).update(gunid=e)
            context2 = {
                "instance2": instance2,
                "instance3": instance3,
                "a": a,
                "b": b,
                "c": c,
                "d": d,
                "e": e
            }
            return redirect(instance3.get_absolute2_url(), context2)
        else:
            form = CustinfoB()
            return render(request, 'egf/cust_info_new.html', {'form': form})
    else:
        form = CustinfoB()
        return render(request, 'egf/cust_info_new.html', {'form': form})


def newgun(request, gun_id=None):
    instance = GunInfo.objects.filter(gun_id=gun_id).last()
    form = GuninfoA(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        a = GunInfo.objects.all()
        b = GunInfo.objects.order_by('gun_id').last()
        instance2 = GunInfo.objects.values_list('gun_id', flat=True).last()
        c = GunInfo.objects.order_by('id').last()
        instance1 = GunInfo.objects.values_list('id', flat=True).last()
        f = WorkOrder.objects.all()
        e = WorkOrder.objects.create(gunid=instance2)
        instance4 = WorkOrder.objects.order_by('workorderid').last()
        instance3 = WorkOrder.objects.values_list('workorderid', flat=True).last()
        instance5 = WorkOrder.objects.values_list('date', flat=True).last()
        instance = WorkOrder.objects.filter(workorderid=instance3).update(workorder=instance3, custid=instance1, workorderdate=instance5)
        context2 = {
            "a": a,
            "b": b,
            "c": c,
            "e": e,
            "f": f,
            "instance": instance,
            "instance1": instance1,
            "instance2": instance2,
            "instance3": instance3,
            "instance4": instance4,

        }
        return redirect(instance4.get_absolute6_url(), context2)
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'ecg/newgun.html', context)


def cust_detail(request, id):
    instance = CustomerInfo.objects.get(id=id)
    form = Custinfoa(request.POST or None, instance=instance)
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'egf/cust_detail.html', context)


def gun_info_existing2(request, id=None):
    queryset = GunInfo.objects.filter(id=id)
    form = GuninfoA(request.POST or None)
    if form.is_valid():
        context2 = {
        }
        return redirect(context2)
    context = {
        "object_list": queryset,
        "form": form,
    }
    return render(request, 'egf/gun_info_existing2.html', context)


def gun_info_existing(request, id=None):
    queryset = GunInfo.objects.filter(id=id)
    form = GuninfoA(request.POST or None)
    GunInfo.objects.create(id=id)

    instance3 = GunInfo.objects.order_by('gun_id').last()
    e = GunInfo.objects.values_list('gun_id', flat=True).last()
    g = GunInfo.objects.values_list('id', flat=True).last()
    GunInfo.objects.filter(gun_id=e).update(gunid=e)
    Evaluation.objects.create(gunid=e)
    f = Evaluation.objects.values_list('id', flat=True).last()
    Evaluation.objects.filter(id=f).update(evalueid=f, custid=g)

    context = {
        "object_list": queryset,
        "form": form,
        "instance3 ": instance3
    }
    return redirect(instance3.get_absolute2_url(), context)


def newgun(request, gun_id=None):
    instance = GunInfo.objects.filter(gun_id=gun_id).last()
    form = GuninfoA(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        a = GunInfo.objects.all()
        b = GunInfo.objects.order_by('gun_id').last()
        instance2 = GunInfo.objects.values_list('gun_id', flat=True).last()
        c = GunInfo.objects.order_by('id').last()
        instance1 = GunInfo.objects.values_list('id', flat=True).last()
        f = WorkOrder.objects.all()
        e = WorkOrder.objects.create(gunid=instance2)
        instance4 = WorkOrder.objects.order_by('workorderid').last()
        instance3 = WorkOrder.objects.values_list('workorderid', flat=True).last()
        instance5 = WorkOrder.objects.values_list('date', flat=True).last()
        instance = WorkOrder.objects.filter(workorderid=instance3).update(workorder=instance3, custid=instance1, workorderdate=instance5)
        context2 = {
            "a": a,
            "b": b,
            "c": c,
            "e": e,
            "f": f,
            "instance": instance,
            "instance1": instance1,
            "instance2": instance2,
            "instance3": instance3,
            "instance4": instance4,

        }
        return redirect(instance4.get_absolute6_url(), context2)
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'egf/newgun.html', context)


def cust_info_edit(request, id=None):
    instance = CustomerInfo.objects.get(id=id)
    form = Custinfoa(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return redirect(instance.get_absolute_url())

    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'egf/edit_cust_info.html', context)


def guninfo(request, gun_id=None):
    instance = GunInfo.objects.get(gun_id=gun_id)
    form = GuninfoA(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        instance2 = GunInfo.objects.values_list('gun_id', flat=True).get(gun_id=gun_id)
        f = WorkOrder.objects.all()
        e = WorkOrder.objects.create(gunid=instance2)
        instance4 = WorkOrder.objects.order_by('workorderid').last()
        instance3 = WorkOrder.objects.values_list('workorderid', flat=True).last()
        instance5 = WorkOrder.objects.order_by('date').last()
        instance6 = WorkOrder.objects.values_list('date', flat=True).last()
        instance7 = GunInfo.objects.values_list('id', flat=True).get(gun_id=gun_id)
        instance = WorkOrder.objects.filter(workorderid=instance3).update(workorder=instance3, workorderdate=instance6, custid=instance7, shipping=0, downpay=0)
        context2 = {
            "e": e,
            "f": f,
            "instance": instance,
            "instance3": instance3,
            "instance4": instance4,
            "instance5": instance5,
            "instance6": instance6

        }
        return redirect(instance4.get_absolute6_url(), context2)
    context2 = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'egf/guninfo.html', context2)


def workorder(request, workorderid=None):
    instance = WorkOrder.objects.filter(workorderid=workorderid).last()
    form = WorkOrderA(request.POST or None, instance=instance)
    recoilpadman = RecoilManChoiceField
    recoilpadstyle = RecoilStyleChoiceField
    recoilpadnumber = RecoilNumberChoiceField
    if form.is_valid():
        form.save()
        instance = WorkOrder.objects.order_by('workorderid').last()


        context2 = {
            "instance": instance,

        }
        return redirect(instance.get_absolute6_url(), context2)
    context = {
        "instance": instance,
        "form": form,
        "recoilpadman": recoilpadman,
        "recoilpadstyle": recoilpadstyle,
        "recoilpadnumber":recoilpadnumber
    }
    return render(request, 'egf/workorder.html', context)


def workorder2(request, workorderid=None):
    instance = WorkOrder.objects.filter(workorderid=workorderid).last()
    form = WorkOrderA(request.POST or None, instance=instance)

    if form.is_valid():
        form.save()
        a = MasterTotal.objects.create(workorder=5)

        context2 = {
            "a": a

        }
        return redirect(instance.get_absolute20_url(), context2)
    context = {
        "instance": instance,
        "form": form,

    }
    return render(request, 'egf/workorder2.html', context)


def delete_workorder(request, workorderid):
    instance = get_object_or_404(WorkOrder, workorder=workorderid)
    a = WorkOrderForm.objects.all()
    b = WorkOrder.objects.values_list('workorder', flat=True).last()
    if request.method == "POST":
        a.filter(workorder=b).delete()
        instance.delete()
        return redirect(instance.get_absolute17_url())
    context = {
        "object": instance,
    }
    return render(request, "egf/delete-workorder.html", context)


def workorderprev(request, workorderid=None):
    instance = WorkOrder.objects.get(workorderid=workorderid)
    form = WorkOrderB(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        context2 = {
        }
        return redirect(instance.get_absolute8_url(), context2)
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'egf/workorderprev.html', context)


def previouswo(request, gunid=None):
    queryset = WorkOrder.objects.filter(gunid=gunid)
    form = WorkOrderA(request.POST or None)
    if form.is_valid():
        context2 = {
        }
        return redirect(context2)
    context = {
        "object_list": queryset,
        "form": form,
    }
    return render(request, 'egf/previouswo.html', context)


def fittime(request, workorderid=None):
    instance = get_object_or_404(WorkOrder, workorderid=workorderid)
    form = WorkOrderA(request.POST or None, instance=instance)
    d = request.POST['id_fittingtime']
    WorkOrder.objects.filter(workorderid=workorderid).update(fittingtime_id=d)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute6_url())
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'egf/workorder.html', context)


def fittime2(request, workorderid=None):
    instance = get_object_or_404(WorkOrder, workorderid=workorderid)
    form = WorkOrderA(request.POST or None, instance=instance)
    b = WorkOrder.objects.values_list('workorder', flat=True).last()
    d = WorkOrder.objects.values_list('gunid', flat=True).last()
    s = WorkOrder.objects.values_list('workorderdate', flat=True).last()
    j = WorkOrder.objects.values_list('custid', flat=True).last()
    c = WorkOrder.objects.values_list('fittingtime_id', flat=True).last()
    e = Labor.objects.values_list('labor', flat=True).last()
    f = c*e
    z = 17
    e = WorkOrderForm.objects.create(workorder=b, ident=z)
    n = 'Fitting Time'
    h = WorkOrderForm.objects.filter(workorder=b, ident=z).update(gunid=d, custid=j, workorderdate=s, description=n, labor=f, retail=0)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute6_url())
    context = {
        "instance": instance,
        "form": form,
        "e": e,
        "h": h
    }
    return render(request, 'egf/workorder.html', context)


def delete_fittime(request, workorderid=None):
    instance = get_object_or_404(WorkOrder, workorderid=workorderid)
    form = WorkOrderA(request.POST or None, instance=instance)
    a = WorkOrderForm.objects.all()
    a.filter(ident=17).delete()
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute6_url())
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'egf/workorder.html', context)


def delete_duplicating(request, workorderid=None):
    instance = get_object_or_404(WorkOrder, workorderid=workorderid)
    form = WorkOrderA(request.POST or None, instance=instance)
    b = WorkOrder.objects.values_list('workorder', flat=True).last()
    n = WorkOrder.objects.values_list('duplicating_id', flat=True).last()
    a = WorkOrderForm.objects.all()
    a.filter(description=n, workorder=b).delete()
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute6_url())
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'egf/workorder.html', context)


def duplicating(request, workorderid=None):
    instance = get_object_or_404(WorkOrder, workorderid=workorderid)
    form = WorkOrderA(request.POST or None, instance=instance)
    d = request.POST['id_duplicating']
    WorkOrder.objects.filter(workorderid=workorderid).update(duplicating_id=d)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute6_url())
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'egf/workorder.html', context)


def duplicating2(request, workorderid=None):
    instance = get_object_or_404(WorkOrder, workorderid=workorderid)
    form = WorkOrderA(request.POST or None, instance=instance)
    b = WorkOrder.objects.values_list('workorder', flat=True).last()
    d = WorkOrder.objects.values_list('gunid', flat=True).last()
    s = WorkOrder.objects.values_list('workorderdate', flat=True).last()
    j = WorkOrder.objects.values_list('custid', flat=True).last()
    n = WorkOrder.objects.values_list('duplicating_id', flat=True).last()
    z = 1
    e = WorkOrderForm.objects.create(workorder=b, ident=z)
    f = Materials.objects.values_list('labor', flat=True).get(description=n)
    g = Materials.objects.values_list('retailcost', flat=True).get(description=n)
    h = WorkOrderForm.objects.filter(workorder=b, ident=z).update(gunid=d, custid=j, workorderdate=s, description=n, labor=f , retail=g)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute6_url())
    context = {
        "instance": instance,
        "form": form,
        "e": e,
        "h": h
    }
    return render(request, 'egf/workorder.html', context)


def fittingstock(request, workorderid=None):
    instance = get_object_or_404(WorkOrder, workorderid=workorderid)
    form = WorkOrderA(request.POST or None, instance=instance)
    d = request.POST['id_fittingstock']
    WorkOrder.objects.filter(workorderid=workorderid).update(fittingstock_id=d)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute6_url())
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'egf/workorder.html', context)


def fittingstock2(request, workorderid=None):
    instance = get_object_or_404(WorkOrder, workorderid=workorderid)
    form = WorkOrderA(request.POST or None, instance=instance)
    a = WorkOrder.objects.order_by('workorder').last()
    b = WorkOrder.objects.values_list('workorder', flat=True).last()
    c = WorkOrder.objects.order_by('gunid').last()
    d = WorkOrder.objects.values_list('gunid', flat=True).last()
    k = WorkOrder.objects.order_by('workorderdate').last()
    s = WorkOrder.objects.values_list('workorderdate', flat=True).last()
    i = WorkOrder.objects.order_by('custid').last()
    j = WorkOrder.objects.values_list('custid', flat=True).last()
    m = WorkOrder.objects.order_by('fittingstock_id').last()
    n = WorkOrder.objects.values_list('fittingstock_id', flat=True).last()
    z = 2
    e = WorkOrderForm.objects.create(workorder=b, ident=z)
    f = Materials.objects.values_list('labor', flat=True).get(description=n)
    g = Materials.objects.values_list('retailcost', flat=True).get(description=n)

    h = WorkOrderForm.objects.filter(workorder=b, ident=z).update(gunid=d, custid=j, workorderdate=s, description=n, labor=f, retail=g)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute6_url())
    context = {
        "instance": instance,
        "form": form,
        "a": a,
        "c": c,
        "e": e,
        "h": h,
        "i": i,
        "k": k,
        "m": m

    }
    return render(request, 'egf/workorder.html', context)


def delete_fittingstock(request, workorderid=None):
    instance = get_object_or_404(WorkOrder, workorderid=workorderid)
    form = WorkOrderA(request.POST or None, instance=instance)
    b = WorkOrder.objects.values_list('workorder', flat=True).last()
    n = WorkOrder.objects.values_list('fittingstock_id', flat=True).last()
    a = WorkOrderForm.objects.all()
    a.filter(description=n, workorder=b).delete()
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute6_url())
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'egf/workorder.html', context)


def refinishing(request, workorderid=None):
    instance = get_object_or_404(WorkOrder, workorderid=workorderid)
    form = WorkOrderA(request.POST or None, instance=instance)
    d = request.POST['id_refinishing']
    WorkOrder.objects.filter(workorderid=workorderid).update(refinishing_id=d)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute6_url())
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'egf/workorder.html', context)


def refinishing2(request, workorderid=None):
    instance = get_object_or_404(WorkOrder, workorderid=workorderid)
    form = WorkOrderA(request.POST or None, instance=instance)
    b = WorkOrder.objects.values_list('workorder', flat=True).last()
    d = WorkOrder.objects.values_list('gunid', flat=True).last()
    s = WorkOrder.objects.values_list('workorderdate', flat=True).last()
    j = WorkOrder.objects.values_list('custid', flat=True).last()
    n = WorkOrder.objects.values_list('refinishing_id', flat=True).last()
    z = 3
    e = WorkOrderForm.objects.create(workorder=b, ident=z)
    f = Materials.objects.values_list('labor', flat=True).get(description=n)
    g = Materials.objects.values_list('retailcost', flat=True).get(description=n)
    h = WorkOrderForm.objects.filter(workorder=b, ident=z).update(gunid=d, custid=j, workorderdate=s, description=n, labor=f , retail=g)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute6_url())
    context = {
        "instance": instance,
        "form": form,
        "e": e,
        "h": h
    }
    return render(request, 'egf/workorder.html', context)


def delete_refinishing(request, workorderid=None):
    instance = get_object_or_404(WorkOrder, workorderid=workorderid)
    form = WorkOrderA(request.POST or None, instance=instance)
    b = WorkOrder.objects.values_list('workorder', flat=True).last()
    n = WorkOrder.objects.values_list('refinishing_id', flat=True).last()
    a = WorkOrderForm.objects.all()
    a.filter(description=n, workorder=b).delete()
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute6_url())
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'egf/workorder.html', context)


def delete_finishtype(request, workorderid=None):
    instance = get_object_or_404(WorkOrder, workorderid=workorderid)
    form = WorkOrderA(request.POST or None, instance=instance)
    b = WorkOrder.objects.values_list('workorder', flat=True).last()
    n = WorkOrder.objects.values_list('finishtype_id', flat=True).last()
    a = WorkOrderForm.objects.all()
    a.filter(description=n, workorder=b).delete()
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute6_url())
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'egf/workorder.html', context)


def finishtype(request, workorderid=None):
    instance = get_object_or_404(WorkOrder, workorderid=workorderid)
    form = WorkOrderA(request.POST or None, instance=instance)
    d = request.POST['id_finishtype']
    WorkOrder.objects.filter(workorderid=workorderid).update(finishtype_id=d)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute6_url())
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'egf/workorder.html', context)


def finishtype2(request, workorderid=None):
    instance = get_object_or_404(WorkOrder, workorderid=workorderid)
    form = WorkOrderA(request.POST or None, instance=instance)
    b = WorkOrder.objects.values_list('workorder', flat=True).last()
    d = WorkOrder.objects.values_list('gunid', flat=True).last()
    s = WorkOrder.objects.values_list('workorderdate', flat=True).last()
    j = WorkOrder.objects.values_list('custid', flat=True).last()
    n = WorkOrder.objects.values_list('finishtype_id', flat=True).last()
    z = 4
    e = WorkOrderForm.objects.create(workorder=b, ident=z)
    f = Materials.objects.values_list('labor', flat=True).get(description=n)
    g = Materials.objects.values_list('retailcost', flat=True).get(description=n)
    h = WorkOrderForm.objects.filter(workorder=b, ident=z).update(gunid=d, custid=j, workorderdate=s, description=n, labor=f , retail=g)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute6_url())
    context = {
        "instance": instance,
        "form": form,
        "e": e,
        "h": h
    }
    return render(request, 'egf/workorder.html', context)


def recoilpad(request, workorderid=None):
    instance = get_object_or_404(WorkOrder, workorderid=workorderid)
    form = WorkOrderA(request.POST or None, instance=instance)
    d = request.POST['id_recoilpad']
    WorkOrder.objects.filter(workorderid=workorderid).update(recoilpad_id=d)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute6_url())
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'egf/workorder.html', context)


def recoilpad2(request, workorderid=None):
    instance = get_object_or_404(WorkOrder, workorderid=workorderid)
    form = WorkOrderA(request.POST or None, instance=instance)
    b = WorkOrder.objects.values_list('workorder', flat=True).last()
    d = WorkOrder.objects.values_list('gunid', flat=True).last()
    s = WorkOrder.objects.values_list('workorderdate', flat=True).last()
    j = WorkOrder.objects.values_list('custid', flat=True).last()
    n = WorkOrder.objects.values_list('recoilpad_id', flat=True).last()
    z = 5
    e = WorkOrderForm.objects.create(workorder=b, ident=z)
    f = Materials.objects.values_list('labor', flat=True).get(description=n)
    g = Materials.objects.values_list('retailcost', flat=True).get(description=n)
    h = WorkOrderForm.objects.filter(workorder=b, ident=z).update(gunid=d, custid=j, workorderdate=s, description=n, labor=f , retail=g)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute6_url())
    context = {
        "instance": instance,
        "form": form,
        "e": e,
        "h": h
    }
    return render(request, 'egf/workorder.html', context)


def delete_recoilpad(request, workorderid=None):
    instance = get_object_or_404(WorkOrder, workorderid=workorderid)
    form = WorkOrderA(request.POST or None, instance=instance)
    b = WorkOrder.objects.values_list('workorder', flat=True).last()
    n = WorkOrder.objects.values_list('recoilpad_id', flat=True).last()
    a = WorkOrderForm.objects.all()
    a.filter(description=n, workorder=b).delete()
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute6_url())
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'egf/workorder.html', context)


def recoilpadman(request, workorderid=None):
    instance = get_object_or_404(WorkOrder, workorderid=workorderid)
    form = WorkOrderA(request.POST or None, instance=instance)
    d = request.POST['id_recoilpadman']
    WorkOrder.objects.filter(workorderid=workorderid).update(recoilpadman=d)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute6_url())
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'egf/workorder.html', context)


def load_recoilpadstyle(request, workorderid=None):
    a = WorkOrder.objects.all()
    instance = get_object_or_404(WorkOrder, workorderid=workorderid)
    form = WorkOrderA(request.POST or None, instance=instance)
    b = a.values_list('recoilpadman', flat=True).get(workorderid=workorderid)
    c = RecoilPadInfo.objects.filter(PadMan=b).values('Padstyle').distinct().order_by('Padstyle')
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute6_url())
    context = {
        "instance": instance,
        "c": c,
        "form": form,
    }
    return render(request, 'egf/recoilstyle_dropdown.html', context)


def recoilpadstyle(request, workorderid=None):
    instance = get_object_or_404(WorkOrder, workorderid=workorderid)
    form = WorkOrderA(request.POST or None, instance=instance)
    d = request.POST.get('id_recoilpadstyle')
    WorkOrder.objects.filter(workorderid=workorderid).update(recoilpadstyle=d)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute6_url())
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'egf/workorder.html', context)


def load_recoilpadnum(request, workorderid=None):
    a = WorkOrder.objects.all()
    instance = get_object_or_404(WorkOrder, workorderid=workorderid)
    form = WorkOrderA(request.POST or None, instance=instance)
    b = a.values_list('recoilpadman', flat=True).get(workorderid=workorderid)
    d = a.values_list('recoilpadstyle', flat=True).get(workorderid=workorderid)
    c = RecoilPadInfo.objects.filter(PadMan=b, Padstyle=d).values("Padnum").distinct().order_by("Padnum")
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute6_url())
    context = {
        "instance": instance,
        "c": c,
        "d": d,
        "form": form,
    }
    return render(request, 'egf/recoilnumber_dropdown.html', context)


def recoilpadnum(request, workorderid=None):
    instance = get_object_or_404(WorkOrder, workorderid=workorderid)
    form = WorkOrderA(request.POST or None, instance=instance)
    d = request.POST.get('id_recoilpadnumber')
    WorkOrder.objects.filter(workorderid=workorderid).update(recoilpadnumber=d)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute6_url())
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'egf/workorder.html', context)


def recoilpadnum2(request, workorderid=None):
    instance = get_object_or_404(WorkOrder, workorderid=workorderid)
    form = WorkOrderA(request.POST or None, instance=instance)
    b = WorkOrder.objects.values_list('workorder', flat=True).last()
    d = WorkOrder.objects.values_list('gunid', flat=True).last()
    s = WorkOrder.objects.values_list('workorderdate', flat=True).last()
    j = WorkOrder.objects.values_list('custid', flat=True).last()
    n = WorkOrder.objects.values_list('recoilpadnumber', flat=True).last()
    z = 6
    e = WorkOrderForm.objects.create(workorder=b, ident=z)
    f = Materials.objects.values_list('labor', flat=True).get(description=n)
    g = Materials.objects.values_list('retailcost', flat=True).get(description=n)
    h = WorkOrderForm.objects.filter(workorder=b, ident=z).update(gunid=d, custid=j, workorderdate=s, description=n, labor=f, retail=g)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute6_url())
    context = {
        "instance": instance,
        "form": form,
        "e": e,
        "h": h
    }
    return render(request, 'egf/workorder.html', context)


def delete_recoilpadnum(request, workorderid=None):
    instance = get_object_or_404(WorkOrder, workorderid=workorderid)
    form = WorkOrderA(request.POST or None, instance=instance)
    b = WorkOrder.objects.values_list('workorder', flat=True).last()
    n = WorkOrder.objects.values_list('recoilpadnumber', flat=True).last()
    a = WorkOrderForm.objects.all()
    a.filter(description=n, workorder=b).delete()
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute6_url())
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'egf/workorder.html', context)


def stockmod1(request, workorderid=None):
    instance = get_object_or_404(WorkOrder, workorderid=workorderid)
    form = WorkOrderA(request.POST or None, instance=instance)
    d = request.POST['id_stockmod1']
    WorkOrder.objects.filter(workorderid=workorderid).update(stockmod1_id=d)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute6_url())
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'egf/workorder.html', context)


def stockmod12(request, workorderid=None):
    instance = get_object_or_404(WorkOrder, workorderid=workorderid)
    form = WorkOrderA(request.POST or None, instance=instance)
    b = WorkOrder.objects.values_list('workorder', flat=True).last()
    d = WorkOrder.objects.values_list('gunid', flat=True).last()
    s = WorkOrder.objects.values_list('workorderdate', flat=True).last()
    j = WorkOrder.objects.values_list('custid', flat=True).last()
    n = WorkOrder.objects.values_list('stockmod1', flat=True).last()
    z = 7
    e = WorkOrderForm.objects.create(workorder=b, ident=z)
    f = Materials.objects.values_list('labor', flat=True).get(description=n)
    g = Materials.objects.values_list('retailcost', flat=True).get(description=n)
    h = WorkOrderForm.objects.filter(workorder=b, ident=z).update(gunid=d, custid=j, workorderdate=s, description=n, labor=f , retail=g)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute6_url())
    context = {
        "instance": instance,
        "form": form,
        "e": e,
        "h": h
    }
    return render(request, 'egf/workorder.html', context)


def delete_stockmod1(request, workorderid=None):
    instance = get_object_or_404(WorkOrder, workorderid=workorderid)
    form = WorkOrderA(request.POST or None, instance=instance)
    b = WorkOrder.objects.values_list('workorder', flat=True).last()
    n = WorkOrder.objects.values_list('stockmod1_id', flat=True).last()
    a = WorkOrderForm.objects.all()
    a.filter(description=n, workorder=b).delete()
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute6_url())
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'egf/workorder.html', context)


def stockmod2(request, workorderid=None):
    instance = get_object_or_404(WorkOrder, workorderid=workorderid)
    form = WorkOrderA(request.POST or None, instance=instance)
    d = request.POST['id_stockmod2']
    WorkOrder.objects.filter(workorderid=workorderid).update(stockmod2_id=d)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute6_url())
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'egf/workorder.html', context)


def stockmod22(request, workorderid=None):
    instance = get_object_or_404(WorkOrder, workorderid=workorderid)
    form = WorkOrderA(request.POST or None, instance=instance)
    b = WorkOrder.objects.values_list('workorder', flat=True).last()
    d = WorkOrder.objects.values_list('gunid', flat=True).last()
    s = WorkOrder.objects.values_list('workorderdate', flat=True).last()
    j = WorkOrder.objects.values_list('custid', flat=True).last()
    n = WorkOrder.objects.values_list('stockmod2', flat=True).last()
    z = 8
    e = WorkOrderForm.objects.create(workorder=b, ident=z)
    f = Materials.objects.values_list('labor', flat=True).get(description=n)
    g = Materials.objects.values_list('retailcost', flat=True).get(description=n)
    h = WorkOrderForm.objects.filter(workorder=b, ident=z).update(gunid=d, custid=j, workorderdate=s, description=n, labor=f , retail=g)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute6_url())
    context = {
        "instance": instance,
        "form": form,
        "e": e,
        "h": h
    }
    return render(request, 'egf/workorder.html', context)


def delete_stockmod2(request, workorderid=None):
    instance = get_object_or_404(WorkOrder, workorderid=workorderid)
    form = WorkOrderA(request.POST or None, instance=instance)
    b = WorkOrder.objects.values_list('workorder', flat=True).last()
    n = WorkOrder.objects.values_list('stockmod2_id', flat=True).last()
    a = WorkOrderForm.objects.all()
    a.filter(description=n, workorder=b).delete()
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute6_url())
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'egf/workorder.html', context)


def stockmod3(request, workorderid=None):
    instance = get_object_or_404(WorkOrder, workorderid=workorderid)
    form = WorkOrderA(request.POST or None, instance=instance)
    d = request.POST['id_stockmod3']
    WorkOrder.objects.filter(workorderid=workorderid).update(stockmod3_id=d)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute6_url())
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'egf/workorder.html', context)


def stockmod32(request, workorderid=None):
    instance = get_object_or_404(WorkOrder, workorderid=workorderid)
    form = WorkOrderA(request.POST or None, instance=instance)
    b = WorkOrder.objects.values_list('workorder', flat=True).last()
    d = WorkOrder.objects.values_list('gunid', flat=True).last()
    s = WorkOrder.objects.values_list('workorderdate', flat=True).last()
    j = WorkOrder.objects.values_list('custid', flat=True).last()
    n = WorkOrder.objects.values_list('stockmod3', flat=True).last()
    z = 9
    e = WorkOrderForm.objects.create(workorder=b, ident=z)
    f = Materials.objects.values_list('labor', flat=True).get(description=n)
    g = Materials.objects.values_list('retailcost', flat=True).get(description=n)
    h = WorkOrderForm.objects.filter(workorder=b, ident=z).update(gunid=d, custid=j, workorderdate=s, description=n, labor=f , retail=g)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute6_url())
    context = {
        "instance": instance,
        "form": form,
        "e": e,
        "h": h
    }
    return render(request, 'egf/workorder.html', context)


def delete_stockmod3(request, workorderid=None):
    instance = get_object_or_404(WorkOrder, workorderid=workorderid)
    form = WorkOrderA(request.POST or None, instance=instance)
    b = WorkOrder.objects.values_list('workorder', flat=True).last()
    n = WorkOrder.objects.values_list('stockmod3_id', flat=True).last()
    a = WorkOrderForm.objects.all()
    a.filter(description=n, workorder=b).delete()
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute6_url())
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'egf/workorder.html', context)


def stockrepairtype(request, workorderid=None):
    instance = get_object_or_404(WorkOrder, workorderid=workorderid)
    form = WorkOrderA(request.POST or None, instance=instance)
    d = request.POST['id_stockrepairtype']
    WorkOrder.objects.filter(workorderid=workorderid).update(stockrepairtype_id=d)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute6_url())
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'egf/workorder.html', context)


def stockrepairtype2(request, workorderid=None):
    instance = get_object_or_404(WorkOrder, workorderid=workorderid)
    form = WorkOrderA(request.POST or None, instance=instance)
    b = WorkOrder.objects.values_list('workorder', flat=True).last()
    d = WorkOrder.objects.values_list('gunid', flat=True).last()
    s = WorkOrder.objects.values_list('workorderdate', flat=True).last()
    j = WorkOrder.objects.values_list('custid', flat=True).last()
    n = WorkOrder.objects.values_list('stockrepairtype_id', flat=True).last()
    z = 10
    e = WorkOrderForm.objects.create(workorder=b, ident=z)
    f = Materials.objects.values_list('labor', flat=True).get(description=n)
    g = Materials.objects.values_list('retailcost', flat=True).get(description=n)
    h = WorkOrderForm.objects.filter(workorder=b, ident=z).update(gunid=d, custid=j, workorderdate=s, description=n, labor=f , retail=g)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute6_url())
    context = {
        "instance": instance,
        "form": form,
        "e": e,
        "h": h
    }
    return render(request, 'egf/workorder.html', context)


def delete_stockrepairtype(request, workorderid=None):
    instance = get_object_or_404(WorkOrder, workorderid=workorderid)
    form = WorkOrderA(request.POST or None, instance=instance)
    b = WorkOrder.objects.values_list('workorder', flat=True).last()
    n = WorkOrder.objects.values_list('stockrepairtype_id', flat=True).last()
    a = WorkOrderForm.objects.all()
    a.filter(description=n, workorder=b).delete()
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute6_url())
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'egf/workorder.html', context)


def stockrepair(request, workorderid=None):
    instance = get_object_or_404(WorkOrder, workorderid=workorderid)
    form = WorkOrderA(request.POST or None, instance=instance)
    d = request.POST['id_stockrepair']
    WorkOrder.objects.filter(workorderid=workorderid).update(stockrepair_id=d)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute6_url())
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'egf/workorder.html', context)


def stockrepair2(request, workorderid=None):
    instance = get_object_or_404(WorkOrder, workorderid=workorderid)
    form = WorkOrderA(request.POST or None, instance=instance)
    b = WorkOrder.objects.values_list('workorder', flat=True).last()
    d = WorkOrder.objects.values_list('gunid', flat=True).last()
    s = WorkOrder.objects.values_list('workorderdate', flat=True).last()
    j = WorkOrder.objects.values_list('custid', flat=True).last()
    c = WorkOrder.objects.values_list('stockrepair_id', flat=True).last()
    e = Labor.objects.values_list('labor', flat=True).last()
    f = c * e
    z = 18
    e = WorkOrderForm.objects.create(workorder=b, ident=z)
    n = 'Stock Repair Time'
    h = WorkOrderForm.objects.filter(workorder=b, ident=z).update(gunid=d, custid=j, workorderdate=s, description=n, labor=f, retail=0)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute6_url())
    context = {
        "instance": instance,
        "form": form,
        "e": e,
        "h": h
    }
    return render(request, 'egf/workorder.html', context)


def delete_stockrepair(request, workorderid=None):
    instance = get_object_or_404(WorkOrder, workorderid=workorderid)
    form = WorkOrderA(request.POST or None, instance=instance)
    a = WorkOrderForm.objects.all()
    a.filter(ident=18).delete()
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute6_url())
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'egf/workorder.html', context)


def checkering(request, workorderid=None):
    instance = get_object_or_404(WorkOrder, workorderid=workorderid)
    form = WorkOrderA(request.POST or None, instance=instance)
    d = request.POST['id_checkering']
    WorkOrder.objects.filter(workorderid=workorderid).update(checkering_id=d)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute6_url())
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'egf/workorder.html', context)


def checkering2(request, workorderid=None):
    instance = get_object_or_404(WorkOrder, workorderid=workorderid)
    form = WorkOrderA(request.POST or None, instance=instance)
    b = WorkOrder.objects.values_list('workorder', flat=True).last()
    d = WorkOrder.objects.values_list('gunid', flat=True).last()
    s = WorkOrder.objects.values_list('workorderdate', flat=True).last()
    j = WorkOrder.objects.values_list('custid', flat=True).last()
    n = WorkOrder.objects.values_list('checkering_id', flat=True).last()
    z = 11
    e = WorkOrderForm.objects.create(workorder=b, ident=z)
    f = Materials.objects.values_list('labor', flat=True).get(description=n)
    g = Materials.objects.values_list('retailcost', flat=True).get(description=n)
    h = WorkOrderForm.objects.filter(workorder=b, ident=z).update(gunid=d, custid=j, workorderdate=s, description=n, labor=f , retail=g)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute6_url())
    context = {
        "instance": instance,
        "form": form,
        "e": e,
        "h": h
    }
    return render(request, 'egf/workorder.html', context)


def delete_checkering(request, workorderid=None):
    instance = get_object_or_404(WorkOrder, workorderid=workorderid)
    form = WorkOrderA(request.POST or None, instance=instance)
    b = WorkOrder.objects.values_list('workorder', flat=True).last()
    n = WorkOrder.objects.values_list('checkering_id', flat=True).last()
    a = WorkOrderForm.objects.all()
    a.filter(description=n, workorder=b).delete()
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute6_url())
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'egf/workorder.html', context)


def wood(request, workorderid=None):
    instance = get_object_or_404(WorkOrder, workorderid=workorderid)
    form = WorkOrderA(request.POST or None, instance=instance)
    d = request.POST['id_wood']
    WorkOrder.objects.filter(workorderid=workorderid).update(wood_id=d)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute6_url())
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'egf/workorder.html', context)


def description1(request, workorderid=None):
    instance = get_object_or_404(WorkOrder, workorderid=workorderid)
    form = WorkOrderA(request.POST or None, instance=instance)
    d = request.POST['id_description1']
    WorkOrder.objects.filter(workorderid=workorderid).update(description1=d)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute6_url())
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'egf/workorder.html', context)


def description12(request, workorderid=None):
    instance = get_object_or_404(WorkOrder, workorderid=workorderid)
    form = WorkOrderA(request.POST or None, instance=instance)
    b = WorkOrder.objects.values_list('workorder', flat=True).last()
    d = WorkOrder.objects.values_list('gunid', flat=True).last()
    s = WorkOrder.objects.values_list('workorderdate', flat=True).last()
    j = WorkOrder.objects.values_list('custid', flat=True).last()
    n = WorkOrder.objects.values_list('description1', flat=True).last()
    o = WorkOrder.objects.values_list('labor1', flat=True).last()
    p = WorkOrder.objects.values_list('retailmaterialcost1', flat=True).last()
    z = 12
    e = WorkOrderForm.objects.create(workorder=b, ident=z)

    h = WorkOrderForm.objects.filter(workorder=b, ident=z).update(gunid=d, custid=j, workorderdate=s, description=n, labor=o, retail=p)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute6_url())
    context = {
        "instance": instance,
        "form": form,
        "e": e,
        "h": h
    }
    return render(request, 'egf/workorder.html', context)


def delete_description1(request, workorderid=None):
    instance = get_object_or_404(WorkOrder, workorderid=workorderid)
    form = WorkOrderA(request.POST or None, instance=instance)
    a = WorkOrderForm.objects.all()
    a.filter(ident=12).delete()
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute6_url())
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'egf/workorder.html', context)


def labor1(request, workorderid=None):
    instance = get_object_or_404(WorkOrder, workorderid=workorderid)
    form = WorkOrderA(request.POST or None, instance=instance)
    d = request.POST['id_labor1']
    WorkOrder.objects.filter(workorderid=workorderid).update(labor1=d)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute6_url())
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'egf/workorder.html', context)


def labor12(request, workorderid=None):
    instance = get_object_or_404(WorkOrder, workorderid=workorderid)
    form = WorkOrderA(request.POST or None, instance=instance)
    b = WorkOrder.objects.values_list('labor1', flat=True).last()
    d = WorkOrder.objects.values_list('description1', flat=True).last()
    g = WorkOrder.objects.values_list('workorder', flat=True).last()
    h = WorkOrderForm.objects.filter(workorder=g, ident=12).update(labor=b)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute6_url())
    context = {
        "instance": instance,
        "form": form,
        "b": b,
        "d": d,
        "h": h,
    }
    return render(request, 'egf/workorder.html', context)


def retailmaterialcost1(request, workorderid=None):
    instance = get_object_or_404(WorkOrder, workorderid=workorderid)
    form = WorkOrderA(request.POST or None, instance=instance)
    d = request.POST['id_retailmaterialcost1']
    WorkOrder.objects.filter(workorderid=workorderid).update(retailmaterialcost1=d)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute6_url())
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'egf/workorder.html', context)


def retailmaterialcost12(request, workorderid=None):
    instance = get_object_or_404(WorkOrder, workorderid=workorderid)
    form = WorkOrderA(request.POST or None, instance=instance)
    b = WorkOrder.objects.values_list('retailmaterialcost1', flat=True).last()
    d = WorkOrder.objects.values_list('description1', flat=True).last()
    g = WorkOrder.objects.values_list('workorder', flat=True).last()
    h = WorkOrderForm.objects.filter(workorder=g, ident=12).update(retail=b)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute6_url())
    context = {
        "instance": instance,
        "form": form,
        "b": b,
        "d": d,
        "h": h,
    }
    return render(request, 'egf/workorder.html', context)


def description2(request, workorderid=None):
    instance = get_object_or_404(WorkOrder, workorderid=workorderid)
    form = WorkOrderA(request.POST or None, instance=instance)
    d = request.POST['id_description2']
    WorkOrder.objects.filter(workorderid=workorderid).update(description2=d)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute6_url())
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'egf/workorder.html', context)


def description22(request, workorderid=None):
    instance = get_object_or_404(WorkOrder, workorderid=workorderid)
    form = WorkOrderA(request.POST or None, instance=instance)
    b = WorkOrder.objects.values_list('workorder', flat=True).last()
    d = WorkOrder.objects.values_list('gunid', flat=True).last()
    s = WorkOrder.objects.values_list('workorderdate', flat=True).last()
    j = WorkOrder.objects.values_list('custid', flat=True).last()
    n = WorkOrder.objects.values_list('description2', flat=True).last()
    o = WorkOrder.objects.values_list('labor2', flat=True).last()
    p = WorkOrder.objects.values_list('retailmaterialcost2', flat=True).last()
    z = 13
    e = WorkOrderForm.objects.create(workorder=b, ident=z)

    h = WorkOrderForm.objects.filter(workorder=b, ident=z).update(gunid=d, custid=j, workorderdate=s, description=n, labor=o, retail=p)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute6_url())
    context = {
        "instance": instance,
        "form": form,
        "e": e,
        "h": h
    }
    return render(request, 'egf/workorder.html', context)


def delete_description2(request, workorderid=None):
    instance = get_object_or_404(WorkOrder, workorderid=workorderid)
    form = WorkOrderA(request.POST or None, instance=instance)
    a = WorkOrderForm.objects.all()
    a.filter(ident=13).delete()
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute6_url())
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'egf/workorder.html', context)


def labor2(request, workorderid=None):
    instance = get_object_or_404(WorkOrder, workorderid=workorderid)
    form = WorkOrderA(request.POST or None, instance=instance)
    d = request.POST['id_labor2']
    WorkOrder.objects.filter(workorderid=workorderid).update(labor2=d)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute6_url())
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'egf/workorder.html', context)


def labor22(request, workorderid=None):
    instance = get_object_or_404(WorkOrder, workorderid=workorderid)
    form = WorkOrderA(request.POST or None, instance=instance)
    b = WorkOrder.objects.values_list('labor2', flat=True).last()
    d = WorkOrder.objects.values_list('description2', flat=True).last()
    g = WorkOrder.objects.values_list('workorder', flat=True).last()
    h = WorkOrderForm.objects.filter(workorder=g, ident=13).update(labor=b)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute6_url())
    context = {
        "instance": instance,
        "form": form,
        "b": b,
        "d": d,
        "h": h,
    }
    return render(request, 'egf/workorder.html', context)


def retailmaterialcost2(request, workorderid=None):
    instance = get_object_or_404(WorkOrder, workorderid=workorderid)
    form = WorkOrderA(request.POST or None, instance=instance)
    d = request.POST['id_retailmaterialcost2']
    WorkOrder.objects.filter(workorderid=workorderid).update(retailmaterialcost2=d)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute6_url())
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'egf/workorder.html', context)


def retailmaterialcost22(request, workorderid=None):
    instance = get_object_or_404(WorkOrder, workorderid=workorderid)
    form = WorkOrderA(request.POST or None, instance=instance)
    b = WorkOrder.objects.values_list('retailmaterialcost2', flat=True).last()
    d = WorkOrder.objects.values_list('description2', flat=True).last()
    g = WorkOrder.objects.values_list('workorder', flat=True).last()
    h = WorkOrderForm.objects.filter(workorder=g, ident=13).update(retail=b)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute6_url())
    context = {
        "instance": instance,
        "form": form,
        "b": b,
        "d": d,
        "h": h,
    }
    return render(request, 'egf/workorder.html', context)


def description3(request, workorderid=None):
    instance = get_object_or_404(WorkOrder, workorderid=workorderid)
    form = WorkOrderA(request.POST or None, instance=instance)
    d = request.POST['id_description3']
    WorkOrder.objects.filter(workorderid=workorderid).update(description3=d)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute6_url())
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'egf/workorder.html', context)


def description32(request, workorderid=None):
    instance = get_object_or_404(WorkOrder, workorderid=workorderid)
    form = WorkOrderA(request.POST or None, instance=instance)
    b = WorkOrder.objects.values_list('workorder', flat=True).last()
    d = WorkOrder.objects.values_list('gunid', flat=True).last()
    s = WorkOrder.objects.values_list('workorderdate', flat=True).last()
    j = WorkOrder.objects.values_list('custid', flat=True).last()
    n = WorkOrder.objects.values_list('description3', flat=True).last()
    o = WorkOrder.objects.values_list('labor3', flat=True).last()
    p = WorkOrder.objects.values_list('retailmaterialcost3', flat=True).last()
    z = 14
    e = WorkOrderForm.objects.create(workorder=b, ident=z)

    h = WorkOrderForm.objects.filter(workorder=b, ident=z).update(gunid=d, custid=j, workorderdate=s, description=n, labor=o, retail=p)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute6_url())
    context = {
        "instance": instance,
        "form": form,
        "e": e,
        "h": h
    }
    return render(request, 'egf/workorder.html', context)


def delete_description3(request, workorderid=None):
    instance = get_object_or_404(WorkOrder, workorderid=workorderid)
    form = WorkOrderA(request.POST or None, instance=instance)
    a = WorkOrderForm.objects.all()
    a.filter(ident=14).delete()
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute6_url())
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'egf/workorder.html', context)


def labor3(request, workorderid=None):
    instance = get_object_or_404(WorkOrder, workorderid=workorderid)
    form = WorkOrderA(request.POST or None, instance=instance)
    d = request.POST['id_labor3']
    WorkOrder.objects.filter(workorderid=workorderid).update(labor3=d)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute6_url())
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'egf/workorder.html', context)


def labor32(request, workorderid=None):
    instance = get_object_or_404(WorkOrder, workorderid=workorderid)
    form = WorkOrderA(request.POST or None, instance=instance)
    b = WorkOrder.objects.values_list('labor3', flat=True).last()
    d = WorkOrder.objects.values_list('description3', flat=True).last()
    g = WorkOrder.objects.values_list('workorder', flat=True).last()
    h = WorkOrderForm.objects.filter(workorder=g, ident=14).update(labor=b)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute6_url())
    context = {
        "instance": instance,
        "form": form,
        "b": b,
        "d": d,
        "h": h,
    }
    return render(request, 'egf/workorder.html', context)


def retailmaterialcost3(request, workorderid=None):
    instance = get_object_or_404(WorkOrder, workorderid=workorderid)
    form = WorkOrderA(request.POST or None, instance=instance)
    d = request.POST['id_retailmaterialcost3']
    WorkOrder.objects.filter(workorderid=workorderid).update(retailmaterialcost3=d)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute6_url())
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'egf/workorder.html', context)


def retailmaterialcost32(request, workorderid=None):
    instance = get_object_or_404(WorkOrder, workorderid=workorderid)
    form = WorkOrderA(request.POST or None, instance=instance)
    b = WorkOrder.objects.values_list('retailmaterialcost3', flat=True).last()
    d = WorkOrder.objects.values_list('description3', flat=True).last()
    g = WorkOrder.objects.values_list('workorder', flat=True).last()
    h = WorkOrderForm.objects.filter(workorder=g, ident=14).update(retail=b)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute6_url())
    context = {
        "instance": instance,
        "form": form,
        "b": b,
        "d": d,
        "h": h,
    }
    return render(request, 'egf/workorder.html', context)


def description4(request, workorderid=None):
    instance = get_object_or_404(WorkOrder, workorderid=workorderid)
    form = WorkOrderA(request.POST or None, instance=instance)
    d = request.POST['id_description4']
    WorkOrder.objects.filter(workorderid=workorderid).update(description4=d)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute6_url())
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'egf/workorder.html', context)


def description42(request, workorderid=None):
    instance = get_object_or_404(WorkOrder, workorderid=workorderid)
    form = WorkOrderA(request.POST or None, instance=instance)
    b = WorkOrder.objects.values_list('workorder', flat=True).last()
    d = WorkOrder.objects.values_list('gunid', flat=True).last()
    s = WorkOrder.objects.values_list('workorderdate', flat=True).last()
    j = WorkOrder.objects.values_list('custid', flat=True).last()
    n = WorkOrder.objects.values_list('description4', flat=True).last()
    o = WorkOrder.objects.values_list('labor4', flat=True).last()
    p = WorkOrder.objects.values_list('retailmaterialcost4', flat=True).last()
    z = 15
    e = WorkOrderForm.objects.create(workorder=b, ident=z)

    h = WorkOrderForm.objects.filter(workorder=b, ident=z).update(gunid=d, custid=j, workorderdate=s, description=n, labor=o, retail=p)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute6_url())
    context = {
        "instance": instance,
        "form": form,
        "e": e,
        "h": h
    }
    return render(request, 'egf/workorder.html', context)


def delete_description4(request, workorderid=None):
    instance = get_object_or_404(WorkOrder, workorderid=workorderid)
    form = WorkOrderA(request.POST or None, instance=instance)
    a = WorkOrderForm.objects.all()
    a.filter(ident=15).delete()
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute6_url())
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'egf/workorder.html', context)


def labor4(request, workorderid=None):
    instance = get_object_or_404(WorkOrder, workorderid=workorderid)
    form = WorkOrderA(request.POST or None, instance=instance)
    d = request.POST['id_labor4']
    WorkOrder.objects.filter(workorderid=workorderid).update(labor4=d)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute6_url())
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'egf/workorder.html', context)


def labor42(request, workorderid=None):
    instance = get_object_or_404(WorkOrder, workorderid=workorderid)
    form = WorkOrderA(request.POST or None, instance=instance)
    b = WorkOrder.objects.values_list('labor4', flat=True).last()
    d = WorkOrder.objects.values_list('description4', flat=True).last()
    g = WorkOrder.objects.values_list('workorder', flat=True).last()
    h = WorkOrderForm.objects.filter(workorder=g, ident=15).update(labor=b)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute6_url())
    context = {
        "instance": instance,
        "form": form,
        "b": b,
        "d": d,
        "h": h,
    }
    return render(request, 'egf/workorder.html', context)


def retailmaterialcost4(request, workorderid=None):
    instance = get_object_or_404(WorkOrder, workorderid=workorderid)
    form = WorkOrderA(request.POST or None, instance=instance)
    d = request.POST['id_retailmaterialcost4']
    WorkOrder.objects.filter(workorderid=workorderid).update(retailmaterialcost4=d)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute6_url())
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'egf/workorder.html', context)


def retailmaterialcost42(request, workorderid=None):
    instance = get_object_or_404(WorkOrder, workorderid=workorderid)
    form = WorkOrderA(request.POST or None, instance=instance)
    b = WorkOrder.objects.values_list('retailmaterialcost4', flat=True).last()
    d = WorkOrder.objects.values_list('description4', flat=True).last()
    g = WorkOrder.objects.values_list('workorder', flat=True).last()
    h = WorkOrderForm.objects.filter(workorder=g, ident=15).update(retail=b)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute6_url())
    context = {
        "instance": instance,
        "form": form,
        "b": b,
        "d": d,
        "h": h,
    }
    return render(request, 'egf/workorder.html', context)


def description5(request, workorderid=None):
    instance = get_object_or_404(WorkOrder, workorderid=workorderid)
    form = WorkOrderA(request.POST or None, instance=instance)
    d = request.POST['id_description5']
    WorkOrder.objects.filter(workorderid=workorderid).update(description5=d)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute6_url())
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'egf/workorder.html', context)


def description52(request, workorderid=None):
    instance = get_object_or_404(WorkOrder, workorderid=workorderid)
    form = WorkOrderA(request.POST or None, instance=instance)
    b = WorkOrder.objects.values_list('workorder', flat=True).last()
    d = WorkOrder.objects.values_list('gunid', flat=True).last()
    s = WorkOrder.objects.values_list('workorderdate', flat=True).last()
    j = WorkOrder.objects.values_list('custid', flat=True).last()
    n = WorkOrder.objects.values_list('description5', flat=True).last()
    o = WorkOrder.objects.values_list('labor5', flat=True).last()
    p = WorkOrder.objects.values_list('retailmaterialcost5', flat=True).last()
    z = 16
    e = WorkOrderForm.objects.create(workorder=b, ident=z)

    h = WorkOrderForm.objects.filter(workorder=b, ident=z).update(gunid=d, custid=j, workorderdate=s, description=n, labor=o, retail=p)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute6_url())
    context = {
        "instance": instance,
        "form": form,
        "e": e,
        "h": h
    }
    return render(request, 'egf/workorder.html', context)


def delete_description5(request, workorderid=None):
    instance = get_object_or_404(WorkOrder, workorderid=workorderid)
    form = WorkOrderA(request.POST or None, instance=instance)
    a = WorkOrderForm.objects.all()
    a.filter(ident=16).delete()
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute6_url())
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'egf/workorder.html', context)


def labor5(request, workorderid=None):
    instance = get_object_or_404(WorkOrder, workorderid=workorderid)
    form = WorkOrderA(request.POST or None, instance=instance)
    d = request.POST['id_labor5']
    WorkOrder.objects.filter(workorderid=workorderid).update(labor5=d)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute6_url())
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'egf/workorder.html', context)


def labor52(request, workorderid=None):
    instance = get_object_or_404(WorkOrder, workorderid=workorderid)
    form = WorkOrderA(request.POST or None, instance=instance)
    b = WorkOrder.objects.values_list('labor5', flat=True).last()
    d = WorkOrder.objects.values_list('description5', flat=True).last()
    g = WorkOrder.objects.values_list('workorder', flat=True).last()
    h = WorkOrderForm.objects.filter(workorder=g, ident=16).update(labor=b)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute6_url())
    context = {
        "instance": instance,
        "form": form,
        "b": b,
        "d": d,
        "h": h,
    }
    return render(request, 'egf/workorder.html', context)


def retailmaterialcost5(request, workorderid=None):
    instance = get_object_or_404(WorkOrder, workorderid=workorderid)
    form = WorkOrderA(request.POST or None, instance=instance)
    d = request.POST['id_retailmaterialcost5']
    WorkOrder.objects.filter(workorderid=workorderid).update(retailmaterialcost5=d)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute6_url())
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'egf/workorder.html', context)


def retailmaterialcost52(request, workorderid=None):
    instance = get_object_or_404(WorkOrder, workorderid=workorderid)
    form = WorkOrderA(request.POST or None, instance=instance)
    b = WorkOrder.objects.values_list('retailmaterialcost5', flat=True).last()
    d = WorkOrder.objects.values_list('description5', flat=True).last()
    g = WorkOrder.objects.values_list('workorder', flat=True).last()
    h = WorkOrderForm.objects.filter(workorder=g, ident=16).update(retail=b)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute6_url())
    context = {
        "instance": instance,
        "form": form,
        "b": b,
        "d": d,
        "h": h,
    }
    return render(request, 'egf/workorder.html', context)


def notes(request, workorderid=None):
    instance = get_object_or_404(WorkOrder, workorderid=workorderid)
    form = WorkOrderA(request.POST or None, instance=instance)
    d = request.POST['id_notes']
    WorkOrder.objects.filter(workorderid=workorderid).update(notes=d)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute6_url())
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'egf/workorder.html', context)


def proposaltype(request, workorderid=None):
    instance = get_object_or_404(WorkOrder, workorderid=workorderid)
    form = WorkOrderA(request.POST or None, instance=instance)
    d = request.POST['id_proposaltype']
    WorkOrder.objects.filter(workorderid=workorderid).update(proposaltype_id=d)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute6_url())
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'egf/workorder.html', context)


def shipping(request, workorderid=None):
    instance = get_object_or_404(WorkOrder, workorderid=workorderid)
    form = WorkOrderA(request.POST or None, instance=instance)
    d = request.POST['id_shipping']
    e = WorkOrder.objects.values_list('totaljobcost', flat=True).last()

    f = WorkOrder.objects.filter(workorderid=workorderid).update(shipping=d)
    g = WorkOrder.objects.values_list('shipping', flat=True).last()
    h = e + g
    i = WorkOrder.objects.filter(workorderid=workorderid).update(jobcostshipping=h, balance=h)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute26_url())
    context = {
        "instance": instance,
        "form": form,
        "h": h,
        "f": f,
        "i": i,
    }
    return render(request, 'egf/proposal.html', context)


def jobcostshipping(request, workorderid=None):
    instance = get_object_or_404(WorkOrder, workorderid=workorderid)
    form = WorkOrderA(request.POST or None, instance=instance)
    d = request.POST['id_jobcostshipping']
    WorkOrder.objects.filter(workorderid=workorderid).update(jobcostshipping=d)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute26_url())
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'egf/proposal.html', context)


def load_jobcostshipping(request, workorderid=None):
    a = WorkOrder.objects.all()
    instance = get_object_or_404(WorkOrder, workorderid=workorderid)
    form = WorkOrderA(request.POST or None, instance=instance)
    jobcostshipping = a.values('jobcostshipping').get(workorderid=workorderid)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute6_url())
    context = {
        "instance": instance,
        'jobcostshipping': jobcostshipping,
        "form": form,
    }
    return render(request, 'egf/jobcostshipping_a.html', context)


def downpay(request, workorderid=None):
    instance = get_object_or_404(WorkOrder, workorderid=workorderid)
    form = WorkOrderA(request.POST or None, instance=instance)
    d = request.POST['id_downpay']
    WorkOrder.objects.filter(workorderid=workorderid).update(downpay=d)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute26_url())
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'egf/proposal.html', context)


def balance(request, workorderid=None):
    instance = get_object_or_404(WorkOrder, workorderid=workorderid)
    form = WorkOrderA(request.POST or None, instance=instance)
    e = WorkOrder.objects.values_list('jobcostshipping', flat=True).last()
    g = WorkOrder.objects.values_list('downpay', flat=True).last()
    h = e - g
    i = WorkOrder.objects.filter(workorderid=workorderid).update(balance=h)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute26_url())
    context = {
        "instance": instance,
        "form": form,
        "i": i,
    }
    return render(request, 'egf/proposal.html', context)


def load_balance(request, workorderid=None):
    a = WorkOrder.objects.all()
    instance = get_object_or_404(WorkOrder, workorderid=workorderid)
    form = WorkOrderA(request.POST or None, instance=instance)
    balance1 = a.values('balance').get(workorderid=workorderid)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute6_url())
    context = {
        "instance": instance,
        'balance1': balance1,
        "form": form,
    }
    return render(request, 'egf/balance_a.html', context)


def checknum1(request, workorderid=None):
    instance = get_object_or_404(WorkOrder, workorderid=workorderid)
    form = WorkOrderA(request.POST or None, instance=instance)
    d = request.POST['id_checknum1']
    WorkOrder.objects.filter(workorderid=workorderid).update(checknum1=d)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute6_url())
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'egf/proposal.html', context)


def checknum2(request, workorderid=None):
    instance = get_object_or_404(WorkOrder, workorderid=workorderid)
    form = WorkOrderA(request.POST or None, instance=instance)
    d = request.POST['id_checknum2']
    WorkOrder.objects.filter(workorderid=workorderid).update(checknum2=d)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute6_url())
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'egf/proposal.html', context)


def downdate(request, workorderid=None):
    instance = get_object_or_404(WorkOrder, workorderid=workorderid)
    form = WorkOrderA(request.POST or None, instance=instance)
    d = request.POST['id_downpaydate']
    WorkOrder.objects.filter(workorderid=workorderid).update(downpaydate=d)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute6_url())
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'egf/proposal.html', context)


def finaldate(request, workorderid=None):
    instance = get_object_or_404(WorkOrder, workorderid=workorderid)
    form = WorkOrderA(request.POST or None, instance=instance)
    d = request.POST['id_finalpaydate']
    WorkOrder.objects.filter(workorderid=workorderid).update(finalpaydate=d)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute6_url())
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'egf/proposal.html', context)


def finalpay(request, workorderid=None):
    instance = get_object_or_404(WorkOrder, workorderid=workorderid)
    form = WorkOrderA(request.POST or None, instance=instance)
    d = request.POST['id_finalpay']
    WorkOrder.objects.filter(workorderid=workorderid).update(finalpay=d)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute6_url())
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'egf/proposal.html', context)

def proposal(request, workorderid=None):
    instance = WorkOrder.objects.filter(workorderid=workorderid).last()
    form = WorkOrderC(request.POST or None, instance=instance)
    a = WorkOrder.objects.all()
    b = WorkOrder.objects.values_list('custid', flat=True).last()
    n = WorkOrder.objects.values_list('workorder', flat=True).last()
    c = CustomerInfo.objects.all()
    custmodeldisplay = c.filter(id=b)
    d = WorkOrder.objects.values_list('gunid', flat=True).last()
    e = GunInfo.objects.all()
    gunmodeldisplay = e.filter(gunid=d)
    m = WorkOrderForm.objects.all()
    f = m.values_list('workorder', flat=True).distinct().filter(workorder=workorderid)
    g = (f[0])
    materialmodeldisplay = m.filter(workorder=g)
    f = m.values_list('workorder', flat=True).distinct().filter(workorder=workorderid)
    h = JobCost.objects.all()
    j = JobCost.objects.create(workorder=f)
    labor = m.values_list('labor', flat=True).filter(workorder=n).aggregate(sum_labor=Sum('labor'))
    laborcost = labor['sum_labor']
    k = WorkOrder.objects.filter(workorderid=workorderid).update(labor=laborcost)
    material = m.values_list('retail', flat=True).filter(workorder=n).aggregate(sum_retail=Sum('retail'))
    matcost = material['sum_retail']
    l = WorkOrder.objects.filter(workorderid=workorderid).update(mat=matcost)
    taxrate = TaxRate.objects.values_list('rate', flat=True).last()
    saletax = matcost*taxrate
    o = WorkOrder.objects.filter(workorderid=workorderid).update(saletax=saletax)
    totalmat = matcost+saletax
    totaljobcost = totalmat + laborcost
    shipping = 0
    jobcostshipping= totaljobcost + shipping
    downpay = 0
    balance = jobcostshipping
    p = WorkOrder.objects.filter(workorderid=workorderid).update(totalmat=totalmat)
    q = WorkOrder.objects.filter(workorderid=workorderid).update(totaljobcost=totaljobcost)
    r = WorkOrder.objects.filter(workorderid=workorderid).update(jobcostshipping=jobcostshipping)
    s = WorkOrder.objects.filter(workorderid=workorderid).update(balance=jobcostshipping)

    if form.is_valid():
        form.save()
        instance = WorkOrder.objects.order_by('workorderid').last()
        context2 = {
            "instance": instance,
        }
        return redirect(instance.get_absolute26_url(), context2)
    context = {
        "instance": instance,
        "form": form,
        "CustomerInfo": custmodeldisplay,
        "GunInfo": gunmodeldisplay,
        "WorkOrderForm": materialmodeldisplay,
        "a": a,
        "h": h,
        "j": j,
        "k": k,
        "l": l,
        "o": o,
        "p": p,
        "q": q,
#        "s": s,
        "saletax": saletax,
        "totalmat": totalmat,
        "totaljobcost": totaljobcost,
        "labor": labor,
        "material": material,
        "jobcostshipping": jobcostshipping,
        "downpay": downpay,
        "shipping": shipping,
        "balance": balance,
    }
    return render(request, 'egf/proposal.html', context)


def proposal_back(request, gunid=None):
    instance = WorkOrder.objects.get(gunid=gunid)
    form = Proposal(request.POST or None, instance=instance)
    if form.is_valid():
        context2 = {
        }
        return redirect(context2)
    context = {
        "instance": instance,
        "form": form,
    }
    return redirect(instance.get_absolute19_url(), context)


def delete_workorder(request, workorderid):
    instance = get_object_or_404(WorkOrder, workorder=workorderid)
    a = WorkOrderForm.objects.all()
    b = WorkOrder.objects.values_list('workorder', flat=True).last()
    if request.method == "POST":
        a.filter(workorder=b).delete()
        instance.delete()
        return redirect(instance.get_absolute17_url())
    context = {
        "object": instance,
    }
    return render(request, "egf/delete-workorder.html", context)


def matnew(request):
    if request.method == 'POST':
        form = MaterialA(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/egf/materialnew')
        else:
            form = MaterialA()
            return render(request, 'egf/materialnew.html', {'form': form})
    else:
        form = MaterialA()
        return render(request, 'egf/materialnew.html', {'form': form})


def mat_info_existing(request):
    queryset = Materials.objects.all()
    search_term = ''
    if 'search' in request.GET:
        search_term = request.GET['search']
        queryset = queryset.filter(Q(id__icontains=search_term)
                                   | Q(description__icontains=search_term))

    paginator = Paginator(queryset, 13)  # Show 6 contacts per page
    page = request.GET.get('page')
    queryset = paginator.get_page(page)
    context = {"object_list": queryset, "search_term": search_term}
    return render(request, 'egf/mat_info_existing.html', context)


def mat_detail(request, id):
    instance = Materials.objects.get(id=id)
    form = MaterialA(request.POST or None, instance=instance)
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'egf/mat_detail.html', context)


def edit_mat_info(request, id=None):
    instance = Materials.objects.get(id=id)
    form = MaterialA(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return redirect(instance.get_absolute9_url())

    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'egf/edit_mat_info.html', context)


def downpay(request, workorderid=None):
    instance = get_object_or_404(WorkOrder, workorderid=workorderid)
    form = WorkOrderA(request.POST or None, instance=instance)
    d = request.POST['id_downpay']
    WorkOrder.objects.filter(workorderid=workorderid).update(downpay=d)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute26_url())
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'egf/proposal.html', context)


def balance(request, workorderid=None):
    instance = get_object_or_404(WorkOrder, workorderid=workorderid)
    form = WorkOrderA(request.POST or None, instance=instance)
    e = WorkOrder.objects.values_list('jobcostshipping', flat=True).last()
    g = WorkOrder.objects.values_list('downpay', flat=True).last()
    h = e - g
    i = WorkOrder.objects.filter(workorderid=workorderid).update(balance=h)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute26_url())
    context = {
        "instance": instance,
        "form": form,
        "i": i,
    }
    return render(request, 'egf/proposal.html', context)


def load_balance(request, workorderid=None):
    a = WorkOrder.objects.all()
    instance = get_object_or_404(WorkOrder, workorderid=workorderid)
    form = WorkOrderA(request.POST or None, instance=instance)
    balance1 = a.values('balance').get(workorderid=workorderid)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute6_url())
    context = {
        "instance": instance,
        'balance1': balance1,
        "form": form,
    }
    return render(request, 'egf/balance_a.html', context)


def checknum1(request, workorderid=None):
    instance = get_object_or_404(WorkOrder, workorderid=workorderid)
    form = WorkOrderA(request.POST or None, instance=instance)
    d = request.POST['id_checknum1']
    WorkOrder.objects.filter(workorderid=workorderid).update(checknum1=d)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute6_url())
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'egf/proposal.html', context)


def checknum2(request, workorderid=None):
    instance = get_object_or_404(WorkOrder, workorderid=workorderid)
    form = WorkOrderA(request.POST or None, instance=instance)
    d = request.POST['id_checknum2']
    WorkOrder.objects.filter(workorderid=workorderid).update(checknum2=d)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute6_url())
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'egf/proposal.html', context)


def downdate(request, workorderid=None):
    instance = get_object_or_404(WorkOrder, workorderid=workorderid)
    form = WorkOrderA(request.POST or None, instance=instance)
    d = request.POST['id_downpaydate']
    WorkOrder.objects.filter(workorderid=workorderid).update(downpaydate=d)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute6_url())
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'egf/proposal.html', context)


def finaldate(request, workorderid=None):
    instance = get_object_or_404(WorkOrder, workorderid=workorderid)
    form = WorkOrderA(request.POST or None, instance=instance)
    d = request.POST['id_finalpaydate']
    WorkOrder.objects.filter(workorderid=workorderid).update(finalpaydate=d)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute6_url())
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'egf/proposal.html', context)


def finalpay(request, workorderid=None):
    instance = get_object_or_404(WorkOrder, workorderid=workorderid)
    form = WorkOrderA(request.POST or None, instance=instance)
    d = request.POST['id_finalpay']
    WorkOrder.objects.filter(workorderid=workorderid).update(finalpay=d)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute6_url())
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'egf/proposal.html', context)


def previouswo(request, gunid=None):
    queryset = WorkOrder.objects.filter(gunid=gunid)
    form = WorkOrderA(request.POST or None)
    if form.is_valid():
        context2 = {
        }
        return redirect(context2)
    context = {
        "object_list": queryset,
        "form": form,
    }
    return render(request, 'egf/previouswo.html', context)


def proposalprev(request, workorderid=None):
    instance = WorkOrder.objects.get(workorderid=workorderid)
    form = Proposal(request.POST or None, instance=instance)
    a = WorkOrder.objects.all()
    b = a.values_list('custid', flat=True).get(workorderid=workorderid)
    c = CustomerInfo.objects.all()
    custmodeldisplay = c.filter(id=b)
    d = a.values_list('gunid', flat=True).get(workorderid=workorderid)
    e = GunInfo.objects.all()
    gunmodeldisplay = e.filter(gunid=d)
    m = WorkOrderForm.objects.all()
    f = m.values_list('workorder', flat=True).distinct().filter(workorder=workorderid)
    g = (f[0])
    materialmodeldisplay = m.filter(workorder=g)
    labor = m.values_list('labor', flat=True).distinct().filter(workorder=workorderid)
    mat = a.values_list('mat', flat=True).distinct().filter(workorder=workorderid)
    if form.is_valid():
        form.save()
        context2 = {
            "instance": instance,

        }
        return redirect(instance.get_absolute26_url(), context2)
    context = {
        "instance": instance,
        "form": form,
        "CustomerInfo": custmodeldisplay,
        "GunInfo": gunmodeldisplay,
        "WorkOrderForm": materialmodeldisplay,
        "a": a,
        "labor": labor,
        "mat": mat,

    }
    return render(request, 'egf/proposalprev.html', context)


class ViewPDF(View):
    def get(self, request, *args, **kwargs):
        pdf = render_to_pdf('egf/proposalpdf.html', data)
        return HttpResponse(pdf, content_type='application/pdf')


def proposalpdf(request, workorderid=None):
    instance = WorkOrder.objects.get(workorderid=workorderid)
    form = Proposal(request.POST or None, instance=instance)
    a = WorkOrder.objects.all()
    b = a.values_list('custid', flat=True).get(workorderid=workorderid)
    c = CustomerInfo.objects.all()
    custmodeldisplay = c.filter(id=b)
    d = a.values_list('gunid', flat=True).get(workorderid=workorderid)
    e = GunInfo.objects.all()
    gunmodeldisplay = e.filter(gunid=d)
    m = WorkOrderForm.objects.all()
    f = m.values_list('workorder', flat=True).distinct().filter(workorder=workorderid)
    g = (f[0])
    materialmodeldisplay = m.filter(workorder=g)
    labor = m.values_list('labor', flat=True).distinct().filter(workorder=workorderid)
    mat = a.values_list('mat', flat=True).distinct().filter(workorder=workorderid)
    n = WorkOrder.objects.all()
    jobmodeldisplay = n.filter(workorder=g)

    p = n.values_list('workorder', flat=True).distinct().filter(workorder=workorderid)
    if form.is_valid():
        form.save()
        context2 = {
        }

        return redirect(instance.get_absolute26_url(), context2)
    context = {
        "instance": instance,
        "form": form,
        "CustomerInfo": custmodeldisplay,
        "GunInfo": gunmodeldisplay,
        "WorkOrderForm": materialmodeldisplay,
        "a": a,
        "labor": labor,
        "mat": mat,
        "WorkOrder": jobmodeldisplay,
        "p": p
        #"config": config,
    }
    return render(request, 'egf/proposalpdf.html', context)


def generate_view(request, workorderid=None):
    instance = WorkOrder.objects.get(workorderid=workorderid)
    form = Proposal(request.POST or None, instance=instance)
    a = WorkOrder.objects.all()
    b = a.values_list('workorder', flat=True).get(workorderid=workorderid)
    h = a.values_list('custid', flat=True).get(workorderid=workorderid)
    c = CustomerInfo.objects.all()
    custmodeldisplay = c.filter(id=h)
    d = a.values_list('gunid', flat=True).get(workorderid=workorderid)
    e = GunInfo.objects.all()
    gunmodeldisplay = e.filter(gunid=d)

    f = a.values_list('workorder', flat=True).distinct().filter(workorder=workorderid)
    g = (f[0])
    k = WorkOrderForm.objects.all()
    l = WorkOrderlabor.objects.all()
    materialmodeldisplay = k.filter(workorder=g)
    description = k.values_list('description', flat=True).distinct().filter(workorder=workorderid)
    labor = l.values_list('labor', flat=True).distinct().filter(workorder=workorderid)
    mat = a.values_list('mat', flat=True).distinct().filter(workorder=workorderid)
    n = WorkOrder.objects.all()
    jobmodeldisplay = n.filter(workorder=g)

    p = n.values_list('workorder', flat=True).distinct().filter(workorder=workorderid)
    if form.is_valid():
        form.save()
        context2 = {
        }

        return redirect(instance.get_absolute26_url(), context2)
    context = {
        "instance": instance,
        "form": form,
        "CustomerInfo": custmodeldisplay,
        "GunInfo": gunmodeldisplay,
        "WorkOrderForm": materialmodeldisplay,
        "a": a,
        "b": b,
        "labor": labor,
        "mat": mat,
        "description": description,
        "WorkOrder": jobmodeldisplay,
        "p": p
    }
    pdf = render_to_pdf('egf/proposalpdf.html', context)
    return HttpResponse(pdf, content_type='application/pdf')


class DownloadPDF(View):
    def get(self, request, *args, workorderid=None):
        instance = WorkOrder.objects.get(workorderid=workorderid)
        form = Proposal(request.POST or None, instance=instance)
        a = WorkOrder.objects.all()
        b = a.values_list('workorder', flat=True).get(workorderid=workorderid)
        h = a.values_list('custid', flat=True).get(workorderid=workorderid)
        c = CustomerInfo.objects.all()
        custmodeldisplay = c.filter(id=h)
        d = a.values_list('gunid', flat=True).get(workorderid=workorderid)
        e = GunInfo.objects.all()
        gunmodeldisplay = e.filter(gunid=d)
        f = a.values_list('workorder', flat=True).distinct().filter(workorder=workorderid)
        g = (f[0])
        k = WorkOrderForm.objects.all()
        l = WorkOrderlabor.objects.all()
        materialmodeldisplay = k.filter(workorder=g)
        description = k.values_list('description', flat=True).distinct().filter(workorder=workorderid)
        labor = l.values_list('labor', flat=True).distinct().filter(workorder=workorderid)
        mat = a.values_list('mat', flat=True).distinct().filter(workorder=workorderid)
        n = WorkOrder.objects.all()
        jobmodeldisplay = n.filter(workorder=g)
        p = n.values_list('workorder', flat=True).distinct().filter(workorder=workorderid)
        if form.is_valid():
            form.save()
            context2 = {
            }
            return redirect(instance.get_absolute26_url(), context2)
        context = {
            "instance": instance,
            "form": form,
            "CustomerInfo": custmodeldisplay,
            "GunInfo": gunmodeldisplay,
            "WorkOrderForm": materialmodeldisplay,
            "a": a,
            "b": b,
            "labor": labor,
            "mat": mat,
            "description": description,
            "WorkOrder": jobmodeldisplay,
            "p": p
        }
        pdf = render_to_pdf('egf/pdf_template.html', context)
        response = HttpResponse(pdf, content_type='application/pdf')
        filename = "Proposal_%s.pdf" % g
        content = "attachment; filename='%s'" % (filename)
        response['Content-Disposition'] = content
        return response


def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None


data = {
    "custfirstname": "Elite Gun Fitting",
    "custadd1": "28435 Silver Palm Dr.",
    "custcity": "Punta Gorda",
    "custst": "FL",


    "custcell1": "815-955-2074",
    "custemail1": "albraner@gmail.com",
}


# Opens up page as PDF
class ViewPDF2(View):
    def get(self, request, *args, **kwargs):
        pdf = render_to_pdf('ecg/evaluepdf.html', data)
        return HttpResponse(pdf, content_type='application/pdf')




def evalue(request, gunid=None):
    instance = Evaluation.objects.get(gunid=gunid)
    form = Evalue(request.POST or None, instance=instance)
    a = GunInfo.objects.all()
    g = a.values_list('id', flat=True).get(gunid=gunid)
    h = CustomerInfo.objects.all()
    custmodeldisplay = h.filter(id=g)
    j = a.values_list('gunid', flat=True).get(gunid=gunid)
    k = GunInfo.objects.all()
    gunmodeldisplay = k.filter(gunid=j)
    m = GunInfo.objects.values_list('gunid', flat=True).get(gunid=gunid)
    n = Evaluation.objects.all()
    evaluemodeldisplay = n.filter(gunid=m)
    if form.is_valid():
        form.save()
        instance = Evaluation.objects.order_by('gunid').last()
        context2 = {
            "instance": instance,
        }
        return redirect(instance.get_absolute27_url(), context2)
    context = {
        "instance": instance,
        "form": form,
        "CustomerInfo": custmodeldisplay,
        "GunInfo": gunmodeldisplay,
        "Evaluation": evaluemodeldisplay,
    }
    return render(request, 'egf/evalue.html', context)





def workorderdate(request, evalueid=None):
    instance = get_object_or_404(Evaluation, evalueid=evalueid)
    form = Evalue(request.POST or None, instance=instance)
    d = request.POST['id_workorderdate']
    Evaluation.objects.filter(evalueid=evalueid).update(workorderdate=d)
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'egf/evalue.html', context)


def eyedom(request, evalueid=None):
    instance = get_object_or_404(Evaluation, evalueid=evalueid)
    form = Evalue(request.POST or None, instance=instance)
    d = request.POST['id_eyedominace']
    Evaluation.objects.filter(evalueid=evalueid).update(eyedominace_id=d)
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'egf/evalue.html', context)


def exhand(request, evalueid=None):
    instance = get_object_or_404(Evaluation, evalueid=evalueid)
    form = Evalue(request.POST or None, instance=instance)
    d = request.POST['id_exhand']
    Evaluation.objects.filter(evalueid=evalueid).update(exhand_id=d)
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'egf/evalue.html', context)


def exlop(request, evalueid=None):
    instance = get_object_or_404(Evaluation, evalueid=evalueid)
    form = Evalue(request.POST or None, instance=instance)
    d = request.POST['id_exlop']
    Evaluation.objects.filter(evalueid=evalueid).update(exlop_id=d)
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'egf/evalue.html', context)


def exdac(request, evalueid=None):
    instance = get_object_or_404(Evaluation, evalueid=evalueid)
    form = Evalue(request.POST or None, instance=instance)
    d = request.POST['id_exdac']
    Evaluation.objects.filter(evalueid=evalueid).update(exdac_id=d)
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'egf/evalue.html', context)


def exdaf(request, evalueid=None):
    instance = get_object_or_404(Evaluation, evalueid=evalueid)
    form = Evalue(request.POST or None, instance=instance)
    d = request.POST['id_exdaf']
    Evaluation.objects.filter(evalueid=evalueid).update(exdaf_id=d)
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'egf/evalue.html', context)


def exdah(request, evalueid=None):
    instance = get_object_or_404(Evaluation, evalueid=evalueid)
    form = Evalue(request.POST or None, instance=instance)
    d = request.POST['id_exdah']
    Evaluation.objects.filter(evalueid=evalueid).update(exdah_id=d)
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'egf/evalue.html', context)


def exdamc(request, evalueid=None):
    instance = get_object_or_404(Evaluation, evalueid=evalueid)
    form = Evalue(request.POST or None, instance=instance)
    d = request.POST['id_exdamc']
    Evaluation.objects.filter(evalueid=evalueid).update(exdamc_id=d)
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'egf/evalue.html', context)


def excast(request, evalueid=None):
    instance = get_object_or_404(Evaluation, evalueid=evalueid)
    form = Evalue(request.POST or None, instance=instance)
    d = request.POST['id_excast']
    Evaluation.objects.filter(evalueid=evalueid).update(excast_id=d)
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'egf/evalue.html', context)


def exlotp(request, evalueid=None):
    instance = get_object_or_404(Evaluation, evalueid=evalueid)
    form = Evalue(request.POST or None, instance=instance)
    d = request.POST['id_exlotp']
    Evaluation.objects.filter(evalueid=evalueid).update(exlotp_id=d)
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'egf/evalue.html', context)


def extoeout(request, evalueid=None):
    instance = get_object_or_404(Evaluation, evalueid=evalueid)
    form = Evalue(request.POST or None, instance=instance)
    d = request.POST['id_extoeout']
    Evaluation.objects.filter(evalueid=evalueid).update(extoeout_id=d)
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'egf/evalue.html', context)


def expitch(request, evalueid=None):
    instance = get_object_or_404(Evaluation, evalueid=evalueid)
    form = Evalue(request.POST or None, instance=instance)
    d = request.POST['id_expitch']
    Evaluation.objects.filter(evalueid=evalueid).update(expitch=d)
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'egf/evalue.html', context)


def newhand(request, evalueid=None):
    instance = get_object_or_404(Evaluation, evalueid=evalueid)
    form = Evalue(request.POST or None, instance=instance)
    d = request.POST['id_newhand']
    Evaluation.objects.filter(evalueid=evalueid).update(newhand_id=d)
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'egf/evalue.html', context)


def newlop(request, evalueid=None):
    instance = get_object_or_404(Evaluation, evalueid=evalueid)
    form = Evalue(request.POST or None, instance=instance)
    d = request.POST['id_newlop']
    Evaluation.objects.filter(evalueid=evalueid).update(newlop_id=d)
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'egf/evalue.html', context)


def newdac(request, evalueid=None):
    instance = get_object_or_404(Evaluation, evalueid=evalueid)
    form = Evalue(request.POST or None, instance=instance)
    d = request.POST['id_newdac']
    Evaluation.objects.filter(evalueid=evalueid).update(newdac_id=d)
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'egf/evalue.html', context)


def newdaf(request, evalueid=None):
    instance = get_object_or_404(Evaluation, evalueid=evalueid)
    form = Evalue(request.POST or None, instance=instance)
    d = request.POST['id_newdaf']
    Evaluation.objects.filter(evalueid=evalueid).update(newdaf_id=d)
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'egf/evalue.html', context)


def newdah(request, evalueid=None):
    instance = get_object_or_404(Evaluation, evalueid=evalueid)
    form = Evalue(request.POST or None, instance=instance)
    d = request.POST['id_newdah']
    Evaluation.objects.filter(evalueid=evalueid).update(newdah_id=d)
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'egf/evalue.html', context)


def newdamc(request, evalueid=None):
    instance = get_object_or_404(Evaluation, evalueid=evalueid)
    form = Evalue(request.POST or None, instance=instance)
    d = request.POST['id_newdamc']
    Evaluation.objects.filter(evalueid=evalueid).update(newdamc_id=d)
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'egf/evalue.html', context)


def newcast(request, evalueid=None):
    instance = get_object_or_404(Evaluation, evalueid=evalueid)
    form = Evalue(request.POST or None, instance=instance)
    d = request.POST['id_newcast']
    Evaluation.objects.filter(evalueid=evalueid).update(newcast_id=d)
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'egf/evalue.html', context)


def newlotp(request, evalueid=None):
    instance = get_object_or_404(Evaluation, evalueid=evalueid)
    form = Evalue(request.POST or None, instance=instance)
    d = request.POST['id_newlotp']
    Evaluation.objects.filter(evalueid=evalueid).update(newlotp_id=d)
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'egf/evalue.html', context)


def newtoeout(request, evalueid=None):
    instance = get_object_or_404(Evaluation, evalueid=evalueid)
    form = Evalue(request.POST or None, instance=instance)
    d = request.POST['id_newtoeout']
    Evaluation.objects.filter(evalueid=evalueid).update(newtoeout=d)
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'egf/evalue.html', context)


def newpitch(request, evalueid=None):
    instance = get_object_or_404(Evaluation, evalueid=evalueid)
    form = Evalue(request.POST or None, instance=instance)
    d = request.POST['id_newpitch']
    Evaluation.objects.filter(evalueid=evalueid).update(newpitch=d)
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'egf/evalue.html', context)


def cor1(request, evalueid=None):
    instance = get_object_or_404(Evaluation, evalueid=evalueid)
    form = Evalue(request.POST or None, instance=instance)
    d = request.POST['id_cor1']
    Evaluation.objects.filter(evalueid=evalueid).update(cor1_id=d)
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'egf/evalue.html', context)


def cor2(request, evalueid=None):
    instance = get_object_or_404(Evaluation, evalueid=evalueid)
    form = Evalue(request.POST or None, instance=instance)
    d = request.POST['id_cor2']
    Evaluation.objects.filter(evalueid=evalueid).update(cor2_id=d)
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'egf/evalue.html', context)


def cor3(request, evalueid=None):
    instance = get_object_or_404(Evaluation, evalueid=evalueid)
    form = Evalue(request.POST or None, instance=instance)
    d = request.POST['id_cor3']
    Evaluation.objects.filter(evalueid=evalueid).update(cor3_id=d)
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'egf/evalue.html', context)


def cor4(request, evalueid=None):
    instance = get_object_or_404(Evaluation, evalueid=evalueid)
    form = Evalue(request.POST or None, instance=instance)
    d = request.POST['id_cor4']
    Evaluation.objects.filter(evalueid=evalueid).update(cor4_id=d)
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'egf/evalue.html', context)


def cor5(request, evalueid=None):
    instance = get_object_or_404(Evaluation, evalueid=evalueid)
    form = Evalue(request.POST or None, instance=instance)
    d = request.POST['id_cor5']
    Evaluation.objects.filter(evalueid=evalueid).update(cor5_id=d)
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'egf/evalue.html', context)


def cor6(request, evalueid=None):
    instance = get_object_or_404(Evaluation, evalueid=evalueid)
    form = Evalue(request.POST or None, instance=instance)
    d = request.POST['id_cor6']
    Evaluation.objects.filter(evalueid=evalueid).update(cor6_id=d)
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'egf/evalue.html', context)


def cor7(request, evalueid=None):
    instance = get_object_or_404(Evaluation, evalueid=evalueid)
    form = Evalue(request.POST or None, instance=instance)
    d = request.POST['id_cor7']
    Evaluation.objects.filter(evalueid=evalueid).update(cor7_id=d)
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'egf/evalue.html', context)


def cor8(request, evalueid=None):
    instance = get_object_or_404(Evaluation, evalueid=evalueid)
    form = Evalue(request.POST or None, instance=instance)
    d = request.POST['id_cor8']
    Evaluation.objects.filter(evalueid=evalueid).update(cor8_id=d)
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'egf/evalue.html', context)


def cor9(request, evalueid=None):
    instance = get_object_or_404(Evaluation, evalueid=evalueid)
    form = Evalue(request.POST or None, instance=instance)
    d = request.POST['id_cor9']
    Evaluation.objects.filter(evalueid=evalueid).update(cor9_id=d)
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'egf/evalue.html', context)


def cor10(request, evalueid=None):
    instance = get_object_or_404(Evaluation, evalueid=evalueid)
    form = Evalue(request.POST or None, instance=instance)
    d = request.POST['id_cor10']
    Evaluation.objects.filter(evalueid=evalueid).update(cor10_id=d)
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'egf/evalue.html', context)


def cor11(request, evalueid=None):
    instance = get_object_or_404(Evaluation, evalueid=evalueid)
    form = Evalue(request.POST or None, instance=instance)
    d = request.POST['id_cor11']
    Evaluation.objects.filter(evalueid=evalueid).update(cor11_id=d)
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'egf/evalue.html', context)


def evaluenotes(request, evalueid=None):
    instance = get_object_or_404(Evaluation, evalueid=evalueid)
    form = Evalue(request.POST or None, instance=instance)
    d = request.POST['id_notes']
    Evaluation.objects.filter(evalueid=evalueid).update(notes=d)
    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, 'egf/evalue.html', context)


def evalueprev(request, gunid=None):
    instance = Evaluation.objects.get(gunid=gunid)
    form = Evalueprev(request.POST or None, instance=instance)
    a = GunInfo.objects.all()
    g = a.values_list('id', flat=True).get(gunid=gunid)
    h = CustomerInfo.objects.all()
    custmodeldisplay = h.filter(id=g)
    j = a.values_list('gunid', flat=True).get(gunid=gunid)
    k = GunInfo.objects.all()
    gunmodeldisplay = k.filter(gunid=j)
    m = GunInfo.objects.values_list('gunid', flat=True).get(gunid=gunid)
    n = Evaluation.objects.all()
    evaluemodeldisplay = n.filter(gunid=m)
    if form.is_valid():
        form.save()
        instance = Evaluation.objects.order_by('gunid').last()
        context2 = {
            "instance": instance,
        }
        return redirect(instance.get_absolute28_url(), context2)
    context = {
        "instance": instance,
        "form": form,
        "CustomerInfo": custmodeldisplay,
        "GunInfo": gunmodeldisplay,
        "Evaluation": evaluemodeldisplay,
    }
    return render(request, 'egf/evalueprev.html', context)


def evaluepdf(request, gunid=None):
    instance = Evaluation.objects.get(gunid=gunid)
    form = Evalue(request.POST or None, instance=instance)
    a = GunInfo.objects.all()
    g = a.values_list('id', flat=True).get(gunid=gunid)
    h = CustomerInfo.objects.all()
    custmodeldisplay = h.filter(id=g)
    j = a.values_list('gunid', flat=True).get(gunid=gunid)
    k = GunInfo.objects.all()
    gunmodeldisplay = k.filter(gunid=j)
    m = GunInfo.objects.values_list('gunid', flat=True).get(gunid=gunid)
    n = Evaluation.objects.all()
    evaluemodeldisplay = n.filter(gunid=m)
    if form.is_valid():
        form.save()
        instance = Evaluation.objects.order_by('gunid').last()
        context2 = {
            "instance": instance,
        }
        return redirect(instance.get_absolute27_url(), context2)
    context = {
        "instance": instance,
        "form": form,
        "CustomerInfo": custmodeldisplay,
        "GunInfo": gunmodeldisplay,
        "Evaluation": evaluemodeldisplay,
    }
    return render(request, 'egf/evaluepdf.html', context)



def generate_view2(request, gunid=None):
    instance = Evaluation.objects.get(gunid=gunid)
    form = Evalueprev(request.POST or None, instance=instance)
    a = GunInfo.objects.all()
    g = a.values_list('id', flat=True).get(gunid=gunid)
    h = CustomerInfo.objects.all()
    custmodeldisplay = h.filter(id=g)
    j = a.values_list('gunid', flat=True).get(gunid=gunid)
    k = GunInfo.objects.all()
    gunmodeldisplay = k.filter(gunid=j)
    m = GunInfo.objects.values_list('gunid', flat=True).get(gunid=gunid)
    n = Evaluation.objects.all()
    evaluemodeldisplay = n.filter(gunid=m)
    if form.is_valid():
        form.save()
        instance = Evaluation.objects.order_by('gunid').last()
        context2 = {
            "instance": instance,
        }
        return redirect(instance.get_absolute28_url(), context2)
    context = {
        "instance": instance,
        "form": form,
        "CustomerInfo": custmodeldisplay,
        "GunInfo": gunmodeldisplay,
        "Evaluation": evaluemodeldisplay,
    }
    pdf = render_to_pdf('egf/evaluepdf.html', context)
    return HttpResponse(pdf, content_type='application/pdf')


class DownloadPDF2(View):
    def get(self, request, *args, gunid=None):
        instance = Evaluation.objects.get(gunid=gunid)
        form = Evalueprev(request.POST or None, instance=instance)
        a = GunInfo.objects.all()
        g = a.values_list('id', flat=True).get(gunid=gunid)
        h = CustomerInfo.objects.all()
        custmodeldisplay = h.filter(id=g)
        j = a.values_list('gunid', flat=True).get(gunid=gunid)
        k = GunInfo.objects.all()
        gunmodeldisplay = k.filter(gunid=j)
        m = GunInfo.objects.values_list('gunid', flat=True).get(gunid=gunid)
        n = Evaluation.objects.all()
        evaluemodeldisplay = n.filter(gunid=m)
        if form.is_valid():
            form.save()
            instance = Evaluation.objects.order_by('gunid').last()
            context2 = {
            "instance": instance,
            }
            return redirect(instance.get_absolute28_url(), context2)
        context = {
            "instance": instance,
            "form": form,
            "CustomerInfo": custmodeldisplay,
            "GunInfo": gunmodeldisplay,
            "Evaluation": evaluemodeldisplay,
            }
        pdf = render_to_pdf('egf/pdf_template2.html', context)
        response = HttpResponse(pdf, content_type='application/pdf')
        filename = "Evaluation_%s.pdf" % g
        content = "attachment; filename='%s'" % (filename)
        response['Content-Disposition'] = content
        return response
