# pyadvantech
## Interact with the Advantech USB-4718
1. Install the module via pip install pyadvantech.
2. You might need to add the libusb.dll to your Path.
3. Plug in the USB-4718 into your machine and install a WINUSB driver as its driver.
```python
import pyadvantech as pya

device = pya.setup()
print(pya.grab_values(device))
```
4. Changes to the Value Ranges of the device can be made with
```python
import pyadvantech as pya

device = pya.setup()
pya.set_channel_range(device,[0x0b,0x0b,0x0b,0x0b,0x0b,0x0b,0x0b,0x0b])

```

