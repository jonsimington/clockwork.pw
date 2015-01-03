cd clockwork

# comment urls
mv urls.py urls.py.old
curl -O https://raw.githubusercontent.com/jonsimington/clockwork.pw/master/clockwork/urls.py

# comment settings
mv settings.py settings.py.old
curl -O https://raw.githubusercontent.com/jonsimington/clockwork.pw/master/clockwork/settings.py

rm urls.py.old
rm settings.py.old
