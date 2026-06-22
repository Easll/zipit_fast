import aspose.zip as zp

def zip_it (input, name, save_path):
    with zp.Archive() as archive:
        try:
            archive.create_entry(name = name, path = input)
            archive.save(save_path)
            return True
        except:
            return False


#def zip_them ()

    