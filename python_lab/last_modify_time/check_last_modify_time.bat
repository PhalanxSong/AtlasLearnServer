@ECHO OFF

REM 设置 检查目录
SET check_dir=%cd%\ExampleFolder
ECHO check_dir:%check_dir%

REM 设置 记录时间文件Temp目录
SET save_dir=%cd%\TempBat
ECHO save_dir:%save_dir%

REM 设置 修改时间 记录文件名
SET modify_time_file=modify_time.txt

REM 设置 排序后修改时间 记录文件名
SET sorted_modify_time_file=sorted_modify_time.txt

REM touch创建记录时间文件Temp目录
MD %save_dir%

REM 如果 sorted_modify_time_file 已存在，则获取记录的最后更新时间 last_time
IF EXIST "%save_dir%\%sorted_modify_time_file%" (
    FOR /F "TOKENS=1 DELIMS=," %%A IN (%save_dir%\%sorted_modify_time_file%) DO (SET last_time=%%~A)
    ) ELSE (
    SET last_time=nan
    )
ECHO last_time:%last_time%

REM 删除记录
IF EXIST "%save_dir%\%modify_time_file%" (
    DEL /Q /F "%save_dir%\%modify_time_file%"
    )
IF EXIST "%save_dir%\%sorted_modify_time_file%" (
    DEL /Q /F "%save_dir%\%sorted_modify_time_file%"
    )

REM 获取当前检查目录的 modify_time
FOR /F "TOKENS=*" %%A IN ('Dir /B /S /OD "%check_dir%"') DO ECHO %%~TA, %%~FPNXA>>"%save_dir%\%modify_time_file%"

REM 为 modify_time 排序 并储存 sorted_modify_time
SORT "%save_dir%\%modify_time_file%">"%save_dir%\%sorted_modify_time_file%"

REM 获取当前最后更新时间 new_last_time
FOR /F "TOKENS=1 DELIMS=," %%A IN (%save_dir%\%sorted_modify_time_file%) DO (SET new_last_time=%%~A)
ECHO new_last_time:%new_last_time%

REM 比较 last_time 和 new_last_time
IF "%last_time%"=="%new_last_time%" (
    SET b_is_same=true
    ) ELSE (
    SET b_is_same=false
    )
ECHO b_is_same:%b_is_same%

PAUSE