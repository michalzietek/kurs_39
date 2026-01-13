# class ZUSReport:
#     def __init(self, document_id, status, document_name):
#         self.document_id = document_id
#         self.status = status
#         self.document_name = document_name
#
#     def generate_report(self):
#         print(f"Generating document {self.document_name} in status {self.status} with id {self.document_id}")
#
#     def approve_by_director(self):
#         self.status = "Approved"
#
#     def send_to_accountant(self):
#         print("Sending to accountant")
#
# class USReport:
#     def __init__(self, document_id, status, document_name):
#         self.document_id = document_id
#         self.status = status
#         self.document_name = document_name
#
#     def generate_report(self):
#         print(f"Generating document {self.document_name} in status {self.status} with id {self.document_id}")
#
#     def approve_by_director(self):
#         self.status = "Approved"
#
#     def send_to_accountant(self):
#         print("Sending to accountant")


class Report:
    def __init__(self, document_id, status, document_name):
        self.document_id = document_id
        self.status = status
        self.document_name = document_name

    def generate_report(self):
        print(f"Generating report for {self.document_name} with status {self.status} and id: {self.document_id}")

class DirectorApprover:

    @staticmethod
    def approve_report(report: Report):
        report.status = "Approved"

class AccountantSender:
    @staticmethod
    def send_documents_to_accountant(documents):
        print(f"Sending documents to accountant: {documents}")

report = Report("123", "to approve", "ZUS123")
director_approver = DirectorApprover()
accountant_sender = AccountantSender()

director_approver.approve_report(report)
accountant_sender.send_documents_to_accountant(report)

report_2 = Report("333", "Closed", "US_123")