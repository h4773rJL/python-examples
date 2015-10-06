#! /usr/bin/python3
# -*- coding:utf-8 -*-

destiny = 'heatseeker.persa@gmail.com'

f = open('nombres.csv', 'r')

for line in f:
    separated = line.split(',')
    name = separated[0] + " " + separated[1] + " " + separated[2]
    email = separated[3]
    print(name, email)

f.close()
