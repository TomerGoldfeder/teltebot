import tensorflow as tf
import matplotlib.pyplot as plt
import datetime
import traceback

fig_format = "{}/{}.png"


class TelegramNotifier(tf.keras.callbacks.Callback):
    def __init__(self, bot, result_dir, include_run_notification=False, metrics=['accuracy'], include_images=False):
        super(TelegramNotifier, self).__init__()
        self.bot = bot
        self.metrics = {x: [] for x in metrics}
        self.result_dir = result_dir
        self.include_run_notification = include_run_notification
        self.start_training = None
        self.end_training = None
        self.include_images = include_images

    def on_train_begin(self, logs=None):
        self.start_training = datetime.datetime.now()
        self.bot.send_message("Training Started...")

    def on_epoch_end(self, epoch, logs=None):
        if self.include_run_notification:
            message = "Epoch {} - Acc: {:.4f}, Loss: {:.4f}".format(epoch, logs['accuracy'], logs['loss'])
            self.bot.send_message(message)
        for metric in self.metrics:
            self.metrics[metric].append(logs[metric])

    def send_images(self, images):
        if not self.include_images:
            return
        for image in images:
            self.bot.send_image(fig_format.format(self.result_dir, image))

    def send_notification(self, message):
        self.bot.send_message(message)
        self.send_images(self.metrics)

    def save_png(self, title, data, fname):
        plt.plot(data)
        plt.title(title)
        plt.xlabel("Epoch")
        plt.ylabel(fname.capitalize())
        plt.savefig(fig_format.format(self.result_dir, fname))

    def save_metric_png(self):
        for metric in self.metrics:
            self.save_png(title="{}: {:.4f}".format(metric.capitalize(), self.metrics[metric][-1]), fname=metric, data=self.metrics[metric])

    def prepare_message(self):
        message = "Finished Training Model\n"
        message += "Training Duration: {:.3f} seconds\n\n".format((self.end_training - self.start_training).total_seconds())
        for metric in self.metrics:
            message += "{}: {:.4f}\n".format(metric.capitalize(), self.metrics[metric][-1])
        return message

    def on_train_end(self, logs=None):
        self.end_training = datetime.datetime.now()
        try:
            message = self.prepare_message()
            self.save_metric_png()
            self.send_notification(message)
        except:
            self.bot.send_message(traceback.format_exc())
