# This is the gene_api.py file for homework06

from flask import Flask, request
import redis
import requests

app = Flask(__name__)


def get_redis_client():
    return redis.Redis(host='127.0.0.1', port=6379, db=0, decode_responses=True)

rd = get_redis_client


@app.route('/data', methods=['GET', 'POST', 'DELETE'])
def handle_data():

    if request.method == 'GET':

        output_list = []
        for item in rd.keys():
            output_list.append(rd.hgetall(item))
        return output_list


    elif request.method == 'POST':
        response = requests.get(url='https://ftp.ebi.ac.uk/pub/databases/genenames/hgnc/json/hgnc_complete_set.json') 
        for item in response.json()['gene_data']:
            key = f'{item["name"]}:{item["id"]}'
            rd.hset(key, mapping=item)
        return 'data has been successfully loaded'

    elif request.method == 'DELETE':
        rd.flushdb()
        return f'data has successfully been deleted, there are {rd.keys()} keys in the data base\n'

    else:
        return 'Invalid Method Used!!'


@app.route('/genes', methods=['GET'])
def get_genes():

    return

@app.route('/genes/<hgnc_id>', methods=['GET'])
def get_gene_info():

    return


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')


