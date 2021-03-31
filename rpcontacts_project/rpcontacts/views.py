# -*- coding: utf-8 -*-
"""This module provides views to mage the contacts table."""
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import(
	QAbstractItemView,
	QDialog,
	QDialogButtonBox,
	QFormLayout,
	QHBoxLayout,
	QLineEdit,
	QMainWindow,
	QMessageBox,
	QPushButton,
	QTableView,
	QVBoxLayout,
	QWidget,
	)
from .model import ContactsModel


class Window(QMainWindow):
	#Main Window

	def __init__(self, parent=None):
		#initializer
		super().__init__(parent)
		self.setWindowTitle("RP Contacts")
		self.resize(550, 250)
		self.centralWidget = QWidget()
		self.setCentralWidget(self.centralWidget)
		self.layout = QHBoxLayout()
		self.centralWidget.setLayout(self.layout)

		self.contactsModel = ContactsModel()
		self.setupUI()

	def setupUI(self):
		#Setup the main windows GUI

		#Create the table view widget.
		self.table = QTableView()
		self.table.setModel(self.contactsModel.model)
		self.table.setSelectionBehavior(QAbstractItemView.SelectRows)
		self.table.resizeColumnsToContents()
		#Create the buttons
		self.addButton = QPushButton("Add...")
		self.deleteButton = QPushButton("Delete")
		self.clearAllButton = QPushButton("clear All")
		#Lay out the GUI
		layout = QVBoxLayout()
		layout.addWidget(self.addButton)
		layout.addWidget(self.deleteButton)
		layout.addStretch()
		layout.addWidget(self.clearAllButton)
		self.layout.addWidget(self.table)
		self.layout.addLayout(layout)

class AddDialog(QDialog):
	#Add Contact dialog
	def __init__(self, parent=None):
		#Initializer
		super().__init__(parent=parent)
		self.setWindowTitle("Add Contacts")
		self.layout = QVBoxLayout()
		self.setLayout(self.layout)
		self.data = None

		self.setupUI()
	
	def setupUI(self):
		#Set up the add Contact dialogs GUI
		#Create line edits for data fields
		self.nameField = QLineEdit()
		self.nameField.setObjectName("Name")
		self.jobField = QLineEdit()
		self.jobField.setObjectName("Job")
		self.emailField = QLineEdit()
		self.emailField.setObjectName("Email")
		#Layout the data fields
		layout = QFormLayout()
		layout.addRow("Name:", self.nameField)
		layout.addRow("Job:", self.jobField)
		layout.addRow("Email:", self.emailField)
		self.layout.addLayout(layout)
		#add standart buttons to the dialog and connect them
		self.buttonsBox = QDialogButtonBox(self)
		self.buttonsBox.setOrientation(Qt.Horizontal)
		self.buttonsBox.setStandardButtons(
			QDialogButtonBox.Ok | QDialogButtonBox.Cancel
			)
		self.buttonsBox.accepted.connect(self.accept)
		self.buttonsBox.rejected.connect(self.reject)
		self.layout.addWidget(self.buttonsBox)

	def accept(self):
		#Accept the data provides through the dialog
		self.data = []
		for field in (self.nameField, self.jobField, self.emailField):
			if not field.text():
				QMessageBox.critical(
					self,
					"Error!",
					f"You must provide a contacts {field.setObjectName()}",
					)
				self.data = None #Reset .data
				return

			self.data.append(field.text())

		if not self.data:
			return

		super().appect()