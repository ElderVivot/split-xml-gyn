import xmltodict as xmldict
import platform

# def readXml(fileBuffer) -> dict:
#     """
#     # :filePath is xml file
#     """
#     try:
#         return xmldict.parse(fileBuffer)
#     except Exception as e:
#         print(e)
#         return {}


def readXml(filePath: str, filterText) -> dict:
    """
    # :filePath is xml file
    """
    try:
        if platform.system() == 'Windows':
            with open(filePath, 'rb') as file:
                data = file.read()
                if data.decode('latin1').find(filterText) >= 0 and filterText != '':
                    return xmldict.parse(data)
        else:
            with open(filePath, 'rb') as file:
                data = file.read()
                if data.decode().find(filterText) >= 0 and filterText != '':
                    return xmldict.parse(data)
    except Exception as e:
        print(e)
        return {}
