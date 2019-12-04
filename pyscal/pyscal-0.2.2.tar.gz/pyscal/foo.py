import pyscal
wo = pyscal.WaterOil(h=0.01, swl=0.1, sorw=0.04)
wo.add_corey_oil()
wo.add_corey_water()
print(wo.SWOF())

