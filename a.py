import zipfile
zip_ref = zipfile.ZipFile("master.zip", 'r')
zip_ref.extractall(".")
zip_ref.close()
