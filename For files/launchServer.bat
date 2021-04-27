@echo off
chcp 437
set /p PR="Enter file name: "
echo Server is starting. Sending file: textFeed.txt
echo Connect ip_address:80
chcp 1251
echo Запуск сервера. Отправляемый файл textFeed.txt
echo Подключение ip_адрес:80
python feeder.py %PR% 80
