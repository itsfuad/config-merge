"""Deep-merge JSON configuration layers with last-layer precedence."""

def analyze(text):
    import json
    data=json.loads(text)
    if not isinstance(data,list):raise ValueError('expected a JSON array of layers')
    def merge(left,right):
        for k,v in right.items():
            if isinstance(v,dict) and isinstance(left.get(k),dict):merge(left[k],v)
            else:left[k]=v
        return left
    result={}
    for layer in data:
        if not isinstance(layer,dict):raise ValueError('layer must be an object')
        merge(result,layer)
    return {'merged':result,'layers':len(data)}
