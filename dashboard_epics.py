import epics
from time import sleep
from nslsii.utils import open_redis_client

import configparser
profile_configuration = configparser.ConfigParser(interpolation=None)
profile_configuration.read_file(open('epicsconfig.ini'))
pc = profile_configuration

import redis
#redis_host = 'xf06bm-ioc2'
#rkvs = redis.Redis(host=redis_host, port=6379, db=0)
redis_host = profile_configuration.get('services', 'nsls2_redis')
redis_port = profile_configuration.get('services', 'redis_port')
redis_ssl  = profile_configuration.get('services', 'redis_ssl')
redis_db   = profile_configuration.get('services', 'bmm_redis')
rkvs = open_redis_client(redis_host, redis_port, redis_ssl, redis_db=redis_db)

maintenance = False
try:
    if 'main' in sys.argv[1].lower():
        maintenance = True
except:
    pass




## ----- various PVs and other scalars
i0     = epics.PV(pc.get('pvs', 'i0'))
it     = epics.PV(pc.get('pvs', 'it'))
if rkvs.get('BMM:Ir').decode('utf-8') == 'quadem':
    ir = epics.PV(pc.get('pvs', 'ir_ic'))
else:
    ir = epics.PV(pc.get('pvs', 'ir_quadem'))
iy     = epics.PV(pc.get('pvs', 'iy'))
#bicron       = epics.PV(pc.get('pvs', 'bicron'))
ring_current = epics.PV(pc.get('pvs', 'ring_current'))
sleep(0.25)
ring_connected = ring_current.connect()

if maintenance is False:
    bl           = epics.PV(pc.get('pvs', 'bl'))
    bmps         = epics.PV(pc.get('pvs', 'bmps'))
    sha          = epics.PV(pc.get('pvs', 'sha'))
    shb          = epics.PV(pc.get('pvs', 'shb'))

bragg        = epics.Motor(pc.get('motors', 'bragg'))
dcmx         = epics.Motor(pc.get('motors', 'dcmx'))
sample       = {'x'     : epics.Motor(pc.get('motors', 'sample_x')),
                'y'     : epics.Motor(pc.get('motors', 'sample_y')),
                'wheel' : epics.Motor(pc.get('motors', 'sample_wheel')),
                'garot' : epics.Motor(pc.get('motors', 'sample_garot')),
                'pitch' : epics.Motor(pc.get('motors', 'sample_pitch')),
                'ref'   : epics.Motor(pc.get('motors', 'sample_ref')),
                'refx'  : epics.Motor(pc.get('motors', 'sample_refx')),
                'det'   : epics.Motor(pc.get('motors', 'sample_det')),
}
vac          = [epics.PV(pc.get('pvs', 'vac0')),
                epics.PV(pc.get('pvs', 'vac1')),
                epics.PV(pc.get('pvs', 'vac2')),
                epics.PV(pc.get('pvs', 'vac3')),
                epics.PV(pc.get('pvs', 'vac4')),
                epics.PV(pc.get('pvs', 'vac5')),
                epics.PV(pc.get('pvs', 'vac6'))]

temperatures = [epics.PV(pc.get('pvs', 't0')),
                epics.PV(pc.get('pvs', 't1')),
                epics.PV(pc.get('pvs', 't2')),
                epics.PV(pc.get('pvs', 't3')),
                epics.PV(pc.get('pvs', 't4')),
                epics.PV(pc.get('pvs', 't5')),
                epics.PV(pc.get('pvs', 't6')),
                epics.PV(pc.get('pvs', 't7')),
                epics.PV(pc.get('pvs', 't8')),
                epics.PV(pc.get('pvs', 't9')),
                epics.PV(pc.get('pvs', 't10')),]

rackA1 = epics.PV(pc.get('pvs', 'rackA1'))
rackB1 = epics.PV(pc.get('pvs', 'rackB1'))
rackC1 = epics.PV(pc.get('pvs', 'rackC1'))
rackC2 = epics.PV(pc.get('pvs', 'rackC2'))
rackC3 = epics.PV(pc.get('pvs', 'rackC3'))

if maintenance is False:
    fe_valves    = [epics.PV(pc.get('pvs', 'fev0')),
                    epics.PV(pc.get('pvs', 'fev1')),
                    epics.PV(pc.get('pvs', 'fev2')),]
valves       = [epics.PV(pc.get('pvs', 'v0')),
                epics.PV(pc.get('pvs', 'v1')),
                epics.PV(pc.get('pvs', 'v2')),
                epics.PV(pc.get('pvs', 'v3')),
                epics.PV(pc.get('pvs', 'v4')),
                epics.PV(pc.get('pvs', 'v5')), ]
ln2 = epics.PV(pc.get('pvs', 'ln2'))
dia = epics.PV(pc.get('pvs', 'dia'))
dib = epics.PV(pc.get('pvs', 'dib'))

try:
    delta         = epics.Motor(pc.get('motors', 'delta'))
    eta           = epics.Motor(pc.get('motors', 'eta'))
    chi           = epics.Motor(pc.get('motors', 'chi'))
    phi           = epics.Motor(pc.get('motors', 'phi'))
    mu            = epics.Motor(pc.get('motors', 'mu'))
    nu            = epics.Motor(pc.get('motors', 'nu'))
except:
    delta = None
    eta = None
    chi = None
    phi = None
    mu = None
    nu = None
    
slits         = [epics.Motor(pc.get('motors', 'slits_o')),
                 epics.Motor(pc.get('motors', 'slits_i')),
                 epics.Motor(pc.get('motors', 'slits_t')),
                 epics.Motor(pc.get('motors', 'slits_b'))]

try:
    linkam = epics.PV(pc.get('pvs', 'linkam'))
except:
    linkam = None
try:
    lakeshore = epics.PV(pc.get('pvs', 'lakeshore'))
except:
    lakeshore = None

