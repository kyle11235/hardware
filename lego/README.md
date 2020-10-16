# lego

- ev3

        - guide
        
                https://www.ev3dev.org/docs/getting-started/ -> download ev3 os image, choose mindstorm ev3 or raspberry pi2/3
                e.g. ev3dev-stretch-rpi2-generic-2019-03-03.zip

        - flash os image
        
                plug SD card into pc, balenaEtcher -> select image -> select drive -> flash image
                edit EV3DEV_BOOT/config.txt, follow guide there to enable BrickPi

        - start

                for raspberry, plug SD card into raspberry and power it on
                if you have a screen it displays the same UI as ev3, for you to setup wifi, browse files/devices

        - connect to wifi / PC host

                - display + keyboard（ev3需要插WiFi USB）
                ui -> network -> wifi, press enter when it focuses on password field, than you can use keyboard to input password directly or use its ui input

                - display + USB mini + ssh + connmanctl
                ui -> network -> wired, it shows IP (which is different with PC's network -> self-signed ip for it)

                - display + bluetooth + ssh + connmanctl（not used）

                - USB Ethernet adapter / cable + ssh + connmanctl（not used）

        - ssh

                ssh robot@x.x.x.x
                password=maker
                root password=maker
                Debian jessie on LEGO MINDSTORMS EV3!

                uname -a
                Linux ev3dev 4.4.87-22-ev3dev-ev3 #1 PREEMPT Sat Sep 9 14:45:55 CDT 2017 armv5tejl GNU/Linux

                - connmanctl

                        enable wifi
                        scan wifi
                        services
                        agent on
                        connect xxx
                        connect xxx_psk
                        quit
                
        - shutdown
        sudo poweroff

- drivers

        http://docs.ev3dev.org/projects/lego-linux-drivers/en/ev3dev-jessie/
        基于 Linux 的 sysfs，sysfs 将设备注册到内存中虚拟的文件中，你通过读取和写入文件属性来管理设备
        
        e.g.
        robot@ev3dev:~$ ls /sys/class/gpio
        export  gpiochip0  gpiochip128  gpiochip32  gpiochip64  gpiochip96  unexport

- libs(python java go...)

        https://www.ev3dev.org/docs/programming-languages/

- python, ev3dev-stretch(v2)

        https://python-ev3dev.readthedocs.io/en/ev3dev-stretch/index.html

        - install vscode plugin for more coding
        
        - upgrade from ev3dev-jessie to stretch(v2)
        https://python-ev3dev.readthedocs.io/en/ev3dev-stretch/upgrading-to-stretch.html
        
        e.g. (too slow... use sd card instead) 
        sudo apt-get update
        sudo apt-get install python3-pip
        pip install python-ev3dev2
        chmod +x && ./run.py

        - error
        If you encounter an error such as /usr/bin/env: 'python3\r': No such file or directory, you must switch your editor’s “line endings” setting for the file from “CRLF” to just “LF”

- demos（code + building guide）

        https://github.com/ev3dev/ev3dev-lang-python-demo
        check ./robots/...
        
        e.g.
        ./robots/educator (very basic usage)
        ./robots/explorer3r(run touch and random turn)

        ./robots/EV3D4(remote control, jquery from google is blocked)
        https://github.com/ev3dev/ev3dev-lang-python/blob/ev3dev-stretch/ev3dev2/control/webserver.py
        if change wifi, forget existing, reset wifi and connect new

        - mqtt example
        https://www.ev3dev.org/docs/tutorials/sending-and-receiving-messages-with-mqtt/

- community

        http://ev3python.com/