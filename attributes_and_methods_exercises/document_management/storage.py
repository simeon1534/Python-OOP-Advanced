from document_management.category import Category
from document_management.topic import Topic
from document_management.document import Document


class Storage:

    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def add_category(self, category: Category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic: Topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document: Document):
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id: int, new_name: str):
        for category_obj in self.categories:
            if category_obj.id == category_id:
                category_obj.name = new_name

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        for topic_obj in self.topics:
            if topic_obj.id == topic_id:
                topic_obj.topic = new_topic
                topic_obj.storage_folder = new_storage_folder

    def edit_document(self, document_id: int, new_file_name: str):
        for document_obj in self.documents:
            if document_obj.id == document_id:
                document_obj.file_name = new_file_name

    def delete_category(self, category_id):
        for category_obj in self.categories:
            if category_obj.id == category_id:
                self.categories.remove(category_obj)

    def delete_topic(self, topic_id):
        for topic_obj in self.topics:
            if topic_obj.id == topic_id:
                self.topics.remove(topic_obj)

    def delete_document(self, document_id):
        for document_obj in self.documents:
            if document_obj.id == document_id:
                self.documents.remove(document_obj)

    def get_document(self, document_id):
        for document_obj in self.documents:
            if document_obj.id == document_id:
                return document_obj

    def __repr__(self):
        res = []
        for document_obj in self.documents:
            res.append(document_obj.__repr__())

        return '\n'.join(res)



c1 = Category(1, "work")
t1 = Topic(1, "daily tasks", "C:\\work_documents")
d1 = Document(1, 1, 1, "finilize project")

d1.add_tag("urgent")
d1.add_tag("work")

storage = Storage()
storage.add_category(c1)
storage.add_topic(t1)
storage.add_document(d1)

print(c1)
print(t1)
print(storage.get_document(1))
print(storage)
