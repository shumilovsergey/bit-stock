from django.db import models

class TelegramUsers(models.Model):
    session_id = models.CharField(max_length=56, unique=True)
    tg_id = models.CharField(max_length=56, default="no-auth")
    name = models.CharField(max_length=56, default="no-auth")
    stocks_id = models.JSONField(default=dict)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.tg_id
    class Meta:
        ordering = ['-created']


# class Org(models.Model):
#     name = models.CharField(max_length=56)
#     boss =  models.ForeignKey(TelegramUsers, on_delete=models.CASCADE)
#     def __str__(self):
#         return self.name
#     class Meta:
#         ordering = ['-created']

# class OrgEmployees():
#     organisation = models.ForeignKey(Org, on_delete=models.CASCADE)
#     employer = models.ForeignKey(TelegramUsers, on_delete=models.CASCADE)
#     def __str__(self):
#         return self.organisation
#     class Meta:
#         ordering = ['-created']

# class OrgCategoris():
#     organistatin = models.ForeignKey(Org, on_delete=models.CASCADE)
#     name = models.CharField(max_length=56)



# !OrgPructs
# name
# category
# description
# photo? 
# date_in
# prcie_in
# date_out
# proce out


#

#// MiddleWare /organisation/<id>/
# session.tg_id in Org.Emploers(filter organisation id)
# if not => fck you page
# if yes => show navbar col

#// HTML templates
# navbar row
# navbar col

#// webpage names
#// webpage icons






