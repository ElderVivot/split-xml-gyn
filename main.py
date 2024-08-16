import json
import os
from src.process import ProcessXmls
from rocketry import Rocketry

dataJson = {}
with open('configuracoes.json', 'r', encoding='utf-8') as f:
    dataJson = json.load(f)

appRocketry = Rocketry()


@appRocketry.task('every 12 hour', name="process_xml_split")
def processXmlSplit():
    ProcessXmls(dataJson['pasta_xml'], dataJson['somente_pasta_com_nome']).process()


if __name__ == "__main__":
    appRocketry.run()
