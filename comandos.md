# Comandos para no olvidar

```bash
python –m venv .venv
(Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned) ; (& \.venv\Scripts\Activate.ps1)
pip install django
python.exe -m pip install --upgrade pip
New-Item requirements.txt
pip freeze > requirements.txt
django-admin startproject conf .
mkdir apps
cd apps
django-admin startapp incidentes
mkdir static
mkdir templates
cd templates
New-Item base.html, detalle.html, crear.html, editar.html, eliminar.html, lista.html
cd ../static
mkdir css
cd css
New-Item custom.css
pip freeze > requirements.txt
net start MongoDB  
git add .
git commit -m "iniciar proyecto"
git branch -M main
git remote add origin <https://github.com/mjperez/ev4-ti3032.git>
git push -u origin main
```
