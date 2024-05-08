import xmltodict as xmldict


def readXml(fileBuffer) -> dict:
    """
    # :filePath is xml file
    """
    try:
        return xmldict.parse(fileBuffer)
    except Exception as e:
        print(e)
        return {}
