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
