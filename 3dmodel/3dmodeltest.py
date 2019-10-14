import ipyvolume
import ipyvolume as ipv
import vaex

ds = vaex.example()
N = 1000

ipv.figure()
quiver = ipv.scatter(ds.data.x[:N], ds.data.y[:N], ds.data.z[:N])
ipv.xyzlim(-30,30)
ipv.show()
