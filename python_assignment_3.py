import configparser
from flask import Flask

from mongo import connect_mongo, save

app = Flask(__name__)


def parse_config():
    config = configparser.ConfigParser()
    config.read('sample.ini')
    sessions = config.sections()
    if (len(sessions) == 0):
        return "no config found"
    config_dic = {}
    for session in sessions:
        config_dic[session] = {}
        for options in config.options(session):
            value = config.get(session, options)
            config_dic[session][options] = value
    return config_dic


def get_config():
    parsed_config = parse_config()
    print(parsed_config)
    config = configparser.ConfigParser()
    config.read('env.ini')
    host = config.get("Database", "host")
    user = config.get("Database", "user")
    password = config.get("Database", "password")
    client = connect_mongo(host, user, password)
    save(client, parsed_config)
    return parsed_config


@app.route('/config', methods=['GET'],)
def config():
    return get_config()


if __name__ == "__main__":
    app.run(debug=True)
