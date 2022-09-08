from flask import Flask

Serv = Flask(__name__)

@Serv.route('/')
def main():
    return 'hello world'


if __name__=='__main__':
    Serv.run(host='0.0.0.0', port = 7000)