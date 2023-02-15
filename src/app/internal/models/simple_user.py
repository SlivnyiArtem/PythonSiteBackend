from django.db import models
from django.contrib import admin


class SimpleUser(models.Model):
    user_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    phone_number = models.IntegerField(null=True)

    def __str__(self):
        return str(self.user_id)

    def get_dictionary_deserialize(self):
        dict = vars(self)
        dict.pop("_state")
        return dict

    def string_deserialize(self):
        des_res = self.get_dictionary_deserialize()
        result_str = ""
        for key, value in des_res.items():
            # if str(key) == "_state":
            #     continue
            result_str += str(key) + " : " + str(value) + "\n"
            # print(str(key) + " : " + str(value))
        # print(result_str)
        # print(des_res)
        #return result_str.encode(encoding="utf-8")
        return result_str
