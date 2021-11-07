from PySide2 import QtGui, QtCore
class StylesMainWindow ():
    def __init__ (self,mainWindow):
        self.widget = mainWindow
        self.window = self.widget.window
        # self.widget.window = mainWindow
        self.set_colors()
        self.set_theme()
        self.setIcons()
        
    def set_colors(self):
        self.hover_button = '#474747'
        self.background = '#D1D1D1'
        self.buttons = '#6E6E6E'
        self.disabled_button = '#C2C2C2'
        self.frame_image = '#D1D1D1'
        self.primaryText = '#000'
        self.secondaryText = '#000'
        self.disbled_buttons = '#E3E3E3'
        
    def setIcons(self):
        pixmap_logo  =QtGui.QPixmap('./views/icons/icon2.png')
        logo_resized = pixmap_logo.scaled(70, 70, QtCore.Qt.KeepAspectRatio)
        self.window.logo_covid.setPixmap(logo_resized)
        
        # self.window.CovidRx.
        
    #     self.window.pushload.setIcon(
    #         QtGui.QPixmap('./views/icons/load_image.png'))
    #     self.window.pushload.setIconSize(QtCore.QSize(55, 55))
    #     self.window.pushload.setToolTip('load image')
    #     self.window.pushload.setText("")
    
    def set_theme(self):
        styleWindow = """
            QWidget{
                background: """ + self.background + """;
                color:  """ + self.primaryText + """;
                border: none;
                font-size: 12pt;
            }
            QPushButton{
                Background: """ + self.buttons + """;
                min-height: 40px;
                border-radius: 2px;
                border: 1px solid #000
                
            
            }       
            QPushButton:pressed {
                background-color: rgb(30, 30, 30);
                border-style: inset;
            } 
            QPushButton:hover {
                background-color: """+self.hover_button+""";
                border-style: inset;
            } 
            QPushButton:disabled{ 
                Background-color: """ + self.disabled_button + """;
                color:  """ + self.disbled_buttons + """;
                min-height: 40px;
                border-radius: 2px;
                border: 1px solid #000}
                
                
                
            QLabel {
                Background: """ + self.buttons + """;
                background-color: """ + self.frame_image + """;
                color: """+self.secondaryText + """;
                font-size: 11pt;
            }    
            QFrame {
                background-color: """ + self.background + """;
            }
            
            
        QMenuBar {
        background-color: #C7C7C7;
        color: #000;
        }
             QMenuBar::item {
            background-color: #C7C7C7;
            color: #000;
        }

        QMenuBar::item::selected {
            background-color: #9E9E9E;
        }

        QMenuBar::item:pressed { /// working
        background: orange;
        color:blue;
        }
        QMessageBox {
            background-color: #333333;
        }

        QMessageBox QLabel {
            color: #aaa;
}
        
            
        """
        self.widget.setStyleSheet(styleWindow)
        
        style_frame_image = """
            background: """ + self.frame_image + """;
            border: 1px solid #000;
        """
        style_frame_image_frame = """
            background: """ + self.background + """;
        """
        style_model_menu = """
            background: """ + self.frame_image + """;
        """
        style_covidRX = """
            background: """ + self.frame_image + """;
            color: #557c3e;
            font-size: 18pt;
            text-transform: uppercase;
            font-weight: bold;
        """
        style_Umag= """
            background: """ + self.frame_image + """;
            font-size: 9pt;
            font-weight: bold;
        """
        self.window.label_4.setStyleSheet(style_frame_image)
        self.window.label_5.setStyleSheet(style_frame_image)
        
        self.window.label_covid.setStyleSheet(style_covidRX)
        self.window.universidad.setStyleSheet(style_Umag)
        # self.window.listWidget.setStyleSheet( 
        #         "QListWidget::item {"
        #             "border-style: solid;" 
        #             "border-width:1px;" 
        #             "border-color:black;" 
        #             "background-color: #DDDBF1;"
        #         "}"
        #         "QListWidget::item:selected {"
        #             "background-color: #7F95D1;"
        #             "color: #1F1F1F;"
        #         "}");
        # self.window.frameDisplayImage.setStyleSheet(style_frame_image_frame) 
        self.widget.setWindowState(QtCore.Qt.WindowMaximized)
        
        