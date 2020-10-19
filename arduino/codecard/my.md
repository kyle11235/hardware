# my

## codecard

        - install driver from silabs(auto for win)
        - plugin device with fully connected cable
                
                mac -> system report -> hardware -> USB -> USB3.0 -> CP2104 USB to UART Bridge Controller
                win -> device manager -> ports > COM3 -> port setting to 115200

        - connect serial with terminal with baud rate = 115200
        - slide power off and on, long press buttons A and B
        - configure

                help (what you type does not show in terminal)
                ssid=k (do not click enter)
                password=codecard
                restart/connect (try restart hotspot)
                buttona1=https://apex.oracle.com/pls/apex/appslab/functions/master (response header must be application/json)
                fingerprinta1=8b8ab033deb977a74dd17d48ebddff154d51e0a6
                shortpressa

        - update firmware with arduino IDE, source code is in path arduino

## terminal

- win -> putty
- mac/linux

        screen /dev/tty.SLAB_USBtoUART 115200 –L

        - minicom

                - configure serial port to /dev/tty.SLAB_USBtoUART by /opt/minicom/2.2/bin/minicom -s
                - save setup as dlf
                - /opt/minicom/2.2/bin/minicom

        - coolterm

        - serial (not free)

                https://www.decisivetactics.com it uses its own driver, not the /dev device
                if wrong encoding occur in serial app, terminal -> reset emulator

- diy serial terminal, check ./terminal, nodejs code

## issue

- driver issue

        missing /dev/tty.xxx caused by mac 13.3 System Integrity Protection
        driver is installed into /Library/Extensions/xxx.kext by default
        but system report -> software -> extensitons -> xxx -> not loaded

        to load/fix it
        - restart and holding command + R -> utils -> terminal -> csrutil disable -> reboot
        - remove in /Library/Extensions/xxx.kext
        - reinstall driver

        to check status
        kextstat | grep silab

        to uninstall it
        sudo kextunload /Library/Extensions/SiLabsUSBDriver.kext
        sudo rm -rf /Library/Extensions/SiLabsUSBDriver.kext

## todo

- arduino

        https://www.arduino.cc/en/Main/Software

        - upload issue
        warning: espcomm_sync failed
        error: espcomm_open failed
        error: espcomm_upload_mem failed
        error: espcomm_upload_mem failed

        - fix (holding button A or B)
        复位引脚应通过按钮连接到接地引脚
        上传代码之前应该按下该按钮
        每次按下该按钮时，ESP8266-01模块上的蓝色LED指示灯将变为高电平，表示模块已复位

- seeedstudio

        http://wiki.seeedstudio.com/Platform/
