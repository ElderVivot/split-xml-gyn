import logging
import os
from src.read_xml import readXml
from src.save_xml import transformToXml
from src.functions import returnDataInDictOrArray

logger = logging.getLogger(__name__)


class ProcessXmls(object):
    def __init__(self, pathWithXmls, folderNameFilter, pathReplaceName) -> None:
        self.__pathWithXmls = pathWithXmls
        self.__folderNameFilter = folderNameFilter
        self.__pathToReplace = pathReplaceName.split('|')[0]
        self.__pathDest = pathReplaceName.split('|')[1]

    def __saveXml(self, nota, pathxml):
        notaSave = {}
        notaSave['GerarNfseResposta'] = nota

        numeroNf = returnDataInDictOrArray(nota, ['ListaNfse', 'CompNfse', 'Nfse', 'InfNfse', 'Numero'])
        codigoVerificao = returnDataInDictOrArray(nota, ['ListaNfse', 'CompNfse', 'Nfse', 'InfNfse', 'CodigoVerificacao'])

        if pathxml.find('/') >= 0:
            pathsavexml = pathxml.split('/')
        else:
            pathsavexml = pathxml.split('\\')

        pathsavexml[-1] = f'{numeroNf}_{codigoVerificao}.xml'
        pathsavexml = '/'.join(pathsavexml)
        pathsavexml = pathsavexml.replace(self.__pathToReplace, self.__pathDest)
        pathDest = '/'.join(pathsavexml.split('/')[:-1])
        if os.path.exists(pathDest) is False:
            os.makedirs(pathDest)

        xml = transformToXml(notaSave)

        with open(pathsavexml, 'w+') as f:
            f.write(xml)

    def __processOneXml(self, pathxml):
        try:
            dataXml = readXml(pathxml, '<geral>')

            if dataXml is not None:
                tagGerarNfseResposta = dataXml['geral']['GerarNfseResposta']
                if isinstance(tagGerarNfseResposta, list):
                    print('\t', len(tagGerarNfseResposta), ' notas')
                    for nota in tagGerarNfseResposta:
                        try:
                            self.__saveXml(nota, pathxml)
                        except Exception as e:
                            logger.exception(e)
                else:
                    print('\t 1 nota')
                    try:
                        self.__saveXml(tagGerarNfseResposta, pathxml)
                    except Exception as e:
                        logger.exception(e)
        except Exception as e:
            print(e)

    def process(self):
        for folder, _, files in os.walk(self.__pathWithXmls):
            for f in files:
                if (folder.find(self.__folderNameFilter) < 0 and self.__folderNameFilter != "") or f.find('.xml') < 0:
                    continue
                print('Lendo arquivo', f'{folder}/{f}')
                self.__processOneXml(f'{folder}/{f}')
