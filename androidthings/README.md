# android things

- platform

        - NXP Pico i.MX7D
        - Raspberry Pi 3 Model B

- flash system

        - guide
        https://developer.android.com/things/hardware/raspberrypi.html

        - plug TF card in FAT32 format into PC (once flashed, cannot write data, can be flashed again)
        - login https://partner.android.com/things/console
        - download tool
        - sudo ./android-things-setup-utility-macos (download image and choose disk)
        - plug disk into board
        - best to plug display into board (display ip, set wifi)

        - issue
        boot only display rainbow image
        try 0.4.1 preview image instead of latest

        - connect to same network by cable to router or to pc (for wifi setup)
        - setup wifi
                - continue to use tool
                - use diaplay ui
                - use adb

- sample app

        - android studio

- serial debug console
