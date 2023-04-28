import matplotlib.pyplot as plt
import numpy as np

#-------------------////////////-----------------
#-------------------///график///-----------------
#-------------------/генерация//-----------------
#-------------------////////////-----------------

# два метода для генерации 100 чисел и их гистограммы
def gauss_array(): 
    import random
    a = []
    for i in range(100):
        a.append(random.gauss(4.97, 0.05))
    print(a)
    with open ('f.txt','w') as file:
        for i in range(100):
            a[i] = round(a[i],2)
            file.write(str(a[i]) + '\n')

def histog():
    a_fig = []
    f = open('f.txt')
    for i in range(100):
        a_fig.append(float(f.readline()))
    fig = plt.figure(figsize=(10, 4))
    ax = plt.subplot()
    ax.hist(a_fig, 10, (4.85, 5.12),color= 'pink', ec = 'blue')
    ax.grid()
    plt.show()

#gauss_array()    
#histog()

#-------------------////////////-----------------
#-------------------/вычисления/-----------------
#-------------------////////////-----------------

def sr(): # среднее значения для 100 символов________она вспомогательная, отдельно вызывать не надо
    f = open('f.txt')
    c = 0
    for i in range(100):
        c += float(f.readline())
    sr_ar = ((c/100))
    return sr_ar

    

def sr_otkl(): # записывает в новый файл второй столбец первой таблицы
    f_r = open('f_a.txt','w')
    f_w = open('f.txt','r')
    c = 0
    print(sr())
    for i in range(100):
        a = float(f_w.readline())
        f_r.write(str((a - sr()))[:7] + '\n') 
        # 3 столбец не всегда корректно считает 
        # разбираться мне лень, так что делай сам
              


def ras_prom():
    # используется для 3 таблицы 1 и 2 столбца 
    prom = [4.84,4.877,4.904,4.931,4.958,4.985,5.012,5.039,5.066,5.093,5.12] # промежутки
    vhoz = [0]* 10 # количество вхождений в промежуток
    sr_sum = [0]* 10 # сумма значений вхождений
    delta_n = [] # для 3 таблицы 2 столбец
    a = []
    f = open('f.txt')
    for i in range(100):
        a.append(float(f.readline()))
    for row in range(10):
        for chis in a:
            if chis > prom[row] and chis <= prom[row + 1]:
                vhoz[row] += 1
                sr_sum[row] += chis
    for i in range(10):
        del_n = vhoz[i]
        del_t = (5.12 - 4.85) / 10
        delta_n.append(round((del_n / (100 * del_t)),3))
    
    print(vhoz,delta_n) # 1 и 2 столбцы 3 таблицы 
    

def sigma(sr_arifm):# на вход получает функцию sr
    # находит выборочное среднеквадратичное отклонение и макс знач плотности распределения
    f = open('f.txt')
    p = [] # массив ро
    c = 0
    for i in range(100):
        a = float(f.readline())
        c += (a - sr_arifm) ** 2
    sigma_n = (c / 99) ** 0.5
    p_max = 1/(round(sigma_n,2) * (2*np.pi)**0.5)
    for i in range(10): # считает р, для второй таблицы
        p.append(round((1/(0.06 * (2*np.pi) ** 0.5)) \
            * np.exp(-((sr() - (4.877 + i*0.027))**2)/(2*0.06**2)),4)) # сюда ваши значения вставить из формулы
    #print(sigma_n,p_max,p) # закомментить строчку, когда нужны резы для 2 таблицы
    # 2 значения для 3 столбца из 1 таблицы 
    # и массив для последней таблицы последнего столбца
    return sigma_n # для 3 таблицы
   

def table2():
    f = open('f.txt','r')
    f_arr = []
    for i in range(100):
        f_arr.append(float(f.readline()))
    vhoz = [0] * 3 # 3 столбец 2 таблицы промежуточное
    for i in range(3):
        sigma_new = i*sigma(sr()) + sigma(sr())
        sigma_plus =round( sr() + sigma_new,2)
        sigma_minus = round(sr() - sigma_new,2)
        for j in range(100):
            if f_arr[j] >= sigma_minus and f_arr[j] <= sigma_plus:
                vhoz[i] += 1 
        print(sigma_minus,sigma_plus, vhoz[i]) # 1,2,3 столбцы таблицы 2
            
        
    
# sigma(sr())
# sr_otkl()
# ras_prom() 
# table2()

