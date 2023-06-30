httperf --hog  --timeout=60 --server=127.0.0.1 --port=3000 --wsesslog=10000000,0,urls.txt --rate $1 -v&
sleep 30
pkill -2  httperf
