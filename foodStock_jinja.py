import cherrypy
import jinja2
import sqlite3 as sql
import math, os

JINJA_ENVIRONMENT = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__),'WebDesign')),extensions=['jinja2.ext.autoescape'])

DB ='foodStock.db'

class FoodWebsite(object):
    @cherrypy.expose
    @cherrypy.tools.gzip()
    def WebDesign(self):
     WebDesign = JINJA_ENVIRONMENT.get_webDesign('currentStock.html')
     WebDesign_values = {
          'foodStock' : self.get_foodStock()}
     return WebDesign.render(WebDesign_values)
     
     def get_foodStock(self):
          foodStocks=[]
          productIDs = self.get_productID()
          barcodes = self.get_barcodes()
          productNames = self.get_productNames()
          brands = self.get_brands()
          stores = self.get_stores()
          stockNumbers = self.get_stockNumbers()
          for i in range (len(productIDs)):
               foodStock.append([productIDs[i], barcodes[i], productNames[i], brands[i], stores[i], stockNumbers[i]])
          return foodStocks
          
    def get_productID(self):
     productIDs = []
     with sql.connect(DB) as cur:
          results = cur.execute('''SELECT productId FROM foodStock;''')
          for productId, in results:
               productIDs.append(str(productId))
     return productIDs

     def get_barcodes(self):
          barcodes = []
          with sql.connect(DB) as cur:
               results = cur.execute('''SELECT barcode from foodStock;''')
               for barcode, in results:
                    barcodes.append(str(barcode))
          return barcodes
     
     def get_productNames(self):
          productNames = []
          with sql.connect(DB) as cur:
               results = cur.execute('''SELECT productName from foodStock;''')
               for productName, in results:
                    productNames.append(str(productName))
          return productNames


    def get_brands(self):
        brands = []
        with sql.connect(DB) as cur:
            results = cur.execute('''SELECT brand FROM foodStock;''')
            for brand, in results:
                brands.append(str(brand))
        return brands

    def get_stockNumbers(self):
        stockNumbers = []
        with sql.connect(DB) as cur:
            result = cur.execute('''SELECT stockNumber FROM foodStock;''')
            for stockNumber, in results:
                stockNumbers.append(str(stockNumber))
        return stockNumbers

if __name__ == '__main__':
    cherrypy.config.update({'server.socket_host': '0.0.0.0'})
    cherrypy.config.update({'server.socket_port': 3000})
    cherrypy.quickstart(FoodWebsite(), '/', {'/': {'tools.gzip.on': True}})
    
                
        
