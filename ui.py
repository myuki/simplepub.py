from book import *
from layout import *

from PySide6 import QtCore, QtGui, QtWidgets
import os


class UI(QMainWindow):
  book: RawBook

  def __init__(self):
    super(UI, self).__init__()
    self.ui = Ui_MainWindow()
    self.ui.setupUi(self)

  @QtCore.Slot()
  def on_openFileButton_clicked(self):
    # Open text file
    filePath, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Open File", os.getcwd(), "Text Files(*.txt);;All Files(*)")

    if filePath != "":
      self.ui.filePathLineEdit.setText(filePath)
      self.book = RawBook(filePath)

      # Display data in different raw text type
      if self.book.rawTextType != RawTextType.default:
        # Metadata
        self.ui.titleLineEdit.setText(self.book.title)
        self.ui.authorLineEdit.setText(self.book.author)
        self.ui.illustratorLineEdit.setText(self.book.illustrator)
        self.ui.translatorLineEdit.setText(self.book.translator)
        self.ui.sourceLineEdit.setText(self.book.source)
        self.ui.languageLineEdit.setText(self.book.language)
        self.ui.subjectLineEdit.setText(self.book.subject)

        # Illustration flag
        self.ui.IllustrationPrefixLineEdit.setText(self.book.illustrationPrefix)
        self.ui.IllustrationSuffixLineEdit.setText(self.book.illustrationSuffix)

      # Display contents
      self.book.initContents()
      if self.book.contents != []:
        contents: str = ""
        for chapter in self.book.contents:
          indent: str = "\t" * chapter.level
          contents = contents + indent + chapter.string + "\n"
        self.ui.contentsTextEdit.setPlainText(contents.strip())

  @QtCore.Slot()
  def on_okButton_clicked(self):
    # Set metadata
    self.book.title = self.ui.titleLineEdit.text()
    self.book.author = self.ui.authorLineEdit.text()
    self.book.illustrator = self.ui.illustratorLineEdit.text()
    self.book.translator = self.ui.translatorLineEdit.text()
    self.book.source = self.ui.sourceLineEdit.text()
    self.book.language = self.ui.languageLineEdit.text()
    self.book.subject = self.ui.subjectLineEdit.text()

    # Set illustration flag
    self.book.illustrationPrefix = self.ui.IllustrationPrefixLineEdit.text()
    self.book.illustrationSuffix = self.ui.IllustrationSuffixLineEdit.text()

    # Set contents
    self.book.setContents(self.ui.contentsTextEdit.toPlainText())
    self.book.initChaptersIndex()
