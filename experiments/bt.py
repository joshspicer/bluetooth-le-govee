from time import sleep
from bleson import get_provider, Observer

def on_advertisement(advertisement):
   print(advertisement)

adapter = get_provider().get_adapter()

observer = Observer(adapter)
observer.on_advertising_data = on_advertisement

observer.start()
sleep(2)
observer.stop()