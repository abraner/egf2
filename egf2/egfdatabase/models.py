from django.db import models
from phone_field import PhoneField

# Create your models here.


class CustomerInfo(models.Model):
    id = models.AutoField(primary_key=True, default=None, verbose_name="ID.")
    idA = models.IntegerField(null=True, default=None, verbose_name="Cust ID.")
    custcompanytname = models.CharField(max_length=50, blank=True, verbose_name="Company Name:")
    custfirstname = models.CharField(max_length=45, verbose_name="First Name:")
    custlastname = models.CharField(max_length=45, verbose_name="Last Name:")
    custadd1 = models.CharField(max_length=45, verbose_name="Address #1:")
    custadd2 = models.CharField(max_length=45, blank=True, verbose_name="Address #2:")
    custcity = models.CharField(max_length=45, verbose_name="City:")
    custst = models.CharField(max_length=2, verbose_name="St:")
    custzipcode = models.CharField(max_length=15, verbose_name="Zip Code:")
    custwork1 = PhoneField(blank=True, verbose_name="Work Phone #1:")
    custwork2 = PhoneField(blank=True, verbose_name="Work Phone #2:")
    custcell1 = PhoneField(blank=True, verbose_name="Cell Phone #1:")
    custcell2 = PhoneField(blank=True, verbose_name="Cell Phone #2:")
    custhome = PhoneField(blank=True, verbose_name="Home Phone:")
    custemail1 = models.EmailField(max_length=254, blank=True, verbose_name="Email #1:")
    custemail2 = models.EmailField(max_length=254, blank=True, verbose_name="Email #2:")

    def get_absolute_url(self):
        return f"/egfdatabase/{self.id}/"

    def get_absolute21_url(self):
        return f"/egfdatabase/{self.id}/proposal/"


class GunInfo(models.Model):
    gun_id = models.AutoField(primary_key=True, default=None, verbose_name="Gun ID.")
    gunid = models.IntegerField(null=True, default=None, blank=True, verbose_name="Gun ID.")
    id = models.IntegerField(null=True, default=None, verbose_name="Cust ID.")
    gunmanufacturer = models.CharField(max_length=50, blank=True, verbose_name="Gun Manufacturer")
    gunmodel = models.CharField(max_length=45, verbose_name="Gun Model")
    gunserialnumber = models.CharField(max_length=45, verbose_name="Gun Serial Number")
    gungauge = models.CharField(max_length=15, verbose_name="Gun Gauge")
    hand = models.CharField(max_length=15, blank=True, verbose_name="Hand")
    lop = models.CharField(max_length=15, blank=True, verbose_name="LOP")
    comb = models.CharField(max_length=15, blank=True, verbose_name="Comb")
    face = models.CharField(max_length=15, blank=True, verbose_name="face")
    heel = models.CharField(max_length=15, blank=True, verbose_name="Heel")
    montecarlo = models.CharField(max_length=15, blank=True, verbose_name="Monte Carlo")
    cast = models.CharField(max_length=15, blank=True, verbose_name="Cast")
    toe = models.CharField(max_length=15, blank=True, verbose_name="Toe")
    trigger = models.CharField(max_length=15, blank=True, verbose_name="Trigger LOP")
    pitch = models.CharField(max_length=15, blank=True, verbose_name="Pitch")

    def get_absolute2_url(self):
        return f"/egfdatabase/{self.gun_id}/newgun/"

    def get_absolute3_url(self):
        return f"/egfdatabase/{self.id}/"

    def get_absolute4_url(self):
        return f"/egfdatabase/{self.gun_id}/guninfo/"

    def get_absolute5_url(self):
        return f"/egfdatabase/{self.gun_id}/"


class ProposalType(models.Model):
    proposal_type = models.CharField(max_length=200, blank=True, unique=True)

    def __str__(self):
        return self.proposal_type


class Wood(models.Model):
    wood_type = models.CharField(max_length=200, blank=True, unique=True)

    def __str__(self):
        return self.wood_type


class Checkering(models.Model):
    checker_type = models.CharField(max_length=200, blank=True, unique=True)

    def __str__(self):
        return self.checker_type


class StockRepairTime(models.Model):
    stock_repair_time = models.DecimalField(decimal_places=2, max_digits=7, default='0.00', unique=True)

    def __str__(self):
        return str(self.stock_repair_time)


class StockRepairType(models.Model):
    stock_repair_type = models.CharField(max_length=200, blank=True, unique=True)

    def __str__(self):
        return self.stock_repair_type


class StockMod3(models.Model):
    stock_mod = models.CharField(max_length=200, blank=True, unique=True)

    def __str__(self):
        return self.stock_mod


class StockMod2(models.Model):
    stock_mod = models.CharField(max_length=200, blank=True, unique=True)

    def __str__(self):
        return self.stock_mod


class StockMod1(models.Model):
    stock_mod = models.CharField(max_length=200, blank=True, unique=True)

    def __str__(self):
        return self.stock_mod


class RecoilPad(models.Model):
    recoil_pad = models.CharField(max_length=200, blank=True, unique=True)

    def __str__(self):
        return self.recoil_pad


class StockRefinishing(models.Model):
    refinish_stock = models.CharField(max_length=200, blank=True, unique=True)

    def __str__(self):
        return self.refinish_stock


class FinishType(models.Model):
    finish_type = models.CharField(max_length=200, blank=True, unique=True)

    def __str__(self):
        return self.finish_type


class FittingStock(models.Model):
    fitting_stock = models.CharField(max_length=200, blank=True, unique=True)

    def __str__(self):
        return self.fitting_stock


class FittingTime(models.Model):
    fitting_time = models.DecimalField(decimal_places=2, max_digits=7, default='0.00', unique=True)

    def __str__(self):
        return str(self.fitting_time)


class DuplicatingType(models.Model):
    duplicating_type = models.CharField(max_length=200, blank=True, unique=True)

    def __str__(self):
        return self.duplicating_type


class WorkOrder(models.Model):
    workorderid = models.AutoField(primary_key=True, default=None, verbose_name="Work Order ID.")
    workorder = models.IntegerField(null=True, default=None, blank=True, verbose_name="Work Order ID.")
    gunid = models.IntegerField(null=True, default=None, verbose_name="Gun ID.")
    custid = models.IntegerField(null=True, default=None, verbose_name="Cust. ID.")
    workorderdate = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True, verbose_name="Last Updated")
    date = models.DateField(auto_now_add=False, auto_now=True, blank=True)
    duplicating = models.ForeignKey(DuplicatingType, to_field="duplicating_type", null=True, blank=True, default=None, on_delete=models.CASCADE, verbose_name="Duplicating")
    fittingtime = models.ForeignKey(FittingTime, to_field="fitting_time", null=True, blank=True, default=None, on_delete=models.CASCADE, verbose_name="Fitting Time")
    fittingstock = models.ForeignKey(FittingStock, to_field="fitting_stock", null=True, blank=True, default=None, on_delete=models.CASCADE, verbose_name="Fitting Stock")
    refinishing = models.ForeignKey(StockRefinishing, to_field="refinish_stock", null=True, blank=True, default=None, on_delete=models.CASCADE, verbose_name="Refinishing")
    finishtype = models.ForeignKey(FinishType, to_field="finish_type", null=True, blank=True, default=None, on_delete=models.CASCADE, verbose_name="Finish Type")
    recoilpad = models.ForeignKey(RecoilPad, to_field="recoil_pad", null=True, blank=True, default=None, on_delete=models.CASCADE, verbose_name="Recoil Pad")
    recoilpadman = models.CharField(max_length=35, blank=True, null=True, default=None, verbose_name="Recoil Pad Manufacturer")
    recoilpadstyle = models.CharField(max_length=70, blank=True, null=True, default=None, verbose_name="Recoil Pad Style")
    recoilpadnumber = models.CharField(max_length=70, blank=True, null=True, default=None, verbose_name="Recoil Pad Number")
    stockmod1 = models.ForeignKey(StockMod1, to_field="stock_mod", null=True, blank=True, default=None, on_delete=models.CASCADE, verbose_name="Modification 1")
    stockmod2 = models.ForeignKey(StockMod2, to_field="stock_mod", null=True, blank=True, default=None, on_delete=models.CASCADE, verbose_name="Modification 2")
    stockmod3 = models.ForeignKey(StockMod3, to_field="stock_mod", null=True, blank=True, default=None, on_delete=models.CASCADE, verbose_name="Modification 3")
    stockrepairtype = models.ForeignKey(StockRepairType, to_field="stock_repair_type", null=True, blank=True, default=None, on_delete=models.CASCADE, verbose_name="Stock Repair Type")
    stockrepair = models.ForeignKey(StockRepairTime, to_field="stock_repair_time", null=True, blank=True, default=None, on_delete=models.CASCADE, verbose_name="Stock Repair")
    checkering = models.ForeignKey(Checkering, to_field="checker_type", null=True, blank=True, default=None, on_delete=models.CASCADE, verbose_name="Checkering")
    wood = models.ForeignKey(Wood, to_field="wood_type", null=True, blank=True, default=None, on_delete=models.CASCADE, verbose_name="Wood")
    description1 = models.CharField(max_length=75, blank=True, verbose_name="Description 1")
    labor1 = models.DecimalField(decimal_places=2, max_digits=7, default='0.00', verbose_name="Labor1")
    retailmaterialcost1 = models.DecimalField(decimal_places=2, max_digits=7, default='0.00', verbose_name="Retail Material Cost1")
    description2 = models.CharField(max_length=75, blank=True, verbose_name="Description 2")
    labor2 = models.DecimalField(decimal_places=2, max_digits=7, default='0.00', verbose_name="Labor2")
    retailmaterialcost2 = models.DecimalField(decimal_places=2, max_digits=7, default='0.00', verbose_name="Retail Material Cost2")
    description3 = models.CharField(max_length=75, blank=True, verbose_name="Description 3")
    labor3 = models.DecimalField(decimal_places=2, max_digits=7, default='0.00', verbose_name="Labor3")
    retailmaterialcost3 = models.DecimalField(decimal_places=2, max_digits=7, default='0.00', verbose_name="Retail Material Cost3")
    description4 = models.CharField(max_length=75, blank=True, verbose_name="Description 4")
    labor4 = models.DecimalField(decimal_places=2, max_digits=7, default='0.00', verbose_name="Labor4")
    retailmaterialcost4 = models.DecimalField(decimal_places=2, max_digits=7, default='0.00', verbose_name="Retail Material Cost4")
    description5 = models.CharField(max_length=75, blank=True, verbose_name="Description 5")
    labor5 = models.DecimalField(decimal_places=2, max_digits=7, default='0.00', verbose_name="Labor5")
    retailmaterialcost5 = models.DecimalField(decimal_places=2, max_digits=7, default='0.00', verbose_name="Retail Material Cost5")
    notes = models.CharField(max_length=255, blank=True, verbose_name="Notes")
    proposaltype = models.ForeignKey(ProposalType, to_field="proposal_type", null=True, blank=True, default=None, on_delete=models.CASCADE, verbose_name="Proposal Type")
    mat = models.DecimalField(max_digits=7, decimal_places=2, null=True, default=None, blank=True, verbose_name="Material")
    labor = models.DecimalField(max_digits=7, decimal_places=2, null=True, default=None, blank=True, verbose_name="Labor")
    saletax = models.DecimalField(max_digits=7, decimal_places=2, null=True, default=None, blank=True, verbose_name="Sales Tax")
    totalmat = models.DecimalField(max_digits=7, decimal_places=2, null=True, default=None, blank=True, verbose_name="Total Material")
    totaljobcost = models.DecimalField(max_digits=7, decimal_places=2, null=True, default=None, blank=True, verbose_name="Total Job Cost")
    shipping = models.DecimalField(max_digits=7, decimal_places=2, null=True, default=None, blank=True, verbose_name="Shipping")
    jobcostshipping = models.DecimalField(max_digits=7, decimal_places=2, null=True, default=None, blank=True, verbose_name="Job Cost Shipping")
    downpay = models.DecimalField(max_digits=7, decimal_places=2, null=True, default=None, blank=True, verbose_name="Down Payment")
    balance = models.DecimalField(max_digits=7, decimal_places=2, null=True, default=None, blank=True, verbose_name="Balance")
    finalpay = models.DecimalField(max_digits=7, decimal_places=2, null=True, default=None, blank=True, verbose_name="Final Payment")
    downpaydate = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True, verbose_name="Down Payment Date")
    finalpaydate = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True, verbose_name="Final Payment Date")
    checknum1 = models.CharField(max_length=75, blank=True, null=True, verbose_name="Down Payment check number")
    checknum2 = models.CharField(max_length=75, blank=True, null=True, verbose_name="Final Payment check number")

    def get_absolute6_url(self):
        return f"/egfdatabase/{self.workorderid}/workorder/"

    def get_absolute26_url(self):
        return f"/egfdatabase/{self.workorderid}/workorder3/"

    def get_absolute5_url(self):
        return f"/egfdatabase/{self.workorderid}/delete_workorder/"

    def get_absolute20_url(self):
        return f"/egfdatabase/{self.workorderid}/workorder2/"

    def get_absolute30_url(self):
        return f"/egfdatabase/{self.workorderid}/proposal/"

    def get_absolute7_url(self):
        return f"/egfdatabase/{self.gunid}/previouswo/"

    def get_absolute17_url(self):
        return f"/egfdatabase/{self.gunid}/guninfo/"

    def get_absolute8_url(self):
        return f"/egfdatabase/{self.workorderid}/workorderprev/"

    def get_absolute18_url(self):
        return f"/egfdatabase/{self.workorderid}/proposalprev/"

    def get_absolute19_url(self):
        return f"/egfdatabase/{self.gunid}/guninfo/previouswo"


class Materials(models.Model):
    description = models.CharField(max_length=100, blank=True, verbose_name="Description")
    labor = models.DecimalField(max_digits=7, decimal_places=2, null=True, default=None, blank=True, verbose_name="Labor Cost")
    wholesalecost = models.DecimalField(max_digits=7, decimal_places=2, null=True, default=None, blank=True, verbose_name="Wholesale Cost")
    retailcost = models.DecimalField(max_digits=7, decimal_places=2, null=True, default=None, blank=True, verbose_name="Retail Cost")

    def get_absolute9_url(self):
        return f"/egfdatabase/{self.id}/mat_detail"

    def get_absolute10_url(self):
        return f"/egfdatabase/{self.id}/edit_mat_info"



class RecoilPadInfo(models.Model):
    PadMan = models.CharField(max_length=50, blank=True, verbose_name="Recoil Pad Manufacturer")
    Padstyle = models.CharField(max_length=70, blank=True, verbose_name="Recoil Pad Style")
    Padnum = models.CharField(max_length=70, blank=True, verbose_name="Recoil Pad Number")


class MasterTotal(models.Model):
    workorder = models.IntegerField(null=True, default=None, blank=True, verbose_name="Work Order ID.")
    gunid = models.IntegerField(null=True, default=None, verbose_name="Gun ID.")
    custid = models.IntegerField(null=True, default=None, verbose_name="Cust. ID.")
    workorderdate = models.DateField()
    description = models.CharField(max_length=75, blank=True, verbose_name="Description")

    def get_absolute16_url(self):
        return f"/egfdatabase/{self.workorder}/workorder/"


class Labor(models.Model):
    labor = models.DecimalField(decimal_places=2, max_digits=7, default='0.00', unique=False, blank=True, verbose_name="Labor")


class FitTime(models.Model):
    workorder = models.IntegerField(null=True, default=None, blank=True, verbose_name="Work Order ID.")
    gunid = models.IntegerField(null=True, default=None, verbose_name="Gun ID.")
    custid = models.IntegerField(null=True, default=None, verbose_name="Cust. ID.")
    workorderdate = models.DateField()
    timefit = models.DecimalField(decimal_places=2, max_digits=7, default='0.00', unique=False, blank=True, verbose_name="Labor Time")


class RepairTime(models.Model):
    workorder = models.IntegerField(null=True, default=None, blank=True, verbose_name="Work Order ID.")
    gunid = models.IntegerField(null=True, default=None, verbose_name="Gun ID.")
    custid = models.IntegerField(null=True, default=None, verbose_name="Cust. ID.")
    workorderdate = models.DateField()
    timerepair = models.DecimalField(decimal_places=2, max_digits=7, default='0.00', unique=False, blank=True, verbose_name="Labor Time")


class MiscServices(models.Model):
    workorder = models.IntegerField(null=True, default=None, blank=True, verbose_name="Work Order ID.")
    gunid = models.IntegerField(null=True, default=None, verbose_name="Gun ID.")
    custid = models.IntegerField(null=True, default=None, verbose_name="Cust. ID.")
    workorderdate = models.DateField(null=True, blank=True)
    description = models.CharField(max_length=75, blank=True, verbose_name="Description ")
    misclabor = models.DecimalField(decimal_places=2, max_digits=7, default='0.00', unique=False, blank=True, verbose_name="Misc. Labor")
    miscretail = models.DecimalField(decimal_places=2, max_digits=7, default='0.00', unique=False, blank=True, verbose_name="Misc. Wholesale")


class WorkOrderForm(models.Model):
    workorder = models.IntegerField(null=True, default=None, blank=True, verbose_name="Work Order ID.")
    gunid = models.IntegerField(null=True, default=None, verbose_name="Gun ID.")
    custid = models.IntegerField(null=True, default=None, verbose_name="Cust. ID.")
    workorderdate = models.DateField(null=True, blank=True)
    ident = models.CharField(max_length=5, blank=True, verbose_name="Ident ")
    description = models.CharField(max_length=75, blank=True, verbose_name="Description ")
    labor = models.DecimalField(decimal_places=2, max_digits=7, default='0.00', unique=False, blank=True, verbose_name="Labor")
    retail = models.DecimalField(decimal_places=2, max_digits=7, default='0.00', unique=False, blank=True, verbose_name="Retail")


class WorkOrderlabor(models.Model):
    workorder = models.IntegerField(null=True, default=None, blank=True, verbose_name="Work Order ID.")
    gunid = models.IntegerField(null=True, default=None, verbose_name="Gun ID.")
    custid = models.IntegerField(null=True, default=None, verbose_name="Cust. ID.")
    workorderdate = models.DateField(null=True, blank=True)
    ident = models.CharField(max_length=5, blank=True, verbose_name="Ident ")
    description = models.CharField(max_length=75, blank=True, verbose_name="Description ")
    labor = models.DecimalField(decimal_places=2, max_digits=7, default='0.00', unique=False, blank=True, verbose_name="Labor")
    retail = models.DecimalField(decimal_places=2, max_digits=7, default='0.00', unique=False, blank=True, verbose_name="Retail")


class JobCost(models.Model):
    workorder = models.IntegerField(null=True, default=None, blank=True, verbose_name="Work Order ID.")
    labor = models.DecimalField(decimal_places=2, max_digits=7, default='0.00', unique=False, blank=True, verbose_name="Labor")
    retail = models.DecimalField(decimal_places=2, max_digits=7, default='0.00', unique=False, blank=True, verbose_name="Retail")
    saletax = models.DecimalField(decimal_places=2, max_digits=7, default='0.00', unique=False, blank=True, verbose_name="Sales Tax")
    totalmat = models.DecimalField(decimal_places=2, max_digits=7, default='0.00', unique=False, blank=True, verbose_name="Total Material")
    totaljobcost = models.DecimalField(decimal_places=2, max_digits=7, default='0.00', unique=False, blank=True, verbose_name="Total Job Cost")
    shipping = models.DecimalField(decimal_places=2, max_digits=7, default='0.00', unique=False, blank=True, verbose_name="Shipping")
    costship = models.DecimalField(decimal_places=2, max_digits=7, default='0.00', unique=False, blank=True, verbose_name="Total Job Cost w/Shipping")
    downpaydate = models.CharField(max_length=75, blank=True, verbose_name="Down Payment Date")
    downcheck = models.CharField(max_length=75, blank=True, verbose_name="Check Number")
    downpay = models.DecimalField(decimal_places=2, max_digits=7, default='0.00', unique=False, blank=True, verbose_name="Down Payment")
    balance = models.DecimalField(decimal_places=2, max_digits=7, default='0.00', unique=False, blank=True, verbose_name="Balance")
    finalpaydate = models.CharField(max_length=75, blank=True, verbose_name="Final Payment Date")
    finalcheck = models.CharField(max_length=75, blank=True, verbose_name="Check Number")
    finalpay = models.DecimalField(decimal_places=2, max_digits=7, default='0.00', unique=False, blank=True, verbose_name="Final Payment")




class TaxRate(models.Model):
    rate = models.DecimalField(decimal_places=3, max_digits=7, default='0.00', unique=False, blank=True, verbose_name="Tax Rate")


class EyeType(models.Model):
    eye_type = models.CharField(max_length=200, blank=True, unique=True)

    def __str__(self):
        return self.eye_type


class HandType(models.Model):
    hand_type = models.CharField(max_length=200, blank=True, unique=True)

    def __str__(self):
        return self.hand_type


class LopType(models.Model):
    lop_type = models.CharField(max_length=200, blank=True, unique=True)

    def __str__(self):
        return self.lop_type


class DacType(models.Model):
    dac_type = models.CharField(max_length=200, blank=True, unique=True)

    def __str__(self):
        return self.dac_type


class DafType(models.Model):
    daf_type = models.CharField(max_length=200, blank=True, unique=True)

    def __str__(self):
        return self.daf_type


class DahType(models.Model):
    dah_type = models.CharField(max_length=200, blank=True, unique=True)

    def __str__(self):
        return self.dah_type


class DamcType(models.Model):
    damc_type = models.CharField(max_length=200, blank=True, unique=True)

    def __str__(self):
        return self.damc_type


class CastType(models.Model):
    cast_type = models.CharField(max_length=200, blank=True, unique=True)

    def __str__(self):
        return self.cast_type


class LotpType(models.Model):
    lotp_type = models.CharField(max_length=200, blank=True, unique=True)

    def __str__(self):
        return self.lotp_type


class ToeoutType(models.Model):
    toeout_type = models.CharField(max_length=200, blank=True, unique=True)

    def __str__(self):
        return self.toeout_type


class NewHandType(models.Model):
    newhand_type = models.CharField(max_length=200, blank=True, unique=True)

    def __str__(self):
        return self.newhand_type


class NewLopType(models.Model):
    newlop_type = models.CharField(max_length=200, blank=True, unique=True)

    def __str__(self):
        return self.newlop_type


class NewDacType(models.Model):
    newdac_type = models.CharField(max_length=200, blank=True, unique=True)

    def __str__(self):
        return self.newdac_type


class NewDafType(models.Model):
    newdaf_type = models.CharField(max_length=200, blank=True, unique=True)

    def __str__(self):
        return self.newdaf_type


class NewDahType(models.Model):
    newdah_type = models.CharField(max_length=200, blank=True, unique=True)

    def __str__(self):
        return self.newdah_type


class NewDamcType(models.Model):
    newdamc_type = models.CharField(max_length=200, blank=True, unique=True)

    def __str__(self):
        return self.newdamc_type


class NewCastType(models.Model):
    newcast_type = models.CharField(max_length=200, blank=True, unique=True)

    def __str__(self):
        return self.newcast_type


class NewLotpType(models.Model):
    newlotp_type = models.CharField(max_length=200, blank=True, unique=True)

    def __str__(self):
        return self.newlotp_type


class NewToeoutType(models.Model):
    newtoeout_type = models.CharField(max_length=200, blank=True, unique=True)

    def __str__(self):
        return self.newtoeout_type


class Cor1Type(models.Model):
    cor1_type = models.CharField(max_length=200, blank=True, unique=True)

    def __str__(self):
        return self.cor1_type


class Cor2Type(models.Model):
    cor2_type = models.CharField(max_length=200, blank=True, unique=True)

    def __str__(self):
        return self.cor2_type


class Cor3Type(models.Model):
    cor3_type = models.CharField(max_length=200, blank=True, unique=True)

    def __str__(self):
        return self.cor3_type


class Cor4Type(models.Model):
    cor4_type = models.CharField(max_length=200, blank=True, unique=True)

    def __str__(self):
        return self.cor4_type


class Cor5Type(models.Model):
    cor5_type = models.CharField(max_length=200, blank=True, unique=True)

    def __str__(self):
        return self.cor5_type


class Cor6Type(models.Model):
    cor6_type = models.CharField(max_length=200, blank=True, unique=True)

    def __str__(self):
        return self.cor6_type


class Cor7Type(models.Model):
    cor7_type = models.CharField(max_length=200, blank=True, unique=True)

    def __str__(self):
        return self.cor7_type


class Cor8Type(models.Model):
    cor8_type = models.CharField(max_length=200, blank=True, unique=True)

    def __str__(self):
        return self.cor8_type


class Cor9Type(models.Model):
    cor9_type = models.CharField(max_length=200, blank=True, unique=True)

    def __str__(self):
        return self.cor9_type


class Cor10Type(models.Model):
    cor10_type = models.CharField(max_length=200, blank=True, unique=True)

    def __str__(self):
        return self.cor10_type


class Cor11Type(models.Model):
    cor11_type = models.CharField(max_length=200, blank=True, unique=True)

    def __str__(self):
        return self.cor11_type



class Evaluation(models.Model):
    evalueid = models.IntegerField(null=True, default=None, blank=True, verbose_name="Evalue. ID.")
    workorder = models.IntegerField(null=True, default=None, blank=True, verbose_name="Work Order ID.")
    gunid = models.IntegerField(null=True, default=None, verbose_name="Gun ID.")
    custid = models.IntegerField(null=True, default=None, verbose_name="Cust. ID.")
    workorderdate = models.DateField(auto_now_add=False, auto_now=False, null=True, blank=True, verbose_name="Last Updated")
    date = models.DateField(auto_now_add=False, auto_now=True, null=True, blank=True)
    eyedominace = models.ForeignKey(EyeType, to_field="eye_type", null=True, blank=True, default=None, on_delete=models.CASCADE, verbose_name="Eye Dominace")
    exhand = models.ForeignKey(HandType, to_field="hand_type", null=True, blank=True, default=None, on_delete=models.CASCADE, verbose_name="Handand")
    exlop = models.ForeignKey(LopType, to_field="lop_type", null=True, blank=True, default=None, on_delete=models.CASCADE, verbose_name="exlop")
    exdac = models.ForeignKey(DacType, to_field="dac_type", null=True, blank=True, default=None, on_delete=models.CASCADE, verbose_name="exdac")
    exdaf = models.ForeignKey(DafType, to_field="daf_type", null=True, blank=True, default=None, on_delete=models.CASCADE, verbose_name="exdaf")
    exdah = models.ForeignKey(DahType, to_field="dah_type", null=True, blank=True, default=None, on_delete=models.CASCADE, verbose_name="exdah")
    exdamc = models.ForeignKey(DamcType, to_field="damc_type", null=True, blank=True, default=None, on_delete=models.CASCADE, verbose_name="exdamc")
    excast = models.ForeignKey(CastType, to_field="cast_type", null=True, blank=True, default=None, on_delete=models.CASCADE, verbose_name="excast")
    exlotp = models.ForeignKey(LotpType, to_field="lotp_type", null=True, blank=True, default=None, on_delete=models.CASCADE, verbose_name="exlotp")
    extoeout = models.ForeignKey(ToeoutType, to_field="toeout_type", null=True, blank=True, default=None, on_delete=models.CASCADE, verbose_name="extoeout")
    expitch = models.CharField(max_length=75, null=True, blank=True, verbose_name="expitch")
    newhand = models.ForeignKey(NewHandType, to_field="newhand_type", null=True, blank=True, default=None, on_delete=models.CASCADE, verbose_name="newhand")
    newlop = models.ForeignKey(NewLopType, to_field="newlop_type", null=True, blank=True, default=None, on_delete=models.CASCADE, verbose_name="newlop")
    newdac = models.ForeignKey(NewDacType, to_field="newdac_type", null=True, blank=True, default=None, on_delete=models.CASCADE, verbose_name="newdac")
    newdaf = models.ForeignKey(NewDafType, to_field="newdaf_type", null=True, blank=True, default=None, on_delete=models.CASCADE, verbose_name="newdaf")
    newdah = models.ForeignKey(NewDahType, to_field="newdah_type", null=True, blank=True, default=None, on_delete=models.CASCADE, verbose_name="newdah")
    newdamc = models.ForeignKey(NewDamcType, to_field="newdamc_type", null=True, blank=True, default=None, on_delete=models.CASCADE, verbose_name="newdamc")
    newcast = models.ForeignKey(NewCastType, to_field="newcast_type", null=True, blank=True, default=None, on_delete=models.CASCADE, verbose_name="newcast")
    newlotp = models.ForeignKey(NewLotpType, to_field="newlotp_type", null=True, blank=True, default=None, on_delete=models.CASCADE, verbose_name="newlotp")
    newtoeout = models.ForeignKey(NewToeoutType, to_field="newtoeout_type", null=True, blank=True, default=None, on_delete=models.CASCADE, verbose_name="newtoeout")
    newpitch = models.CharField(max_length=75, null=True, blank=True, verbose_name="newpitch")
    evaluationgunfit = models.CharField(max_length=75, null=True, blank=True, verbose_name="evaluationgunfit")
    cor1 = models.ForeignKey(Cor1Type, to_field="cor1_type", null=True, blank=True, default=None, on_delete=models.CASCADE, verbose_name="cor1")
    cor2 = models.ForeignKey(Cor2Type, to_field="cor2_type", null=True, blank=True, default=None, on_delete=models.CASCADE, verbose_name="cor2")
    cor3 = models.ForeignKey(Cor3Type, to_field="cor3_type", null=True, blank=True, default=None, on_delete=models.CASCADE, verbose_name="cor3")
    cor4 = models.ForeignKey(Cor4Type, to_field="cor4_type", null=True, blank=True, default=None, on_delete=models.CASCADE, verbose_name="cor4")
    cor5 = models.ForeignKey(Cor5Type, to_field="cor5_type", null=True, blank=True, default=None, on_delete=models.CASCADE, verbose_name="cor5")
    cor6 = models.ForeignKey(Cor6Type, to_field="cor6_type", null=True, blank=True, default=None, on_delete=models.CASCADE, verbose_name="cor6")
    cor7 = models.ForeignKey(Cor7Type, to_field="cor7_type", null=True, blank=True, default=None, on_delete=models.CASCADE, verbose_name="cor7")
    cor8 = models.ForeignKey(Cor8Type, to_field="cor8_type", null=True, blank=True, default=None, on_delete=models.CASCADE, verbose_name="cor8")
    cor9 = models.ForeignKey(Cor9Type, to_field="cor9_type", null=True, blank=True, default=None, on_delete=models.CASCADE, verbose_name="cor9")
    cor10 = models.ForeignKey(Cor10Type, to_field="cor10_type", null=True, blank=True, default=None, on_delete=models.CASCADE, verbose_name="cor10")
    cor11 = models.ForeignKey(Cor11Type, to_field="cor11_type", null=True, blank=True, default=None, on_delete=models.CASCADE, verbose_name="cor11")
    notes = models.CharField(max_length=225, null=True, blank=True, verbose_name="Notes")

    def get_absolute27_url(self):
        return f"/egfdatabase/{self.evalueid}/evalue/"

    def get_absolute28_url(self):
        return f"/egfdatabase/{self.gunid}/guninfo/evalueprev/"
