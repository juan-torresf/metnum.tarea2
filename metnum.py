from tarea2 import np,fx as f,dfx as df,d2fx as d2f,xdfx as xdf

t = []

def biseccion(a,m=52,ε=1e-6,df=df):

    global t

    i = 0

    while(i<=m):

        t.append((i,i<=m,((a[0]+a[1])/2),(abs(a[1]-a[0]))/2))

        if(((df((a[0]+a[1])/2))==0)or((abs(a[1]-a[0]))/2<ε)):
            return (a[0]+a[1])/2
        elif(np.sign(df((a[0]+a[1])/2))==np.sign(df(a[0]))):
            a[0] = (a[0]+a[1])/2
        else:
            a[1] = (a[0]+a[1])/2

        i += 1

    t.append((i,i<=m,((a[0]+a[1])/2),(abs(a[1]-a[0]))/2))
    print('máximas iteraciones excedidas') #18
    return (a[0]+a[1])/2

def punto_fijo(x,m=31,ε=1e-6,xdf=xdf):

    global t

    i = 0

    while(i<=m):

        t.append((i,i<=m,xdf(x),abs(xdf(x)-x)))

        if(abs(xdf(x)-x)<ε):
            return xdf(x)
        
        x = xdf(x)
        i += 1

    t.append((i,i<=m,xdf(x),abs(xdf(x)-x)))
    print('máximas iteraciones excedidas') #10
    return x

def newton_raphson(x,m=4,ε=1e-6,df=df,d2f=d2f):

    global t

    i = 0

    while(i<=m):

        t.append((i,i<=m,x-df(x)/d2f(x),abs(df(x)/d2f(x))))

        if(abs(df(x)/d2f(x))<ε):
            return x-df(x)/d2f(x)

        x = x-df(x)/d2f(x)

        i += 1

    t.append((i,i<=m,x-df(x)/d2f(x),abs(df(x)/d2f(x))))
    #print('máximas iteraciones excedidas') #3
    return x-df(x)/d2f(x)

def secante(a,m=7,ε=1e-6,df=df):

    global t

    i = 0

    while(i<=m):

        t.append((i,i<=m,a[1]-(df(a[1])*(a[1]-a[0]))/(df(a[1])-df(a[0])),abs((df(a[1])*(a[1]-a[0]))/(df(a[1])-df(a[0])))))

        if(abs((df(a[1])*(a[1]-a[0]))/(df(a[1])-df(a[0])))<ε):
            return a[1]-(df(a[1])*(a[1]-a[0]))/(df(a[1])-df(a[0]))

        a = [a[1],(a[1]-(df(a[1])*(a[1]-a[0]))/(df(a[1])-df(a[0])))]

        i += 1

    t.append((i,i<=m,a[1]-(df(a[1])*(a[1]-a[0]))/(df(a[1])-df(a[0])),abs((df(a[1])*(a[1]-a[0]))/(df(a[1])-df(a[0])))))
    print('máximas iteraciones excedidas') #4
    return a[1]-(df(a[1])*(a[1]-a[0]))/(df(a[1])-df(a[0]))

def seccion_aurea(a,m=76,ε=1e-6,f=f):

    global t

    i = 0

    φ = (5**0.5-1)/2

    x1 = a[1]-φ*(a[1]-a[0])
    x2 = a[0]+φ*(a[1]-a[0])

    while(i<=m):

        t.append((i,i<=m,(a[0]+a[1])/2,a[1]-a[0]))

        if(a[1]-a[0]<ε):
            return (a[0]+a[1])/2
        
        if(f(x1)<f(x2)):
            
            a[1] = x2
            x2 = x1
            x1 = a[1]-φ*(a[1]-a[0])

        else:

            a[0] = x1
            x1 = x2
            x2 = a[0]+φ*(a[1]-a[0])

        i += 1
    t.append((i,i<=m,(a[0]+a[1])/2,a[1]-a[0]))
    print('máximas iteraciones excedidas') #28
    return (a[0]+a[1])/2
