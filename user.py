#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import uuid
import psycopg2

try:
  conn = psycopg2.connect("dbname='python' user='admin' host='127.3.167.1' password='ex-vF1Acs9j3'")
  cursor = conn.cursor()
except:
  raise Exception('connect error')

def add_user(login,password,home,apartment):
  try:
    cursor.execute("INSERT INTO users (login, password, home, apartment) VALUES (%s, %s, %s, %s)", (login,password,home,apartment))
    conn.commit()
    return 1
  except:
   return 0

def auth(login,password):
  try:
    cursor.execute("SELECT * FROM users WHERE login = %s and password = %s", (login,password))
    data = cursor.fetchone()
    if login == data[1]:
      if password == data[2]:
        return 1
  except:
   return 0

def find(login):
  try:
    cursor.execute("SELECT * FROM users WHERE login = '%s'" % login )
    data = cursor.fetchone()
    if login == data[1]:
        return 1
  except:
   return 0

def get_data(login):
  try:
    cursor.execute("SELECT * FROM users WHERE login = '%s'" % login )
    data = cursor.fetchone()
    return list(data[3:])
  except:
   return 0