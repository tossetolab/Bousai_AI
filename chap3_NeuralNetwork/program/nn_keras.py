import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.optimizers import SGD

# トレーニングデータ
# XOR
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
Y = np.array([[0], [1], [1], [0]])

# モデル設定
model = Sequential()

# 入力層 - 隠れ層
model.add(Dense(input_dim=2, units=2))
model.add(Activation('sigmoid'))

# 隠れ層 - 出力層
model.add(Dense(units=1))
model.add(Activation('linear'))

model.compile(loss='mean_squared_error', optimizer=SGD(lr=0.1))

# モデル学習
model.fit(X, Y, epochs=4000, batch_size=4)

# 学習結果の確認
print(model.predict(X, batch_size=4))
