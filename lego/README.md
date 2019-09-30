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

        - connect to wifi / PC host

                - display + keyboard
                ui -> network -> wifi, press enter when it focuses on password field, than you can use keyboard to input password directly or use its ui input

                - display + USB mini + ssh + connmanctl
                ui -> network -> wired, it shows IP (which is different with PC's network -> self-signed ip for it)

                - display + bluetooth + ssh + connmanctl

                - USB Ethernet adapter / cable + ssh + connmanctl

        - ssh
                ssh robot@x.x.x.x
                password=maker
                root password=maker
                Debian jessie on LEGO MINDSTORMS EV3!

        - connmanctl

                enable wifi
                scan wifi
                services
                agent on
                connect xxx
                connect xxx_psk
                quit

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
