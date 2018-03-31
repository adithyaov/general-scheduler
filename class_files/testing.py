from PSRB import *

s = StaticVariables.sdata
d = StaticVariables.duration

for date in StaticVariables.tdata:
    absent_teacher_list = StaticVariables.tdata[date]
    a = PSRB(date, absent_teacher_list, s, d)
    ttable = a.create_graph()
    print date
    if type(ttable) != type('str'):
        print tabulate(ttable, headers=["X"]+range(StaticVariables.p_max), tablefmt='fancy_grid').encode('utf-8')
    else:
        print ttable