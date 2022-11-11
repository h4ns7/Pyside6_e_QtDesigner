# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Cadastro.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QTabWidget, QTableWidget, QTableWidgetItem, QTextEdit,
    QToolBox, QVBoxLayout, QWidget)
import icons__rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(992, 656)
        MainWindow.setStyleSheet(u"background-color: rgb(80, 98, 102);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"*{\n"
"\n"
"	border: none;\n"
"\n"
"}\n"
"\n"
"QLabel{\n"
"\n"
"	color:rgb(255,255,255);\n"
"}\n"
"\n"
"")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, -1, 0, -1)
        self.left_container = QFrame(self.centralwidget)
        self.left_container.setObjectName(u"left_container")
        self.left_container.setMaximumSize(QSize(200, 16777215))
        self.left_container.setFrameShape(QFrame.StyledPanel)
        self.left_container.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.left_container)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.left_container)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame)
        self.horizontalLayout_4.setSpacing(9)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 9, 0)
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_4.addWidget(self.label_3, 0, Qt.AlignHCenter)


        self.verticalLayout_2.addWidget(self.frame)

        self.frame_2 = QFrame(self.left_container)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(34, 65, 71);\n"
"}\n"
"\n"
"QToolBox{\n"
"\n"
"text-align: left;\n"
"background-color: rgb(115, 142, 148);\n"
"}\n"
"\n"
"QToolBox::tab{\n"
"\n"
"\n"
"borde-radius:2px;\n"
"text-align: left;\n"
"background-color: rgb(155, 191, 199);\n"
"\n"
"}")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.toolBox = QToolBox(self.frame_2)
        self.toolBox.setObjectName(u"toolBox")
        self.toolBox.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(34, 65, 71);\n"
"	border-top-left-radius: 15px\n"
"}\n"
"\n"
"QPushButton{\n"
"\n"
"	color: rgb(255,255,255);\n"
"\n"
"}")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page.setGeometry(QRect(0, 0, 200, 538))
        self.verticalLayout_4 = QVBoxLayout(self.page)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 9, 0, 0)
        self.btn_inicio = QPushButton(self.page)
        self.btn_inicio.setObjectName(u"btn_inicio")
        self.btn_inicio.setMinimumSize(QSize(0, 30))
        font = QFont()
        font.setPointSize(11)
        self.btn_inicio.setFont(font)
        self.btn_inicio.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_4.addWidget(self.btn_inicio)

        self.btn_cadastrar = QPushButton(self.page)
        self.btn_cadastrar.setObjectName(u"btn_cadastrar")
        self.btn_cadastrar.setMinimumSize(QSize(0, 30))
        self.btn_cadastrar.setFont(font)
        self.btn_cadastrar.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_4.addWidget(self.btn_cadastrar)

        self.btn_consultar = QPushButton(self.page)
        self.btn_consultar.setObjectName(u"btn_consultar")
        self.btn_consultar.setMinimumSize(QSize(0, 30))
        self.btn_consultar.setFont(font)
        self.btn_consultar.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_4.addWidget(self.btn_consultar)

        self.btn_contatos = QPushButton(self.page)
        self.btn_contatos.setObjectName(u"btn_contatos")
        self.btn_contatos.setMinimumSize(QSize(0, 30))
        self.btn_contatos.setFont(font)
        self.btn_contatos.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_4.addWidget(self.btn_contatos)

        self.btn_sobre = QPushButton(self.page)
        self.btn_sobre.setObjectName(u"btn_sobre")
        self.btn_sobre.setMinimumSize(QSize(0, 30))
        self.btn_sobre.setFont(font)
        self.btn_sobre.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_4.addWidget(self.btn_sobre)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.toolBox.addItem(self.page, u"Page 1")
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setGeometry(QRect(0, 0, 200, 538))
        self.verticalLayout_8 = QVBoxLayout(self.page_2)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.textEdit = QTextEdit(self.page_2)
        self.textEdit.setObjectName(u"textEdit")

        self.verticalLayout_8.addWidget(self.textEdit, 0, Qt.AlignVCenter)

        self.toolBox.addItem(self.page_2, u"Page 2")

        self.verticalLayout_3.addWidget(self.toolBox)


        self.verticalLayout_2.addWidget(self.frame_2)


        self.horizontalLayout.addWidget(self.left_container)

        self.main_container = QFrame(self.centralwidget)
        self.main_container.setObjectName(u"main_container")
        self.main_container.setFrameShape(QFrame.StyledPanel)
        self.main_container.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.main_container)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.head_frame = QFrame(self.main_container)
        self.head_frame.setObjectName(u"head_frame")
        self.head_frame.setFrameShape(QFrame.StyledPanel)
        self.head_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.head_frame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 8)
        self.btn_toggle = QPushButton(self.head_frame)
        self.btn_toggle.setObjectName(u"btn_toggle")
        icon = QIcon()
        icon.addFile(u":/newPrefix/menu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_toggle.setIcon(icon)
        self.btn_toggle.setIconSize(QSize(32, 32))

        self.horizontalLayout_2.addWidget(self.btn_toggle, 0, Qt.AlignLeft)

        self.label = QLabel(self.head_frame)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)


        self.verticalLayout.addWidget(self.head_frame)

        self.main_frame = QFrame(self.main_container)
        self.main_frame.setObjectName(u"main_frame")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_frame.sizePolicy().hasHeightForWidth())
        self.main_frame.setSizePolicy(sizePolicy)
        self.main_frame.setStyleSheet(u"background-color: rgb(34, 65, 71);")
        self.main_frame.setFrameShape(QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.main_frame)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.pages = QStackedWidget(self.main_frame)
        self.pages.setObjectName(u"pages")
        self.pg_home = QWidget()
        self.pg_home.setObjectName(u"pg_home")
        self.verticalLayout_6 = QVBoxLayout(self.pg_home)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.logo = QLabel(self.pg_home)
        self.logo.setObjectName(u"logo")

        self.verticalLayout_6.addWidget(self.logo)

        self.pages.addWidget(self.pg_home)
        self.pg_cadastrar = QWidget()
        self.pg_cadastrar.setObjectName(u"pg_cadastrar")
        self.verticalLayout_7 = QVBoxLayout(self.pg_cadastrar)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.tabWidget = QTabWidget(self.pg_cadastrar)
        self.tabWidget.setObjectName(u"tabWidget")
        self.cadastro_aluno = QWidget()
        self.cadastro_aluno.setObjectName(u"cadastro_aluno")
        self.verticalLayout_10 = QVBoxLayout(self.cadastro_aluno)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.frame_cadastro = QFrame(self.cadastro_aluno)
        self.frame_cadastro.setObjectName(u"frame_cadastro")
        self.frame_cadastro.setStyleSheet(u"QLineEdit{\n"
"\n"
"	background-color: rgb(255,255,255);\n"
"	font: 10pt \"MS Shell Dlg 2\";	\n"
"}\n"
"\n"
"QFrame{\n"
"\n"
"	background-color: rgb(231,231,231);\n"
"}\n"
"")
        self.frame_cadastro.setFrameShape(QFrame.StyledPanel)
        self.frame_cadastro.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_cadastro)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_cadastro_aluno = QLabel(self.frame_cadastro)
        self.label_cadastro_aluno.setObjectName(u"label_cadastro_aluno")
        self.label_cadastro_aluno.setStyleSheet(u"color: rgb(155, 191, 199);")

        self.gridLayout.addWidget(self.label_cadastro_aluno, 0, 0, 1, 6)

        self.txt_nome = QLineEdit(self.frame_cadastro)
        self.txt_nome.setObjectName(u"txt_nome")
        self.txt_nome.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_nome, 1, 0, 1, 4)

        self.txt_email = QLineEdit(self.frame_cadastro)
        self.txt_email.setObjectName(u"txt_email")
        self.txt_email.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_email, 1, 4, 1, 2)

        self.txt_cpf = QLineEdit(self.frame_cadastro)
        self.txt_cpf.setObjectName(u"txt_cpf")
        self.txt_cpf.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_cpf, 2, 0, 1, 2)

        self.txt_complemento = QLineEdit(self.frame_cadastro)
        self.txt_complemento.setObjectName(u"txt_complemento")
        self.txt_complemento.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_complemento, 4, 2, 1, 3)

        self.txt_numero = QLineEdit(self.frame_cadastro)
        self.txt_numero.setObjectName(u"txt_numero")
        self.txt_numero.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_numero, 4, 5, 1, 1)

        self.txt_uf = QLineEdit(self.frame_cadastro)
        self.txt_uf.setObjectName(u"txt_uf")
        self.txt_uf.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_uf, 5, 4, 1, 2)

        self.txt_datanascimento = QLineEdit(self.frame_cadastro)
        self.txt_datanascimento.setObjectName(u"txt_datanascimento")
        self.txt_datanascimento.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_datanascimento, 2, 3, 1, 2)

        self.txt_logradouro = QLineEdit(self.frame_cadastro)
        self.txt_logradouro.setObjectName(u"txt_logradouro")
        self.txt_logradouro.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_logradouro, 3, 0, 1, 6)

        self.txt_municipio = QLineEdit(self.frame_cadastro)
        self.txt_municipio.setObjectName(u"txt_municipio")
        self.txt_municipio.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_municipio, 5, 0, 1, 3)

        self.txt_cep = QLineEdit(self.frame_cadastro)
        self.txt_cep.setObjectName(u"txt_cep")
        self.txt_cep.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_cep, 4, 0, 1, 1)

        self.txt_telefone = QLineEdit(self.frame_cadastro)
        self.txt_telefone.setObjectName(u"txt_telefone")
        self.txt_telefone.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_telefone, 2, 5, 1, 1)


        self.verticalLayout_10.addWidget(self.frame_cadastro)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_10.addItem(self.verticalSpacer_5)

        self.btn_cadastro = QPushButton(self.cadastro_aluno)
        self.btn_cadastro.setObjectName(u"btn_cadastro")
        self.btn_cadastro.setMinimumSize(QSize(120, 30))
        self.btn_cadastro.setFont(font)
        self.btn_cadastro.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_cadastro.setStyleSheet(u"QPushButton:hover{\n"
"\n"
"	background-color:rgb(115, 142, 148);\n"
"	border-radius: 15px;\n"
"	color: #fff\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton{\n"
"	border-radius: 15px;\n"
"	background-color: rgb(155, 191, 199);\n"
"	\n"
"}")

        self.verticalLayout_10.addWidget(self.btn_cadastro, 0, Qt.AlignHCenter)

        self.tabWidget.addTab(self.cadastro_aluno, "")
        self.cadastro_instrutor = QWidget()
        self.cadastro_instrutor.setObjectName(u"cadastro_instrutor")
        self.verticalLayout_11 = QVBoxLayout(self.cadastro_instrutor)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.frame_cadastro_2 = QFrame(self.cadastro_instrutor)
        self.frame_cadastro_2.setObjectName(u"frame_cadastro_2")
        self.frame_cadastro_2.setStyleSheet(u"QLineEdit{\n"
"\n"
"	background-color: rgb(255,255,255);\n"
"	font: 10pt \"MS Shell Dlg 2\";	\n"
"}\n"
"\n"
"QFrame{\n"
"\n"
"	background-color: rgb(231,231,231);\n"
"}\n"
"")
        self.frame_cadastro_2.setFrameShape(QFrame.StyledPanel)
        self.frame_cadastro_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_cadastro_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.txt_complemento_2 = QLineEdit(self.frame_cadastro_2)
        self.txt_complemento_2.setObjectName(u"txt_complemento_2")
        self.txt_complemento_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.txt_complemento_2, 5, 1, 1, 2)

        self.txt_municipio_2 = QLineEdit(self.frame_cadastro_2)
        self.txt_municipio_2.setObjectName(u"txt_municipio_2")
        self.txt_municipio_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.txt_municipio_2, 5, 3, 1, 2)

        self.txt_uf_2 = QLineEdit(self.frame_cadastro_2)
        self.txt_uf_2.setObjectName(u"txt_uf_2")
        self.txt_uf_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.txt_uf_2, 5, 5, 1, 1)

        self.txt_cep_2 = QLineEdit(self.frame_cadastro_2)
        self.txt_cep_2.setObjectName(u"txt_cep_2")
        self.txt_cep_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.txt_cep_2, 3, 3, 1, 3)

        self.txt_numero_2 = QLineEdit(self.frame_cadastro_2)
        self.txt_numero_2.setObjectName(u"txt_numero_2")
        self.txt_numero_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.txt_numero_2, 5, 0, 1, 1)

        self.txt_logradouro_2 = QLineEdit(self.frame_cadastro_2)
        self.txt_logradouro_2.setObjectName(u"txt_logradouro_2")
        self.txt_logradouro_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.txt_logradouro_2, 4, 0, 1, 6)

        self.txt_nome_2 = QLineEdit(self.frame_cadastro_2)
        self.txt_nome_2.setObjectName(u"txt_nome_2")
        self.txt_nome_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.txt_nome_2, 1, 0, 1, 4)

        self.txt_email_2 = QLineEdit(self.frame_cadastro_2)
        self.txt_email_2.setObjectName(u"txt_email_2")
        self.txt_email_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.txt_email_2, 1, 4, 1, 2)

        self.txt_datanascimento_2 = QLineEdit(self.frame_cadastro_2)
        self.txt_datanascimento_2.setObjectName(u"txt_datanascimento_2")
        self.txt_datanascimento_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.txt_datanascimento_2, 2, 2, 1, 3)

        self.txt_valor_hora_2 = QLineEdit(self.frame_cadastro_2)
        self.txt_valor_hora_2.setObjectName(u"txt_valor_hora_2")
        self.txt_valor_hora_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.txt_valor_hora_2, 2, 5, 1, 1)

        self.txt_cpf_2 = QLineEdit(self.frame_cadastro_2)
        self.txt_cpf_2.setObjectName(u"txt_cpf_2")
        self.txt_cpf_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.txt_cpf_2, 2, 0, 1, 2)

        self.txt_telefone_2 = QLineEdit(self.frame_cadastro_2)
        self.txt_telefone_2.setObjectName(u"txt_telefone_2")
        self.txt_telefone_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.txt_telefone_2, 3, 0, 1, 3)

        self.label_cadastro_instrutor = QLabel(self.frame_cadastro_2)
        self.label_cadastro_instrutor.setObjectName(u"label_cadastro_instrutor")
        self.label_cadastro_instrutor.setStyleSheet(u"color: rgb(155, 191, 199);")

        self.gridLayout_2.addWidget(self.label_cadastro_instrutor, 0, 0, 1, 6)


        self.verticalLayout_11.addWidget(self.frame_cadastro_2)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_11.addItem(self.verticalSpacer_4)

        self.btn_cadastro_2 = QPushButton(self.cadastro_instrutor)
        self.btn_cadastro_2.setObjectName(u"btn_cadastro_2")
        self.btn_cadastro_2.setMinimumSize(QSize(120, 30))
        self.btn_cadastro_2.setFont(font)
        self.btn_cadastro_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_cadastro_2.setStyleSheet(u"QPushButton:hover{\n"
"\n"
"	background-color:rgb(115, 142, 148);\n"
"	border-radius: 15px;\n"
"	color: #fff\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton{\n"
"	border-radius: 15px;\n"
"	background-color: rgb(155, 191, 199);\n"
"	\n"
"}")

        self.verticalLayout_11.addWidget(self.btn_cadastro_2, 0, Qt.AlignHCenter)

        self.tabWidget.addTab(self.cadastro_instrutor, "")
        self.cadatro_curso = QWidget()
        self.cadatro_curso.setObjectName(u"cadatro_curso")
        self.verticalLayout_12 = QVBoxLayout(self.cadatro_curso)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.frame_curso = QFrame(self.cadatro_curso)
        self.frame_curso.setObjectName(u"frame_curso")
        self.frame_curso.setStyleSheet(u"QLineEdit{\n"
"\n"
"	background-color: rgb(255,255,255);\n"
"	font: 10pt \"MS Shell Dlg 2\";	\n"
"}\n"
"\n"
"QFrame{\n"
"\n"
"	background-color: rgb(231,231,231);\n"
"}\n"
"")
        self.frame_curso.setFrameShape(QFrame.StyledPanel)
        self.frame_curso.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_curso)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_7 = QLabel(self.frame_curso)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"color: rgb(155, 191, 199);")

        self.gridLayout_4.addWidget(self.label_7, 0, 0, 1, 2)

        self.carga_horaria_3 = QLineEdit(self.frame_curso)
        self.carga_horaria_3.setObjectName(u"carga_horaria_3")
        self.carga_horaria_3.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.carga_horaria_3, 5, 0, 1, 1)

        self.instrutor_responsavel_3 = QLineEdit(self.frame_curso)
        self.instrutor_responsavel_3.setObjectName(u"instrutor_responsavel_3")
        self.instrutor_responsavel_3.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.instrutor_responsavel_3, 3, 0, 1, 2)

        self.valor_hora_3 = QLineEdit(self.frame_curso)
        self.valor_hora_3.setObjectName(u"valor_hora_3")
        self.valor_hora_3.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.valor_hora_3, 5, 1, 1, 1)

        self.nome_curso_3 = QLineEdit(self.frame_curso)
        self.nome_curso_3.setObjectName(u"nome_curso_3")
        self.nome_curso_3.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.nome_curso_3, 2, 0, 1, 2)


        self.verticalLayout_12.addWidget(self.frame_curso)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_12.addItem(self.verticalSpacer_2)

        self.btn_cadastro_3 = QPushButton(self.cadatro_curso)
        self.btn_cadastro_3.setObjectName(u"btn_cadastro_3")
        self.btn_cadastro_3.setMinimumSize(QSize(120, 30))
        self.btn_cadastro_3.setFont(font)
        self.btn_cadastro_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_cadastro_3.setStyleSheet(u"QPushButton:hover{\n"
"\n"
"	background-color:rgb(115, 142, 148);\n"
"	border-radius: 15px;\n"
"	color: #fff\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton{\n"
"	border-radius: 15px;\n"
"	background-color: rgb(155, 191, 199);\n"
"	\n"
"}")

        self.verticalLayout_12.addWidget(self.btn_cadastro_3, 0, Qt.AlignHCenter)

        self.tabWidget.addTab(self.cadatro_curso, "")

        self.verticalLayout_7.addWidget(self.tabWidget)

        self.pages.addWidget(self.pg_cadastrar)
        self.pg_consultar = QWidget()
        self.pg_consultar.setObjectName(u"pg_consultar")
        self.verticalLayout_19 = QVBoxLayout(self.pg_consultar)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.tabWidget_2 = QTabWidget(self.pg_consultar)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        self.tab_7 = QWidget()
        self.tab_7.setObjectName(u"tab_7")
        self.verticalLayout_32 = QVBoxLayout(self.tab_7)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.label_22 = QLabel(self.tab_7)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setAutoFillBackground(False)
        self.label_22.setStyleSheet(u"background-color: rgb(155, 191, 199);")

        self.verticalLayout_32.addWidget(self.label_22)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.tableWidget_8 = QTableWidget(self.tab_7)
        if (self.tableWidget_8.columnCount() < 11):
            self.tableWidget_8.setColumnCount(11)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget_8.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget_8.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget_8.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget_8.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget_8.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget_8.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget_8.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget_8.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget_8.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget_8.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget_8.setHorizontalHeaderItem(10, __qtablewidgetitem10)
        self.tableWidget_8.setObjectName(u"tableWidget_8")
        self.tableWidget_8.setStyleSheet(u"QHeaderView::section {\n"
"\n"
"	background-color: rgb(115, 142, 148);\n"
"	color: rgb(255,255,255);\n"
"	font: 10pt \"MS Shel  Dlg 2\";\n"
"\n"
"}\n"
"\n"
"\n"
"QTableWidget{\n"
"	\n"
"background-color: rgb(252, 252, 252);\n"
"\n"
"}")

        self.horizontalLayout_12.addWidget(self.tableWidget_8)

        self.frame_16 = QFrame(self.tab_7)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setStyleSheet(u"\n"
"\n"
"QFrame {\n"
"	\n"
"	background-color: rgb(230,230,230);\n"
"\n"
"}\n"
"\n"
"QPushButton{\n"
"\n"
"	border-radius:15px;\n"
"	background-color: rgb(155, 191, 199);\n"
"	font: 11 pt \"MS Shell Dlg 2\";\n"
"	color:  rgb(34, 65, 71);\n"
"\n"
"}")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.verticalLayout_31 = QVBoxLayout(self.frame_16)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.btn_excel_8 = QPushButton(self.frame_16)
        self.btn_excel_8.setObjectName(u"btn_excel_8")
        self.btn_excel_8.setMinimumSize(QSize(100, 30))
        font1 = QFont()
        font1.setFamilies([u"MS Shell Dlg 2"])
        font1.setPointSize(8)
        font1.setBold(False)
        font1.setItalic(False)
        self.btn_excel_8.setFont(font1)
        self.btn_excel_8.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_excel_8.setStyleSheet(u"QPushButton:hover{\n"
"\n"
"	color: rgb(255,255,255);\n"
"	background-color: rgb(49,147,0);\n"
"\n"
"\n"
"}")

        self.verticalLayout_31.addWidget(self.btn_excel_8)

        self.btn_alterar_8 = QPushButton(self.frame_16)
        self.btn_alterar_8.setObjectName(u"btn_alterar_8")
        self.btn_alterar_8.setMinimumSize(QSize(100, 30))
        self.btn_alterar_8.setFont(font1)
        self.btn_alterar_8.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_alterar_8.setStyleSheet(u"QPushButton:hover{\n"
"\n"
"	color: rgb(255,255,255);\n"
"	background-color:rgb(253, 210, 10)\n"
"\n"
"\n"
"}")

        self.verticalLayout_31.addWidget(self.btn_alterar_8)

        self.btn_excluir_8 = QPushButton(self.frame_16)
        self.btn_excluir_8.setObjectName(u"btn_excluir_8")
        self.btn_excluir_8.setMinimumSize(QSize(100, 30))
        self.btn_excluir_8.setFont(font1)
        self.btn_excluir_8.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_excluir_8.setStyleSheet(u"QPushButton:hover{\n"
"\n"
"	color: rgb(255,255,255);\n"
"	background-color: rgb(236, 37, 66)\n"
"\n"
"\n"
"}")

        self.verticalLayout_31.addWidget(self.btn_excluir_8)

        self.verticalSpacer_15 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_31.addItem(self.verticalSpacer_15)


        self.horizontalLayout_12.addWidget(self.frame_16)


        self.verticalLayout_32.addLayout(self.horizontalLayout_12)

        self.tabWidget_2.addTab(self.tab_7, "")
        self.tab_8 = QWidget()
        self.tab_8.setObjectName(u"tab_8")
        self.verticalLayout_21 = QVBoxLayout(self.tab_8)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.label_15 = QLabel(self.tab_8)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setAutoFillBackground(False)
        self.label_15.setStyleSheet(u"background-color: rgb(155, 191, 199);")

        self.verticalLayout_21.addWidget(self.label_15)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.tableWidget_4 = QTableWidget(self.tab_8)
        if (self.tableWidget_4.columnCount() < 12):
            self.tableWidget_4.setColumnCount(12)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(0, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(1, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(2, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(3, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(4, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(5, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(6, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(7, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(8, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(9, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(10, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(11, __qtablewidgetitem22)
        self.tableWidget_4.setObjectName(u"tableWidget_4")
        self.tableWidget_4.setStyleSheet(u"QHeaderView::section {\n"
"\n"
"	background-color: rgb(115, 142, 148);\n"
"	color: rgb(255,255,255);\n"
"	font: 10pt \"MS Shel  Dlg 2\";\n"
"\n"
"}\n"
"\n"
"\n"
"QTableWidget{\n"
"	\n"
"background-color: rgb(252, 252, 252);\n"
"\n"
"}")

        self.horizontalLayout_8.addWidget(self.tableWidget_4)

        self.frame_9 = QFrame(self.tab_8)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setStyleSheet(u"\n"
"\n"
"QFrame {\n"
"	\n"
"	background-color: rgb(230,230,230);\n"
"\n"
"}\n"
"\n"
"QPushButton{\n"
"\n"
"	border-radius:15px;\n"
"	background-color: rgb(155, 191, 199);\n"
"	font: 11 pt \"MS Shell Dlg 2\";\n"
"	color:  rgb(34, 65, 71);\n"
"\n"
"}")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.frame_9)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.btn_excel_4 = QPushButton(self.frame_9)
        self.btn_excel_4.setObjectName(u"btn_excel_4")
        self.btn_excel_4.setMinimumSize(QSize(100, 30))
        self.btn_excel_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_excel_4.setStyleSheet(u"QPushButton:hover{\n"
"\n"
"	color: rgb(255,255,255);\n"
"	background-color: rgb(49,147,0);\n"
"\n"
"\n"
"}")

        self.verticalLayout_20.addWidget(self.btn_excel_4)

        self.btn_alterar_4 = QPushButton(self.frame_9)
        self.btn_alterar_4.setObjectName(u"btn_alterar_4")
        self.btn_alterar_4.setMinimumSize(QSize(100, 30))
        self.btn_alterar_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_alterar_4.setStyleSheet(u"QPushButton:hover{\n"
"\n"
"	color: rgb(255,255,255);\n"
"	background-color:rgb(253, 210, 10)\n"
"\n"
"\n"
"}")

        self.verticalLayout_20.addWidget(self.btn_alterar_4)

        self.btn_excluir_4 = QPushButton(self.frame_9)
        self.btn_excluir_4.setObjectName(u"btn_excluir_4")
        self.btn_excluir_4.setMinimumSize(QSize(100, 30))
        self.btn_excluir_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_excluir_4.setStyleSheet(u"QPushButton:hover{\n"
"\n"
"	color: rgb(255,255,255);\n"
"	background-color: rgb(236, 37, 66)\n"
"\n"
"\n"
"}")

        self.verticalLayout_20.addWidget(self.btn_excluir_4)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_20.addItem(self.verticalSpacer_8)


        self.horizontalLayout_8.addWidget(self.frame_9)


        self.verticalLayout_21.addLayout(self.horizontalLayout_8)

        self.tabWidget_2.addTab(self.tab_8, "")
        self.tab_9 = QWidget()
        self.tab_9.setObjectName(u"tab_9")
        self.verticalLayout_34 = QVBoxLayout(self.tab_9)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.label_23 = QLabel(self.tab_9)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setAutoFillBackground(False)
        self.label_23.setStyleSheet(u"background-color: rgb(155, 191, 199);")

        self.verticalLayout_34.addWidget(self.label_23)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.tableWidget_9 = QTableWidget(self.tab_9)
        if (self.tableWidget_9.columnCount() < 8):
            self.tableWidget_9.setColumnCount(8)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tableWidget_9.setHorizontalHeaderItem(0, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.tableWidget_9.setHorizontalHeaderItem(1, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.tableWidget_9.setHorizontalHeaderItem(2, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.tableWidget_9.setHorizontalHeaderItem(3, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.tableWidget_9.setHorizontalHeaderItem(4, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.tableWidget_9.setHorizontalHeaderItem(5, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.tableWidget_9.setHorizontalHeaderItem(6, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.tableWidget_9.setHorizontalHeaderItem(7, __qtablewidgetitem30)
        self.tableWidget_9.setObjectName(u"tableWidget_9")
        self.tableWidget_9.setStyleSheet(u"QHeaderView::section {\n"
"\n"
"	background-color: rgb(115, 142, 148);\n"
"	color: rgb(255,255,255);\n"
"	font: 10pt \"MS Shel  Dlg 2\";\n"
"\n"
"}\n"
"\n"
"\n"
"QTableWidget{\n"
"	\n"
"background-color: rgb(252, 252, 252);\n"
"\n"
"}")

        self.horizontalLayout_13.addWidget(self.tableWidget_9)

        self.frame_17 = QFrame(self.tab_9)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setStyleSheet(u"\n"
"\n"
"QFrame {\n"
"	\n"
"	background-color: rgb(230,230,230);\n"
"\n"
"}\n"
"\n"
"QPushButton{\n"
"\n"
"	border-radius:15px;\n"
"	background-color: rgb(155, 191, 199);\n"
"	font: 11 pt \"MS Shell Dlg 2\";\n"
"	color:  rgb(34, 65, 71);\n"
"\n"
"}")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.verticalLayout_33 = QVBoxLayout(self.frame_17)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.btn_excel_9 = QPushButton(self.frame_17)
        self.btn_excel_9.setObjectName(u"btn_excel_9")
        self.btn_excel_9.setMinimumSize(QSize(100, 30))
        self.btn_excel_9.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_excel_9.setStyleSheet(u"QPushButton:hover{\n"
"\n"
"	color: rgb(255,255,255);\n"
"	background-color: rgb(49,147,0);\n"
"\n"
"\n"
"}")

        self.verticalLayout_33.addWidget(self.btn_excel_9)

        self.btn_alterar_9 = QPushButton(self.frame_17)
        self.btn_alterar_9.setObjectName(u"btn_alterar_9")
        self.btn_alterar_9.setMinimumSize(QSize(100, 30))
        self.btn_alterar_9.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_alterar_9.setStyleSheet(u"QPushButton:hover{\n"
"\n"
"	color: rgb(255,255,255);\n"
"	background-color:rgb(253, 210, 10)\n"
"\n"
"\n"
"}")

        self.verticalLayout_33.addWidget(self.btn_alterar_9)

        self.btn_excluir_9 = QPushButton(self.frame_17)
        self.btn_excluir_9.setObjectName(u"btn_excluir_9")
        self.btn_excluir_9.setMinimumSize(QSize(100, 30))
        self.btn_excluir_9.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_excluir_9.setStyleSheet(u"QPushButton:hover{\n"
"\n"
"	color: rgb(255,255,255);\n"
"	background-color: rgb(236, 37, 66)\n"
"\n"
"\n"
"}")

        self.verticalLayout_33.addWidget(self.btn_excluir_9)

        self.verticalSpacer_16 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_33.addItem(self.verticalSpacer_16)


        self.horizontalLayout_13.addWidget(self.frame_17)


        self.verticalLayout_34.addLayout(self.horizontalLayout_13)

        self.tabWidget_2.addTab(self.tab_9, "")

        self.verticalLayout_19.addWidget(self.tabWidget_2)

        self.pages.addWidget(self.pg_consultar)
        self.pg_contatos = QWidget()
        self.pg_contatos.setObjectName(u"pg_contatos")
        self.verticalLayout_9 = QVBoxLayout(self.pg_contatos)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_4 = QLabel(self.pg_contatos)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_9.addWidget(self.label_4)

        self.label_11 = QLabel(self.pg_contatos)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setLayoutDirection(Qt.LeftToRight)
        self.label_11.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_11)

        self.label_12 = QLabel(self.pg_contatos)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setLayoutDirection(Qt.LeftToRight)
        self.label_12.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_12)

        self.label_13 = QLabel(self.pg_contatos)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setLayoutDirection(Qt.LeftToRight)
        self.label_13.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_13)

        self.pages.addWidget(self.pg_contatos)
        self.pg_sobre = QWidget()
        self.pg_sobre.setObjectName(u"pg_sobre")
        self.verticalLayout_18 = QVBoxLayout(self.pg_sobre)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.label_10 = QLabel(self.pg_sobre)
        self.label_10.setObjectName(u"label_10")

        self.verticalLayout_18.addWidget(self.label_10)

        self.label_14 = QLabel(self.pg_sobre)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setWordWrap(True)

        self.verticalLayout_18.addWidget(self.label_14)

        self.pages.addWidget(self.pg_sobre)

        self.verticalLayout_5.addWidget(self.pages)


        self.verticalLayout.addWidget(self.main_frame)

        self.footer_frame = QFrame(self.main_container)
        self.footer_frame.setObjectName(u"footer_frame")
        self.footer_frame.setFrameShape(QFrame.StyledPanel)
        self.footer_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.footer_frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(9, 0, 0, 0)
        self.label_2 = QLabel(self.footer_frame)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_3.addWidget(self.label_2)


        self.verticalLayout.addWidget(self.footer_frame)


        self.horizontalLayout.addWidget(self.main_container)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.toolBox.setCurrentIndex(0)
        self.pages.setCurrentIndex(2)
        self.tabWidget.setCurrentIndex(2)
        self.tabWidget_2.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><img src=\":/icons/nova (1).png\"/></p></body></html>", None))
        self.btn_inicio.setText(QCoreApplication.translate("MainWindow", u"Inicio", None))
        self.btn_cadastrar.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.btn_consultar.setText(QCoreApplication.translate("MainWindow", u"Consultar", None))
        self.btn_contatos.setText(QCoreApplication.translate("MainWindow", u"Contatos", None))
        self.btn_sobre.setText(QCoreApplication.translate("MainWindow", u"Sobre", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), QCoreApplication.translate("MainWindow", u"Page 1", None))
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">Usuario</span><span style=\" font-size:12pt;\">: Pilor School</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">Sistema</span><span style=\" font-"
                        "size:12pt;\">: Cadastro</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">Status</span><span style=\" font-size:12pt;\">: Ativo</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">Venc:</span><span style=\" font-size:12pt;\"> 01/01/2023</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bott"
                        "om:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p></body></html>", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), QCoreApplication.translate("MainWindow", u"Page 2", None))
        self.btn_toggle.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">Sistema de cadastro</span></p></body></html>", None))
        self.logo.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><img src=\":/icons/logo_ps-removebg-preview (1).png\"/></p></body></html>", None))
        self.label_cadastro_aluno.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Cadastro Aluno</span></p></body></html>", None))
        self.txt_nome.setPlaceholderText(QCoreApplication.translate("MainWindow", u"NOME", None))
        self.txt_email.setPlaceholderText(QCoreApplication.translate("MainWindow", u"E-MAIL", None))
        self.txt_cpf.setPlaceholderText(QCoreApplication.translate("MainWindow", u"CPF", None))
        self.txt_complemento.setPlaceholderText(QCoreApplication.translate("MainWindow", u"COMPLEMENTO", None))
        self.txt_numero.setPlaceholderText(QCoreApplication.translate("MainWindow", u"N\u00ba", None))
        self.txt_uf.setPlaceholderText(QCoreApplication.translate("MainWindow", u"UF", None))
        self.txt_datanascimento.setPlaceholderText(QCoreApplication.translate("MainWindow", u"DATA NASCIMENTO", None))
        self.txt_logradouro.setPlaceholderText(QCoreApplication.translate("MainWindow", u"LOUGRADOURO", None))
        self.txt_municipio.setPlaceholderText(QCoreApplication.translate("MainWindow", u"MUNICIPIO", None))
        self.txt_cep.setPlaceholderText(QCoreApplication.translate("MainWindow", u"CEP", None))
        self.txt_telefone.setPlaceholderText(QCoreApplication.translate("MainWindow", u"TELEFONE", None))
        self.btn_cadastro.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.cadastro_aluno), QCoreApplication.translate("MainWindow", u"Cadastro Aluno", None))
        self.txt_complemento_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"COMPLEMENTO", None))
        self.txt_municipio_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"MUNICIPIO", None))
        self.txt_uf_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"UF", None))
        self.txt_cep_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"CEP", None))
        self.txt_numero_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"N\u00ba", None))
        self.txt_logradouro_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"LOGRADOURO", None))
        self.txt_nome_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"NOME", None))
        self.txt_email_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"E-MAIL", None))
        self.txt_datanascimento_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"DATA NASCIMENTO", None))
        self.txt_valor_hora_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"VALOR HORA R$", None))
        self.txt_cpf_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"CPF", None))
        self.txt_telefone_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"TELEFONE", None))
        self.label_cadastro_instrutor.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Cadastro Insrutor</span></p></body></html>", None))
        self.btn_cadastro_2.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.cadastro_instrutor), QCoreApplication.translate("MainWindow", u"Cadastro Instrutor", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Cadastro Curso</span></p></body></html>", None))
        self.carga_horaria_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"CARGA HOR\u00c1RIA", None))
        self.instrutor_responsavel_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"INSTRUTOR RESPONS\u00c1VEL", None))
        self.valor_hora_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"VALOR R$", None))
        self.nome_curso_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"NOME DO CURSO", None))
        self.btn_cadastro_3.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.cadatro_curso), QCoreApplication.translate("MainWindow", u"Cadastro Curso", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Alunos</span></p></body></html>", None))
        ___qtablewidgetitem = self.tableWidget_8.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Nome", None));
        ___qtablewidgetitem1 = self.tableWidget_8.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"E-mail", None));
        ___qtablewidgetitem2 = self.tableWidget_8.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"CPF", None));
        ___qtablewidgetitem3 = self.tableWidget_8.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Data nascimento", None));
        ___qtablewidgetitem4 = self.tableWidget_8.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Telefone", None));
        ___qtablewidgetitem5 = self.tableWidget_8.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"CEP", None));
        ___qtablewidgetitem6 = self.tableWidget_8.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Lougradouro", None));
        ___qtablewidgetitem7 = self.tableWidget_8.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Numero", None));
        ___qtablewidgetitem8 = self.tableWidget_8.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Complemento", None));
        ___qtablewidgetitem9 = self.tableWidget_8.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Municipio", None));
        ___qtablewidgetitem10 = self.tableWidget_8.horizontalHeaderItem(10)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"UF", None));
        self.btn_excel_8.setText(QCoreApplication.translate("MainWindow", u"Gerar Excel", None))
        self.btn_alterar_8.setText(QCoreApplication.translate("MainWindow", u"Alterar", None))
        self.btn_excluir_8.setText(QCoreApplication.translate("MainWindow", u"Excluir", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_7), QCoreApplication.translate("MainWindow", u"Aluno", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Instrutores</span></p></body></html>", None))
        ___qtablewidgetitem11 = self.tableWidget_4.horizontalHeaderItem(0)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Nome", None));
        ___qtablewidgetitem12 = self.tableWidget_4.horizontalHeaderItem(1)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"E-mail", None));
        ___qtablewidgetitem13 = self.tableWidget_4.horizontalHeaderItem(2)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"CPF", None));
        ___qtablewidgetitem14 = self.tableWidget_4.horizontalHeaderItem(3)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Data nascimento", None));
        ___qtablewidgetitem15 = self.tableWidget_4.horizontalHeaderItem(4)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"Valor Hora R$", None));
        ___qtablewidgetitem16 = self.tableWidget_4.horizontalHeaderItem(5)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"Telefone", None));
        ___qtablewidgetitem17 = self.tableWidget_4.horizontalHeaderItem(6)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"CEP", None));
        ___qtablewidgetitem18 = self.tableWidget_4.horizontalHeaderItem(7)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"Lougradouro", None));
        ___qtablewidgetitem19 = self.tableWidget_4.horizontalHeaderItem(8)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"Numero", None));
        ___qtablewidgetitem20 = self.tableWidget_4.horizontalHeaderItem(9)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"Complemento", None));
        ___qtablewidgetitem21 = self.tableWidget_4.horizontalHeaderItem(10)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"Municipio", None));
        ___qtablewidgetitem22 = self.tableWidget_4.horizontalHeaderItem(11)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"UF", None));
        self.btn_excel_4.setText(QCoreApplication.translate("MainWindow", u"Gerar Excel", None))
        self.btn_alterar_4.setText(QCoreApplication.translate("MainWindow", u"Alterar", None))
        self.btn_excluir_4.setText(QCoreApplication.translate("MainWindow", u"Excluir", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_8), QCoreApplication.translate("MainWindow", u"Instrutor", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">Cursos</span></p></body></html>", None))
        ___qtablewidgetitem23 = self.tableWidget_9.horizontalHeaderItem(0)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"Nome", None));
        ___qtablewidgetitem24 = self.tableWidget_9.horizontalHeaderItem(1)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"CPF", None));
        ___qtablewidgetitem25 = self.tableWidget_9.horizontalHeaderItem(2)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"E-mail", None));
        ___qtablewidgetitem26 = self.tableWidget_9.horizontalHeaderItem(3)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"Telefone", None));
        ___qtablewidgetitem27 = self.tableWidget_9.horizontalHeaderItem(4)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"Data nascimento", None));
        ___qtablewidgetitem28 = self.tableWidget_9.horizontalHeaderItem(5)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"Estado", None));
        ___qtablewidgetitem29 = self.tableWidget_9.horizontalHeaderItem(6)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"Endere\u00e7o", None));
        ___qtablewidgetitem30 = self.tableWidget_9.horizontalHeaderItem(7)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"Bairro", None));
        self.btn_excel_9.setText(QCoreApplication.translate("MainWindow", u"Gerar Excel", None))
        self.btn_alterar_9.setText(QCoreApplication.translate("MainWindow", u"Alterar", None))
        self.btn_excluir_9.setText(QCoreApplication.translate("MainWindow", u"Excluir", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_9), QCoreApplication.translate("MainWindow", u"Curso", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">Contatos</span></p></body></html>", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><img src=\":/icons/icons8-whatsapp-48.png\"/><span style=\" font-size:28pt; vertical-align:super;\">(11)9800-7000 </span></p></body></html>", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><img src=\":/icons/icons8-circled-envelope-50.png\"/><span style=\" font-size:14pt;\"/><span style=\" font-size:26pt; vertical-align:super;\">contatopilotscholl@gmail.com</span></p></body></html>", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><img src=\":/icons/icons8-youtube-48.png\"/><span style=\" font-size:26pt; vertical-align:super;\">Pilot School</span></p></body></html>", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">Sobre</span></p></body></html>", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt;\">Esse sistema faz consulta do CEP, ultilizando a API do governo e faz cadastro no banco de dados SQLITE3. Objetvo desse sistema \u00e9 otimizar o cadastro da empresa Pilot school aplicando linguagem Python e aplica\u00e7\u00f5es modernas e funcionais ultilizadas pelo QT.</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt;\">\u00a9 Pilot School 2022</span></p></body></html>", None))
    # retranslateUi

