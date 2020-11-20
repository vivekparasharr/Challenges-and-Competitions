
# https://plotly.com/python/lines-on-mapbox/

import plotly.graph_objects as go

##### 
fig = go.Figure(go.Scattermapbox( #del-addis ababa-sao paolo-sgo
    mode = "markers+lines",
    lon = [77, 38.8, -46.6, -70.7],
    lat = [28, 9, -23.5, -33.4],
    marker = {'size': 10}))
fig.add_trace(go.Scattermapbox( #sgo-toronto-edmonton
    mode = "markers+lines",
    lon = [-70.7, -79.35, -113.32],
    lat = [-33.4, 43.65, 53.63],
    marker = {'size': 10}))
fig.add_trace(go.Scattermapbox( #sgo-lima-cusco
    mode = "markers+lines",
    lon = [-70.7, -77, -72],
    lat = [-33.4, -12, -13.52],
    marker = {'size': 10}))
fig.add_trace(go.Scattermapbox( # del - mumbai
    mode = "markers+lines",
    lon = [77, 73],
    lat = [28, 19.1],
    marker = {'size': 10}))
fig.add_trace(go.Scattermapbox( # del - doha - sao paolo - buenos aires - sgo
    mode = "markers+lines",
    lon = [77, 51.5, -46.6, -58.4, -70.7],
    lat = [28, 25.3, -23.5, -34.6, -33.4],
    marker = {'size': 10}))
fig.add_trace(go.Scattermapbox( # del - sao paolo - dubai - sgo
    mode = "markers+lines",
    lon = [77, 55.36, -46.6, -70.7],
    lat = [28, 25.25, -23.5, -33.4],
    marker = {'size': 10}))
fig.add_trace(go.Scattermapbox( # sgo - miami - charlotte
    mode = "markers+lines",
    lon = [-70.7, -80.1918, -80.8431],
    lat = [-33.4, 25.7617, 35.2271],
    marker = {'size': 10}))
fig.add_trace(go.Scattermapbox( # sgo - atlanta - charlotte
    mode = "markers+lines",
    lon = [-70.7, -84.3880, -80.8431],
    lat = [-33.4, 33.7490, 35.2271],
    marker = {'size': 10}))
fig.add_trace(go.Scattermapbox( # sgo - dallas - st louis
    mode = "markers+lines",
    lon = [-70.7, -96.7970, -90.1994],
    lat = [-33.4, 32.7767, 38.6270],
    marker = {'size': 10}))
#new
fig.add_trace(go.Scattermapbox( #vina-sgo-rancagua-osorno-puerto montt-chiloe
    mode = "markers+lines",
    lon = [-71.5500, -70.6693, -70.7406, -73.1149, -72.9411, -73.9266],
    lat = [-33.0153, -33.4489, -34.1701, -40.5762, -41.4689, -42.6240],
    marker = {'size': 10}))

fig.add_trace(go.Scattermapbox( #rapa nui-sgo-rancagua
    mode = "markers+lines",
    lon = [-109.3497, -70.6693, -70.7406],
    lat = [-27.1127, -33.4489, -34.1701],
    marker = {'size': 10}))


fig.add_trace(go.Scattermapbox( # del - agra - mathura
    mode = "markers+lines",
    lon = [77, 78.0081, 77.6737],
    lat = [28, 27.1767, 27.4924],
    marker = {'size': 10}))
fig.add_trace(go.Scattermapbox( # hoshiarpur - katra
    mode = "markers+lines",
    lon = [75.9115, 74.9318],
    lat = [31.5143, 32.9915],
    marker = {'size': 10}))


##### cosi
fig.add_trace(go.Scattermapbox( #sgo-mendoza
    mode = "markers+lines",
    lon = [-70.7, -68.8458],
    lat = [-33.4, -32.8895],
    marker = {'size': 10}))
fig.add_trace(go.Scattermapbox( #sgo-lima-cusco
    mode = "markers+lines",
    lon = [-70.7, -72.94289],
    lat = [-33.4, -41.46574],
    marker = {'size': 10}))
fig.add_trace(go.Scattermapbox( #talca-concepcion-chillan-temuco---osorno-puerto montt-chiloe
    mode = "markers+lines",
    lon = [-70.7406, -71.6485, -72.1023, -73.0444, -72.5904, -73.1149, -72.9411, -73.9266],
    lat = [-34.1701, -35.4232, -36.6063, -36.8201, -38.7359, -40.5762, -41.4689, -42.6240],
    marker = {'size': 10}))


##### neety
fig.add_trace(go.Scattermapbox( # del - london
    mode = "markers+lines",
    lon = [77, 0.1278],
    lat = [28, 51.5074],
    marker = {'size': 10}))
fig.add_trace(go.Scattermapbox( # del - bangalore
    mode = "markers+lines",
    lon = [77, 77.5946],
    lat = [28, 12.9716],
    marker = {'size': 10}))
fig.add_trace(go.Scattermapbox( # del - patna
    mode = "markers+lines",
    lon = [77, 85.1376],
    lat = [28, 25.5941],
    marker = {'size': 10}))
fig.add_trace(go.Scattermapbox( # del - ranchi
    mode = "markers+lines",
    lon = [77, 85.3096],
    lat = [28, 23.3441],
    marker = {'size': 10}))
##new
fig.add_trace(go.Scattermapbox( # del - baghdogra - purnia - patna
    mode = "markers+lines",
    lon = [77, 88.3117, 87.4753, 85.1376],
    lat = [28, 26.6986, 25.7771, 25.5941],
    marker = {'size': 10}))
fig.add_trace(go.Scattermapbox( # del - ahmedabad - bhuj - katch
    mode = "markers+lines",
    lon = [77, 72.5714, 69.6669, 69.8597],
    lat = [28, 23.0225, 23.2420, 23.7337],
    marker = {'size': 10}))
fig.add_trace(go.Scattermapbox( # del - panjim, goa - belgam, karnataka - bangalore
    mode = "markers+lines",
    lon = [77, 73.8278, 74.4977, 77.5946],
    lat = [28, 15.4909, 15.8497, 12.9716],
    marker = {'size': 10}))
fig.add_trace(go.Scattermapbox( # del - jammu - srinagar - ganderbal 
    mode = "markers+lines",
    lon = [77, 74.8570, 74.7973, 74.7719],
    lat = [28, 32.7266, 34.0837, 34.2165],
    marker = {'size': 10}))
fig.add_trace(go.Scattermapbox( # del - allahabad
    mode = "markers+lines",
    lon = [77, 81.8463],
    lat = [28, 25.4358],
    marker = {'size': 10}))
fig.add_trace(go.Scattermapbox( # del - bolangir - puri - bhuvaneshwar
    mode = "markers+lines",
    lon = [77, 83.4846, 85.8312, 85.8245],
    lat = [28, 20.7011, 19.8135, 20.2961],
    marker = {'size': 10}))
fig.add_trace(go.Scattermapbox( # del - jaipur
    mode = "markers+lines",
    lon = [77, 75.7873],
    lat = [28, 26.9124],
    marker = {'size': 10}))
fig.add_trace(go.Scattermapbox( # del - chandigarh - kasauli
    mode = "markers+lines",
    lon = [77, 76.7794, 76.9649],
    lat = [28, 30.7333, 30.9013],
    marker = {'size': 10}))
fig.add_trace(go.Scattermapbox( # del - hoshiarpur
    mode = "markers+lines",
    lon = [77, 75.9115],
    lat = [28, 31.5143],
    marker = {'size': 10}))
fig.add_trace(go.Scattermapbox( # del - banaras - mirzapur
    mode = "markers+lines",
    lon = [77, 82.9739, 82.5644],
    lat = [28, 25.3176, 25.1337],
    marker = {'size': 10}))
fig.add_trace(go.Scattermapbox( # del - bangalore - mysore
    mode = "markers+lines",
    lon = [77, 77.5946, 76.6394],
    lat = [28, 12.9716, 12.2958],
    marker = {'size': 10}))
fig.add_trace(go.Scattermapbox( # del - bharatpur
    mode = "markers+lines",
    lon = [77, 77.5030],
    lat = [28, 27.2152],
    marker = {'size': 10}))
fig.add_trace(go.Scattermapbox( # del - rishikesh
    mode = "markers+lines",
    lon = [77, 78.2676],
    lat = [28, 30.0869],
    marker = {'size': 10}))
fig.add_trace(go.Scattermapbox( # del - dehradun
    mode = "markers+lines",
    lon = [77, 78.0322],
    lat = [28, 30.3165],
    marker = {'size': 10}))
fig.add_trace(go.Scattermapbox( # del - mussorrie
    mode = "markers+lines",
    lon = [77, 78.0644],
    lat = [28, 30.4598],
    marker = {'size': 10}))

###### pops
fig.add_trace(go.Scattermapbox( # del - bhuvaneshwar
    mode = "markers+lines",
    lon = [77, 85.8245],
    lat = [28, 20.2961],
    marker = {'size': 10}))
# new
fig.add_trace(go.Scattermapbox( # coimbatore - ooty
    mode = "markers+lines",
    lon = [76.9558, 76.6950],
    lat = [11.0168, 11.4102],
    marker = {'size': 10}))
fig.add_trace(go.Scattermapbox( # punjab - coimbatore
    mode = "markers+lines",
    lon = [75.9115, 76.9558],
    lat = [31.5143, 11.0168],
    marker = {'size': 10}))
fig.add_trace(go.Scattermapbox( # punjab - chennai - andeman
    mode = "markers+lines",
    lon = [75.9115, 80.2707, 92.6586],
    lat = [31.5143, 13.0827, 11.7401],
    marker = {'size': 10}))


##### jorge
fig.add_trace(go.Scattermapbox( #sgo-tarna-lima-
    mode = "markers+lines",
    lon = [-70.7, -75.6889, -77.0428, -79.2113, -79.8891, -78.4678],
    lat = [-33.4, -11.4193, -12.0464, -4.0079, -2.1894, -0.1807],
    marker = {'size': 10}))


fig.update_layout(
    margin ={'l':0,'t':0,'b':0,'r':0},
    mapbox = {
        'center': {'lon': 10, 'lat': 10},
        #'style': "open-street-map",
        'style': "carto-positron",
        #'style': "carto-darkmatter",
        #'style': "stamen-terrain",
        'center': {'lon': -20, 'lat': -20},
        'zoom': 1}    
        )

fig.show()

