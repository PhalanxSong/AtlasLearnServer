@ECHO OFF

REM ���� ���Ŀ¼
SET check_dir=%cd%\ExampleFolder
ECHO check_dir:%check_dir%

REM ���� ��¼ʱ���ļ�TempĿ¼
SET save_dir=%cd%\TempBat
ECHO save_dir:%save_dir%

REM ���� �޸�ʱ�� ��¼�ļ���
SET modify_time_file=modify_time.txt

REM ���� ������޸�ʱ�� ��¼�ļ���
SET sorted_modify_time_file=sorted_modify_time.txt

REM touch������¼ʱ���ļ�TempĿ¼
MD %save_dir%

REM ��� sorted_modify_time_file �Ѵ��ڣ����ȡ��¼��������ʱ�� last_time
IF EXIST "%save_dir%\%sorted_modify_time_file%" (
    FOR /F "TOKENS=1 DELIMS=," %%A IN (%save_dir%\%sorted_modify_time_file%) DO (SET last_time=%%~A)
    ) ELSE (
    SET last_time=nan
    )
ECHO last_time:%last_time%

REM ɾ����¼
IF EXIST "%save_dir%\%modify_time_file%" (
    DEL /Q /F "%save_dir%\%modify_time_file%"
    )
IF EXIST "%save_dir%\%sorted_modify_time_file%" (
    DEL /Q /F "%save_dir%\%sorted_modify_time_file%"
    )

REM ��ȡ��ǰ���Ŀ¼�� modify_time
FOR /F "TOKENS=*" %%A IN ('Dir /B /S /OD "%check_dir%"') DO ECHO %%~TA, %%~FPNXA>>"%save_dir%\%modify_time_file%"

REM Ϊ modify_time ���� ������ sorted_modify_time
SORT "%save_dir%\%modify_time_file%">"%save_dir%\%sorted_modify_time_file%"

REM ��ȡ��ǰ������ʱ�� new_last_time
FOR /F "TOKENS=1 DELIMS=," %%A IN (%save_dir%\%sorted_modify_time_file%) DO (SET new_last_time=%%~A)
ECHO new_last_time:%new_last_time%

REM �Ƚ� last_time �� new_last_time
IF "%last_time%"=="%new_last_time%" (
    SET b_is_same=true
    ) ELSE (
    SET b_is_same=false
    )
ECHO b_is_same:%b_is_same%

PAUSE