import numpy as np
import keras
from keras import layers
from keras import optimizers

# Створення моделі
model = keras.Sequential([
    layers.Dense(units=3, activation='linear',  input_shape=(2,)),
    layers.Dense(units=4, bias_initializer='ones', activation='softplus'),
    layers.Dense(units=1)
])

# Компіляція моделі
model.compile(optimizer=keras.optimizers.Adafactor(learning_rate=0.01),
              loss='mean_squared_error')

# Підготовка даних для тренування
# Приклад: множимо числа від 0 до 99
x = np.array([[i, j] for i in range(100) for j in range(100)])
y = np.prod(x, axis=1)

# Тренування моделі
model.fit(x, y, epochs=50)

# Перевірка результату
test_input = np.array([[5, 6]])
predicted = model.predict(test_input)
print(f"Результат множення {test_input[0][0]} на {test_input[0][1]}: {predicted[0][0]}")