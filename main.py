import json
import os
from src.process import ProcessXmls

dataJson = {}
with open('configuracoes.json', 'r', encoding='utf-8') as f:
    dataJson = json.load(f)

ProcessXmls(dataJson['pasta_xml'], dataJson['somente_pasta_com_nome']).process()

os.system('pause > nul')
