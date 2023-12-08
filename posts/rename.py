# -*- coding: utf-8 -*-

import os
import re
import shutil

def get_dir_list(init_path):
    dir_list = []
    for i in os.listdir(init_path):
        i_path = os.path.join(init_path, i)
        if os.path.isdir(i_path):
            dir_list.append(i)
    return dir_list

def get_file_list(init_path):
    file_list = []
    for i in os.listdir(init_path):
        i_path = os.path.join(init_path, i)
        if os.path.isfile(i_path):
            file_list.append(i)
    return file_list
        
 

def main():
    root_path = os.getcwd()
    dir_list_year = get_dir_list(root_path)
    for year in dir_list_year:
        year_path = os.path.join(root_path, year)
        dir_list_month = get_dir_list(year_path)
        # print(dir_list_month)
        for month in dir_list_month:
            month_path = os.path.join(year_path, month)
            dir_list_day = get_dir_list(month_path)
            for day in dir_list_day:
                day_path = os.path.join(month_path, day)
                # print(dir_list_blog)
                file_list = get_file_list(day_path)
                try:
                    if len(file_list):
                        # print(file_list)
                        for file in file_list:
                            pattern = re.compile(r'\d{4}-\d{2}-\d{2}-')
                            if '.md' in file:
                                date_str = pattern.findall(file)[0]
                                new_dir_name = file.split(date_str)[-1].split('.md')[0]
                                new_dir_path = os.path.join(day_path, new_dir_name)
                                ori_path = os.path.join(day_path, file)
                                dest_path = os.path.join(day_path, 'index.md')
                                file_list[file_list.index(file)] = 'index.md'
                                os.rename(ori_path, dest_path)
                                os.mkdir(new_dir_path)

                        for file in file_list:
                            dir_path = get_dir_list(day_path)[0]
                            ori_path = os.path.join(day_path, file)
                            dest_path = os.path.join(os.path.join(day_path, dir_path), file)
                            shutil.move(ori_path, dest_path)
                except Exception as e:
                    print(day_path)
                    print(e)






if __name__ == '__main__':
    main()