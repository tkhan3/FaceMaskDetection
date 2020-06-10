import os
import cv2
from PIL.ImageOps import grayscale
from watchdog.events import RegexMatchingEventHandler
import TelegramBot
import sys
import time
from watchdog.observers import Observer

class ImagesEventHandler(RegexMatchingEventHandler):
    THUMBNAIL_SIZE = (128, 128)
    IMAGES_REGEX = [r".*[^_thumbnail]\.jpg$"]

    def __init__(self):
        super().__init__(self.IMAGES_REGEX)

    def on_created(self, event):
        self.process(event)

    def process(self, event):
        filename, ext = os.path.splitext(event.src_path)
        filename = f"{filename}_thumbnail.jpg"

        #image = Image.open(event.src_path)
        image = cv2.imread(event.src_path)
        #image = grayscale(image)
        #image.thumbnail(self.THUMBNAIL_SIZE)
        TelegramBot.send_violation_text()

class ImagesWatcher:
    def __init__(self, src_path):
        self.__src_path = src_path
        self.__event_handler = ImagesEventHandler()
        self.__event_observer = Observer()

    def run(self):
        self.start()
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            self.stop()

    def start(self):
        self.__schedule()
        self.__event_observer.start()

    def stop(self):
        self.__event_observer.stop()
        self.__event_observer.join()

    def __schedule(self):
        self.__event_observer.schedule(
            self.__event_handler,
            self.__src_path,
            recursive=True
        )

if __name__ == "__main__":
    src_path = "C:\\tanveer\\images\\"
    ImagesWatcher(src_path).run()