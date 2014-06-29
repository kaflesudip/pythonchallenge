"""Question no. 6 of PythonChallenge """
import zipfile


def main():
    """Main function """
    zipped_file = 'channel.zip'
    zipped = zipfile.ZipFile(zipped_file)
    nothing_no = '90052'

    comment_list = []

    try:
        while True:
            file_name = "{0}.txt".format(nothing_no)
            comment = zipped.getinfo(file_name).comment
            comment_list.append(comment)
            read_item = zipped.read(file_name).decode('utf-8')
            print(comment)
            nothing_no = str(read_item).split(' ')[-1]
    except:
        comment_list = [i.decode('utf-8') for i in comment_list]
        print(''.join(comment_list))

if __name__ == main():
    main()

# http://www.pythonchallenge.com/pc/def/hockey.html
# oxygen is the solution to next riddle
# http://www.pythonchallenge.com/pc/def/oxygen.html
