import re
import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols,exp,diff,lambdify,latex,Rational,solve,factor,sympify

x,y = symbols('x y')
f = Rational(1,2)*x**3+exp(-x)
df = diff(f,x)
d2f = diff(df,x)

xdf = sympify(f'sqrt({factor(solve(df.subs(exp(x),exp(y)),x)[1].subs(exp(y),exp(x))**2)})',evaluate=False)

fx = lambdify(x,f,'numpy')
dfx = lambdify(x,df,'numpy')
d2fx = lambdify(x,d2f,'numpy')

xdfx = lambdify(x,xdf,'numpy') #solve(df)[1].evalf() = 2*LambertW(sqrt(6)/6) = 0.603744212350924

def frac_latex(match):
        
        num = match.group(1)
        den = match.group(2)
        
        if(' ' in num):
            return r'\frac{'+num.split(' ',1)[0]+'}{'+den+r'} '+num.split(' ',1)[1]
        if(num.isdigit()):
            return r'\frac{'+num+'}{'+den+'}'
        else:
            return r'\frac{1}{'+den+'}'+num

f = re.sub(r'\\frac{(.*?)}{(.*?)}',frac_latex,latex(f,mode='inline',fold_short_frac=False))
df = re.sub(r'\\frac{(.*?)}{(.*?)}',frac_latex,latex(df,mode='inline',fold_short_frac=False))
d2f = re.sub(r'\\frac{(.*?)}{(.*?)}',frac_latex,latex(d2f,mode='inline',fold_short_frac=False))

xdf = re.sub(r'\\frac{(.*?)}{(.*?)}',frac_latex,latex(xdf,mode='inline',fold_short_frac=False))

y = [fx(np.linspace(-3,3,400)),dfx(np.linspace(-3,3,400)),d2fx(np.linspace(-3,3,400))]

fig,ax = plt.subplots(figsize=(10,6))
ax.plot(np.linspace(-3,3,400),y[0],linestyle='solid',linewidth=3,label=fr"f(x) = {f}",color='red')
ax.plot(np.linspace(-3,3,400),y[1],linestyle='solid',linewidth=3,label=f"f'(x) = {df}",color='green')
ax.plot(np.linspace(-3,3,400),y[2],linestyle='solid',linewidth=3,label=f"f''(x) = {d2f}",color='blue')

ax.plot(np.linspace(-3,3,400),y[2],linestyle='solid',linewidth=2,label=f'g(x) = {xdf}',color='black')

ax.axhline(0,color='black',linestyle='solid',linewidth=1)
ax.axvline(0,color='black',linestyle='solid',linewidth=1)

ax.set_xlim(-2.5,2.5)
ax.set_ylim(-2,5)

ax.set_xlabel('x',fontsize=20)
ax.set_ylabel('y',fontsize=20,rotation=0)

ax.yaxis.set_label_coords(-0.08,0.25)

ax.set_title("f(x),f'(x) y f''(x)")
ax.legend()
ax.grid(True)

plt.show()
