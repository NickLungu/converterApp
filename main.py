from PIL import Image
import easygui
import os


def convert4tg(input_file):
    path_list = input_file

    for counter, path in enumerate(path_list):

        # working with path
        if counter == 0:
            splited_path = path.split("\\")
            folder = '\\'.join(splited_path[:-1])
            new_folder = folder + '\\' + "converted"
        path_out = new_folder + '\\' + str(counter+1) + ".png"

        # open and work with image
        im1 = Image.open(path)
        width, height = im1.size
        coef = 512/max(width, height)
        width_new = width * coef
        height_new = height * coef
        im1_out = im1.resize((int(width_new), int(height_new)))

        # save image
        if not os.path.isdir(new_folder):
            os.makedirs(new_folder)
        im1_out.save(path_out)

    return len(path_list), new_folder


