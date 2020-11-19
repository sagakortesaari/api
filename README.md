# api-testing
I'm currently learning Flask. 👩🏼‍🎓

## Getting set up
```
$ git clone https://github.com/sagakortesaari/api
```
Go to the folder & install required libs
```
$ python3 -m pip install -r requirements.txt
```

## Adding images to the API
```
$ curl -d '{"type":"put type of animal here", "url":"put url here"}' -H "Content-Type: application/json" -X POST localhost
```
