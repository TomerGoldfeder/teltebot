# Tensorflow Telegram Notifier Bot

Tensorflow Telegram Notifier is build using Tensorflow callback object.

  - Quick installation and easy to use
  - Option to select different metrics to send via bot
  - Option to include graph images of metrics

### Python Packages

The notifier uses a number of packages to work properly:

* Tensorflow - (tested on version: 2.3.0)
* Matplotlib - (tested on version: 3.3.1)
* Requests - (tested on version: 2.25.1)


### Installation
```sh
$ pip install teltebot
```
### Usage

You can use the notifier as a "free agent" or as a Tensorflow callback function.

To use the bot as a "free agent":
```sh
from TelegramNotifierBot import TelegramBot
import traceback

USER_ID = "your_bot_user_id"
TOKEN = "your_token_from_telegram"
bot = TelegramBot(user_id=USER_ID, token=TOKEN)

try:
    ...
    your code here
    ...

    bot.send_message("Test Message")
except:
    bot.send_message(traceback.format_exc()
```

Use as a Tensorflow callback function:
```sh
import tensorflow as tf
from TelegramCallback import TelegramNotifier
from TelegramNotifierBot import TelegramBot
import traceback

USER_ID = "your_bot_user_id"
TOKEN = "your_token_from_telegram"
bot = TelegramBot(user_id=USER_ID, token=TOKEN)

user_data = {
    "bot": bot,
    "metrics": ['accuracy', 'mean_squared_error'],
    "result_dir": "."
}

...

try:
    model.fit(
            x_train,y_train,
            batch_size=32,epochs=1,verbose=0,validation_split=0.3,
            callbacks=[TelegramNotifier(**user_data)],
        )
except:
    bot.send_message(traceback.format_exc()

```
You can include sending images at the end of the training and send metrics updates during training by adding to `user_data` setting the `include_images` argument and set it to `True`, and the `include_run_notification` to `True`:

```
user_data = {
    "bot": bot,
    "metrics": ['accuracy', 'mean_squared_error'],
    "result_dir": ".",
    "include_run_notification": True,
    "include_images": True
}
```
