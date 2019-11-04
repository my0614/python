# keras

케라스는 파이썬으로 작성된 오픈 소스 신경망 라이브러리이다.
개발절차  
1.데이터 준비
2. model 설게
3. Loss 및 optimizer 설정
4. fitting(학습)
5. predict(모델검증)

## 선형회귀

☆집가격 상승하기

```
from keras.models import Sequential
from keras.layers import Dense
from sklearn.model_selection import train_test_split

import numpy as np
import keras.optimizers as optimizers
import pandas as pd
import tensorflow as tf
import matplotlib.pyplot as plt

seed = 0
np.random.seed(seed)
tf.set_random_seed(seed)

df = pd.read_csv("C:/Users/user/Desktop/dataset/housing.csv", delim_whitespace = True, header=None)

dataset = df.values
x = dataset[:,0:13]
y = dataset[:,13]
x_train,x_test,y_train,y_test= train_test_split(x,y,test_size=0.3, random_state=seed)
                                                
model = Sequential()
model.add(Dense(30,input_dim=13, activation='relu'))
model.add(Dense(6, activation = 'relu'))
model.add(Dense(1))
model.summary()
model.compile(loss='mse',optimizer='adam')
model.fit(x_train,y_train, epochs=200, batch_size =10)

y_prediction = model.predict(x_test).flatten()
for i in range(10):
    label = y_test[i]
    prediction = y_prediction[i]
    print("실제가격 : {:.3f}, 예상가격 : {:.3f}".format(label,prediction))

    import matplotlib.pyplot as plt
plt.plot(y_test,'b')
plt.plot(y_prediction,'r')
plt.show()
```

## 로지스틱 회귀의 정의
-> 시그모이드 함수 사용하기!!
ax + b 라는 식으로 하는데, a가 클수록 오차가 커진다. 또한 b에 따라서 기울기가 달라진다. 
★시그모이드 함수 방정식  

y = 1/(1+np.e**(a*x_data +b))

```
import tensorflow as tf
import numpy as np

data = [[2,0],[4,0],[6,0],[8,1],[10,1],[12,1],[14,1]]
x_data = [x_row[0] for x_row in data]
y_data = [y_row[1] for y_row in data]

a = tf.Variable(tf.random_normal([1],dtype=tf.float64, seed=0))
b = tf.Variable(tf.random_normal([1],dtype=tf.float64, seed=0))

y = 1/(1+np.e**(a*x_data +b))
# loss 를 구하는 함수
loss = -tf.reduce_mean(np.array(y_data)* tf.log(y) +(1-np.array(y_data)) * tf.log(1-y))
# 학습률 값
learning_rate = 0.5
# loss 를 최소로 하는 값 찾기
gradient_decent = tf.train.GradientDescentOptimizer(learning_rate).minimize(loss)
# 학습
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for i in range(60001):
        sess.run(gradient_decent)
        if i % 6000 == 0:
            print("Epoch: %.f,loss = %.4f,기울기 = %.4f, y절편 = %.4f" % (i,sess.run(loss),sess.run(a),sess.run(b)))
```

☆예측하기 생존률 확률
```
from keras.models import Sequential
from keras.layers import Dense

import numpy as np
import tensorflow as tf

seed = 0
np.random.seed(seed)
tf.set_random_seed(seed)

Data_set = np.loadtxt("C:/Users/user/Desktop/dataset/ThoraricSurgery.csv",delimiter=",")

x = Data_set[:,0:17]
y = Data_set[:,17]

model = Sequential()
model.add(Dense(30,input_dim= 17, activation = 'relu'))
model.add(Dense(1,activation='sigmoid'))
model.compile(loss = 'mse',optimizer='adam',metrics=['accuracy'])
model.fit(x,y,epochs = 30, batch_size = 10)
print("\n accurapy : %.4f" %(model.evaluate(x,y)[0] *100))
```
