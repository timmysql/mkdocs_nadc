Set-Location "C:\Users\timko\code\mkdocs_nadc\"
venv\Scripts\Activate

Set-Location "C:\Users\timko\code\mkdocs_nadc\" 
python.exe c:/Users/timko/code/mkdocs_nadc/database_daily_process.py

Set-Location "C:\Users\timko\code\mkdocs_nadc" 
python.exe c:/Users/timko/code/mkdocs_nadc/markdown_refresh_main.py

Set-Location "C:\Users\timko\code\mkdocs_nadc\nadc"
mkdocs gh-deploy

# Set-Location "C:\Users\timko\code\mkdocs_nadc\nadc"
# mkdocs serve

