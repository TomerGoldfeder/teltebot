import tensorflow as tf
from TelegramCallback import TelegramNotifier
from TelegramNotifierBot import TelegramBot
import os
import traceback


bot = TelegramBot(user_id=os.environ['USER_ID'], token=os.environ['TELE'])
result_dir = "."
user_data = {
    "bot": bot,
    "metrics": ['accuracy', 'mean_squared_error'],
    "result_dir": result_dir,
    "include_run_notification": True,
    "include_images": True
}

(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()
x_train = x_train.reshape(-1, 784).astype("float32") / 255.0
x_test = x_test.reshape(-1, 784).astype("float32") / 255.0

x_train = x_train[:1000]
y_train = y_train[:1000]
x_test = x_test[:1000]
y_test = y_test[:1000]


model = tf.keras.Sequential()
model.add(tf.keras.layers.Dense(1, input_dim=784))
model.compile(
    optimizer=tf.keras.optimizers.RMSprop(learning_rate=0.1),
    loss="mean_squared_error",
    metrics=user_data['metrics'],
)

#################################################################################
# with training updates and images
#################################################################################
try:
    model.fit(
        x_train,
        y_train,
        batch_size=128,
        epochs=3,
        verbose=0,
        validation_split=0.5,
        callbacks=[TelegramNotifier(**user_data)],
    )
except:
    print(traceback.format_exc())
    bot.send_message(traceback.format_exc())

#################################################################################
# without notifications during training and with images
#################################################################################
del user_data['include_run_notification']
try:
    model.fit(
        x_train,
        y_train,
        batch_size=128,
        epochs=3,
        verbose=0,
        validation_split=0.5,
        callbacks=[TelegramNotifier(**user_data)],
    )
except:
    print(traceback.format_exc())
    bot.send_message(traceback.format_exc())



#################################################################################
# without notifications or images
#################################################################################
del user_data['include_images']
try:
    model.fit(
        x_train,
        y_train,
        batch_size=128,
        epochs=3,
        verbose=0,
        validation_split=0.5,
        callbacks=[TelegramNotifier(**user_data)],
    )
except:
    print(traceback.format_exc())
    bot.send_message(traceback.format_exc())

