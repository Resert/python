#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import psycopg2

try:
  conn = psycopg2.connect("dbname='python' user='admin' host='127.3.167.1' password='ex-vF1Acs9j3'")
  cursor = conn.cursor()
except:
  raise Exception('connect error')

def update(home,apartment,cold,hot,date,login):
  try:
    cursor.execute("INSERT INTO counters (home, apartment, cold, hot, date, who) VALUES (%s, %s, %s, %s, %s, %s)", (home,apartment,cold,hot,date,login))
    conn.commit()
    return 1
  except:
   return 0

def get_apartment(home,apartment):
  try:
    cursor.execute("SELECT * FROM counters WHERE home = %s and apartment = %s", (home,apartment))
    return cursor.fetchall()
  except:
   return 0

def get_home(home):
  try:
    cursor.execute("SELECT * FROM counters WHERE home = '%s' " % home)
    data = cursor.fetchall()
    apartments = []
    homeList = []
    for x in data:
      apartments.append(x[2])
    apartments = list(set(apartments))
    for x in apartments:
      cursor.execute("SELECT * FROM counters WHERE apartment = '%s' " % x)
      data = cursor.fetchall()
      homeList.append(data[len(data)-1])
    return homeList
  except:
   return 0
