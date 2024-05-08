import xmltodict as xmldict


def transformToXml(fileDict) -> dict:
    """
    # :filePath is xml file
    """
    try:
        return xmldict.unparse(fileDict)
    except Exception as e:
        print(e)
        return {}
