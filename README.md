# pyadvantech
## Interact with the Advantech USB-4718
1. Install the module via:
    ```cmd
    pip install pyadvantech
    ```
2. You might need to add the libusb.dll to your Path. 

3. Plug in the USB-4718 into your machine and install a WINUSB driver as its driver.
    ```python
    import pyadvantech.pyadvantech as pya
    
    device = pya.setup(vendor_id=None,device_id=None)
    pya.prepare_read()
    print(pya.read(device))
    ```
    The vendor id and device id can be manually set but if left unspecified will default to the known tested values.    
    Prepare read tells the device that it should now read the thermocouple. This call might not be necessary but it is a good Idea to call it as it moves the device out of a setup stage into the read stage.

4. Changes to the Value Ranges of the device can be made with:
    ```python
    import pyadvantech.pyadvantech as pya
    
    device = pya.setup()
    pya.set_channel_range(device,values=[0x0e,0x0b,0x0b,0x0b,0x0b,0x0b,0x0b,0x0b])
    
    ```
    If values is left as none it will reset the device to the 0-100mv range.
5. Multiple values can be selected and saved with:
   ```python
   import pyadvantech.pyadvantech as pya
   device = pya.setup()
   pya.read_and_save(device,channel=1,length=1000,update=0.1,file_name="test.csv")
   ```
   | Variable Name  | Description | Default Value |
   | ------------- | ------------- | ------------- |
   | device  | The Device handle  | required  |
   | channel  | The channel to be saved and stored  | required [0:7]  |
   | length  | Number of measurements to be taken  | 1000  |
   | update | The update time in sec  | 0.1  |
   | file_name  | The file name must end in .csv  | format "%Y_%m_%d_%H_%M_%S".csv  |
6. An Experimental plotting tool is also provided:
   ```python
   import pyadvantech.pyadvantech as pya
   device = pya.setup()
   pya.plot_out(device,channel=1,x_name=None,y_name=None,x_range=60,update=None,acquisition_len=None)
   ```
   | Variable Name  | Description | Default Value |
   | ------------- | ------------- | ------------- |
   | device  | The Device handle  | required  |
   | channel  | The channel to be saved and stored  | required [0:7]  |
   | x_name  | X axis label  | Time in *update* sec intervals  |
   | y_name  | Y axis label  | Output of USB device  |
   | x_range  | Range of x axis, if left *None* will just add new values continuously  | None  |
   | update | The update time in sec  | 0.1  |
   | acquisition_len  | Number of measurements to be taken  | 500 can be set to "inf"  |
   
   
   
   
