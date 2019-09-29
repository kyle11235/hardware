# lego

- ev3

        - guide
        https://www.ev3dev.org/docs/getting-started/ -> download ev3 os image, choose mindstorm ev3 or raspberry pi2/3
        e.g. ev3dev-stretch-rpi2-generic-2019-03-03.zip

        - flash os image
        plug SD card into pc, balenaEtcher -> select image -> select drive -> flash image
        edit EV3DEV_BOOT/config.txt, follow guide there to enable BrickPi

        - start
        plug SD card into raspberry and power it on
        if you have a screen it displays the same UI as ev3, for you to setup wifi, browse files/devices

        - connect it to PC host (Tethering)

                - With a Wi-Fi dongle to hotpot / router (wifi receiver / wireless internet card, ev3 has screen to login)
                - With USB mini, connect from ev3 network -> wired, it shows IP (which is different with PC's network -> self-signed ip for it)
                - With Bluetooth
                - special for Raspberry
                        - for no-display, must use wired Ethernet port for the first time through a remote SSH session
                        - for display connected Raspberry, Ctrl+Alt+F6 at end of boot -> connmanctl -> setup wireless networking
                                enable wifi
                                scan wifi
                                services
                                agent on
                                connect xxx
                                connect xxx_psk
                                quit

        - connect it to internet

                - With a Wi-Fi dongle to hotpot / router (wifi receiver / wireless internet card, ev3 has screen to login)
                - With USB mini through a PC (add it as device of PC to have its ip -> share internet to it)
                - With Bluetooth through a PC (add it as device of PC to have its ip -> share internet to it)
                - With a USB Ethernet adapter (connect to ethernet cable, ssh and setup wifi (connmanctl))

        - connect it to internet if it's ev3 image

                - give it a display screen for ev3 os has builtin UI
                - press enter when it focuses on password field, than you can use keyboard to input password directly or use its ui input

        - ssh
                ssh robot@x.x.x.x
                password=maker
                root password=maker
                Debian jessie on LEGO MINDSTORMS EV3!

        - write some code

                - original drivers - http://docs.ev3dev.org/projects/lego-linux-drivers/en/ev3dev-jessie/
                Each hardware device is represented by a directory in sysfs called a device node. Each device node has attributes that are represented by files. You monitor and control the hardware by reading and writing these attribute files

                - community libs

                        - python
                        https://github.com/ev3dev/ev3dev-lang-python
                        https://sites.google.com/site/ev3devpython/

                        - java
                        https://github.com/ev3dev-lang-java/ev3dev-lang-java

                        - go
                        https://github.com/ev3go/ev3dev

        - shutdown
        sudo poweroff

- todo

        voice input
