cd clockwork

# comment urls
mv urls.py urls.py.old
curl -O https://gist.githubusercontent.com/jonsimington/0cdbeca6f867fcb3e0ae/raw/b9d58a5d5be487e533a9f94041e0f46dde5dbd9e/urls.py

# comment settings
mv settings.py settings.py.old
curl -O https://gist.githubusercontent.com/jonsimington/a52cc35705fd0b80dc70/raw/91c4a1839782dfc797fa75d3f85dab80487e46d4/settings.py

rm urls.py.old
rm settings.py.old
