from flask import Flask, request
import redis
import requests
import os
import matplotlib.pyplot as plt
import numpy as np

app = Flask(__name__)


def get_redis_client():
    redis_ip = os.environ.get('REDIS_IP')
    if not redis_ip:
        raise Exception()
    return redis.Redis(host=redis_ip, port=6379, db=0, decode_responses=True)
rd = get_redis_client 

def get_second_redis_client():
    redis_ip = os.environ.get('REDIS_IP')
    if not redis_ip:
        raise Exception()
    return redis.Redis(host=redis_ip, port=6379, db=1) 
rd_second = get_second_redis_client 


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
            rd.hset(item.get('hgnc_id', json.dumps(item)))
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
        alldata.append(json.loads(rd.get(item)))
    for point in alldata:
        if point == id_string:
            gene_info = json.dumps(point)

    return gene_info


@app.route('/image', methods=['GET', 'POST', 'DELETE'])
def get_image():
    '''
    This function will create a plot for the given data, show the user the plot and also delete the plot
    based on user method input. The function will iterate throughout the data and plot how many genes were apporved
    that year. In other words, genes approved is the y-axis and year is the x-axis.

    Returns:
        success or error messages and for the GET method, the user will get the plot image.
    '''
    if request.method == 'GET':
        rd_second.get("gene_plot.png") # the argument needs the image key that will be stored in the POST method
        return image

    elif request.method == 'POST':
        for rd.keys("date_approved_reserved") in rd.keys():
            if

        plt.plot(year, data_approved_number)
        plt.savefig("gene_plot.png") # would i need both the plt.favefig and the rd.set
        rd_second.set("gene_plot.png") # this stores the image and will be used in the GET method
        return 'image has been sucessfully loaded.'

    elif request.method == 'DELETE':
        rd_second.delete() 
        return f'image has been successfully deleted.'

    else:
        return 'Invalid Method Used!!'



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
