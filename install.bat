>nul 2>nul assoc .py
if exist %systemdrive%%homepath%\InfoCreeper\InfoCreeper.exe (
    cls
    echo "Program already installed.. "
    pause
) else (
    if errorlevel 1 (
        echo Not available
        @"%SystemRoot%\System32\WindowsPowerShell\v1.0\powershell.exe" -NoProfile -InputFormat None -ExecutionPolicy Bypass -Command "iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))" && SET "PATH=%PATH%;%ALLUSERSPROFILE%\chocolatey\bin"
        choco install -y python3
    )
    python --version
    python3 -m venv .\venv
    call .\venv\Scripts\activate.bat
    call pip install -r requirements.txt
    pyinstaller --name InfoCreeper --console --onefile --clean --distpath %systemdrive%%homepath%\InfoCreeper --icon icon.ico  --windowed main.py
    copy icon.ico %systemdrive%%homepath%\InfoCreeper\
    copy config.yml %systemdrive%%homepath%\InfoCreeper\
    rd /s/q "build"
    rd /s/q "__pycache__"
    del InfoCreeper.spec
)