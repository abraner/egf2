from django import forms
from .models import CustomerInfo, GunInfo, WorkOrder, RecoilPadInfo, Materials, Evaluation



class Custinfoa(forms.ModelForm):
    class Meta:
        model = CustomerInfo
        fields = [
            'id',
            'idA',
            'custcompanytname',
            'custfirstname',
            'custlastname',
            'custadd1',
            'custadd2',
            'custcity',
            'custst',
            'custzipcode',
            'custwork1',
            'custwork2',
            'custcell1',
            'custcell2',
            'custhome',
            'custemail1',
            'custemail2'
        ]


class CustinfoB(forms.ModelForm):
    class Meta:
        model = CustomerInfo
        fields = [
            'custcompanytname',
            'custfirstname',
            'custlastname',
            'custadd1',
            'custadd2',
            'custcity',
            'custst',
            'custzipcode',
            'custwork1',
            'custwork2',
            'custcell1',
            'custcell2',
            'custhome',
            'custemail1',
            'custemail2'
        ]


class GuninfoA(forms.ModelForm):
    class Meta:
        model = GunInfo
        fields = [
            'id',
            'gunid',
            'gunmanufacturer',
            'gunmodel',
            'gunserialnumber',
            'gungauge',
            'hand',
            'lop',
            'comb',
            'face',
            'heel',
            'montecarlo',
            'cast',
            'toe',
            'trigger',
            'pitch'
        ]
class WorkOrderA(forms.ModelForm):
    class Meta:
        model = WorkOrder
        fields = [
            'custid',
            'gunid',
            'workorderid',
            'workorder',
            'workorderdate',
            'duplicating',
            'fittingtime',
            'fittingstock',
            'refinishing',
            'finishtype',
            'recoilpad',
            'recoilpadman',
            'recoilpadstyle',
            'recoilpadnumber',
            'stockmod1',
            'stockmod2',
            'stockmod3',
            'stockrepairtype',
            'stockrepair',
            'checkering',
            'description1',
            'labor1',
            'retailmaterialcost1',
            'description2',
            'labor2',
            'retailmaterialcost2',
            'description3',
            'labor3',
            'retailmaterialcost3',
            'description4',
            'labor4',
            'retailmaterialcost4',
            'description5',
            'labor5',
            'retailmaterialcost5',
            'proposaltype',
            'shipping',
            'jobcostshipping',
            'downpay',
            'balance',
            'finalpay',
            'downpaydate',
            'finalpaydate',
            'checknum1',
            'checknum2',
            'notes',
        ]

    workorderdate = forms.DateField(
        widget=forms.DateInput(format='%m/%d/%Y'),
        input_formats=('%m/%d/%Y',)
    )

    description1 = forms.CharField(
        widget=forms.TextInput(
            attrs={'onblur': 'Description1Function(); Descr1Function(); Description1dFunction()', }, ),
        required=False,
    )

    labor1 = forms.CharField(
        widget=forms.TextInput(attrs={'onblur': 'Labor1Function(); LaborFunction1()', }, ),
        required=False,
    )

    retailmaterialcost1 = forms.CharField(
        widget=forms.TextInput(attrs={'onblur': 'RetailMaterialCost1Function(); RetailMat1CostFunction()', }, ),
        required=False,
    )

    description2 = forms.CharField(
        widget=forms.TextInput(
            attrs={'onblur': 'Description2Function(); Descr2Function(); Description2dFunction()', }, ),
        required=False,
    )

    labor2 = forms.CharField(
        widget=forms.TextInput(attrs={'onblur': 'Labor2Function(); LaborFunction2()', }, ),
        required=False,
    )

    retailmaterialcost2 = forms.CharField(
        widget=forms.TextInput(attrs={'onblur': 'RetailMaterialCost2Function(); RetailMat2CostFunction()', }, ),
        required=False,
    )

    description3 = forms.CharField(
        widget=forms.TextInput(
            attrs={'onblur': 'Description3Function(); Descr3Function(); Description3dFunction()', }, ),
        required=False,
    )

    labor3 = forms.CharField(
        widget=forms.TextInput(attrs={'onblur': 'Labor3Function(); LaborFunction3()', }, ),
        required=False,
    )

    retailmaterialcost3 = forms.CharField(
        widget=forms.TextInput(attrs={'onblur': 'RetailMaterialCost3Function(); RetailMat3CostFunction()', }, ),
        required=False,
    )

    description4 = forms.CharField(
        widget=forms.TextInput(
            attrs={'onblur': 'Description4Function(); Descr4Function(); Description4dFunction()', }, ),
        required=False,
    )

    labor4 = forms.CharField(
        widget=forms.TextInput(attrs={'onblur': 'Labor4Function(); LaborFunction4()', }, ),
        required=False,
    )

    retailmaterialcost4 = forms.CharField(
        widget=forms.TextInput(attrs={'onblur': 'RetailMaterialCost4Function(); RetailMat4CostFunction()', }, ),
        required=False,
    )

    description5 = forms.CharField(
        widget=forms.TextInput(
            attrs={'onblur': 'Description5Function(); Descr5Function(); Description5dFunction()', }, ),
        required=False,
    )

    labor5 = forms.CharField(
        widget=forms.TextInput(attrs={'onblur': 'Labor5Function(); LaborFunction5()', }, ),
        required=False,
    )

    retailmaterialcost5 = forms.CharField(
        widget=forms.TextInput(attrs={'onblur': 'RetailMaterialCost5Function(); RetailMat5CostFunction()', }, ),
        required=False,
    )

    notes = forms.CharField(
        widget=forms.Textarea(attrs={"rows": 5, 'onblur': 'NotesFunction()'}),
        required=False,
    )


class RecoilManChoiceField(forms.Form):
    recoilpadman = forms.ModelChoiceField(
        RecoilPadInfo.objects.values_list('PadMan', flat=True).distinct(),
        required=False,
        empty_label='',
        label="")


class RecoilStyleChoiceField(forms.Form):
    recoilpadstyle = forms.ModelChoiceField(
        RecoilPadInfo.objects.values_list('Padstyle', flat=True).distinct(),
        required=False,
        empty_label='',
        label="")


class RecoilNumberChoiceField(forms.Form):
    recoilpadnumber = forms.ModelChoiceField(
        RecoilPadInfo.objects.values_list('Padnum', flat=True).distinct(),
        required=False,
        empty_label='',
        label="")


class WorkOrderB(forms.ModelForm):
    class Meta:
        model = WorkOrder
        fields = [
            'custid',
            'gunid',
            'workorderid',
            'workorder',
            'workorderdate',
            'duplicating',
            'fittingtime',
            'fittingstock',
            'refinishing',
            'finishtype',
            'recoilpad',
            'recoilpadman',
            'recoilpadstyle',
            'recoilpadnumber',
            'stockmod1',
            'stockmod2',
            'stockmod3',
            'stockrepairtype',
            'stockrepair',
            'checkering',
            'wood',
            'description1',
            'labor1',
            'retailmaterialcost1',
            'description2',
            'labor2',
            'retailmaterialcost2',
            'description3',
            'labor3',
            'retailmaterialcost3',
            'description4',
            'labor4',
            'retailmaterialcost4',
            'description5',
            'labor5',
            'retailmaterialcost5',
            'notes',
            'proposaltype'
        ]

class Proposal(forms.ModelForm):
    class Meta:
        model = WorkOrder
        fields = [
            'custid',
            'gunid',
            'workorderid',
            'workorder',
            'workorderdate',
            'labor',
            'mat',
            'saletax',
            'totalmat',
            'totaljobcost',
            'shipping',
            'jobcostshipping',
            'shipping',
            'jobcostshipping',
            'downpay',
            'balance',
            'finalpay',
            'downpaydate',
            'finalpaydate',
            'checknum1',
            'checknum2',
            'notes',
        ]

    workorderdate = forms.DateField(
        widget=forms.DateInput(format='%m/%d/%Y'),
        input_formats=('%m/%d/%Y',)
    )

    labor = forms.CharField(
        widget=forms.TextInput(attrs={'readonly': 'readonly'}),
        required=False,
    )

    mat = forms.CharField(
        widget=forms.TextInput(attrs={'readonly': 'readonly'}),
        required=False,
    )

    saletax = forms.CharField(
        widget=forms.TextInput(attrs={'readonly': 'readonly'}),
        required=False,
    )

    totalmat = forms.CharField(
        widget=forms.TextInput(attrs={'readonly': 'readonly'}),
        required=False,
    )

    totaljobcost = forms.CharField(
        widget=forms.TextInput(attrs={'readonly': 'readonly'}),
        required=False,
    )

    finalpay = forms.CharField(
        widget=forms.TextInput(attrs={'readonly': 'readonly'}),
        required=False,
    )

    balance = forms.CharField(
        widget=forms.TextInput(attrs={'readonly': 'readonly'}),
        required=False,
    )

    downpay = forms.CharField(
        widget=forms.TextInput(attrs={'readonly': 'readonly'}),
        required=False,
    )

    jobcostshipping = forms.CharField(
        widget=forms.TextInput(attrs={'readonly': 'readonly'}),
        required=False,
    )

    workorder = forms.CharField(
        widget=forms.TextInput(attrs={'readonly': 'readonly'}),
        required=False,
    )

    notes = forms.CharField(
        widget=forms.Textarea(attrs={"rows": 5, 'readonly': 'readonly'}),
        required=False,
    )

    shipping = forms.CharField(
        widget=forms.TextInput(attrs={'onblur': 'ShippingFunction()'}),
        required=False,
    )


class DateInput2(forms.DateInput):
    input_type = 'date'


class WorkOrderC(forms.ModelForm):
    class Meta:
        model = WorkOrder
        fields = [
            'custid',
            'gunid',
            'workorderid',
            'workorder',
            'workorderdate',
            'shipping',
            'jobcostshipping',
            'downpay',
            'balance',
            'finalpay',
            'downpaydate',
            'finalpaydate',
            'checknum1',
            'checknum2',
            'notes',
        ]

    workorderdate = forms.DateField(
        widget=forms.DateInput(format='%m/%d/%Y'),
        input_formats=('%m/%d/%Y',)
    )

    shipping = forms.CharField(
        widget=forms.TextInput(attrs={'onblur': 'ShippingFunction()'}),
        required=False,
    )

    jobcostshipping = forms.CharField(
        widget=forms.TextInput(attrs={'onblur': 'JobCostShippingFunction()'}),
        required=False,
    )

    downpay = forms.CharField(
        widget=forms.TextInput(attrs={'onblur': 'DownPayFunction(); BalanceFunction()', }, ),
        required=False,
    )

    checknum1 = forms.CharField(
        widget=forms.TextInput(attrs={'onblur': 'CheckNum1Function()'}),
        required=False,
    )

    checknum2 = forms.CharField(
        widget=forms.TextInput(attrs={'onblur': 'CheckNum2Function()'}),
        required=False,
    )

    downpaydate = forms.CharField(
        widget=DateInput2(attrs={'onblur': 'DownPayDateFunction()'}),
        required=False,
    )

    finalpaydate = forms.CharField(
        widget=DateInput2(attrs={'onblur': 'FinalPayDateFunction()'}),
        required=False,
    )

    finalpay = forms.CharField(
        widget=forms.DateInput(attrs={'onblur': 'FinalPayFunction()'}),
        required=False,
    )

    notes = forms.CharField(
        widget=forms.Textarea(attrs={"rows": 5}),
        required=False,
    )


class MaterialA(forms.ModelForm):
    class Meta:
        model = Materials
        fields = [
            'description',
            'labor',
            'wholesalecost',
            'retailcost',
        ]

class Evalue(forms.ModelForm):
    class Meta:
        model = Evaluation
        fields = [
            'evalueid',
            'gunid',
            'custid',
            'workorderdate',
            'eyedominace',
            'exhand',
            'exlop',
            'exdac',
            'exdaf',
            'exdah',
            'exdamc',
            'excast',
            'exlotp',
            'extoeout',
            'expitch',
            'newhand',
            'newlop',
            'newdac',
            'newdaf',
            'newdah',
            'newdamc',
            'newcast',
            'newlotp',
            'newtoeout',
            'newpitch',
            'cor1',
            'cor2',
            'cor3',
            'cor4',
            'cor5',
            'cor6',
            'cor7',
            'cor8',
            'cor9',
            'cor10',
            'cor11',
            'notes',
        ]

    workorderdate = forms.CharField(
        widget=DateInput2(attrs={'onblur': 'WorkOrderDateFunction()'}),
        required=False,
    )

    notes = forms.CharField(
        widget=forms.Textarea(attrs={"rows": 5, 'onblur': 'EvalueNotesFunction()'}),
        required=False,
    )

    expitch = forms.CharField(
        widget=forms.TextInput(attrs={'onblur': 'ExPitchFunction()'}),
        required=False,
    )

    newpitch = forms.CharField(
        widget=forms.TextInput(attrs={'onblur': 'NewPitchFunction()'}),
        required=False,
    )

class Evalueprev(forms.ModelForm):
    class Meta:
        model = Evaluation
        fields = [
            'evalueid',
            'gunid',
            'custid',
            'workorderdate',
            'eyedominace',
            'exhand',
            'exlop',
            'exdac',
            'exdaf',
            'exdah',
            'exdamc',
            'excast',
            'exlotp',
            'extoeout',
            'expitch',
            'newhand',
            'newlop',
            'newdac',
            'newdaf',
            'newdah',
            'newdamc',
            'newcast',
            'newlotp',
            'newtoeout',
            'newpitch',
            'cor1',
            'cor2',
            'cor3',
            'cor4',
            'cor5',
            'cor6',
            'cor7',
            'cor8',
            'cor9',
            'cor10',
            'cor11',
            'notes',
        ]

    workorderdate = forms.CharField(
        widget=forms.TextInput(attrs={'readonly': 'readonly'}),
        required=False,
    )

    eyedominace = forms.CharField(
        widget=forms.TextInput(attrs={'readonly': 'readonly'}),
        required=False,
    )

    exhand = forms.CharField(
        widget=forms.TextInput(attrs={'readonly': 'readonly'}),
        required=False,
    )

    exlop = forms.CharField(
        widget=forms.TextInput(attrs={'readonly': 'readonly'}),
        required=False,
    )

    exdac = forms.CharField(
        widget=forms.TextInput(attrs={'readonly': 'readonly'}),
        required=False,
    )

    exdaf = forms.CharField(
        widget=forms.TextInput(attrs={'readonly': 'readonly'}),
        required=False,
    )

    exdah = forms.CharField(
        widget=forms.TextInput(attrs={'readonly': 'readonly'}),
        required=False,
    )

    exdamc = forms.CharField(
        widget=forms.TextInput(attrs={'readonly': 'readonly'}),
        required=False,
    )

    excast = forms.CharField(
        widget=forms.TextInput(attrs={'readonly': 'readonly'}),
        required=False,
    )

    exlotp = forms.CharField(
        widget=forms.TextInput(attrs={'readonly': 'readonly'}),
        required=False,
    )

    extoeout = forms.CharField(
        widget=forms.TextInput(attrs={'readonly': 'readonly'}),
        required=False,
    )

    expitch = forms.CharField(
        widget=forms.TextInput(attrs={'readonly': 'readonly'}),
        required=False,
    )

    newhand = forms.CharField(
        widget=forms.TextInput(attrs={'readonly': 'readonly'}),
        required=False,
    )

    newlop = forms.CharField(
        widget=forms.TextInput(attrs={'readonly': 'readonly'}),
        required=False,
    )

    newdac = forms.CharField(
        widget=forms.TextInput(attrs={'readonly': 'readonly'}),
        required=False,
    )

    newdaf = forms.CharField(
        widget=forms.TextInput(attrs={'readonly': 'readonly'}),
        required=False,
    )

    newdah = forms.CharField(
        widget=forms.TextInput(attrs={'readonly': 'readonly'}),
        required=False,
    )

    newdamc = forms.CharField(
        widget=forms.TextInput(attrs={'readonly': 'readonly'}),
        required=False,
    )

    newcast = forms.CharField(
        widget=forms.TextInput(attrs={'readonly': 'readonly'}),
        required=False,
    )

    newlotp = forms.CharField(
        widget=forms.TextInput(attrs={'readonly': 'readonly'}),
        required=False,
    )

    newtoeout = forms.CharField(
        widget=forms.TextInput(attrs={'readonly': 'readonly'}),
        required=False,
    )

    newpitch = forms.CharField(
        widget=forms.TextInput(attrs={'readonly': 'readonly'}),
        required=False,
    )

    cor1 = forms.CharField(
        widget=forms.TextInput(attrs={'readonly': 'readonly'}),
        required=False,
    )

    cor2 = forms.CharField(
        widget=forms.TextInput(attrs={'readonly': 'readonly'}),
        required=False,
    )

    cor3 = forms.CharField(
        widget=forms.TextInput(attrs={'readonly': 'readonly'}),
        required=False,
    )

    cor4 = forms.CharField(
        widget=forms.TextInput(attrs={'readonly': 'readonly'}),
        required=False,
    )

    cor5 = forms.CharField(
        widget=forms.TextInput(attrs={'readonly': 'readonly'}),
        required=False,
    )

    cor6 = forms.CharField(
        widget=forms.TextInput(attrs={'readonly': 'readonly'}),
        required=False,
    )

    cor7 = forms.CharField(
        widget=forms.TextInput(attrs={'readonly': 'readonly'}),
        required=False,
    )

    cor8 = forms.CharField(
        widget=forms.TextInput(attrs={'readonly': 'readonly'}),
        required=False,
    )

    cor9 = forms.CharField(
        widget=forms.TextInput(attrs={'readonly': 'readonly'}),
        required=False,
    )

    cor10 = forms.CharField(
        widget=forms.TextInput(attrs={'readonly': 'readonly'}),
        required=False,
    )

    cor11 = forms.CharField(
        widget=forms.TextInput(attrs={'readonly': 'readonly'}),
        required=False,
    )

    notes = forms.CharField(
        widget=forms.Textarea(attrs={"rows": 5, 'readonly': 'readonly'}),
        required=False,
    )
