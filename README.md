# LibShortText-for-Windows
LibShortText Library for Windows user.

## Notes
* LibShortText is an open source tool for short-text classification and analysis.
* No need to installation
* Python version must be 2.6 or newer
* You can run command in Microsoft command prompt Window
* This modify the source codes from Libshorttext: https://www.csie.ntu.edu.tw/~cjlin/libshorttext/

## Usage
The same as Unix-version of LibShortText. For example, for training phase
```shell
D:\LibShortText-for-Windows> python text-train.py your_train_file your_saved_model_dir
```
For predict phase
```shell
D:\LibShortText-for-Windows> python text-predict.py [options] your_test_file your_saved_model_dir output
```

## Other Issue
If you encounter the following problem:
```shell
無法啟動程式，因為你的電腦遺失VCRUNTIME140.dll。請嘗試重新安裝以修正這個問題。
```
Please refer to: http://www.zoearthmoon.net/blog/program/item/1328.html