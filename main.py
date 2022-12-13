import announcement_client
import edge_tts
import subprocess
import os

if not os.path.exists('device_name.conf'):
    open('device_name.conf', 'x').close()
    raise announcement_client.AnnouncementsError('Please set a device name in the device_name.conf file')

device_name_f = open('device_name.conf')

device_name = device_name_f.read().replace('\n', '')

device_name_f.close()

@announcement_client.announcement_callback
def callback(message, name):
    subprocess.Popen(['./edge_tts.sh', 'New announcement from {}, {}'.format(name, message)])

announcement_client.run_client(device_name)
