cd clockwork

# comment urls
mv urls.py urls.py.old
curl -O https://gist.githubusercontent.com/jonsimington/a52cc35705fd0b80dc70/raw/91c4a1839782dfc797fa75d3f85dab80487e46d4/settings.py

# comment settings
mv settings.py settings.py.old
curl -O https://gist.githubusercontent.com/jonsimington/a52cc35705fd0b80dc70/raw/2afec80a7c2d7dd6b342fd4292fb5cb304a3e5bf/settings.py

rm urls.py.old
rm settings.py.old
