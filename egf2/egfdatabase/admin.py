from django.contrib import admin


from .models import DuplicatingType, FittingTime, FittingStock, StockRefinishing, StockMod1, StockMod2,  StockMod3,StockRepairTime, StockRepairType, Checkering, Wood,\
    ProposalType, FinishType, RecoilPad, RecoilPadInfo, Materials, Labor, TaxRate, EyeType, HandType, LopType, DacType, Cor1Type, Cor2Type, Cor3Type, Cor4Type, Cor5Type,\
    Cor6Type, Cor7Type, Cor8Type, Cor9Type, Cor10Type, Cor11Type, DafType, DahType, DamcType, CastType, LotpType, ToeoutType, NewLopType, NewDacType, NewDafType, NewDahType,\
    NewDamcType, NewCastType, NewLotpType, NewToeoutType, NewHandType

# Register your models here.
admin.site.site_header = 'EGF Bidding Dashboard'
admin.site.register(DuplicatingType)
admin.site.register(FittingStock)
admin.site.register(FittingTime)
admin.site.register(StockRefinishing)
admin.site.register(FinishType)
admin.site.register(Labor)
admin.site.register(RecoilPad)
admin.site.register(Materials)
admin.site.register(TaxRate)
admin.site.register(StockRepairType)
admin.site.register(StockRepairTime)
admin.site.register(Wood)
admin.site.register(ProposalType)
admin.site.register(EyeType)
admin.site.register(HandType)
