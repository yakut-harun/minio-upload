import boto3

import math
import os
import os
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from storages.backends.s3boto3 import S3Boto3Storage


class MediaStorage(S3Boto3Storage):
    location = 'static/media'
    file_overwrite = False
    print("kdnlvjb ")
    def save(self, name, content, max_length=None):
        print("save içi")
        if content.size < 5242880:  # 5MB'dan küçükse tek parça halinde yükle
            print("uzunluk kontrolu tek yükle")
            return super(MediaStorage, self).save(name, content)

        else:  # 5MB'dan büyükse multipart olarak yükle
            # Multipart yükleme için gerekli bilgileri tanımla
            multipart_upload = self.connection.meta.client.create_multipart_upload(Bucket=self.bucket_name, Key=name)
            upload_id = multipart_upload['UploadId']
            part_size = 100000000
            print("else içi")

            part_info = []

            # Dosyayı parçalara ayır ve S3'e yükle
            i = 1
            while True:
                data = content.read(part_size)
                print("dongü içi")
                print(i)
                if not data:
                    print("dongü sonu ")
                    break
                response = self.connection.meta.client.upload_part(Bucket=self.bucket_name, Key=name, UploadId=upload_id, PartNumber=i, Body=data)
                part_info.append({'PartNumber': i, 'ETag': response['ETag']})
                i += 1

            # Multipart yükleme işlemini tamamla
            self.connection.meta.client.complete_multipart_upload(Bucket=self.bucket_name, Key=name, UploadId=upload_id, MultipartUpload={'Parts': part_info})

            # Dosyayı static/media klasörüne kaydet
            return super(MediaStorage, self).save(name, content)
