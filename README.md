# hardware / 嵌入式开发

- x86 架构

        CPU
        由 Intel / AMD 制造
        性能强，功耗大，主导 PC / 服务器

- ARM 架构

        CPU / 芯片
        ARM 公司设计，授权其它公司生产
        功耗低，性能低，适合嵌入式，执行固定任务，但也在改进性能，进攻 Intel的x86服务器市场，有各种linux system -> 软件不兼容
        e.g. ait8328

- 单片机

        微型控制单元 / MCU
        基于 ARM / x86，中央处理器内核加了一些外围接口电路，做到一个芯片中
        自己编写库函数 + C + 自己设计PCB板

- Arduino

        开发平台
        基于AVR单片机 / ARM Cortex / ESP8266（Tensilica CPU）
        库函数 + C/C++ + IDE + 扩展硬件 + 开源
        e.g. codecard

- raspberry pi

        卡片式电脑
        基于 ARM / x86
        完整 linux，任何语言 -> 软件兼容

- Android

        Java
        e.g. androidthings (raspberry pi)
        e.g. rk3128 (ARM, android / ubuntu)

- arduino vs 树莓派

        Arduino 与树莓派 Raspberry Pi 的差异谈不上优缺点，而是他们是两个完全不同的产品
        1. 产品定位上：Arduino的定位是单片机，侧重IO性能；Raspberry Pi的定位是电脑侧重计算性能
        2. 运算性能：Arduino以UNO为例是AVR核心的8位单片机，运算频率16Mhz；树莓派3B版为例，是ARM核心的64位微处理器，运算频率1.2GHz 
        3. IO性能：Arduino包含数字IO和模拟IO,可以连接大量数字和模拟传感器，树莓派只有数字IO
        4. 开发工具：Arduino以Arduino C语言为开发环境；Raspberry Pi以Python开发为主，，兼顾其他Linux下的开发环境
        5. 操作系统：Arduino无操作系统；Raspberry Pi一般采用Linux作为操作系统
        6. 应用领域：Arduino一般用于传感器、设备控制；Raspberry Pi一般作为服务器或运算单元

        - https://pypi.org/project/RPi.GPIO/
        Note that this module is unsuitable for real-time or timing critical applications. This is because you can not predict when Python will be busy garbage collecting. It also runs under the Linux kernel which is not suitable for real time applications - it is multitasking O/S and another process may be given priority over the CPU, causing jitter in your program. If you are after true real-time performance and predictability, buy yourself an Arduino http://www.arduino.cc !

- solution

        - device
        
                - 单片机 -> c, upload
                - arduino -> c++, opensource，IDE, upload
                - lego -> linux, plugin sensor/motor, ev3 lib，Python
                - raspberry pi -> linux
                - 安卓 -> android API
                - PC -> linux

        - communication module

                - Bluetooth（ESP32）
                - WiFi（ESP32），Ethernet，SIM card
                - radio（射频编解码，NRF24l01）

        - protocal

                - bluetooth（主设，外设）
                - HTTP/TCP（server，client）
                - searial（sender，receiver）

                
        

