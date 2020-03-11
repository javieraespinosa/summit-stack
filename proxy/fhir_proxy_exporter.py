
import redis
from mitmproxy import ctx, flowfilter



class Counter:
    
    def __init__(self):
        self.redis = redis.Redis(host='redis')


    def load(self, loader):
        loader.add_option(name ="flowfilter", typespec=str,  default="~u /fhir", help="??")
        

    def configure(self, updated):
        self.filter = flowfilter.parse(ctx.options.flowfilter)


    def request(self, flow):
        
        ## Filter requests targeting the '/fhir' endpoint
        if flowfilter.match(self.filter, flow):
            method   = flow.request.method
            resource = flow.request.path.replace("/fhir", "")
            
            print(method, resource)
                        
            # if not self.redis.exists('methods'):
            #     print('No methods')
                
            
            self.redis.hincrby('resource:get:count', resource, 1)
            
                
            
            #self.redis.set('method', method)
            #self.redis.set('resource', resource)

        


addons = [
    Counter(),
]

