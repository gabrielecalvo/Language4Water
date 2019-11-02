@echo off

for %%x in (
    C:\Users\%USERNAME%\Anaconda3\Scripts\activate.bat
    C:\Users\%USERNAME%\AppData\Local\Continuum\Anaconda3\Scripts\activate.bat
    C:\ProgramData\Anaconda3\Scripts\activate.bat
    C:\Users\%USERNAME%\Miniconda3\Scripts\activate.bat
    C:\Users\%USERNAME%\AppData\Local\Continuum\miniconda3\Scripts\activate.bat
    C:\ProgramData\Miniconda3\Scripts\activate.bat
) do (
    echo checking if file exists %%x ..

    IF EXIST %%x (
        echo running conda from %%x ..
        CALL %%x
    )
)

echo running jupyter lab..
jupyter lab

pause