import matplotlib.pyplot as plt
import usb.core
import usb.util
import time
import numpy as np
import csv
from tqdm import tqdm

VENDOR_ID = 0x1809
DEVICE_ID = 0x4718


def set_channel_range(dev_handle, values=None):
    if values is None:
        values = [0x0b, 0x0b, 0x0b, 0x0b, 0x0b, 0x0b, 0x0b, 0x0b]
    dev_handle.ctrl_transfer(0xc0, 127, 0x0001, 0, (0, 0, 0, 0))
    dev_handle.ctrl_transfer(0xc0, 127, 0x000a, 0, (0, 0, 0, 0))
    dev_handle.ctrl_transfer(0xc0, 127, 0x000c, 0, (0, 0, 0, 0))
    dev_handle.ctrl_transfer(0xc0, 127, 0x000b, 0, (0, 0, 0, 0))
    dev_handle.ctrl_transfer(0xc0, 127, 0x000d, 0, (0, 0, 0, 0))
    channels = [0, 0x01, 0x02, 0x03, 0x04, 0x04, 0x05, 0x06, 0x07]
    assert len(values) == len(channels)
    for i, value in enumerate(values):
        if value:
            try:
                dev_handle.ctrl_transfer(0x40, 2, 0x0006, 0,
                                         (0, channels[i], 0, 0x01, 00, value, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                          0))
            except:
                EnvironmentError("USB ERROR")
                break
        else:
            ValueError("Value must have value between 0x00 and 0x07")
            break
    dev_handle.ctrl_transfer(0x40, 2, 0x0040, 0, (0x02, 0x10, 0, 0, 0, 0x08))
    dev_handle.ctrl_transfer(0xc0, 2, 0x0041, 0, (tuple(0 for _ in range(36))))
    dev_handle.ctrl_transfer(0x40, 2, 0x0040, 0, (0x02, 0x20, 0, 0, 0, 0x08))
    dev_handle.ctrl_transfer(0xc0, 2, 0x0041, 0, (tuple(0 for _ in range(36))))
    dev_handle.ctrl_transfer(0x40, 1, 0x0001, 0, (0, 0, 0, 0x01, 0, 0, 0, 0))
    dev_handle.ctrl_transfer(0x40, 127, 0x0007, 0, (tuple(0 for _ in range(4))))
    dev_handle.ctrl_transfer(0x40, 127, 0x0008, 0, (tuple(0 for _ in range(4))))
    dev_handle.ctrl_transfer(0x40, 127, 0x0007, 0, (tuple(0 for _ in range(4))))
    dev_handle.ctrl_transfer(0x40, 127, 0x0008, 0, (tuple(0 for _ in range(4))))


def prepare_read(dev_handle):
    try:
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

        return dev_handle, True
    except:
        Warning("The Device rejected the read setup, a read might still work")
        return dev_handle, False


def read(dev_handle):
    return dev_handle.ctrl_transfer(0xc0, 2, 0x0005, 0, (
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0))


def read_and_update_plot(dev_handle, x_range, x, count, y, offset, line1, ax, figure, update, max_y):
    if x_range is None:
        x.append(count)
        count = count + 1

    out = read(dev_handle)

    y.append(
        out[offset] * 255 * 255 * 255 + out[offset + 1] * 255 * 255 + out[offset + 2] * 255 + out[offset + 3])
    if y[-1] > max_y:
        max_y = y[-1] * 1.05
    line1.set_ydata(y[-x_range:])
    line1.set_xdata(x)
    ax.set_ylim(bottom=0, top=max_y)
    ax.set_xlim(left=0, right=x[-1])
    ax.autoscale_view(True, True, True)

    figure.canvas.draw()
    figure.canvas.flush_events()
    time.sleep(update)
    return count, x, y, line1, ax, figure, max_y


def plot_out(dev_handle, channel, x_name=None, y_name=None, x_range=None, update=None, acquisition_len=None):
    if update is None:
        update = 0.1
    if x_name is None:
        x_name = "Time in " + str(update) + " sec intervals"
    if y_name is None:
        y_name = "Output of USB device"
    if acquisition_len is None:
        acquisition_len = 500

    prepare_read(dev_handle)
    plt.ion()
    x = [0]
    offset = channel * 4
    y = []
    out = read(dev_handle)
    y.append(out[offset] * 255 * 255 * 255 + out[offset + 1] * 255 * 255 + out[offset + 2] * 255 + out[offset + 3])
    count = 1
    if x_range is not None:
        x = np.linspace(0, x_range - 1, x_range).tolist()
        y = np.zeros(x_range).tolist()

    figure, ax = plt.subplots(figsize=(10, 8))
    plt.xlabel(x_name)
    plt.grid(visible=True, which='major', ds='steps-mid')
    plt.ylabel(y_name)
    line1, = ax.plot(x, y)
    ax.minorticks_on()
    ax.grid(which='minor', linestyle=':', linewidth='0.5', color='grey')
    ax.autoscale_view(True, True, True)
    max_y = 0
    if acquisition_len == "inf":
        while True:
            count, x, y, line1, ax, figure, max_y = read_and_update_plot(dev_handle, x_range, x, count, y, offset,
                                                                         line1, ax,
                                                                         figure, update, max_y)
    else:
        for i in range(acquisition_len):
            count, x, y, line1, ax, figure, max_y = read_and_update_plot(dev_handle, x_range, x, i + 1, y, offset,
                                                                         line1, ax,
                                                                         figure, update, max_y)


def setup(vendor_id=None, device_id=None):
    if vendor_id is None:
        vendor_id = VENDOR_ID
    if device_id is None:
        device_id = DEVICE_ID
    dev_handle = usb.core.find(idVendor=vendor_id, idProduct=device_id)
    return dev_handle


def read_and_save(dev_handle, channel, length=None, update=None, file_name=None):
    values = []
    offset = channel * 4
    if length is None:
        length = 1000
    if update is None:
        update = 0.1
    if file_name is None:
        file_name = time.strftime("%Y_%m_%d_%H_%M_%S") + ".csv"
    prepare_read(dev_handle)
    with open(file_name, 'w', newline='') as fp:
        for _ in tqdm(range(length)):
            out = read(dev_handle)
            values.append([str(time.strftime("%H:%M:%S")),
                           out[offset] * 255 * 255 * 255 + out[offset + 1] * 255 * 255 + out[offset + 2] * 255 + out[
                               offset + 3]])
            time.sleep(update)
        writer = csv.writer(fp)
        writer.writerows(values)
    return values
