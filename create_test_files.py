"""Creates multiple files for testing purposes"""
# -*- coding: utf-8 -*-
import argparse
import os
import test_tools.csv_file_creator as csv_creator

THIS_FOLDER = os.path.dirname(os.path.realpath(__file__))
TEST_FOLDER_PREFIX = "csv_tests_files"
TEST_FOLDER = os.path.join(THIS_FOLDER, TEST_FOLDER_PREFIX)


def create_csv_files(path):
    """Create the csv files in the path folder according to the
    arguments number_of_files and number_of_lines

        Arguments:
            path str(): the folder path where the files are going
            to be generated
    """
    for _, n in enumerate(range(arguments.number_of_files)):
        file_path = os.path.join(path, "file{}".format(n))
        csv_creator.create_csv_file(arguments.number_of_lines, file_path)


def create_root_test_folder():
    """Creates the TEST_FOLDER_PREFIX folder"""
    if not os.path.exists(TEST_FOLDER_PREFIX):
        os.mkdir(TEST_FOLDER)


def create_test_folder():
    """Creates a new folder path according to the number_of_lines argument.

    Returns:
        new_tests_folder_file (str): Path where the files will be created
    """
    test_folders = []
    test_folder_path = os.path.join(THIS_FOLDER, TEST_FOLDER_PREFIX)
    test_csv_folder = "test_csv_files_"
    new_test_folder = test_csv_folder + \
        "0_{}".format(arguments.number_of_lines)
    for folder in os.listdir(test_folder_path):
        if os.path.isdir(os.path.join(test_folder_path, folder)) and folder.startswith(test_csv_folder):
            test_folders.append(folder)
    if len(test_folders) > 0:
        max_old_folder = max([int(old_folder.split("_")[3])
                              for old_folder in test_folders])
        new_test_folder = test_csv_folder + \
            "{}_{}".format(max_old_folder + 1, arguments.number_of_lines)
    new_tests_folder_path = os.path.join(test_folder_path, new_test_folder)
    os.mkdir(new_tests_folder_path)
    return new_tests_folder_path


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Creates test csv files")
    parser.add_argument('number_of_files', type=int,
                        help="number of test files to create")
    parser.add_argument('number_of_lines', type=int,
                        help="number of lines for each file")
    arguments = parser.parse_args()
    create_root_test_folder()
    test_folder = create_test_folder()
    create_csv_files(test_folder)
