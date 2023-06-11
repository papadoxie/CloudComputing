#!/bin/bash

for (( i=10; i<=1000; i+=5 ))
do
	./httperf_script.sh $i 
done


