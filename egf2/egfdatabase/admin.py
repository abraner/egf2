from django.contrib import admin


from .models import DuplicatingType, FittingTime, FittingStock, StockRefinishing, StockRepairTime, StockRepairType, Wood, ProposalType, FinishType, Materials, Labor, TaxRate, EyeType, HandType, RecoilPad

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
