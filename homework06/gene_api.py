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
    ''' 
    This function will get, post, or delete data from/to the redis client depending on the user's input

    Returns:
        output_list : list of all data in redis
        return messages : will return a 'sucess' message when the data has either been deleted or posted
    '''

    if request.method == 'GET':

        output_list = []
        for item in rd.keys():
            output_list.append(rd.hgetall(item))
        return output_list


    elif request.method == 'POST':
        response = requests.get(url='https://ftp.ebi.ac.uk/pub/databases/genenames/hgnc/json/hgnc_complete_set.json') 
        for item in response.json()['response']['docs']:
            key = f'{item["hgnc_id"]}'
            rd.hset(item.get('hgnc_id', json.dumps(item))
        return 'data has been successfully reloaded'

    elif request.method == 'DELETE':
        rd.flushdb()
        return f'data has successfully been deleted, there are {rd.keys()} keys in the data base\n'

    else:
        return 'Invalid Method Used!!'



@app.route('/genes', methods=['GET'])
def get_genes():
    '''
    This function will display to the user a list of all of the genes in the data set.

    Returns:
        output : this is a list of all of the genes in the data set
    '''
    output = []
    for item in rd.keys():
        if item == 'hgnc_id':
        output.append(item)

    return output



@app.route('/genes/<int:hgnc_id>', methods=['GET'])
def get_gene_info(gene_id_num):
    '''
    This function will display to the user information on a specified gene.

    Args:
        hgnc_id(int) : identification number for a specific gene

    Returns:
        items : list/dictionary of the information for that specific gene
    '''
    id_string = "HGNC:"+gene_id_num
    alldata = []
    gene_info = []
    for item in rd.keys():
        alldata.append()json.loads(rd.get(item)))
    for point in alldata:
        if point == id_string:
            gene_info = json.dumps(point)
    
    return gene_info


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')


