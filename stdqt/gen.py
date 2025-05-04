if __name__ == '__main__':
    from PyQt5 import *
    from PyQt5.QtWidgets import *
    from PyQt5.QtCore import *
    from PyQt5.QtGui import *
    from PyQt5.QtMultimedia import *
    from PyQt5.QtNetwork import *
    from PyQt5.QtWebEngine import *
    from PyQt5.QtWebEngineWidgets import *
    from PyQt5.QtWebEngineCore import *
    from PyQt5.QtXml import *
    from PyQt5.QtWinExtras import *
    from PyQt5.QtWebSockets import *
    from PyQt5.QtWebChannel import *
    from PyQt5.QtTextToSpeech import *
    from PyQt5.QtTest import *
    from PyQt5.QtSvg import *
    from PyQt5.QtSql import *
    from PyQt5.QtSerialPort import *
    from PyQt5.QtSensors import *
    from PyQt5.QtRemoteObjects import *
    from PyQt5.QtQuick import *
    from PyQt5.QtQuickWidgets import *
    from PyQt5.QtQuick3D import *
    from PyQt5.QtQml import *
    from PyQt5.QtPrintSupport import *
    from PyQt5.QtPositioning import *
    from PyQt5.QtOpenGL import *
    from PyQt5.QtNfc import *
    from PyQt5.QtMultimediaWidgets import *
    from PyQt5.QtLocation import *
    from PyQt5.QtHelp import *
    from PyQt5.QtDesigner import *
    from PyQt5.QtDBus import *
    from PyQt5.QtBluetooth import *


    from PyQt5 import (
        QtGui, 
        QtWidgets, 
        QtCore, 
        QtMultimedia, 
        QtNetwork, 
        QtWebEngine, 
        QtWebEngineWidgets, 
        QtWebEngineCore, 
        QtXml, 
        QtWinExtras, 
        QtWebSockets, 
        QtWebChannel,
        QtTextToSpeech,
        QtDesigner,
        QtHelp,
        QtDBus,
        QtBluetooth,
        QtLocation,
        QtOpenGL,
        QtNfc,
        QtMultimediaWidgets,
        QtPositioning,
        QtPrintSupport,
        QtQml,
        QtQuick3D,
        QtQuickWidgets,
        QtQuick,
        QtRemoteObjects,
        QtSensors,
        QtSerialPort,
        QtTest,
        QtSql,
        QtSvg
    )

    qModules = (
        QtGui, 
        QtWidgets, 
        QtCore, 
        QtMultimedia, 
        QtNetwork, 
        QtWebEngine, 
        QtWebEngineWidgets, 
        QtWebEngineCore, 
        QtXml, 
        QtWinExtras, 
        QtWebSockets, 
        QtWebChannel,
        QtTextToSpeech,
        QtDesigner,
        QtHelp,
        QtDBus,
        QtBluetooth,
        QtLocation,
        QtOpenGL,
        QtNfc,
        QtMultimediaWidgets,
        QtPositioning,
        QtPrintSupport,
        QtQml,
        QtQuick3D,
        QtQuickWidgets,
        QtQuick,
        QtRemoteObjects,
        QtSensors,
        QtSerialPort,
        QtTest,
        QtSql,
        QtSvg
    )

    classes_to_import:list[str] = []

    for k, v in list(globals().items()):
        if k.startswith('Q'):
            classes_to_import.append(k)
            print(k)

    print(classes_to_import)

    text = f"""from PyQt5 import (
    QtGui, 
    QtWidgets, 
    QtCore, 
    QtMultimedia, 
    QtNetwork, 
    QtWebEngine, 
    QtWebEngineWidgets, 
    QtWebEngineCore, 
    QtXml, 
    QtWinExtras, 
    QtWebSockets, 
    QtWebChannel,
    QtTextToSpeech,
    QtDesigner,
    QtHelp,
    QtDBus,
    QtBluetooth,
    QtLocation,
    QtOpenGL,
    QtNfc,
    QtMultimediaWidgets,
    QtPositioning,
    QtPrintSupport,
    QtQml,
    QtQuick3D,
    QtQuickWidgets,
    QtQuick,
    QtRemoteObjects,
    QtSensors,
    QtSerialPort,
    QtTest,
    QtSql,
    QtSvg
)

from stdqt._all import (
    {',\n    '.join(classes_to_import)}
)"""

    with open('./stdqt/__init__.py', 'w', encoding='utf-8') as f:
        f.write(text)