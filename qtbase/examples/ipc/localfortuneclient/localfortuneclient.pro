HEADERS       = client.h
SOURCES       = client.cpp \
                main.cpp
QT           += network widgets

# install
target.path = $$[QT_INSTALL_EXAMPLES]/ipc/localfortuneclient
INSTALLS += target


simulator: warning(This example might not fully work on Simulator platform)
