
from ma import ma

import connexion

connex_app = connexion.App("__name__",specification_dir='./')
connex_app.add_api('swagger.yml')

app = connex_app.app

#@api.route('/showUser')
#class HelloWorld2(Resource):
 #   def get(self):
  #      redis.incr('hits')
   #     counter = str(redis.get('hits'),'utf-8')
    #    cursor = conn.cursor()
     #   cursor.execute("SELECT * FROM user_data WHERE id = 1")
      #  var1 = cursor.fetchone()
       # text = 'name ist {}'.format(var1[1])
        
        # return {'user': text}

if __name__ == "__main__":
   
    ma.init_app(app)
   
    app.run(host="0.0.0.0", port=3001, debug=True)
   

