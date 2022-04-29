from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def main():
  return "join our discord server here https://discord.gg/7rjU4SfZwy"

def run():
  app.run(host="0.0.0.0", port=8080)

def alive():
  server = Thread(target=run)
  server.start()
