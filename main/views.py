from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
import json
from django.conf import settings 
import os

# Create your views here.
def main(request):
    json_file_path = os.path.join(settings.BASE_DIR, 'static', 'json', 'convenience_store.json')
    with open(json_file_path, encoding='utf-8') as json_file:
        data = json.load(json_file)
        convenience_stores = data
        
        convenience_list = []
        for store in convenience_stores:
            if 'REFINE_LOTNO_ADDR' in store:
                convenience = {
                    "name": store['BIZPLC_NM'],
                    "state": store['BSN_STATE_NM'],
                    "address": store['REFINE_LOTNO_ADDR'],
                }
                convenience_list.append(convenience)
        
        convenience_json = json.dumps(convenience_list, ensure_ascii=False)
        
        context = {
            'convenience_json': convenience_json,
        }
        
        return render(request, 'html/main.html', context)