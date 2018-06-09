# Repository for IQ championship

## How to use
1. requirements.txtから必要ライブラリをインストール(pip install -r requirements.txt)
2. chrome用のweb driverをインストールして任意の場所に置く(https://sites.google.com/a/chromium.org/chromedriver/)
3. [config/local_config.py](https://github.com/kacky24/websim/blob/master/config/local_config.py)に自分のアドレスとパスワードを記入
4. [config/config.yml](https://github.com/kacky24/websim/blob/master/config/config.yml)にweb driverの場所などの設定を記入
5. python simulate.pyでalphas.txt内のアルファを自動でシミュレーション

## Requirement
- python 3.6.1

## Reference
### code sample
- https://github.com/nhatson/websim
- https://github.com/d07s1d0s4d1/alphatron
- https://github.com/robotpy/robotpy-websim

### how to use selenium
- https://www.inet-solutions.jp/technology/python-selenium/
- https://qiita.com/kinpira/items/383b0fbee6bf229ea03d
