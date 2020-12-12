import scipy.integrate #미분방정식
import numpy #다차원배열
import matplotlib.pyplot as pyplot # 그래프


# S = 감염가능 I = 감염자 R =면역,회복 
def SIR_model(y,t,beta,gamma):

    S,I,R = y

    # S가 줄어드니깐 기울기가 음수가 된다. (S,I에 비례)
    dS_dt = -beta*S*I #(s의 기울기설명)

    # I의 기울기가 증가하면 0보다 클때 , 기울기가 감소하면 0보다 작을때
    dI_dt = beta*S*I - gamma*I #(I의 기울기 설명)

    #회복자이므로 감염자에 회복
    dR_dt = gamma*I #(R의 기울기 설명)

    return([dS_dt,dI_dt,dR_dt])
    
S0 = 0.9 #최초감염자
I0 = 0.1
R0 = 0.0 #기초재생산지수
beta =0.35 #전파율 
gamma = 0.1 #회복율


t= numpy.linspace(0,100,10000) #linspace(시작,끝값,사이간격) 0~100사이의 간격은 10000으로 각각의 요소를 만들어준다.
solution = scipy.integrate.odeint(SIR_model,[S0,I0,R0],t,args=(beta,gamma)) #odeint는 수치적분을 하기위한 함수, 함수의 인수는 (함수,초기값,시간) 
solution = numpy.array(solution) # solution배열 만들기

#그래프 출력

plt.plot(t,solution[:,0],label="S(t)")
plt.plot(t,solution[:,1],label="I(t)")
plt.plot(t,solution[:,2],label="R(t)")
plt.show()
