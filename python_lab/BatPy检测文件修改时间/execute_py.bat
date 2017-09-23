
@echo off

PYTHON check_last_modify_time.py
SET /p modify_signal=<Temp/signal.txt
ECHO modify_signal=%modify_signal%
PAUSE