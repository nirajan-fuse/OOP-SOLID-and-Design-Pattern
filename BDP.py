# [Builder Design Pattern] Design a document generator using the Builder Design Pattern. Create a DocumentBuilder that creates 
# documents of various types (e.g., PDF, HTML, Plain Text). Implement the builder methods to format the document content and 
# structure according to the chosen type. Demonstrate how the Builder Design Pattern allows for the creation of different 
# document formats without tightly coupling the document generation logic.

from abc import ABC, abstractmethod

class Document:
    def __init__(self):
        self.title = None
        self.subject = None
        self.document = None

class DocumentBuilder(ABC):
    @abstractmethod
    def set_title(self, title):
        pass

    @abstractmethod
    def set_subject(self, subject):
        pass

    @abstractmethod
    def set_document(self, document):
        pass

class PDFBuilder(DocumentBuilder):
    def __init__(self, document):
        self.document = document()

    def set_title(self, title):
        self.document.title = title

    def set_subject(self, subject):
        self.document.subject = subject

    def set_document(self, document):
        self.document.document = document

class HTMLBuilder(DocumentBuilder):
    def __init__(self, document):
        self.document = document()

    def set_title(self, title):
        self.document.title = title

    def set_subject(self, subject):
        self.document.subject = subject

    def set_document(self, document):
        self.document.document = document

class PlainTextBuilder(DocumentBuilder):
    def __init__(self, document):
        self.document = document()

    def set_title(self, title):
        self.document.title = title

    def set_subject(self, subject):
        self.document.subject = subject

    def set_document(self, document):
        self.document.document = document

class DocumentDirector:
    def __init__(self, builder):
        self.builder = builder

    def build_document(self, title, subject, document):
        self.builder.set_title(title)
        self.builder.set_subject(subject)
        self.builder.set_document(document)

def main():
    plain_text_builder = PlainTextBuilder(Document)
    document_director = DocumentDirector(plain_text_builder)
    document_director.build_document("Plain Text", "Plain Text Subject", "Plain Text Document")

    built_document = plain_text_builder.document
    print("Title:", built_document.title)
    print("Subject:", built_document.subject)
    print("Content:", built_document.document)

if __name__ == "__main__":
    main()