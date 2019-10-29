# tensorflow

## palceholder (플레이스 홀더)
입력값ㅇ르 공급하기 위한 내장구조를 가진다.  
행에서는 none을 사용한다.

## variable (변수)
현재상태가 반복과정에서 상태에 영향을 준다.  
모델의 매개변수를 조정하는 역할을 한다.  메모리를 할당받는다.
이것은 프로그램이 자동조절을 한다. 


☆placeholder 사용하기
```
import tensorflow as tf

a = tf.placeholder(tf.int16)
b = tf.placeholder(tf.int16)
mul = tf.multiply(a,b)

x = list(range(1,10,1))
y = list(range(2,20,2))

with tf.Session() as sess:
    z = sess.run(mul, feed_dict = {a:x,b:y})
for x,y,z in zip(x,y,z):
    print(x,'*',y,'=' ,z)
    
```


☆Variable 사용하기
```
weights = tf.Variable(tf.random_normal([2,3],stddev = 1), name= 'weight')
biases = tf.Variable(tf.zeros([10], name = "biases"))

init = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init)
    print(sess.run(weights))
    print(sess.run(biases))
    
```

☆placeholder 와Variable 둘다 사용하기
```
import tensorflow as tf

x = tf.placeholder(tf.float32, [None, 3])
print(x)
x_data = [[1,2,3],[4,5,6]]

w = tf.Variable(tf.random_normal([3,2]))
b = tf.Variable(tf.random_normal([2,1]))

expr = tf.matmul(x,w) + b

sess= tf.Session()

sess.run(tf.global_variables_initializer())

print("=====x_data=====")
print(x_data)
print("===== w =====")
print(sess.run(w))
print("===== b =====")
print(sess.run(b))
print("====expr=====")

print(sess.run(expr, feed_dict = {x: x_data}))
sess.close()
    
```


☆Variable 사용하기
```
weights = tf.Variable(tf.random_normal([2,3],stddev = 1), name= 'weight')
biases = tf.Variable(tf.zeros([10], name = "biases"))

init = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init)
    print(sess.run(weights))
    print(sess.run(biases))
    
```

☆실제값과 예측값을 통해서 정확도 알아보기
```
   import tensorflow as tf
import numpy as np

x_data = np.array (([0,0],[1,0],[1,1],[0,0],[0,0,],[0,1]))

y_data =np.array([
    [1,0,0],
    [0,1,0],
    [0,0,1],
    [1,0,0],
    [1,0,0],
    [0,0,1]
])

x = tf.placeholder(tf.float32)
y = tf.placeholder(tf.float32)

w1 = tf.Variable(tf.random_uniform([2,10],-1,1))
w2 = tf.Variable(tf.random_uniform([10,3],-1,1))

b1 = tf.Variable(tf.zeros([10]))
b2 = tf.Variable(tf.zeros([3]))

l1 = tf.add(tf.matmul(x,w1),b1)
l1 = tf.nn.relu(l1)

model = tf.add(tf.matmul(l1,w2),b2)

cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits_v2(labels=y, logits=model))

opimizer = tf.train.AdamOptimizer(learning_rate = 0.01)
train = optimizer.minimize(cost)

init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)

for step in range(100):
    sess.run(train, feed_dict = {x:x_data, y:y_data})
    if (step + 1) % 10 == 0:
        print(step + 1 ,sess.run(cost, feed_dict = {x:x_data,y:y_data}))
        
prediction = tf.argmax(model,1)
target = tf.argmax(y,1)
print(sess.run(prediction, feed_dict = {x:x_data}))
print(sess.run(target, feed_dict = {y:y_data}))

is_correct = tf.equal(prediction, target)
accuracy = tf.reduce_mean(tf.cast(is_correct, tf.float32))
print("정확도 : %.2f" % sess.run(accuracy * 100, feed_dict = {x:x_data, y:y_data}))
 
```

-> 딥러닝을 하려면 선형회귀와 로지스틱회귀를 알아야 한다.  

선형회귀란? 
=> 예측선을 잘 알아야 한다.// 
더 많은 정보가 더 정확한 예측을 가능케 하고, 이때의 많은 정보가 곧 빅데이터이다. 즉 입력은 정보가 될수 있다. 
※x값에 따라 y 값이 달라진다. x가 독립변수이고 y가 종속변수이다. 
선형회귀란? 독립 변수를 사용해 종속변수의 움직임을 예측하고 설명하는 작업이다.  
1. 단순선형회귀 : 하나의 독립변수값으로도 종속변수를 구할수 있을때
2. 중복선형회귀 : 독립변수가 여러개 일때
 
최소제곱법을 사용하자!!

☆ 기울기 구하는 공식
```
divisor = sum([(mx - i)**2 for i in x])
def top(x,mx,y,my):
    d = 0
    for i in range(len(x)):
        d += (x[i]-mx) * (y[i] - my)
    return d
dividend = top(x,mx,y,my)

print("분모 : ",divisor)
print("분자 : ",dividend)

a = dividend / divisor
b = my - (mx*a)

print("기울기 a : ",a)
print("기울기 b : ",b)

```

☆ 평균 제곱근 오차 구하기
```


```
