from odoo import api, models


class WarehouseReport(models.AbstractModel):
    _name = 'warehouse.list'
    _description = 'Warehouse Report'

    @api.model
    def _get_report_values(self, docids, data=None):
        print("print from applicant report method")
        # print("ids",docids[0])
        print("self", self)
        print("data", data)
        docs = self.env['warehouse.list'].browse(docids[0])
        # issued_report = self.env['lms.issue.books'].search([('member.id','=',docids[0])])

        # issue_book_list = []
        # for issue in issued_report:
        #     vals ={
        #         'book': issue.book.book_name,
        #         'return': issue.return_date,
        #         'status': issue.issue_book_status,
        #         'image': issue.book.book_image

        #     }
        #     issue_book_list.append(vals)
        # print("docs",docs)

        # print("list",issue_book_list)
        return {
            'doc_model': 'warehouse.list',
            'data': data,
            'docs': docs,

        }
