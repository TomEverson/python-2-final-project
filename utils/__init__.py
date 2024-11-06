from csv import DictWriter


def write_to_csv(product: str):

    field_names = ["Title", "Value"]

    with open('event.csv', 'a') as f_object:

        dictwriter_object = DictWriter(f_object, fieldnames=field_names)

        dictwriter_object.writerow(product)

        f_object.close()
