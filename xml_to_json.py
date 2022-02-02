import json

import xmltodict
from argparse import ArgumentParser


def convert_xml_to_json(xml_file_path):
    with open(xml_file_path) as xml_file:
        data_dict = xmltodict.parse(xml_file.read())
    xml_file.close()
    json_data = json.dumps(data_dict)
    return json_data


def write_json(json_data, dest_file_path):
    with open(dest_file_path, "w") as json_file:
        json_file.write(json_data)
    json_file.close()


def main(xml_file_path, dest_file_path):
    json_data = convert_xml_to_json(xml_file_path)
    write_json(json_data, dest_file_path)


if __name__ == "__main__":
    parser = ArgumentParser(description="...")
    parser.add_argument("-xml_file_path", metavar="xml_file_path",
                        help="Path to the xml file")
    parser.add_argument("-dest_file_path", "--dest_file_path",
                        dest="dest_file_path",
                        help="Path to write the json file")
    args = parser.parse_args()
    main(args.xml_file_path, args.dest_file_path)
