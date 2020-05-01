import cherrypy
import sqlite3 as sql

DB ='foodStock.db'

class IProductTrackingWeb(object):
    @cherrypy.expose
    @cherrypy.tools.gzip()
    def index(self):
        productNames = []
        with sql.connect(DB) as cur:
            results = cur.execute('''SELECT productName from foodStock;''')
            for productName, in results:
                productNames.append(str(productName))
        print (productNames)
        return productNames
        
if __name__ =='__main__':
    cherrypy.config.update({'server.socket_host': '0.0.0.0'})
    cherrypy.config.update({'server.socket_port': 3000})
    cherrypy.quickstart(IProductTrackingWeb(), '/', {'/': {'tools.gzip.on': True}})
    
                
        
