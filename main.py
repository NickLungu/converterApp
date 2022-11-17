from PIL import Image
import easygui


def convert4tg(input_file):
    path = input_file
    im1 = Image.open(path)
    width, height = im1.size

    path_out = ('.'.join(path.split(".")[:-1])) + ".png"

    coef = 512/max(width, height)

    width_new = width * coef
    height_new = height * coef

    im1_out = im1.resize((int(width_new), int(height_new)))

    im1_out.save(path_out)


if __name__ == '__main__':

    input_file = easygui.fileopenbox(filetypes=["*.img"])
    convert4tg(input_file)

