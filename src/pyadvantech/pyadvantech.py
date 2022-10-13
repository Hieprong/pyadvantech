import matplotlib.pyplot as plt
import numpy as np
import matplotlib

import usb.core
import usb.util
import time
VENDOR_ID =0x1809
DEVICE_ID =0x4718

def set_channel_range(dev_handle,values):
    dev_handle.ctrl_transfer(0xc0, 127, 0x0001, 0, (0, 0, 0, 0))
    dev_handle.ctrl_transfer(0xc0, 127, 0x000a, 0, (0, 0, 0, 0))
    dev_handle.ctrl_transfer(0xc0, 127, 0x000c, 0, (0, 0, 0, 0))
    dev_handle.ctrl_transfer(0xc0, 127, 0x000b, 0, (0, 0, 0, 0))
    dev_handle.ctrl_transfer(0xc0, 127, 0x000d, 0, (0, 0, 0, 0))
    channels = [0,0x01,0x02,0x03,0x04,0x04,0x05,0x06,0x07]
    for i, value in enumerate(values):
        if value:
            try:
                dev_handle.ctrl_transfer(0x40, 2, 0x0006, 0,
                                            (0, channels[i], 0, 0x01, 00, value, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0))
            except:
                EnvironmentError("USB ERROR")
        else:
            ValueError("Value must have value between 0x00 and 0x07")


    dev_handle.ctrl_transfer(0x40,2,0x0040,0,(0x02,0x10,0,0,0,0x08))
    dev_handle.ctrl_transfer(0xc0, 2, 0x0041, 0,(tuple(0 for i in range(36))))
    dev_handle.ctrl_transfer(0x40, 2, 0x0040, 0, (0x02, 0x20, 0, 0, 0, 0x08))
    dev_handle.ctrl_transfer(0xc0, 2, 0x0041, 0, (tuple(0 for i in range(36))))
    dev_handle.ctrl_transfer(0x40, 1, 0x0001, 0, (0, 0, 0, 0x01, 0, 0,0,0))
    dev_handle.ctrl_transfer(0x40, 127, 0x0007, 0, (tuple(0 for i in range(4))))
    dev_handle.ctrl_transfer(0x40, 127, 0x0008, 0, (tuple(0 for i in range(4))))
    dev_handle.ctrl_transfer(0x40, 127, 0x0007, 0, (tuple(0 for i in range(4))))
    dev_handle.ctrl_transfer(0x40, 127, 0x0008, 0, (tuple(0 for i in range(4))))



def grab_values(dev_handle):
    dev_handle.ctrl_transfer(0x40, 127, 0x0007, 0, (0, 0, 0, 0))
    dev_handle.ctrl_transfer(0x40, 127, 0x0008, 0, (0, 0, 0, 0))
    dev_handle.ctrl_transfer(0x40, 127, 0x0007, 0, (0, 0, 0, 0))
    dev_handle.ctrl_transfer(0x40, 127, 0x0008, 0, (0, 0, 0, 0))
    dev_handle.ctrl_transfer(0x40, 127, 0x0007, 0, (0, 0, 0, 0))
    dev_handle.ctrl_transfer(0xc0, 2, 0x0021, 0, (0, 0, 0, 0))
    dev_handle.ctrl_transfer(0xc0, 2, 0x0023, 0, (0, 0, 0, 0, 0, 0, 0, 0))
    dev_handle.ctrl_transfer(0xc0, 2, 0x0023, 0, (0, 0, 0, 0, 0, 0, 0, 0))
    dev_handle.ctrl_transfer(0xc0, 2, 0x0023, 0, (0, 0, 0, 0, 0, 0, 0, 0))
    dev_handle.ctrl_transfer(0xc0, 2, 0x0023, 0, (0, 0, 0, 0, 0, 0, 0, 0))
    dev_handle.ctrl_transfer(0xc0, 2, 0x0023, 0, (0, 0, 0, 0, 0, 0, 0, 0))
    dev_handle.ctrl_transfer(0x40, 127, 0x0008, 0, (0, 0, 0, 0))
    dev_handle.ctrl_transfer(0x40, 127, 0x0007, 0, (0, 0, 0, 0))
    dev_handle.ctrl_transfer(0x40, 127, 0x0008, 0, (0, 0, 0, 0))
    dev_handle.ctrl_transfer(0x40, 127, 0x0007, 0, (0, 0, 0, 0))
    dev_handle.ctrl_transfer(0xc0, 2, 0x0021, 0, (0, 0, 0, 0))
    dev_handle.ctrl_transfer(0xc0, 2, 0x0023, 0, (0, 0, 0, 0, 0, 0, 0, 0))
    dev_handle.ctrl_transfer(0xc0, 2, 0x0023, 0, (0, 0, 0, 0, 0, 0, 0, 0))
    dev_handle.ctrl_transfer(0xc0, 2, 0x0023, 0, (0, 0, 0, 0, 0, 0, 0, 0))
    dev_handle.ctrl_transfer(0xc0, 2, 0x0023, 0, (0, 0, 0, 0, 0, 0, 0, 0))
    dev_handle.ctrl_transfer(0xc0, 2, 0x0023, 0, (0, 0, 0, 0, 0, 0, 0, 0))
    dev_handle.ctrl_transfer(0x40, 2, 0x0004, 0, (0, 0, 0, 0x01, 0, 0, 0, 0))

    out = dev_handle.ctrl_transfer(0xc0, 2, 0x0005, 0, (
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0))


    return out

def printout(dev_handle,channel):
    dev_handle.ctrl_transfer(0x40, 127, 0x0007, 0, (0, 0, 0, 0))
    dev_handle.ctrl_transfer(0x40, 127, 0x0008, 0, (0, 0, 0, 0))
    dev_handle.ctrl_transfer(0x40, 127, 0x0007, 0, (0, 0, 0, 0))
    dev_handle.ctrl_transfer(0x40, 127, 0x0008, 0, (0, 0, 0, 0))
    dev_handle.ctrl_transfer(0x40, 127, 0x0007, 0, (0, 0, 0, 0))
    dev_handle.ctrl_transfer(0xc0, 2, 0x0021, 0, (0, 0, 0, 0))
    dev_handle.ctrl_transfer(0xc0, 2, 0x0023, 0, (0, 0, 0, 0, 0, 0, 0, 0))
    dev_handle.ctrl_transfer(0xc0, 2, 0x0023, 0, (0, 0, 0, 0, 0, 0, 0, 0))
    dev_handle.ctrl_transfer(0xc0, 2, 0x0023, 0, (0, 0, 0, 0, 0, 0, 0, 0))
    dev_handle.ctrl_transfer(0xc0, 2, 0x0023, 0, (0, 0, 0, 0, 0, 0, 0, 0))
    dev_handle.ctrl_transfer(0xc0, 2, 0x0023, 0, (0, 0, 0, 0, 0, 0, 0, 0))
    dev_handle.ctrl_transfer(0x40, 127, 0x0008, 0, (0, 0, 0, 0))
    dev_handle.ctrl_transfer(0x40, 127, 0x0007, 0, (0, 0, 0, 0))
    dev_handle.ctrl_transfer(0x40, 127, 0x0008, 0, (0, 0, 0, 0))
    dev_handle.ctrl_transfer(0x40, 127, 0x0007, 0, (0, 0, 0, 0))
    dev_handle.ctrl_transfer(0xc0, 2, 0x0021, 0, (0, 0, 0, 0))
    dev_handle.ctrl_transfer(0xc0, 2, 0x0023, 0, (0, 0, 0, 0, 0, 0, 0, 0))
    dev_handle.ctrl_transfer(0xc0, 2, 0x0023, 0, (0, 0, 0, 0, 0, 0, 0, 0))
    dev_handle.ctrl_transfer(0xc0, 2, 0x0023, 0, (0, 0, 0, 0, 0, 0, 0, 0))
    dev_handle.ctrl_transfer(0xc0, 2, 0x0023, 0, (0, 0, 0, 0, 0, 0, 0, 0))
    dev_handle.ctrl_transfer(0xc0, 2, 0x0023, 0, (0, 0, 0, 0, 0, 0, 0, 0))
    dev_handle.ctrl_transfer(0x40, 2, 0x0004, 0, (0, 0, 0, 0x01, 0, 0, 0, 0))
    plt.ion()
    len = [0]

    y = []
    out = dev_handle.ctrl_transfer(0xc0, 2, 0x0005, 0, (
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0))
    y.append(out[7])

    count = 1

    figure, ax = plt.subplots(figsize=(10, 8))
    line1, = ax.plot(len, y)
    ax.autoscale_view(True, True, True)
    offset = channel*4
    while True:
        len.append(count)
        count = count + 1

        out = dev_handle.ctrl_transfer(0xc0, 2, 0x0005, 0, (
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0))
        print(out)

        y.append(out[offset] * 255*255*255+out[offset+1] * 255*255+out[offset+2] * 255 + out[offset+3])

        line1.set_ydata(y)
        line1.set_xdata(len)
        ax.relim()
        ax.autoscale_view(True, True, True)

        figure.canvas.draw()
        figure.canvas.flush_events()
        time.sleep(0.2)




def setup():
    dev_handle =usb.core.find(idVendor=VENDOR_ID, idProduct=DEVICE_ID)
    return dev_handle





