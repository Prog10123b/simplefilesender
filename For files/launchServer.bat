@echo off
chcp 437
set /p PR="Enter file name: "
echo Server is starting. Sending file: textFeed.txt
echo Connect ip_address:80
chcp 1251
echo ������ �������. ������������ ���� textFeed.txt
echo ����������� ip_�����:80
python feeder.py %PR% 80
