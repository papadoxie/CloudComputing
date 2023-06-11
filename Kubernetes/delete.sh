#!/usr/bin/env bash

kubectl delete deployment fft
kubectl delete service fft-lb
kubectl delete hpa fft-hpa