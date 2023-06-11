#!/usr/bin/env bash

kubectl create -f fft.yml
kubectl apply -f loadbalancer.yml
kubectl apply -f hpa.yml
