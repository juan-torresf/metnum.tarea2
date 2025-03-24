from time import sleep
from os import name,system
from rich.live import Live
from rich.table import Table
from rich.console import Console
from metnum import biseccion,punto_fijo,newton_raphson,secante,seccion_aurea,t,f,df,d2f

system('cls' if name == 'nt' else 'clear')

metodos = {
    'bisección':('bisección (.5,1)',biseccion,[.5,1]),
    'punto fijo':('punto fijo .5',punto_fijo,.5),
    'newton-raphson':('newton-raphson .5',newton_raphson,.5),
    'secante':('secante (.5,1)',secante,[.5,1]),
    'sección áurea':('sección áurea (.5,1)',seccion_aurea,[.5,1])}

def tablazo(metodo):

    if(metodo not in metodos):
        print('método no valido')
        sleep(1)
        system('cls' if name == 'nt' else 'clear')
        return

    global t

    print('\n')

    table = Table(title=metodos[metodo][0])
    table.add_column('i',justify='right')
    table.add_column('i≤m',justify='center')
    table.add_column('aproximación',justify='left')
    table.add_column('convergencia',justify='center')

    metodos[metodo][1](list(metodos[metodo][2]) if isinstance(metodos[metodo][2],list) else metodos[metodo][2])

    with Live(table,console=Console()):

        for i in range(t[-1][0]+1):
            table.add_row(str(t[i][0]),"✓" if t[i][1] else "✗",f'{round(t[i][2],10)}'.lstrip('0'),f"{(_ := f'{t[i][3]:.10e}'.split('e')[0].rstrip('0').rstrip('.'))}×10{str(int(f'{t[i][3]:.10e}'.split('e')[1])).translate(str.maketrans('0123456789-', '⁰¹²³⁴⁵⁶⁷⁸⁹⁻'))}")
            sleep(.2)

    print('\n')
    
    h = str(t[-1][2])

    analyze = Table(title=metodos[metodo][0])
    analyze.add_column('punto',justify='center')
    analyze.add_column('f(x)≈',justify='center')
    analyze.add_column("f'(x)≈",justify='center')
    analyze.add_column("f''(x)≈",justify='center')
    analyze.add_row('x','mínimo' if df(newton_raphson(.5,ε=0) if df(t[-1][2])-df(newton_raphson(.5,ε=0))<=1e-6 else t[-1][2])==0 and d2f(newton_raphson(.5,ε=0) if df(t[-1][2])-df(newton_raphson(.5,ε=0))<=1e-6 else t[-1][2])>0 else ('máximo' if df(newton_raphson(.5,ε=0) if df(t[-1][2])-df(newton_raphson(.5,ε=0))<=1e-6 else t[-1][2])==0 and d2f(newton_raphson(.5,ε=0) if df(t[-1][2])-df(newton_raphson(.5,ε=0))<=1e-6 else t[-1][2])<0 else 'punto'),'punto crítico' if df(newton_raphson(.5,ε=0) if df(t[-1][2])-df(newton_raphson(.5,ε=0))<=1e-6 else t[-1][2])==0 else 'punto','convexo' if d2f(newton_raphson(.5,ε=0) if df(t[-1][2])-df(newton_raphson(.5,ε=0))<=1e-6 else t[-1][2])>0 else 'cóncavo')
    analyze.add_row(h,str(f(newton_raphson(.5,ε=0) if df(t[-1][2])-df(newton_raphson(.5,ε=0))<=1e-6 else t[-1][2])),str(df(newton_raphson(.5,ε=0) if df(t[-1][2])-df(newton_raphson(.5,ε=0))<=1e-6 else t[-1][2])),str(d2f(newton_raphson(.5,ε=0) if df(t[-1][2])-df(newton_raphson(.5,ε=0))<=1e-6 else t[-1][2])))
    
    Console().print(analyze)
    t.clear()

def tabla():

    global t

    print('\n')

    p = Table(title='punto mínimo')
    p.add_column('i',justify='center')
    p.add_column('bisección',justify='center')
    p.add_column('punto fijo',justify='center')
    p.add_column('newton-raphson',justify='center')
    p.add_column('secante',justify='center')
    p.add_column('sección áurea',justify='center')

    m = [[] for _ in range(5)] 

    for index,metodo in enumerate([biseccion,punto_fijo,newton_raphson,secante,seccion_aurea]):
        metodo([.5,1] if index!=1 and index!=2 else .5)
        for i in range(t[-1][0]+1):
            m[index].append(t[i][2])
        t.clear()

    for i in range(max(len(metodo) for metodo in m)):
        row = [str(i)]
        for metodo in m:
            row.append(str(metodo[i]) if i < len(metodo) else '') 
        p.add_row(*row)

    Console().print(p)
    print('\n')

while 1:
    while 1:
        try:
            if(bool(int(input('1:métodos,0:método: ')))):
                tabla()
                break
            else:
                system('cls' if name == 'nt' else 'clear')
                print('métodos\n')
                tablazo(input('bisección, punto fijo, newton-raphson, secante o sección áurea: '))
                break
        except ValueError:
            system('cls' if name == 'nt' else 'clear')
    while 1:
        try:
            if(not bool(int(input('1:continuar,0:terminar: ')))):
                system('cls' if name == 'nt' else 'clear')
                exit()
            system('cls' if name == 'nt' else 'clear')
            break
        except ValueError:
            system('cls' if name == 'nt' else 'clear')