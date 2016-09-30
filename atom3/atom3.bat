@echo off
echo Batch file starting AToM3 with splash by default, no splash if argument given
echo .
echo If your using Windows, you really don't need this batch file!
echo Simply start atom3.py or atom3NoSplash.py directly instead


rem If not arguments are given
if {%1}=={} (goto :NO_ARGS) else (goto :WITH_ARGS)


:NO_ARGS
python atom3.py
goto :EOF


:WITH_ARGS
echo 'Batch file is starting AToM3 with splash disabled'
python atom3NoSplash.py
goto :EOF