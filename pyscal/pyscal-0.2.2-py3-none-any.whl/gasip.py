from pyscal import *
import matplotlib.pyplot as plt
import copy

go0 = GasOil(sorg=0.5)
go1 = GasOil(sorg=0.2)
go0.add_corey_gas(ng=2, krgend=0.9)
go1.add_corey_gas(ng=2, krgend=0.8)
go0.add_corey_oil(nog=2)
go1.add_corey_oil(nog=2)
ip = GasOil()
utils.interpolator(
    ip, copy.deepcopy(go0), copy.deepcopy(go1), 0.5, sat="sg", kr1="krg", kr2="krog"
)
(fig, ax) = plt.subplots()
go0.plotkrgkrog(ax=ax, color="blue")
go1.plotkrgkrog(ax=ax, color="red")
ip.plotkrgkrog(ax=ax, color="green")
plt.show()
