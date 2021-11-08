import requests
import json

network_id = 'uniandes_network_01'
subscriber_id = 'IMSI901700100001113'
pemPath = '../../admin_operator.pem'

def upgradeBandwidth():
    response2 = requests.get('https://localhost:9443/magma/v1/lte/'+ network_id +'/subscribers/'+ subscriber_id,cert=(pemPath, pemPath),verify=False)
    data = response2.json()
    currentPolicy = data['active_policies'][0]
    if currentPolicy == 'low_policy': 
        newPolicy = ['medium_policy']
        print('incrementado a medium')
    elif currentPolicy == 'medium_policy':
        newPolicy = ['high_policy']
        print('incrementado a high')
    else:
        newPolicy = ['high_policy']
        print('Esta en el maximo')

    data['active_policies'] = newPolicy
    requestBody = json.dumps(data)
    headers={
    'Content-type':'application/json', 
    'Accept':'application/json'
    }
    responseUpgrade = requests.put('https://localhost:9443/magma/v1/lte/'+ network_id +'/subscribers/'+ subscriber_id,headers=headers,data=requestBody,cert=('../../admin_operator.pem','../../admin_operator.pem'),verify=False)

def downgradeBandwidth():
    response2 = requests.get('https://localhost:9443/magma/v1/lte/'+ network_id +'/subscribers/'+ subscriber_id,cert=(pemPath, pemPath),verify=False)
    data = response2.json()
    currentPolicy = data['active_policies'][0]
    if currentPolicy == 'low_policy': 
        newPolicy = ['low_policy']
        print('Esta en minimo')
    elif currentPolicy == 'medium_policy':
        newPolicy = ['low_policy']
        print('disminuyendo a low')
    else:
        newPolicy = ['medium_policy']
        print('disminuyendo a low')

    data['active_policies'] = newPolicy
    requestBody = json.dumps(data)
    headers={
    'Content-type':'application/json', 
    'Accept':'application/json'
    }
    responseUpgrade = requests.put('https://localhost:9443/magma/v1/lte/'+ network_id +'/subscribers/'+ subscriber_id,headers=headers,data=requestBody,cert=('../../admin_operator.pem','../../admin_operator.pem'),verify=False)