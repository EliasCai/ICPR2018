1. 环境说明：WIN7/64位/PY3.5
2. 安装步骤：主要[按照官方说明文档](https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/installation.md)，但一些重点的步骤说明如下：
    1. 步骤一：只能下载[protoc-3.4.0-win32.zip](https://github.com/google/protobuf/releases/download/v3.4.0/protoc-3.4.0-win32.zip)，虽然有其他更新的版本，但是只有这个版本管用
    2. 步骤二：添加系统变量![image](https://cdn-images-1.medium.com/max/1600/1*SKX64WwYgCYKXToHPZusXg.png)
    3. 步骤三：运行以下命令，这一步很坑，很多网上的教程都没有这一步
        ```
        1、in models\research directory run the following:
        python setup.py build
        python setup.py install
        
        2. go to model/research/slim and run the following:
        `pip install -e .`
        ```
    3. 安装完成，运行官方的测试代码，成功的话返回以下信息
    
        ```
        python object_detection/builders/model_builder_test.py
        ```
        ![image](https://github.com/EliasCai/ICPR2018/raw/master/install_ok.JPG)
             
