import json

def test_port_and_region(client):
    response = client.get("/rates", 
                    query_string = {'date_from': '2016-01-01',
                                    'date_to': '2016-01-10',
                                    'origin': 'CNSGH',
                                    'destination': 'north_europe_main'})

    data_list = json.loads(response.data.decode("utf-8"))

    assert response.status_code == 200
    assert len(data_list) == 10
    assert data_list[1]['day'] == '2016-01-02'
    assert data_list[1]['average_price'] == 1112
    assert data_list[2]['day'] == '2016-01-03'
    assert data_list[2]['average_price'] == None
    assert data_list[3]['day'] == '2016-01-04'
    assert data_list[3]['average_price'] == None
    assert data_list[8]['day'] == '2016-01-09'
    assert data_list[8]['average_price'] == 1124

def test_port_and_port(client):
    response = client.get("/rates", 
                    query_string = {'date_from': '2016-01-01',
                                    'date_to': '2016-01-10',
                                    'origin': 'CNSGH',
                                    'destination': 'EETLL'})

    data_list = json.loads(response.data.decode("utf-8"))

    assert response.status_code == 200
    assert len(data_list) == 10
    assert data_list[1]['day'] == '2016-01-02'
    assert data_list[1]['average_price'] == 1059
    assert data_list[2]['day'] == '2016-01-03'
    assert data_list[2]['average_price'] == None
    assert data_list[3]['day'] == '2016-01-04'
    assert data_list[3]['average_price'] == None
    assert data_list[8]['day'] == '2016-01-09'
    assert data_list[8]['average_price'] == 1060

def test_region_and_region(client):
    response = client.get("/rates", 
                    query_string = {'date_from': '2016-01-01',
                                    'date_to': '2016-01-10',
                                    'origin': 'china_east_main',
                                    'destination': 'scandinavia'})

    data_list = json.loads(response.data.decode("utf-8"))

    assert response.status_code == 200
    assert len(data_list) == 10
    assert data_list[1]['day'] == '2016-01-02'
    assert data_list[1]['average_price'] == 1686
    assert data_list[2]['day'] == '2016-01-03'
    assert data_list[2]['average_price'] == None
    assert data_list[3]['day'] == '2016-01-04'
    assert data_list[3]['average_price'] == None
    assert data_list[8]['day'] == '2016-01-09'
    assert data_list[8]['average_price'] == 1572

def test_missing_date_from(client):
    response = client.get("/rates", 
                    query_string = {'date_to': '2016-01-10',
                                    'origin': 'CNSGH',
                                    'destination': 'north_europe_main'})
    assert response.status_code == 422

def test_missing_date_to(client):
    response = client.get("/rates", 
                    query_string = {'date_from': '2016-01-01',
                                    'origin': 'CNSGH',
                                    'destination': 'north_europe_main'})
    assert response.status_code == 422

def test_missing_origin(client):
    response = client.get("/rates", 
                    query_string = {'date_from': '2016-01-01',
                                    'date_to': '2016-01-10',
                                    'destination': 'north_europe_main'})
    assert response.status_code == 422

def test_missing_destination(client):
    response = client.get("/rates", 
                    query_string = {'date_from': '2016-01-01',
                                    'date_to': '2016-01-10',
                                    'origin': 'CNSGH'})
    assert response.status_code == 422

def test_wrong_port(client):
    response = client.get("/rates", 
                    query_string = {'date_from': '2016-01-01',
                                    'date_to': '2016-01-10',
                                    'origin': 'LLLLL',
                                    'destination': 'north_europe_main'})

    assert response.status_code == 400
    assert response.json['message'] == 'Invalid region name for origin'

def test_wrong_region(client):
    response = client.get("/rates", 
                    query_string = {'date_from': '2016-01-01',
                                    'date_to': '2016-01-10',
                                    'origin': 'CNSGH',
                                    'destination': 'north_euro'})

    assert response.status_code == 400
    assert response.json['message'] == 'Invalid region name for destination'