def record_generate(cur_record):
    max_record = open("Record.txt", mode="r+")
    if int(max_record.readline()) < cur_record:
        max_record.seek(0)
        max_record.write(str(cur_record))
    max_record.seek(0)
    cur_record = max_record.readline()
    max_record.close()
    return cur_record